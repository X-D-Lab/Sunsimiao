# 孙思邈中文医疗大模型
 <p align="center">
  <a href="https://github.com/thomas-yanxin/Sunsimiao"><img src="https://img.shields.io/badge/GitHub-24292e" alt="github"></a>
  <a href="https://huggingface.co/thomas-yanxin/Sunsimiao-0.1M-lora"><img src="https://img.shields.io/badge/HuggingFace-yellow" alt="HuggingFace"></a>
  <a href="https://modelscope.cn/models/thomas/Sunsimiao_lora/summary"><img src="https://img.shields.io/badge/ModelScope-blueviolet" alt="modelscope"></a>
  <a href="https://openi.pcl.ac.cn/Learning-Develop-Union/Sunsimiao"><img src="https://img.shields.io/badge/-OpenI-337AFF" alt="OpenI"></a>
</p> 
<div align=center><img width = '400' height ='400' src ="https://github.com/thomas-yanxin/Sunsimiao/blob/master/image/sunsimiao.png"/></div>  

### 模型介绍

**孙思邈**, 唐代医药学家、道士, 被后人尊称为"药王". 其十分重视民间的医疗经验, 不断积累走访, 及时记录下来, 写下著作《千金要方》. 唐朝建立后, 孙思邈接受朝廷的邀请, 与政府合作开展医学活动, 完成了世界上第一部国家药典《唐新本草》.  

**孙思邈中文医疗大模型**(简称: Sunsimiao)希望能够遵循孙思邈的生平轨迹, 重视民间医疗经验, 不断累积中文医疗数据, 并将数据附加给模型, 致力于提供**安全、可靠、普惠**的中文医疗大模型.

目前, **Sunsimiao**是由**baichuan-7B**在10w条高质量的中文医疗数据中通过qlora微调而得, 后续将收集更多数据, 扩充模型能力, 不断迭代更新, 相关细节工作正在整理, 敬请期待.

### 使用方法

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

### 致谢

1. [LLaMA-Efficient-Tuning](https://github.com/hiyouga/LLaMA-Efficient-Tuning): 提供微调代码
2. [OpenI启智社区](https://openi.pcl.ac.cn/): 提供模型训练算力
3. [魔搭ModelScope](https://modelscope.cn/home): 提供训练思路和模型存储
4. [文心一格](https://yige.baidu.com/): 生成模型logo

### 免责申明

1. **孙思邈中文医疗大模型**存在固有的局限性, 可能产生错误的、有害的、冒犯性的或其他不良的输出. 用户在关键或高风险场景中应谨慎行事, 不要使用这些模型作为最终决策参考, 以免导致人身伤害、财产损失或重大损失. 

2. **孙思邈中文医疗大模型**由**baichuan-7B**模型微调而得, 按"原样"提供, 在任何情况下, 作者、贡献者或版权所有者均不对因软件或使用或其他软件交易而产生的任何索赔、损害赔偿或其他责任(无论是合同、侵权还是其他原因)承担责任.

3. 使用**孙思邈中文医疗大模型**即表示您同意这些条款和条件, 并承认您了解其使用可能带来的潜在风险. 您还同意赔偿并使作者、贡献者和版权所有者免受因您使用**孙思邈中医药大模型**而产生的任何索赔、损害赔偿或责任的影响.

### 引用
@misc{Sunsimiao,
  author={Xin Yan, Dong Xue},
  title = {Sunsimiao：孙思邈中文医疗大模型},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/thomas-yanxin/Sunsimiao}},
}
