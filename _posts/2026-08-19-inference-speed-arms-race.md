---
layout: post
title: "当AI开始比拼'谁更快'：推理速度军备竞赛背后的真实逻辑"
date: 2026-08-19 12:00:00 +0800
categories: [AI观点, AI基础设施]
tags: [AI, 推理速度, Gemini, GPT-5.6, Cerebras, Agent]
cover: /assets/img/posts/2026-08-19-cover.png
---

> "750 tokens per second」——这个数字的意义不在于它本身有多大，而在于它意味着AI终于可以假装自己在实时思考了。

![当AI开始比拼谁更快]({{ page.cover }})

## 同一天，两家公司讲了一模一样的故事

8月中旬的这一天，Google和OpenAI几乎同时宣布了各自的"超快"模型。Google把Gemini 3.7 Flash正式开放给全球160多个国家的开发者，OpenAI则放出GPT-5.6 Sol Ultrafast的预览版，但只邀请了一小部分API客户。

两家公司想传递的信息完全一样：AI现在快到可以驱动实时Agent了。

我注意到一个有意思的细节。Google这边是直接全量上线，OpenAI那边还是邀请制。表面上看是"容量限制"，但更实际的原因可能是Cerebras的晶圆级芯片产能确实有限，而Google用的是自家TPU集群，部署节奏完全自己可控。

说白了，一个是"来吧，都能用"，一个是"别急，排着队"。同一条赛道，两种姿态。

---

## Gemini 3.7 Flash：不只是快，还便宜得离谱

先看Google这边的成绩单。

Gemini 3.7 Flash能吃下100万个输入token（大约75万个英文单词），吐出64000个输出token。它同时处理文本、图片、视频、音频和PDF，还能调用工具、控制电脑。Google给它的定位很明确：自主Agent的"低成本大脑"。

价格方面，到今年年底之前，输入每百万token只要0.75美元，输出3.75美元。什么概念？这比上一代Gemini 3.6 Flash发布时的价格便宜一半。当然，明年1月1号开始价格翻倍，但即便翻倍后，在同级别模型里依然算便宜。

我自己比较关心的是那个编码测试。Google说同一个编程任务，3.7 Flash用了2分13秒完成，而上一代Flash用了超过5分钟。速度提升了一倍多，质量也有明显差距——Google自己的说法是"肉眼可见"。

不过话说回来，"Google自己的基准测试"这五个字本身就值得打个折扣。但如果你用过3.6 Flash再试3.7，体感上的提升确实存在。这东西不是一个需要跑benchmark才能感知到的差异。

![AI芯片与数据中心的未来](/assets/img/posts/2026-08-19-photo1.jpg)
<p style="text-align:center;font-size:0.78rem;color:#94a3b8;">📷 <a href="https://unsplash.com/photos/a-computer-circuit-board-with-a-brain-on-it-_0iV9LmPDn0?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Photo by Steve A Johnson</a> on <a href="https://unsplash.com?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Unsplash</a></p>

## GPT-5.6 Sol Ultrafast：借别人的刀，砍自己的路

OpenAI这边的策略更有意思。

Ultrafast不是新模型，它就是GPT-5.6 Sol，只不过跑在Cerebras的晶圆级芯片上，所以快了14倍。750 tokens per second，换算下来差不多每秒560个英文单词。这个速度已经快到什么程度？快到语音Agent可以在通话过程中"边想边说"，不用先沉默三秒再往外蹦字。

Jane Street的AI工程师说这种速度"让模型的使用方式完全不同了"。Podium的产品负责人说它"完全改变了通话体验"。这些都是OpenAI官方引用的客户评价，得打折看。不过他们说的方向没错：速度到达某个阈值之后，确实会催生新的应用形态。

OpenAI没公布Ultrafast模式的基准测试分数，只说了是"同样的GPT-5.6 Sol"。这其实透露了一个信号：OpenAI对自家旗舰模型的能力是有信心的，它现在要解决的不是"够不够聪明"的问题，而是"够不够快"的问题。

风向确实在变。

---

## 从"谁最聪明"到"谁够快"：赛道的切换

过去两年，AI行业的竞争叙事一直是"谁的benchmark分数更高"。GPT-4出来的时候比Claude强，Claude 3.5又追上来，Gemini Pro试图居中——大家在数学推理、编程能力、多模态理解上反复角力。

但现在风向变了。

原因是Agent。当AI从"你问一句它答一句"变成"你给个目标，它自己拆解任务、调用工具、多步执行"，延迟就成了致命瓶颈。一个自主Agent可能需要在一次任务中调用模型几十次。如果每次调用都要等几秒钟，整个流程就变得不可忍受。但如果每次调用只需要零点几秒，Agent的体验就完全不同了。

| 维度 | Gemini 3.7 Flash | GPT-5.6 Sol Ultrafast |
|------|-----------------|----------------------|
| 可用性 | 全量上线（160+国家） | 邀请制 |
| 输入上限 | 100万token | 与GPT-5.6 Sol相同 |
| 输出上限 | 6.4万token | 与GPT-5.6 Sol相同 |
| 速度提升 | 相比上代快约2.3倍 | 相比标准模式快14倍 |
| 硬件 | Google TPU | Cerebras晶圆级芯片 |
| 输入价格 | $0.75/M（年底前） | 未公开 |
| 输出价格 | $3.75/M（年底前） | 未公开 |

这张表对比下来，两家选择了完全不同的路径。Google押注"用自家硬件把模型做到又快又便宜，直接铺给所有人"，OpenAI则是"我的模型够强了，现在借Cerebras的硬件来补速度短板"。

哪种策略更好？现在下结论太早。但有一点我觉得值得注意：Google的定价策略明显是冲着"用低价把开发者生态抢过来"去的。年底前的促销价，说白了就是在抢用户。等到明年价格翻倍，你已经用习惯了，迁移成本早就盖过了差价。这招互联网公司玩了几十年了，熟悉的味道。

![芯片微观世界](/assets/img/posts/2026-08-19-photo2.jpg)
<p style="text-align:center;font-size:0.78rem;color:#94a3b8;">📷 <a href="https://unsplash.com/photos/tilt-shift-photography-of-green-computer-motherboard-bN5XdU-bap4?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Photo by Chris Ried</a> on <a href="https://unsplash.com?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Unsplash</a></p>

## 速度的尽头是什么？

说真的，我有时候会想，这个速度竞赛最终会停在哪里。

750 tokens per second听起来很快，但对于一个需要同时处理多个Agent任务的系统来说，可能还不够。而且速度越快，对后端的压力就越大——Cerebras芯片再强，单张晶圆的产能也是有限的。OpenAI选择邀请制，恐怕不只是营销策略，而是真的供不上。

更深一层的问题是：当速度不再是瓶颈，下一个瓶颈是什么？

我觉得答案可能是可靠性。Agent能在0.1秒内给你一个回答，但如果这个回答有10%的概率是错的——在自主执行多步任务的时候，错误会累积、放大。一个两步任务，每步90%的准确率，整体成功率就只剩81%。十步任务呢？直接掉到35%以下。

所以这个行业可能在经历一个"先堆速度，再补可靠性"的周期。像极了当年互联网的"先上线再迭代"，只不过现在迭代的代价可能更高——因为Agent在自动执行操作，一个错误可能不只是显示个404页面，而是真的把钱转走了或者把数据库删了。

---

## 几个值得关注的后续信号

如果你在关注这个方向，我觉得接下来这几个时间节点值得盯：

1. OpenAI Ultrafast的公开时间表。Cerebras产能跟不上的话，这个"预览"阶段可能会持续比预期更久。
2. Google年底的价格翻倍。看看有多少开发者会因此转向其他选择，还是乖乖接受涨价。
3. Anthropic和Meta的跟进。速度赛道不可能只有两家玩。Anthropic如果推出更快的Claude推理模式，Meta如果用Llama在这个方向发力，竞争格局会立刻变化。
4. 实际Agent产品的用户反馈。benchmark归benchmark，真正跑起Agent任务来，体感延迟和可靠性才是决定产品能不能用的关键。

> 速度是Agent时代的入场券，但不是通行证。能快是好事，能快还能不犯错，那才是真正的门槛。

回到开头那个数字。750 tokens per second，大约每秒560个单词。人类正常说话的速度大概是每秒2-3个单词。AI在文字输出上已经比人类快了将近200倍，现在它又提速了14倍。我们正在制造一种"思考速度"远超自身的工具，然后指望它能帮我们处理越来越多的事情。

这个趋势到底会走向何方，说实话我现在也看不太清。但有一点是确定的：速度竞赛才刚刚开始，而且它正在重新定义"AI够不够好"这个问题的标准。