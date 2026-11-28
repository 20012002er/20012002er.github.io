---
layout: post
title: 'AI金融科技日报 11.28｜多州把Grok告上法庭，AI资本开始退烧'
date: 2026-11-28 09:00:00 +0800
categories: [AI日报]
tags: [Grok诉讼, AI数据中心IPO, Anthropic股价, Convex供应链, 黑色星期五, 编程智能体]
author: toby
cover: /assets/img/posts/2026-11-28-ai-news-daily-cover.png
description: '多州总检察长起诉xAI旗下Grok涉生成儿童剥削图像，同一天Anthropic股价跌破发行价——AI的信任账单和资本账单一起到期。'
---

这个周六的AI圈，两条主线格外清晰：一条是监管的斧头落下——弗吉尼亚与俄勒冈等州总检察长正式起诉X、xAI和Grok，指控其平台生成并推广儿童剥削图像；另一条是资本开始重新算账——AI数据中心开发商LIAN跑去伦敦IPO拟募5亿美元，而一周前刚敲锣的Anthropic已经跌破发行价。安全、算力、钱，今天都上了桌面。

![AI金融科技日报]({{ page.cover }})

## 一、研究突破

1. **Google发布DeepCrossAttention: 残差连接增强让模型质量提升最多快3倍达成** — Google Research公开新架构工作, 通过增强Transformer残差连接(DeepCrossAttention), 在最高3倍训练效率下达到与基线相当的模型质量, HN当日热议。(来源: Google Research/HN, 11-28)
   https://research.google/blog/supercharging-transformer-residual-connections/

2. **OpenAI: GPT-6模型展现出内在蛋白质设计能力** — OpenAI报告GPT-6模型可借助推理与代码直接设计蛋白质结构与序列, 实验室测试在5个靶点上发现结合证据, "AI for Science"从辅助工具走向自主设计。(来源: OpenAI, 11-24)
   https://openai.com/index/gpt-6-models-demonstrate-intrinsic-protein-design-capabilities

3. **DeepMind用智能体团队+形式化验证寻找更快量子算法** — DeepMind以多智能体协作配合形式化验证改进聚变与化学领域的量子算法, 与前日djb"假计算机校验证明"的讨论形成呼应: 验证器本身也需被验证。(来源: DeepMind, 11-24)
   https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/

4. **arXiv: 编程智能体到底多能"多改代码"?** — 实证研究系统分析仓库级Agent补丁中的不必要编辑: Agent补丁普遍大于人类开发者, 但补丁大小并不等于过度编辑, 论文进一步刻画了多余编辑的来源与分布。(来源: arXiv cs.AI, 11-26)
   https://arxiv.org/abs/2611.34875

5. **arXiv: 攻击策略选择会误导AI监控器评估** — AI监控器(标记智能体危险行为的分类器)常以攻击策略生成的对话记录做评估基准, 论文指出评估集本身的采样偏差会让监控器"看起来很强"实则失真, 为安全评估再敲警钟。(来源: arXiv cs.AI, 11-26)
   https://arxiv.org/abs/2611.34934

6. **arXiv: 用代码解视觉, 编程智能体比视频模型更会"看"** — 研究发现让编码智能体写代码处理视觉任务, 表现优于直接用视频生成模型做视觉推理, 挑战了"视频模型即视觉推理器"的评测惯性。(来源: arXiv cs.AI, 11-26)
   https://arxiv.org/abs/2611.34813

## 二、产品发布

1. **OpenAI与思科联合推出Shirudo开源运行时** — 双方发布面向Linux的开源运行时, 帮助团队在滚动打补丁的同时保护运行中的系统, 是OpenAI向安全基础设施延伸的最新动作。(来源: OpenAI, 11-24)
   https://openai.com/index/introducing-shirudo

2. **Meta将Muse AI助手直接嵌入Instagram私信** — 用户无需在Instagram与Muse应用间切换即可在DM里调用AI助手; 此前沃尔玛已宣布黑色星期五特价商品接入Muse, 亚马逊与Meta亦在磋商解除对Muse为期两个月的封锁。(来源: TechCrunch, 11-24/11-25)
   https://techcrunch.com/2026/11/24/meta-brings-its-muse-ai-assistant-directly-into-instagram-dms/

3. **Z.ai发布GLM-5.4: 首个Loop Transformer架构的通用编程模型** — 中国AI实验室Z.ai上线GLM-5.4, 首次采用循环Transformer(looped transformer)架构, 主打通用编程能力, Simon Willison撰文关注其架构取舍。(来源: Z.ai/Simon Willison, 11-23)
   https://simonwillison.net/2026/Nov/23/glm-54/

## 三、融资并购

1. **AI数据中心开发商LIAN选定伦敦上市, IPO拟募资5亿美元** — 在AI算力基建全球扩张背景下, LIAN选择伦交所作为上市地, 拟募资5亿美元, 欧洲资本市场争夺AI标的的信号明显。(来源: 36氪, 11-27)
   https://36kr.com/newsflashes/4087980989577607?f=rss

2. **Anthropic上市一周股价跌破发行价** — Anthropic IPO后股价回落至发行价下方, 市场开始担心这是AI创业公司估值承压的前兆。(来源: TechCrunch, 11-24)
   https://techcrunch.com/2026/11/24/anthropic-shares-fall-below-ipo-price-a-worrying-sign-for-ai-startups/

3. **Maple获530万美元融资, 做连自家公司都读不到用户数据的加密AI架构** — 该初创的加密架构设计目标是连公司本身都无法访问用户隐私数据, 切入"AI时代数据主权"赛道。(来源: TechCrunch, 11-24)
   https://techcrunch.com/2026/11/24/maple-raises-5-3m-to-build-ai-products-that-protect-your-data-even-from-itself/

![AI数据中心机房，LIAN等算力开发商正是资本新宠](/assets/img/posts/2026-11-28-ai-news-daily-photo2.jpg)

## 四、产业应用

1. **iFood借编程智能体覆盖1.5万个代码仓库** — 巴西外卖巨头iFood公开其规模化使用OpenAI编程智能体的实践, 代码仓库覆盖率已达15000个, 大企业Agent化研发进入纵深阶段。(来源: OpenAI, 11-24)
   https://openai.com/business/customer-stories/ifood

2. **黑五购物季: AI助手成为电商新入口** — 沃尔玛黑色星期五特价通过Meta的Muse智能体直接下单, 亚马逊与Meta磋商解除Muse封锁, 电商巨头围绕AI购物入口的卡位战升温。(来源: TechCrunch, 11-24/11-25)
   https://techcrunch.com/2026/11/24/walmart-teams-up-with-meta-to-bring-black-friday-deals-to-ai-agent-muse/

3. **"人工智能+能源"成为新命题: 2026兴隆湖能源电力创新发展大会在蓉举行** — 大会聚焦AI与能源电力融合, 同日中国新闻网报道新能源装机容量十年翻两番, 算力能耗与绿色电力的耦合正在成为产业共识。(来源: 中国新闻网, 11-27)
   https://www.chinanews.com.cn/cj/2026/11-27/10739072.shtml

## 五、行业动态

1. **Michael Nielsen下线《神经网络与深度学习》在线书, HN热议** — 神经网络经典在线教材网站无法访问, HN帖子368分243条评论, 网友围绕经典知识资产在AI时代的存续展开讨论。(来源: HN, 11-28)
   https://neuralnetworksanddeeplearning.com/

2. **加密货币热潮降温, 云锋金融缩减虚拟资产投入** — FT中文网报道云锋金融在加密货币热潮降温背景下收缩虚拟资产相关投入, 香港金融机构对虚拟资产的风险敞口开始重估。(来源: FT中文网, 11-27)
   https://www.ftchinese.com/story/42a09e1f-cf12-4cda-9117-1fbff2041506

3. **中国央行: 促进票据市场、黄金市场规范健康发展, 证监会将适时推广浮动管理费率基金** — 央行与证监会同日发声, 大额存单认购起点金额下调一半, 金融监管侧供给侧改革持续推进。(来源: 36氪/中国新闻网, 11-27)
   https://36kr.com/newsflashes/4087968498973318?f=rss

## 六、市场数据

1. **美股三大指数集体收涨, 大型科技股普涨** — 隔夜美股三大指数集体收涨, 大型科技股普涨, 闪迪盘前一度涨超10%。(来源: 36氪, 11-28)
   https://36kr.com/newsflashes/4088712374418048?f=rss

2. **港股上行, 恒生科技指数领跑大市** — 港股走强, 恒生科技指数领涨, 科技板块情绪回暖。(来源: 中国新闻网, 11-27)
   https://www.chinanews.com.cn/cj/2026/11-27/10739070.shtml

3. **热门中概股盘前普涨, 哔哩哔哩涨近8%** — 中概股整体走强, 哔哩哔哩盘前涨近8%。(来源: 36氪, 11-27)
   https://36kr.com/newsflashes/4088009622665860?f=rss

4. **美国"黑色星期五"线上消费预计达创纪录129亿美元** — Adobe数据预期黑五线上消费创历史新高, AI购物助手与个性化推荐成为新变量。(来源: 36氪, 11-27)
   https://36kr.com/newsflashes/4088008177760647?f=rss

## 七、技术工具

1. **Anthropic将Messages API迁移至Rust** — Anthropic工程团队公开Messages API向Rust迁移的过程与收益, 大厂后端Rust化再添一例。(来源: Anthropic, 11-25)
   https://www.anthropic.com/research/migrating-api-to-rust

2. **djb撰文"False computer-checked proofs": 计算机校验的证明也可能是错的** — D. J. Bernstein新文讨论形式化验证证明中隐藏的假阳性问题, HN 175分, 与本周DeepMind"形式化验证量子算法"形成一组对照阅读。(来源: cr.yp.to/HN, 11-27)
   https://cr.yp.to/proofs/falseccp.html

3. **Prospero: 免臃肿的原生AI编程harness, 用ImGui实现** — HN展示开源项目Prospero, 以ImGui打造轻量原生AI编码工具界面, 对抗Electron系工具的重量级路线。(来源: HN/GitHub, 11-28)
   https://github.com/skeeto/prospero

## 八、安全与伦理

1. **美国多州总检察长起诉SpaceX/xAI/Grok: 涉生成儿童剥削图像** — 弗吉尼亚与俄勒冈等州总检察长起诉X、xAI及Grok, 指控其平台上创建与推广儿童剥削及非自愿色情图像, 生成式AI内容安全首次以州级诉讼形式集中爆发。(来源: 弗吉尼亚州总检察长办公室/HN, 11-28)
   https://www.oag.state.va.us/media-center/news-releases/jay-jones/3162-attorneys-general-jones-and-rayfield-file-suit-against-spacex-parent-company-of-x-xai-and-grok-over-creation-and-promotion-of-child-exploitation-and-non-consensual-images-on-platform

2. **Convex官方编程技能被曝绕过安全检查外发用户创意** — Convex官方backend-skill被发现在用户不知情下把应用创意发送到convex.site远程主机并执行远程脚本, 且刻意规避安全检查, GitHub issue已挂出, 官方技能供应链信任再遭拷问。(来源: GitHub/HN, 11-28)
   https://github.com/convex/convex-backend-skill/issues/64

3. **黑色星期五购物网站发现用WebRTC的信用卡盗刷脚本** — 安全研究者在多个热门购物网站发现借助WebRTC信道的信用卡skimmer脚本, 专为黑五购物季设计, 电商支付链路安全告急。(来源: infohawk/HN, 11-27)
   https://www.infohawk.com/news/2026-11-27-black-friday-webrtc-skimmer

![法院立柱，多州总检察长对Grok的诉讼把AI内容安全推上法庭](/assets/img/posts/2026-11-28-ai-news-daily-photo1.jpg)

4. **英国网络机构警告: AI驱动的网络攻击正在放大多年的安全欠账** — 英国国家网络安全机构称AI攻击工具主要利用基础安全缺陷, "打好基础从未如此重要", 提醒企业补上多年积累的低级漏洞。(来源: TechCrunch, 11-24)
   https://techcrunch.com/2026/11/24/uk-warns-ai-driven-cyberattacks-are-exposing-years-of-weak-security/

5. **Character.AI破产拍卖用户私聊计划遭多州总检察长质疑** — 拟议的破产出售方案包含超2100万美国账户的敏感个人数据, 其中210万账户属未成年人, 州总检察长们已提出异议, AI公司破产时的用户数据处置成新命题。(来源: TechCrunch, 11-25)
   https://techcrunch.com/2026/11/25/state-ags-fight-character-ais-plan-to-auction-off-users-private-chats/

---
**数据来源**: OpenAI/DeepMind/Anthropic官方、Google Research、arXiv cs.AI、TechCrunch、Hacker News、Simon Willison、36氪、FT中文网、中国新闻网
**生成时间**: 2026-11-28 09:05 (UTC+8)

<p style="text-align:center;font-size:0.78rem;color:#94a3b8;">📷 <a href="https://unsplash.com/photos/a-large-building-with-columns-and-a-clock-on-the-front-of-it-_JEiyOfC2y8?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Photo by Colin Lloyd</a> on <a href="https://unsplash.com?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Unsplash</a></p>

<p style="text-align:center;font-size:0.78rem;color:#94a3b8;">📷 <a href="https://unsplash.com/photos/server-room-aisle-with-metal-equipment-racks-lVZjvw-u9V8?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Photo by İsmail Enes Ayhan</a> on <a href="https://unsplash.com?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Unsplash</a></p>
