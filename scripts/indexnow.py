#!/usr/bin/env python3
"""IndexNow 提交器（Bing / Yandex / Seznam / Naver）。

用法：
  python3 scripts/indexnow.py                      # 提交 sitemap 里近 2 天更新的 URL
  python3 scripts/indexnow.py --days 7             # 放宽到 7 天
  python3 scripts/indexnow.py --urls https://...   # 提交指定 URL
  python3 scripts/indexnow.py --dry-run            # 只打印不提交

密钥文件：仓库根目录下 <key>.txt（内容就是 key 本身），IndexNow 会来验证。
"""
import argparse, json, re, sys, time, urllib.request, urllib.error, pathlib

SITE = "https://toby-blog.com"
SITEMAP = f"{SITE}/sitemap.xml"
ENDPOINT = "https://api.indexnow.org/indexnow"
ROOT = pathlib.Path(__file__).resolve().parent.parent


def find_key():
    """在仓库根目录找 <32位hex>.txt 的 IndexNow 密钥文件"""
    for p in ROOT.glob("*.txt"):
        name = p.stem
        if not re.fullmatch(r"[0-9a-fA-F]{8,128}", name):
            continue
        content = p.read_text(encoding="utf-8", errors="ignore").strip()
        if content == name:
            return name, f"{SITE}/{name}.txt"
    sys.exit("FAIL: 没找到 IndexNow 密钥文件（<key>.txt，内容等于文件名）")


def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": "toby-blog-indexnow/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "ignore")


def sitemap_urls(days):
    """解析 sitemap，按 lastmod 过滤最近 N 天；没有 lastmod 的保留首页/最新页兜底"""
    xml = fetch(SITEMAP)
    entries = re.findall(
        r"<url>\s*<loc>(.*?)</loc>\s*(?:<lastmod>(.*?)</lastmod>)?", xml, re.S)
    cutoff = time.time() - days * 86400
    picked = []
    for loc, lastmod in entries:
        loc = loc.strip()
        if not lastmod:
            continue
        ts = parse_iso(lastmod.strip())
        if ts and ts >= cutoff:
            picked.append((ts, loc))
    picked.sort(reverse=True)
    # 过滤掉资源类/演示类页面，只提交文章与栏目页
    skip = ("/assets/", "/skills/", ".xml", ".json")
    return [u for _, u in picked if not any(s in u for s in skip)]


def parse_iso(s):
    for fmt in ("%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d"):
        try:
            import datetime
            dt = datetime.datetime.strptime(s.replace("Z", "+0000"), fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=datetime.timezone.utc)
            return dt.timestamp()
        except Exception:
            continue
    return None


def fallback_urls():
    """没有任何近期待更新时，至少提交首页 + sitemap 前 10 条"""
    xml = fetch(SITEMAP)
    locs = re.findall(r"<loc>(.*?)</loc>", xml)
    return [SITE + "/"] + locs[:10]


def submit(urls, key, key_location):
    body = json.dumps({
        "host": "toby-blog.com",
        "key": key,
        "keyLocation": key_location,
        "urlList": urls[:10000],
    }).encode()
    req = urllib.request.Request(
        ENDPOINT, data=body,
        headers={"Content-Type": "application/json; charset=utf-8",
                 "User-Agent": "toby-blog-indexnow/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.read().decode("utf-8", "ignore")[:200]
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "ignore")[:200]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=2)
    ap.add_argument("--urls", nargs="*")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    key, key_loc = find_key()
    if a.urls:
        urls = a.urls
    else:
        urls = sitemap_urls(a.days) or fallback_urls()

    print(f"key={key[:8]}… keyLocation={key_loc} urls={len(urls)}")
    if a.dry_run:
        for u in urls[:20]:
            print("  ", u)
        return
    if not urls:
        print("skip: no urls")
        return
    status, text = submit(urls, key, key_loc)
    print(f"IndexNow HTTP {status} {text}".strip())
    # 200/202 表示已接收
    sys.exit(0 if status in (200, 202) else 1)


if __name__ == "__main__":
    main()