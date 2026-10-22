---
layout: post
title: '挖洞的变成了机器，补丁的还是人类'
date: 2026-10-22 12:00:00 +0800
categories: [AI观点]
tags: [网络安全, 漏洞挖掘, 软件供应链, 协调披露, 攻击面缩减, 补丁速度]
author: toby
cover: /assets/img/posts/2026-10-22-ai-patch-velocity-gap-cover.png
description: 'OpenAI和Wiz挖出PHP远古级漏洞，互联网吓出一身冷汗，结果exp根本不存在——真正成立的警报是：发现漏洞已经是机器的速度，修复还排着人类的日历。'
---

> 10月21日，互联网集体做了一次"末日演习"：OpenAI和谷歌旗下Wiz宣布在PHP核心里找到远古级远程代码执行漏洞php2shell，CVE编号当场挂出，AWS发安全公告，Cloudflare连夜上线WAF规则，PHP Foundation紧急发布多版本修复，Hacker News一条帖子涌进331条评论。同一天，PyPI上的LiteLLM 1.107.0被投毒，AI开发者装个标配库，附赠凭据窃取器和后门。这一天最值得记下的不是哪个洞更致命，而是一个正在拉开的速度差：挖洞的变成了机器，补丁的还是人类。

![挖洞的变成了机器，补丁的还是人类]({{ page.cover }})

## 一场先喊"末日"再悄悄收回的恐慌

php2shell的剧情走向很值得玩味。漏洞公告一出，"PHP末日"的标题在技术社区刷了屏——毕竟PHP还撑着互联网相当大比例的老系统，一个"远古级RCE"听上去就像给全世界的旧服务器集体判了死刑。AWS发公告，Cloudflare上规则，PHP Foundation在同一天发布多版本紧急更新，还顺手公布了一个长期安全强化计划，阵仗给得很足。

但24小时之内，风向往回拐了：有研究者指出，实际并不存在轻易可用的exp（漏洞利用程序）。换句话说，这是一对编号很吓人、武器化程度存疑的漏洞。HN上331条评论里，恐慌派和理性派吵成一团，最后大家发现，这场"末日"更像一次压力测试——测试的对象不是PHP，而是整个行业的应急神经。

测试结果其实不差：发现问题、挂编号、发公告、上规则、出补丁，整条链条在一天内走完。可别急着鼓掌，因为这恰恰暴露了问题——这次能跑这么快，是因为挖洞的是OpenAI和Wiz，是"自己人"按负责任披露的剧本走。当挖洞的不只是一家实验室，而是成千上万台不知疲倦、不求名利、不需要睡觉的机器时，这条以人类为节点的链条，还跑得动吗？

## 挖洞这件事，已经流水线化了

把同一天的新闻连起来看，你会发现"挖洞工业化"不是比喻，是已经上线的产品。

OpenAI在同日启动了"Patch the Planet"计划：AI智能体批量发现关键漏洞之后，建立全球响应协调机制，漏洞的发现、通报、修复闭环正在自动化。请注意"批量"这个词——漏洞挖掘这门手艺，过去靠的是少数顶尖研究者的直觉加运气，一个人一辈子能挖穿几个核心组件就算行业大牛；现在它变成了智能体的工作队列，挖掘的边际成本正在向电费靠拢。

Anthropic那边也没闲着，同日公布了用Claude给代码"缩小攻击面"的技术：自动化攻击面分析与缩减，已经在大型开源代码库上实测并公布了数据。这招的思路比"找洞"更进一步——与其等着别人来翻，不如让AI直接把能被攻击的表面积砍小。防守方第一次拥有了和进攻方同一量级的自动化工具，这个意义怎么估都不过分。

再看OpenAI让数千个智能体并行挖掘生物学数据的新线索，你会发现这是同一个模式在不同领域的复刻：凡是"大海捞针"型的智力劳动——找漏洞、找线索、找规律——AI都在把整片针海对机器敞开。旧的攻防平衡建立在"发现是稀缺的"这个前提上：顶尖研究者有限，披露周期以年计，安全团队可以按部就班。当发现变得不稀缺，所有下游环节都得跟着重排。

![暗色屏幕上滚动的代码，每一段都可能藏着一条只有机器看得见的小路](/assets/img/posts/2026-10-22-ai-patch-velocity-gap-photo1.jpg)

## 而刀已经先捅进了AI自己的供应链

讽刺的是，就在整个行业享受"AI帮我们找漏洞"的爽感时，LiteLLM在PyPI上的1.107.0版本被投了毒——装上即带凭据窃取器和后门。LiteLLM是什么？是AI开发生态里最常见的组件之一，接大模型API的事实标准，无数团队的生产系统每天靠它调用模型。供应链攻击者根本没去碰任何一家实验室的堡垒，他们只是在包管理器里放了一个带毒的版本，然后等开发者亲手把自己环境的钥匙交出来。

同一天还有一串：GitLab因整数溢出可致远程代码执行，紧急发布19.5.1补丁并建议立即升级；mitmproxy针对eMudhra中间CA失陷事件火速加入模拟选项；Railway发布安全披露；HTTP/3服务器遭Qpack放大攻击。一天之内五件安全大事，件件都需要人来响应——运维读公告、工程师升级版本、安全团队排查是否中招，每一个环节都排着人类的日程表。

这就是那个真正成立的警报：发现的成本被AI打到了地板上，而修复依然是串行的、靠日历驱动的、需要人半夜爬起来干的活。挖掘可以并行一万路，补丁却只能一条条合并、测试、灰度、上线。这道剪刀差每扩大一点，攻防的天平就朝进攻方多倾斜一分。

![港口里堆叠如山的集装箱，一条链条上最薄弱的那节决定整批货的命运](/assets/img/posts/2026-10-22-ai-patch-velocity-gap-photo2.jpg)

## 别再数挖出多少洞，数补丁跑到生产要几天

所以我的看法是：php2shell的恐慌可以翻篇，但它留下的考题必须留下。行业该换考核指标了——过去大家比的是"发现了多少漏洞"，CVE编号像军功章一样挂满墙；未来该比的是"补丁从仓库跑到生产环境要几天"。当发现端是机器速度，修复端的人类速度就成了全系统唯一的瓶颈；瓶颈不解决，挖得越多，暴露期越长，安全公告只会越堆越高。

方向其实已经有人指出来了："Patch the Planet"把通报和修复纳入闭环自动化，这是对的一步——这个闭环的每一环都应该奔着无人化去：自动生成补丁、自动验证回归、自动协调披露。企业这边该做的更朴素：把依赖清单和版本锁定当成卫生习惯而不是合规负担，默认自己用的每一个AI组件都可能在某天早晨变成投毒现场——LiteLLM已经示范过了。

最后说句不太客气的话：安全的旧剧本靠的是藏——藏代码、藏漏洞、藏路径，赌的就是发现者永远不够多。现在人人手里都有挖掘机，藏是藏不住的。以后比的不是谁埋得深，是谁补得快。机器已经开始计时了。

<p style="text-align:center;font-size:0.78rem;color:#94a3b8;">📷 <a href="https://unsplash.com/photos/macbook-pro-with-images-of-computer-language-codes-fPkvU7RDmCo?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Photo by Caspar Camille Rubin</a> on <a href="https://unsplash.com?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Unsplash</a></p>

<p style="text-align:center;font-size:0.78rem;color:#94a3b8;">📷 <a href="https://unsplash.com/photos/assorted-color-filed-intermodal-containers-tjX_sniNzgQ?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Photo by frank mckenna</a> on <a href="https://unsplash.com?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Unsplash</a></p>
