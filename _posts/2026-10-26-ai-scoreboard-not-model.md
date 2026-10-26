---
layout: post
title: '赢的不是模型，是计分板'
date: 2026-10-26 12:00:00 +0800
categories: [AI观点]
tags: [AI科学家, 自动验证, 量子计算, 蛋白质设计, 皮肤癌诊断, 评测基准]
author: toby
cover: /assets/img/posts/2026-10-26-ai-scoreboard-not-model-cover.png
description: 'Claude把量子电路效率推高一个量级、设计出蝎毒结合蛋白，却被一个2015年的CNN在皮肤癌上按着打——这三件事其实是同一件事。'
---

> 同一个星期里，Anthropic宣布Claude设计的量子电路效率超过已发表最优方案，实验室测出了能咬住蝎子神经毒素的蛋白；而一位皮肤科医生在自己做的两百例测试里，看着GPT-6 Astra和Claude Fable 5.1把一张恶性黑色素瘤认成「无害的脂溢性角化病，可以回家」。如果你把这三条新闻当成三条新闻，你会得出「AI又强又不行」的糊涂账。它们其实是同一件事的三张照片。

![赢的不是模型，是计分板]({{ page.cover }})

## 八道题，一个循环：赢在计分板手里

先看量子电路这件事的真正配方。Anthropic没有让Claude「自由发挥量子力学才华」，他们做的东西寒酸得很：八道题——来自化学、优化、物理模拟和数论——每道题只用自然语言写清楚电路必须算什么，然后配一个自动评分器，按量子比特数和Toffoli门数打分。分数喂回给Claude，Claude改一版，再评分，再改。如此循环。

结果：八道题里七道，门数和量子比特数双双显著下降；剩下那道模逆运算，Claude没走寻常路，自己翻出了一篇关于divsteps算法的老论文，判断这个思路搬到量子场景有戏，做出了一种新的可逆架构，在门数和比特数的权衡上比已有设计更划算。The Quantum Insider给的对照数字很具体：椭圆曲线运算那道题，基线设计要510万个Toffoli门，Claude的版本砍掉一大截，峰值量子比特需求也从1938压到1837。

这里最该被盯住的不是「提升一个量级」，而是那个循环的形状。Claude是靠懂量子物理赢的吗？不是。它是靠**每一轮都能拿到一个不带情面的分数**赢的。题目可以被代码验证——这类量子算法每个输入都有确定输出，普通计算机就能对答案——所以「懂不懂」这件事被外包给了评分器，模型只负责在分数的鞭子下往前挪。八道题，每道题都有一个自动考官。这才是全部魔法。

![密布逻辑门的芯片电路板——每一道电路都有便宜的裁判](/assets/img/posts/2026-10-26-ai-scoreboard-not-model-photo1.jpg)

## 31.8万个蛋白，最后说了算的是仪器

蝎毒那篇更能说明问题。全球每年有三千多人死于蝎子蜇伤，儿童首当其冲，而抗蝎毒血清至今还是老工艺。Anthropic让内部研究版Claude自主跑了一场蛋白设计战役：给它五个神经毒素（墨西哥的Cn2、巴西的Ts1、北非的AaH I和AaH II、中东的LqhIII）和一个初始提示，之后64小时里Claude只被人类追加了四次方向性指令。它自己挑毒素结构、自己定设计靶点、自己设定质量阈值、自己调度12种设计工具，生成了**318,484个**候选蛋白，做55万次设计-毒素配对筛选，烧掉约一万GPU小时，最后挑出180个送检，加上后续补充的31个，共211个送去Adaptyv Bio和Twist Bioscience两家实验室。湿实验结果：17个达到结合标准，其中最强的Cn2-B1对墨西哥蝎毒Cn2的结合力到了个位数纳摩尔级别，竞争实验显示它结合的位点与一只已证实能在小鼠体内中和Cn2的抗体高度重合。

数字漂亮，但论文里有一句更值得裱起来的坦白：**Claude自己定的那套计算端评分体系，「在事后复盘中未能从同组设计里挑出真正的结合蛋白」**。也就是说，那31.8万个设计是用计分板筛出来的，但计分板只能负责把沙里淘到「可能有金」的粗粒；哪一粒真金，最后是由表面等离子共振仪——一台物理仪器对着真实蛋白测出来的曲线——说了算的。18%的成功率也不过是蛋白设计行业的常规水平，Claude没有点石成金，它只是把「出候选」这个环节的边际成本打到了近乎零，然后诚实地把裁判权交还给实验室。

顺带一个黑色幽默：这项研究的合作方里有一家叫Citrini Research的机构——一家金融投资研究公司。华尔街已经开始给AI科学研究出题了，这大概比任何论文摘要都更能说明资金在往哪边看。

![荧光显微镜下的细胞成像——最后的裁判是仪器，不是模拟分数](/assets/img/posts/2026-10-26-ai-scoreboard-not-model-photo2.jpg)

## 2015年的CNN，把两个前沿模型打回原形

现在看第三张照片。Lynch实验室那位皮肤科医生做了一场颇有横劲的测试：从国际皮肤影像协作组2025年公开的MILK10k数据集里随机抽200个经活检确诊的皮损——100个不能放走的（30个黑色素瘤、25个基底细胞癌、25个鳞状细胞癌、20个光化性角化病），100个可以放走的——同时喂给GPT-6 Astra、Claude Fable 5.1，和一个2015年谷歌发布的Inception v3。这个CNN架构老了十年，用公开皮肤科图像微调只花了约二十分钟。

比分：CNN答对125个，62%；两个前沿大模型分别答对84和85个，42%。更扎眼的是那个具体病例——一张不到0.8毫米厚的耳部侵袭性黑色素瘤，两个2026年的旗舰模型异口同声说是良性的脂溢性角化病，建议患者出院。当然，公道话也要说：把提问方式换成病人视角——「我需要看医生吗」——两个LLM在100个黑色素瘤里劝人就医99次和98次，几乎从不放走任何人。它们不会判别，但很会避险；这两种能力在临床上是两回事，前者是知识，后者是话术。

有人会说数据集2025年就公开了，LLM可能见过——可那只会帮它们，结果还是输。有人会说专用医疗AI早就在监管审批的产品里表现更好——完全正确，而这恰恰是我的论点而不是反驳。同一个星期，微软的Mustafa Suleyman宣布其AI在疑难病例上超越医生、剑指「医疗超级智能」。一边是实验室里两百例活检确诊的横评，一边是发布会的措辞。**区别不在模型，在计分板归谁管。**

## 结语

把三件事叠在一起看，模式清楚得近乎无趣：凡是能造出便宜、自动、不带情面的计分板的地方——电路有对答案，蛋白有折叠分数加湿实验，皮肤影像有活检金标准——AI的进展快得吓人，快到十年前的架构都还能守住城池，因为「专用+好考卷」天然碾压「通用+没有考卷」。而凡是计分板昂贵、模糊、或者干脆攥在利益相关方手里的地方，我们得到的就是「超级智能」的形容词，以及把黑色素瘤认成角化病的自信。

所以别再问「模型什么时候变聪明」。聪明的成分里，一大半是刷题刷出来的，而题，是人出的。下一个十年AI科学竞赛的真实瓶颈，不是算力，不是参数，是**肯下笨功夫把评分器造出来、把活检做掉的那批人**。计分板便宜的地方，自动化已经在路上；计分板昂贵的地方，先到的从来不是智能，是发布会。

---

*参考：Anthropic《Designing more efficient quantum circuits with Claude》（2026-10-16）及蝎毒结合蛋白技术报告（2026-10-20）；Lynch实验室《A 10-year-old CNN outperforms frontier LLMs for skin cancer diagnosis》；The Quantum Insider（2026-10-17）。*

<p style="text-align:center;font-size:0.78rem;color:#94a3b8;">📷 <a href="https://unsplash.com/photos/blue-circuit-board-jXd2FSvcRr8?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Photo by Umberto</a> on <a href="https://unsplash.com?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Unsplash</a></p>

<p style="text-align:center;font-size:0.78rem;color:#94a3b8;">📷 <a href="https://unsplash.com/photos/a-group-of-blue-and-green-lights-on-a-black-background-Dl3nfUma65A?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Photo by Tayfun Dikmen</a> on <a href="https://unsplash.com?utm_source=toby-blog&utm_medium=referral" target="_blank" rel="noopener">Unsplash</a></p>

