<h1 align="center">孙思邈中文医疗大模型</h1>
<p align="center">

<p align="center">
<a href="https://github.com/thomas-yanxin/Sunsimiao"><img src="https://img.shields.io/badge/GitHub-24292e" alt="github"></a>
<a href="https://huggingface.co/thomas-yanxin/Sunsimiao-01M-lora"><img src="https://img.shields.io/badge/HuggingFace-yellow" alt="HuggingFace"></a>
<a href="https://modelscope.cn/models/thomas/Sunsimiao_lora/summary"><img src="https://img.shields.io/badge/ModelScope-blueviolet" alt="modelscope"></a>
<a href="https://openi.pcl.ac.cn/Learning-Develop-Union/Sunsimiao"><img src="https://img.shields.io/badge/-OpenI-337AFF" alt="OpenI"></a>
</p> 

<div align="center">

[![GitHub Stars](https://img.shields.io/github/stars/thomas-yanxin/Sunsimiao)](https://github.com/thomas-yanxin/Sunsimiao/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/thomas-yanxin/Sunsimiao)](https://github.com/thomas-yanxin/Sunsimiao/fork)
[![GitHub Contributors](https://img.shields.io/github/contributors/thomas-yanxin/Sunsimiao)](https://github.com/thomas-yanxin/Sunsimiao/graphs/contributors)  
**[中文](README_CN.md) | [English](README_EN.md)**

**在线体验：[ModelScope](https://modelscope.cn/studios/jingnant/Sunsimiao)**
</div>

<div align="center">

👋 **联系我们**: xd.lab2023@gmail.com

</div>


<div align=center><img width = '400' height ='400' src ="https://github.com/X-D-Lab/Sunsimiao/blob/master/image/sunsimiao.png"/></div>  

</div>

<br>

## 🎉 项目进展


**🔥更好的模型永远在路上!🔥**

* Sept 12,2024： **上传Sunsimiao-7B**至[WiseModel](https://wisemodel.cn/models/Alanjn/Sunsimiao-7B-Qwen2/intro),以供下载

* Sept 9,2024： **提供Sunsimiao-7B**模型**在线体验**，欢迎前往[ModelScope](https://modelscope.cn/studios/jingnant/Sunsimiao)体验模型！
  
* Jul 23,2024： **开源**7B量级模型**Sunsimiao-7B**！由**Qwen2-7B**微调而得，擅长于**医学问答、医学考试**。
  
* Jul 6, 2023： **首次**提交孙思邈（Sunsimiao）中文医疗大模型

## 🌈  模型介绍

**孙思邈**, 唐代医药学家、道士, 被后人尊称为"药王". 其十分重视民间的医疗经验, 不断积累走访, 及时记录下来, 写下著作《千金要方》. 唐朝建立后, 孙思邈接受朝廷的邀请, 与政府合作开展医学活动, 完成了世界上第一部国家药典《唐新本草》.  

**孙思邈中文医疗大模型**(简称: Sunsimiao)希望能够遵循孙思邈的生平轨迹, 重视民间医疗经验, 不断累积中文医疗数据, 并将数据附加给模型, 致力于提供**安全、可靠、普惠**的中文医疗大模型.

🚩 **Sunsimiao-7B**模型由**Qwen2-7B**模型与**高质量医疗数据微调**而得，在**CMB-Exam**中达到**30B**量级模型**SOTA！** 同时在**中国国家执业医师、药师、护士资格考试**中均取得**优异成绩**。



## 📅  模型列表

| 模型名称 | lora权重 | 合并后的权重 |
| :----: | :----: | :----: |
| :new:Sunsimiao-7B |🤖modelscope / 🤗huggingface|[🤖modelscope](https://www.modelscope.cn/models/X-D-Lab/Sunsimiao-Qwen2-7B) /✡️[WiseModel](https://wisemodel.cn/models/Alanjn/Sunsimiao-7B-Qwen2/intro)/ 🤗huggingface|
| Sunsimiao-01M | [🤖modelscope](https://modelscope.cn/models/thomas/Sunsimiao_lora/summary) / [🤗huggingface](https://huggingface.co/thomas-yanxin/Sunsimiao-0.1M-lora) | [🤖modelscope](https://modelscope.cn/models/AI-ModelScope/Sunsimiao/summary) / 🤗huggingface |
| Sunsimiao-01M-Chat | [🤖modelscope](https://modelscope.cn/models/thomas/Sunsimiao-01M-Chat-lora/summary) / 🤗huggingface | [🤖modelscope](https://modelscope.cn/models/thomas/Sunsimiao-01M-Chat/summary) / 🤗huggingface |
| Sunsimiao-01M-6B | 🤖modelscope / 🤗huggingface | [🤖modelscope](https://modelscope.cn/models/thomas/Sunsimiao-6B/summary) / 🤗huggingface |



## 📚 数据详情

**Sunsimiao**的各个版本训练数据均取自我们精心构建的**医疗数据池**，该数据池融合各类**医疗文献及教材、多科室诊断数据、海量医疗问诊对话、医学知识问答、病历分析**等，基于**开源数据**和**GPT4自动构建**，经**人工清洗标注、自动化数据分析处理**所得。
<div align='center'><img src='https://github.com/X-D-Lab/Sunsimiao/blob/master/image/data_info.png' width='750px'></div>

**该数据池仍在持续更新中！** 部分数据样例参考：`data/example_single.json` `data/example_multi.json`



## 🎓 模型评估
##### CMB-Exam
**Sunsimiao-7B**在**CMB-Exam**中具体表现如下：
<div align='center'><img src='https://github.com/X-D-Lab/Sunsimiao/blob/master/image/cmb_eval.png' width='550px'></div>

注：图中模型分数均取自CMB榜单数据，具体分数统计于`data/cmb_compare.xlsx`，详见：[CMB-Leaderboard](https://cmedbenchmark.llmzoo.com/static/leaderboard.html)

#### 考试表现
<div align='left'>

| 模型名称 | 考试名称 | 题目数量 | 准确率 |
| :----: | :----: | :----: | :----: |
| Sunsimiao-7B|中国国家执业医师资格考试|3000|79.23%|
| Sunsimiao-7B|中国国家执业药师资格考试|2400|71.33%|
| Sunsimiao-7B|中国国家执业护士资格考试|1200|83.83%|

</div>

## 🔓 使用方法

```Python
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

pipe = pipeline(task=Tasks.text_generation, model='AI-ModelScope/Sunsimiao', model_revision='v1.0.0')

query = '小孩发烧了怎么办？'

prompt="Below is an instruction that describes a task. Write a response that appropriately completes the request."
prompt+="### Instruction:\n{}\n\n### Response:\n".format(query)

result = pipe(prompt)
print(result)
```

```
{'text': 'Below is an instruction that describes a task. Write a response that appropriately completes the request.### Instruction:\n小孩发烧了怎么办？\n\n### Response:\n\n如果您的孩子发烧了，您可以参考以下建议：\n\n1. 帮助孩子退热：\n\n将冷水倒入一个杯子，放在孩子的腋下(或额头)，每5分钟转一次。\n\n将冰毛巾擦在孩子的胸部、颈部和后背。\n\n将退烧药放在孩子额头或颈部。\n\n2. 检查孩子的症状：\n\n是否咳嗽、鼻塞或流鼻涕？\n\n3. 根据症状：\n\n如果孩子咳嗽，可以给孩子喝些水或温水，并给孩子喝一些蜂蜜;\n\n如果孩子鼻塞，可以给孩子吸入一些蒸汽;\n\n如果孩子发烧，可以给孩子喂些温水，并让孩子休息;\n\n如果孩子呼吸急促或呼吸困难，应立即就医。\n\n4. 如果孩子有其他不适：\n\n如果孩子没有食欲或呕吐，可以给孩子吃些软餐;\n\n如果孩子感到疲倦，可以让孩子休息;\n\n如果孩子的眼睛出现红色或分泌物，应立即就医。\n\n5. 注意孩子的个人卫生：\n\n让孩子勤喝水，勤洗手，保持室内通风;\n\n避免孩子与别的孩子进行密切接触，以免传染。\n\n祝您的孩子早日康复！'}
```  
**更多使用方法见[scripts](./scripts/)**


### 致谢

本项目由**华东理工大学 信息科学与工程学院 薛栋副教授**发起, 并受到以下项目及平台的大力支持, 在此表示感谢!
1. [LLaMA-Efficient-Tuning](https://github.com/hiyouga/LLaMA-Efficient-Tuning): 提供微调代码
2. [OpenI启智社区](https://openi.pcl.ac.cn/): 提供模型训练算力
3. **魔搭ModelScope、OpenXLab、Huggingface**：模型存储和体验空间;
4. [文心一格](https://yige.baidu.com/): 生成模型logo

特别感谢**上海人工智能实验室推出的书生·浦语大模型实战营**、[**InternStudio**](https://studio.intern-ai.org.cn/)为我们的项目提供宝贵的技术指导和强大的算力支持! 
<div align="center">
</div>

```
@Misc{llama-efficient-tuning, 
  title = {LLaMA Efficient Tuning}, 
  author = {hiyouga}, 
  howpublished = {\url{https://github.com/hiyouga/LLaMA-Efficient-Tuning}}, 
  year = {2023}
}

@article{qwen,
  title={Qwen Technical Report},
  author={Jinze Bai and Shuai Bai and Yunfei Chu and Zeyu Cui and Kai Dang and Xiaodong Deng and Yang Fan and Wenbin Ge and Yu Han and Fei Huang and Binyuan Hui and Luo Ji and Mei Li and Junyang Lin and Runji Lin and Dayiheng Liu and Gao Liu and Chengqiang Lu and Keming Lu and Jianxin Ma and Rui Men and Xingzhang Ren and Xuancheng Ren and Chuanqi Tan and Sinan Tan and Jianhong Tu and Peng Wang and Shijie Wang and Wei Wang and Shengguang Wu and Benfeng Xu and Jin Xu and An Yang and Hao Yang and Jian Yang and Shusheng Yang and Yang Yao and Bowen Yu and Hongyi Yuan and Zheng Yuan and Jianwei Zhang and Xingxuan Zhang and Yichang Zhang and Zhenru Zhang and Chang Zhou and Jingren Zhou and Xiaohuan Zhou and Tianhang Zhu},
  journal={arXiv preprint arXiv:2309.16609},
  year={2023}
}

@misc{2023internlm,
    title={InternLM: A Multilingual Language Model with Progressively Enhanced Capabilities},
    author={InternLM Team},
    howpublished = {\url{https://github.com/InternLM/InternLM-techreport}},
    year={2023}
}
```

<a href="https://github.com/thomas-yanxin/Sunsimiao/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=thomas-yanxin/Sunsimiao" />
</a>  

### 免责申明

1. **孙思邈中文医疗大模型**存在固有的局限性, 可能产生错误的、有害的、冒犯性的或其他不良的输出. 用户在关键或高风险场景中应谨慎行事, 不要使用这些模型作为最终决策参考, 以免导致人身伤害、财产损失或重大损失. 

2. **孙思邈中文医疗大模型**由**baichuan-7B**、**Qwen2-7B**模型微调而得, 按"原样"提供, 在任何情况下, 作者、贡献者或版权所有者均不对因软件或使用或其他软件交易而产生的任何索赔、损害赔偿或其他责任(无论是合同、侵权还是其他原因)承担责任.

3. 使用**孙思邈中文医疗大模型**即表示您同意这些条款和条件, 并承认您了解其使用可能带来的潜在风险. 您还同意赔偿并使作者、贡献者和版权所有者免受因您使用**孙思邈中医药大模型**而产生的任何索赔、损害赔偿或责任的影响.

### 引用

```

@misc{Sunsimiao, 
  author={Xin Yan, Dong Xue*}, 
  title = {Sunsimiao: Chinese Medicine LLM}, 
  year = {2023}, 
  publisher = {GitHub}, 
  journal = {GitHub repository}, 
  howpublished = {\url{https://github.com/thomas-yanxin/Sunsimiao}}, 
}
```
