---
layout: post
title: 'token见顶了，钱还在抢跑'
date: 2026-10-20 12:00:00 +0800
categories: [AI观点]
tags: [OpenAI融资, 高收益债, CoreWeave, 算力, 信用市场]
author: toby
cover: /assets/img/posts/2026-10-20-ai-token-plateau-capital-race-cover.png
description: '同一周里三条曲线分手：股权市场在抢跑，token曲线在喘气，债市直接报出了63%的违约概率。'
---

> 同一个星期里，三件事同时发生：OpenAI在抢一笔300亿美元的融资，估值要冲1.4万亿；CoreWeave的债券收益率摸到16%，信用市场给它的五年违约概率标到了63%；而那条支撑着所有故事的曲线——token用量——三年半以来第一次露出了疲态。钱在踩地板油，表盘上的转速在掉。

![token见顶了，钱还在抢跑]({{ page.cover }})

## 十一周翻倍的机器，第一次喘气

要看懂这轮AI繁荣，别盯着发布会，盯OpenRouter。这个「统一的模型接口」从四个模型起步，如今接入五百多个模型，token用量自上线以来涨了三万倍，年化运行率超过4.5千万亿（quadrillion）。据其早期投资方Menlo Ventures的披露，它连续三年保持33%的月增长，折算下来大约每十一个星期翻一倍。这个数字不是虚荣指标，它是「推理时扩展」时代的水表：模型越会思考，烧掉的token越多，「用量驱动的收入故事」就越成立。

10月20日，HN上出现一个帖子，标题直白：《Token-maxxing已死》。作者观察到OpenRouter的用量曲线出现了平台期。帖子很快被flag了，但评论区拿出的辩护反而更说明问题：有人说用量大头是Agent框架在反复刷系统提示词，一次请求二三十k token的开销「用十几行Python就能省掉」；有人说大家正在集体换用Flash级别的便宜模型，MiniMax当天发布的低延迟新模型冲上了热榜。你品品这两条辩护——它们等于承认，增长引擎已经从「用得更多」切换成了「用得更省」：缓存命中率上去了，单次请求的token数下来了，思考过程被砍短了。水表还在转，只是转得越来越慢。对整个行业的叙事来说，这两种说法没有任何区别。

## 钱在抢IPO前的最后一个座位

资本市场没工夫等水表。路透10月19日的独家消息：OpenAI正抢在Anthropic预计11月中旬的IPO之前，加速推进一轮约300亿美元的融资，估值超过1.4万亿美元。要知道今年3月它才刚以8520亿美元的估值完成破纪录的1220亿美元融资（含亚马逊最高500亿美元的承诺）。七个月，估值再涨64%以上。它目前的年化营收约500亿美元，年底目标700亿——就算一分不差地达标，市销率仍有20倍。

这个数字本身不新鲜，新鲜的是节奏。为什么这么急？答案就写在新闻导语里：「赶在Anthropic之前」。两家头部实验室正在向同一批投资人募资，谁先锁定定价，谁就把资金池抽干。同一天，彭博报道算力新贵Nscale正在与Anthropic磋商第二笔约450亿美元的算力合同——而第一笔450亿8月26日刚签掉：西弗吉尼亚460兆瓦、英伟达Vera Rubin芯片、六年租约。第一笔还没交付，第二笔已经在谈了。

这不是信心的节奏，是抢跑的节奏。当一家公司融资的紧迫性来自对手的融资时间表，说明两边都清楚这口井的水位。股权市场的估值由「最后一轮」定价，而最后一轮的出价人，正变得比token曲线更不耐烦。

![数据中心里密密麻麻的线缆，每一根都在计费](/assets/img/posts/2026-10-20-ai-token-plateau-capital-race-photo1.jpg)

## 债市先说真话

股权市场可以按梦想定价，债券市场只能按现金流定价。10月中旬，背负约500亿美元债务的「新云」CoreWeave，2031年到期债券的价格跌到79美分，收益率逼近16%——远超市场通常认定「困境」的水平。马斯克在社交媒体上对这组数字只回了两个词：Yikes。更冷的是信用违约互换：为它的债买保险的成本爬到约1000个基点，市场给它五年内违约的定价是63%的概率——一年前，这个数字是30%。别忘了它背后站着英伟达，兜底协议签到2032年4月，卖不掉的算力照单全收。连这种级别的背书都压不住收益率，说明债市担心的早已不是某一家公司，而是整条融资结构。

结构变化有更硬的数字。据巴克莱统计，2025年数据中心债券发行360亿美元，其中垃圾债只有86亿；今年发行800亿，垃圾债占到370亿——占比从不到四分之一涨到接近一半，规模是去年的四倍多。研究机构Gartner测算，如果维持当前投入节奏，到2030年约80%的neocloud可能关门，超过3.5万亿美元的AI支出面临减值风险。标普全球的数字基础设施负责人Mark Habib则在10月19日的伦敦圆桌上说了句大实话：「可以安全地假设，还有我们看不到的债。」他指的是那些「互联融资结构」——巨头为数据中心建设担保、又回头采购小公司的算力，这些循环计息的债务，很多根本不进资产负债表。

![交易屏幕上跳动的红色数字，是债市在发言](/assets/img/posts/2026-10-20-ai-token-plateau-capital-race-photo2.jpg)

## 结语

三条曲线里，token是唯一没法靠修辞改善的那条。营收可以做「年化」，估值可以找「对标」，违约概率可以用兜底协议对冲，唯独水表上的数字，是几亿个真实请求一秒一秒累出来的。所以下一阶段的裁判不是分析师，而是那条曲线：如果它恢复十一个周翻倍的斜率，1.4万亿就是便宜的；如果它继续喘气，股权市场最后一位出价人，就要独自面对债市早已标好的价格。Anthropic十一月的IPO定价会给出第一个裁决——它按OpenAI的倍数定价，还是按CoreWeave的收益率定价。两个市场已经分手，接下来看谁先回头。

<p style="text-align:center;font-size:0.78rem;color:#94a3b8;">📷 <a href="https://unsplash.com/photos/fiber-optic-cables-in-network-switch-eVWWr6nmDf8?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Photo by Kirill Sh</a> on <a href="https://unsplash.com?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Unsplash</a></p>
<p style="text-align:center;font-size:0.78rem;color:#94a3b8;">📷 <a href="https://unsplash.com/photos/screen-showing-bitcoin-trading-chart-N__BnvQ_w18?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Photo by Nick Chong</a> on <a href="https://unsplash.com?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Unsplash</a></p>
