---
layout: post
title: '绿格子还在涨，人已经下桌了'
date: 2026-10-29 12:00:00 +0800
categories: [AI观点]
tags: [GitHub, 智能体编程, StackOverflow, 提交通胀, 代码指标, 开发者生态]
author: toby
cover: /assets/img/posts/2026-10-29-ai-commit-inflation-cover.png
description: '一年之内，GitHub月合并PR涨了三倍，StackOverflow月提问跌破一千条——同一个开发者世界，一边在通胀，一边在失血。'
---

> 全球程序员一年之内的手速不可能翻三倍，但他们提交的代码翻了三倍。当指标开始脱离人，我们该追问的就不是"AI多能写"，而是"这些数字还在测量什么"。

![绿格子还在涨，人已经下桌了]({{ page.cover }})

## 每秒钟两千八百次commit，是人敲出来的吗

GitHub一年一度的Octoverse，往年是开发者生态的成绩单，今年更像一封自首书。10月底发布的2026年版数据：月合并Pull Request一年内涨到2.2亿个，三倍；月commit 73.8亿个，超过三倍；每月新增仓库3030万个，翻倍。

把73.8亿摊开，折合全球每秒钟约两千八百次commit、每秒钟合并85个PR。就算把地球上所有的职业开发者拉成三班倒、24小时不吃不喝地敲，人肉也填不出这个量级的增量——何况真实世界的开发者还要开会、要对齐、还要在IM里解释为什么这个需求做不了。唯一能一年翻三倍的生产函数，是agent：写、提、修、再提，不知疲倦，不请假，也不在乎自己的名字落在谁的contribution graph上。

更耐人寻味的是GitHub自己的动作：为了修正远程开发者用VPN造成的地理偏差，他们用LLM重新给贡献者分类；行业归属靠嵌入模型来归。换句话说，这份报告的测量仪器本身，已经开始用模型来对付模型制造的数据。用模型测量模型，误差项里坐满了当事人，这份成绩单的精度，恐怕连GitHub自己都不敢拍胸脯。

Simon Willison把2025年11月称为编码Agent的拐点，今年10月则是"氛围游戏开发"的拐点——可用性确实在跃迁，这一点不必抬杠。问题在于，拐点过后留下来填表的，是换了一群"员工"。

![开发者工作台：键盘还在响，节奏已经变了](/assets/img/posts/2026-10-29-ai-commit-inflation-photo1.jpg)

## 提问量跌破一千条：解放，还是断粮

同一个10月，另一张图表安静地滑过了心理关口：StackOverflow的月提问量跌破1000条。十年前，这里是全球程序员的图书馆、急诊室和茶水间，月提问量以十万计。如今一千条，一个中型公司的内部群都比这热闹。

第一种解读是凯旋：AI替人回答了，效率万岁，旧时代的图书馆当然要关门。这个说法只对了一半。错的那一半是：StackOverflow从来不只是"答案获取渠道"，它是全球程序员的公共学习回路——新人提问，老人纠偏，答案被成千上万双眼睛审过、踩过、改过。这条回路断掉之后，新人不再需要理解"为什么"，只需要理解"怎么让AI改到能跑"。

更深一层的讽刺是：今天这些编码Agent的本事，很大一部分就是当年从StackOverflow的问答语料里学来的。吃完图书馆，回头把图书馆的读者也领走了。下一代模型若要从"AI生成、AI审查、AI引用"的语料里继续进化，等于让满屋子的人互相抄作业——学界管这叫模型崩塌的风险，产业界管这叫"数据飞轮"。词很顺口，方向是反的。

## 通胀的绿格子，和跟着通胀的一切

指标通胀从来不只是技术圈的自嗨，它会顺着考核体系往下渗。

往上渗一层是企业管理：当commit数、PR数、repo数被agent灌了水，还拿这些数字考核团队的管理者，测到的将是agent的勤奋程度，而不是产品的好坏。古德哈特定律说，当一个指标变成目标，它就不再是好指标——现在的情况更彻底，指标连"人"这个测量对象都换掉了。往下渗一层是个人：作品集上挂三十个仓库，面试官已经没法靠数量分辨是练手还是批量生成，绿色格子从简历资产贬值成了装饰品。

钱倒是没含糊。微软同周首次披露Azure单季营收332亿美元，其中来自OpenAI的收入就有100亿美元——代码通胀的每一格绿，最后都结算成算力账单上的真金白银。平台方是这场通胀里唯一稳赚不赔的角色：他们收的是钱，不是commit。

## 结语

十年前我们调侃程序员的核心竞争力是搜索，后来是提问，现在轮到验收。当生产数字的机器和统计数字的机器都换成了模型，人剩下的位置其实在链条两端：一端是决定什么值得做的问题，另一端是愿意为结果签名背书的信用。GitHub的绿格子会继续涨，涨到没人记得它原本测的是人。这本身没什么可怕，可怕的是我们跟着指标一起，把"有东西在被生产"误读成"有价值在被创造"。

<p style="text-align:center;font-size:0.78rem;color:#94a3b8;">📷 <a href="https://unsplash.com/photos/person-using-laptop-computers-9SoCnyQmkzI?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Photo by Jefferson Santos</a> on <a href="https://unsplash.com?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Unsplash</a></p>

<p style="text-align:center;font-size:0.78rem;color:#94a3b8;">📷 <a href="https://unsplash.com/photos/ladder-on-brown-wooden-bookshelf-g_Y9K409vNw?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Photo by Mitchell Luo</a> on <a href="https://unsplash.com?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Unsplash</a></p>
