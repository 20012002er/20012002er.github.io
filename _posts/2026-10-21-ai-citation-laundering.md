---
layout: post
title: '谷歌把它埋了，ChatGPT把它供起来了'
date: 2026-10-21 12:00:00 +0800
categories: [AI观点]
tags: [GEO, ChatGPT搜索, 数据投毒, 引用洗白, AI搜索, 信息污染]
author: toby
cover: /assets/img/posts/2026-10-21-ai-citation-laundering-cover.png
description: '50美元、五万条全是编的假数据，谷歌把它摁死了，ChatGPT却天天去抄——现在这些数字躺在学术论文和银行研报里，煞有介事。'
---

> 今年3月，一位GEO研究员花了大约50美元：买个新域名，用GPT-4.1在一天之内生成五万个统计页面，数字全是编的，一条都没核实。七个月过去，这个网站被谷歌摁到几乎不可见，却被ChatGPT当成了香饽饽——仅过去30天，ChatGPT的实时检索就光顾了它七万二千次；它的假数据进了学术论文，进了卡塔尔最大财团的投资研报，三百多个网站反过来引用它。这件事最可怕的地方不是有人造假，而是造假根本不需要勇气——只需要五十美元。

![谷歌把它埋了，ChatGPT把它供起来了]({{ page.cover }})

## 五十美元，五万条假数据，一天上线

先把这个实验的账本摊开。网站叫stateglobe.com，号称提供200个国家在SEO、内容营销、电商、社交媒体等领域的统计数据。作者Metehan Yesilyurt用GPT-4.1一天生成了五万个统计页面，成本约30美元；后来又追加了1.5万篇清单文，花了20美元。生成用的提示词，他自己形容就两句话加一份国家与主题清单。这些数字没有任何出处、没有任何核实流程——因为它们本来就是编的，这是实验的前提，不是疏漏。

按搜索引擎时代的剧本，故事到这里就该结束了。事实也确实如此：谷歌两次算法更新之后，这个站的可见度当场崩塌，被索引页面的展示量长期在5到20之间徘徊，约等于社会性死亡。但它的后半生，活得比大多数认真做内容的网站都滋润。

原因在于，统计页面天然长着一张"被AI引用"的脸。当下越来越多的内容是AI写的，而AI写作遇到知识空洞时，最想捡的就是一个具体数字。"远程办公在增长"是句废话，"73%的员工每周至少远程办公一次"是条证据——哪怕它是编的，它也比废话更像证据。而LLM回答时的检索预算是掐着延迟和成本算的：抓几个页面、抽出相关段落、开写。整条流水线里压根没有"核实"这个工位，重排序器打的是相关性分，不是真实性分。只要一段话长得像权威，它就会被用。

![档案架上密密麻麻的资料册，每一本都曾被当作不容置疑的证据](/assets/img/posts/2026-10-21-ai-citation-laundering-photo1.jpg)

## 谷歌埋了它，ChatGPT供着它

这个实验最有信息量的部分，其实是两家引擎的分道扬镳。谷歌那边：几个月不可见，展示量个位数。ChatGPT这边：过去30天，Cloudflare记录到超过60万次爬虫请求，其中7.2万次来自ChatGPT-User——注意，这不是训练爬虫，是ChatGPT在回答真实用户问题时实时打开页面的那个agent。七个月里，仅ChatGPT一个来源就给这个假数据站送来一万多个会话。到10月7日，在作者追踪的一组提示词下，stateglobe的可见度排名第二，前面只压着一个正牌数据巨头Statista。

作者把这课总结成一句话：检索不是排名（Retrieval is not ranking）。ChatGPT不再照抄谷歌的前十名，它把你的问题改写成自己的子查询，从自建索引和缓存里拉候选，重排序，再打开几页落地。一个页面可以在谷歌那里社会性死亡，同时在LLM检索的每一步都表现优异。

这件事的行业含义，比"ChatGPT搜索质量不行"严重得多。谷歌花了二十年堆起来的反作弊体系——Penguin、Helpful Content、各种E-E-A-T信号——至少是冲着"识别垃圾"去的，真假数据在这里有待遇差。ChatGPT的自建索引还年轻，它的筛选标准里，"长得像统计页"的权重明显高过"数据可溯源"。于是一个荒诞的局面出现了：人类搜索引擎的门槛，成了AI搜索引擎的入场券。造假者不需要攻破谷歌，只需要绕开它——而绕开它的路，AI自己修好了。

## 引用洗白：假数据的镀金流水线

真正精彩的在下游。stateglobe的假数据，被一篇学术论文引用了；被卡塔尔最大金融集团的投资研报用了；被印度的经济学刊物引了。Ahrefs和Semrush数出来三百三十多个反链域名，里面有Shopify、DHL、Bluehost这种正经品牌——大概率是它们的AI生成内容在"做研究"时顺手抄的。作者还提醒：这些只是留了链接的，没留链接就把数字用掉的，只会更多。

作者给这个现象起了个准确的名字：引用洗白（citation laundering）。把流程拆开看：第一天，一个假数字挂在全新域名上，权威度为零；然后一篇论文引了它，一家银行用了它；接下来，任何下一个查这个数的人——或者模型——看到的都是一个"有出处"的数字，而且这个出处还被严肃机构背过书。假数字并没有变成真的，但每一次引用都在给它镀一层金。学术论文的公信力被拿来给一个编造的统计做担保，银行研报的风控流程，拦不住一个GPT-4.1随口编出来的数。

还有最后一环。被反复检索、被反复引用了七个月的页面，会进网络爬虫的数据池；数据池，会进下一代模型的训练集。一个GPT-4.1编出来的数字，可能就这么变成下一个模型"知识"的一部分。到那一步，连"去原始出处核实"这条退路都没了——错误已经内化成常识。

有意思的是对照组：Peec团队后来用真数据、每条注明出处，正经搭了个统计页，立刻也引来一批疑似AI批量产内容的站点反链。这个对照反而把问题照得更清楚——假数据管用，真数据同样管用。战术从来不是问题，问题是从头到尾没人验货。

![机房里成排的服务器，ChatGPT正在这样的硬件上重建一个没有门卫的互联网索引](/assets/img/posts/2026-10-21-ai-citation-laundering-photo2.jpg)

## 结语：数字的格莱欣法则

格莱欣法则说劣币驱逐良币。放到信息市场，它同样成立，而且更加彻底：当编造一条数据只要两句话和三毛钱、被引用的成本为零、而验证一条数据却要找到独立信源交叉比对时，理性人的最优策略就是编。这不是什么道德滑坡，这是教科书级的定价错误——诚实被标了价，撒谎被免了单。

所以，往后你从AI嘴里听到的每一个"据统计"，都值得多问一句：这个统计是真的有人统计过，还是某个模型在知识空洞里随手捡来的一块砖？AI搜索没有让信息变得更免费，它只是把"核实"的成本，从搜索引擎的机房挪到了每一个读者的脑子里。这笔账现在还没几个人意识到自己在付——但账单已经在路上了。


<p style="text-align:center;font-size:0.78rem;color:#94a3b8;">📷 <a href="https://unsplash.com/photos/a-row-of-bookshelves-in-a-library-filled-with-books-jiVBqdZNXcg?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Photo by Zetong Li</a> on <a href="https://unsplash.com?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Unsplash</a></p>

<p style="text-align:center;font-size:0.78rem;color:#94a3b8;">📷 <a href="https://unsplash.com/photos/close-up-of-server-cooling-fans-in-a-vibrant-data-center-iZe21DzHnUg?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Photo by Winston Chen</a> on <a href="https://unsplash.com?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Unsplash</a></p>
