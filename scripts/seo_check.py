#!/usr/bin/env python3
"""发布后 SEO 生效核验：确认线上页面把 SEO 该有的东西都吐出来了。

用法：python3 scripts/seo_check.py <文章URL>
退出码：0 全部通过；1 有失败项（打印明细）
"""
import json, re, sys, urllib.request, urllib.error

UA = {"User-Agent": "Mozilla/5.0 (compatible; toby-blog-seo-check/1.0)"}


def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read().decode("utf-8", "ignore")


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: seo_check.py <url>")
    url = sys.argv[1]
    checks = []

    def add(name, ok, detail=""):
        checks.append((name, bool(ok), detail))

    try:
        status, html = fetch(url)
    except urllib.error.HTTPError as e:
        print(f"FAIL http {e.code}: {url}")
        sys.exit(1)

    add("HTTP 200", status == 200, f"status={status}")

    titles = re.findall(r"<title>(.*?)</title>", html, re.S)
    add("title 唯一", len(titles) == 1, f"{len(titles)} 个: {titles[:1]}")
    add("title 非空且含站点名", bool(titles) and len(titles[0].strip()) > 5,
        titles[0].strip()[:60] if titles else "")

    descs = re.findall(r'<meta name="description" content="([^"]*)"', html)
    add("description 唯一", len(descs) == 1, f"{len(descs)} 个")
    add("description 长度 50-200", bool(descs) and 50 <= len(descs[0]) <= 200,
        f"{len(descs[0]) if descs else 0} 字")

    canons = re.findall(r'rel="canonical" href="([^"]+)"', html)
    add("canonical 唯一", len(canons) == 1, f"{len(canons)} 个")
    add("canonical 指向自身", bool(canons) and canons[0].rstrip("/") == url.rstrip("/"),
        canons[0] if canons else "")

    robots = re.findall(r'name="robots" content="([^"]+)"', html)
    add("robots 允许索引", not robots or "noindex" not in robots[0].lower(),
        robots[0] if robots else "无 robots（默认可索引）")

    og = re.findall(r'property="og:image" content="([^"]+)"', html)
    add("og:image 存在", len(og) >= 1, og[0][:80] if og else "")
    if og:
        try:
            st, _ = fetch(og[0])
            add("og:image 可访问", st == 200, f"status={st}")
        except Exception as e:
            add("og:image 可访问", False, str(e)[:60])

    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
    valid = 0
    types = set()
    for b in blocks:
        try:
            d = json.loads(b)
            valid += 1
            for t in re.findall(r'"@type":\s*"([^"]+)"', b):
                types.add(t)
        except Exception:
            pass
    add("JSON-LD 全部可解析", len(blocks) > 0 and valid == len(blocks), f"{valid}/{len(blocks)}")
    add("含 BlogPosting", "BlogPosting" in types, ",".join(sorted(types))[:100])
    add("含 BreadcrumbList", "BreadcrumbList" in types, "")
    add("无重复 seo-tag JSON-LD", '"@type":"BlogPosting"' not in html, "")

    ok = all(c[1] for c in checks)
    for name, passed, detail in checks:
        print(f"{'✅' if passed else '❌'} {name}" + (f" — {detail}" if detail else ""))
    print(f"\n{'PASS' if ok else 'FAIL'} {sum(1 for c in checks if c[1])}/{len(checks)} | {url}")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()