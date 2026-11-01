---
layout: post
title: 'AI没抢走工作，先没收了学徒期'
date: 2026-11-01 12:00:00 +0800
categories: [AI观点]
tags: [去技能化, SRE, 学徒制, 初级岗位, 运维, AI依赖]
author: toby
cover: /assets/img/posts/2026-11-01-ai-confiscated-apprenticeship-cover.png
description: 'HN本周最热的帖子把话说得很直白：AI没有取代SRE，它只是替新人跳过了打基础的阶段——岗位还在，配得上岗位的人却断供了。'
---

> 本周Hacker News最热的一篇帖子拿了647分、474条评论，标题起得像句判词：**《AI不是在取代SRE，而是在去技能化SRE》**。上千楼的争论吵到最后，留下一个没人反驳的共识——AI拿走的从来不是你的工位，而是通往这个工位的那段楼梯。

![AI没抢走工作，先没收了学徒期]({{ page.cover }})

## 岗位还在，会干的人断供了

"去技能化"（deskilling）不是什么新发明。民航业几十年前就有个刺耳的外号，叫"洋红线的一代"（children of the magenta line）——因为飞行管理系统的航迹在仪表上是洋红色，新一代飞行员从训练第一天起就跟着这条线飞，手动飞行时间被压缩到最低。结果就是：自动驾驶一切正常时他们比老机长还稳，系统一旦掉线，手上的肌肉记忆撑不过三十秒。放射科、制造业、甚至是外科手术，都上演过几乎一模一样的剧本。

现在轮到运维了。Signoz那篇文章的核心观察并不复杂：告警被AI汇总归因，runbook由AI现场生成，故障复盘让AI写摘要，连变更窗口的沟通话术都能让模型润色。每一项单拎出来都是效率的胜利，加在一起却构成一个残酷的事实——一个入行三年的SRE，可能从来没有完整地徒手排查过一次"为什么"。而他第一次真正面对这个问题的时刻，往往是凌晨三点、P0响成一片、AI的归因恰好指错方向的时候。工具替他把基础训练全跳过去了，唯独跳不过那次真实世界的期末考试。

批评者最常用的辩护是"AI只是工具，关键看人"。这话在电钻和计算器时代成立，是因为那些工具只外包了力气和算术，判断力还得自己长。而大模型外包的恰恰是判断力本身，这就不是"工具好不好用"的问题了，是"人还有没有机会变强"的问题。

## Cisco发了无限token，顺手收走了必经之路

同一周里还有一条更热闹的新闻：Cisco总裁Jeetu Patel公开讲，公司让一位27岁的工程师拿着"无限AI token"去重写遗留系统，这帖子在HN上拿了302分、370条评论，讨论的火药味全在标题的后半句——初级岗位会被如何重塑。

支持者的画面很美好：一个人干一个团队的活，效率拉满。但很少有人问一句，那位27岁的工程师，判断力是从哪来的？答案大概率还是遗留系统。祖传代码在老工程师眼里是墓志铭，在初级工程师眼里却是教科书——读那些写于二十年前的抽象、修那些没人说得清来龙去脉的bug，本质上是拿工资换判断力的学徒交易。公司付你入门级的薪水，你交出的是在廉价项目里犯错的权利，攒下的是昂贵项目里救火的本事。

现在这笔交易被单方面终止了。AI十分钟给出重构方案，新人审都没审就按下合并，因为"反正模型比我有经验"。听起来合理，但经验不会凭空生成，它需要有人在便宜的场合犯过错。学徒期被拆掉之后，市场上会只剩两种人：租过判断力的，和从未攒下判断力的。而租金，是年年涨价、永远不归你所有的。

![幽长的走廊一眼望不到头——以前的新人要一段一段走完，现在的按钮一键传送](/assets/img/posts/2026-11-01-ai-confiscated-apprenticeship-photo1.jpg)

## 更讽刺的是：它帮你跳级，还不许你自学

如果故事到这里为止，顶多算一声叹息。真正荒诞的是本周的另一条新闻：Anthropic开始主动拦截视频游戏克隆与逆向工程类的请求，Tom's Hardware报道了官方拦截行为，HN上还有用户抱怨"任何涉及训练更大模型的话题"都可能触发封号。

把这两件事并排放着看，讽刺就冒烟了。逆向工程、拆解、克隆重写，是人类最古老的学习方式：收音机是拆出来的，汽车是拆出来的，整整一代程序员是在反汇编DOS游戏里学会写代码的。现在这家公司一边推出帮你跳过基本功的产品，一边没收你拆开东西自学的路径——好比给学琴的孩子配了个代练包办所有练习曲，然后校方宣布禁止扒谱。跳级的便利它卖给你，自学的门它替你锁上，两门生意出自同一家公司，且都不觉得矛盾。

有人会说这是合规和安全的必要代价，我不反对给企业行为留余地。但当"拆解式学习"在AI公司这里被系统性污名化，而全社会的技能养成又越来越依赖这些公司的产品时，我们实际上是在把一代人的能力基础设施，外包给几个商业利益并不与你一致的董事会。

## 稀缺品正在换个名字贵起来

反例这周也凑齐了。Show HN上有人把语言模型塞进了512字节的x86引导扇区，没有操作系统、没有依赖，推理直接跑在裸机上；另一个项目把世界模型压缩到树莓派Pico 2W那颗几美元的MCU上。能在这种地方干活的人，恰恰是那些拒绝跳级、坚持把底层摸透的人——只是这样的人，正在从"行业标配"变成"手工限定款"。

这不是什么值得庆祝的浪漫故事。一个去技能化的团队，最大的风险不是平庸，而是脆弱：每个人都用着同样的AI，也就共享着同样的盲区，当模型归因出错时，房间里没有一个能回答"为什么错了"的人。到那时，那些会看底层的工程师要的就不再是技能溢价，而是保险费——而且这个险种，正在变得越来越难投保。

所以别再问"AI什么时候取代我的工作"了，它做的这件事更彻底：把"配得上这份工作"的那段路拆掉，铺成了收费高速。跳上去的人确实快了，但在所有车都走高速的世界里，会认路的司机反而成了传说中的生物。工具本身没有原罪，问题只在于它好得过分——好到让整整一代人，忘了自己原本也需要变好。

---

*本文基于2026年10月30日至11月1日的公开报道：Signoz《AI isn't replacing SREs, it's deskilling》（HN 647分）、Fortune对Cisco Jeetu Patel的访谈、Tom's Hardware关于Claude拦截逆向工程请求的报道，以及HN上的bootgpt与tinyworldformer项目。*

<p style="text-align:center;font-size:0.78rem;color:#94a3b8;">📷 <a href="https://unsplash.com/photos/a-long-hallway-with-glass-doors-leading-to-another-room-s0XabTAKvak?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Photo by Paul Hanaoka</a> on <a href="https://unsplash.com?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Unsplash</a></p>

<p style="text-align:center;font-size:0.78rem;color:#94a3b8;">📷 <a href="https://unsplash.com/photos/black-laptop-computer-turned-on-near-black-flat-screen-computer-monitor-2836IR07ocg?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Photo by Frederic Köberl</a> on <a href="https://unsplash.com?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Unsplash</a></p>
