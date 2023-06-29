<h1 align="center">Sunsimiao: Chinese Medical LLM</h1>

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
**English | [中文](README_CN.md)**
</div>
<div align=center><img width = '400' height ='400' src ="https://github.com/thomas-yanxin/Sunsimiao/blob/master/image/sunsimiao.png"/></div>  

### Model Introduction

**Sunsimiao**, A Tang dynasty medical scientist and Taoist priest, he was known as the 'King of Medicine'. He was also known as the "King of Medicine" and was a great admirer of folk medicine, visiting and recording the experiences of the people and writing his book "A Thousand Gold Prescriptions". After the establishment of the Tang dynasty, Sun Simiao accepted the invitation to collaborate with the government on medical activities and completed the world's first national pharmacopoeia, the Tang Xin Ben Cao.  

**Sunsimiao: Chinese Medical LLM**(Abbreviations: Sunsimiao)hopes to follow the trajectory of Sun Simiao's life, focusing on folk medical experience, accumulating Chinese medical data, and attaching it to the model, dedicated to providing **safe, reliable, and universal** Chinese medical grand model.

At present, **Sunsimiao** is fine-tuned from **baichuan-7B** and **ChatGLM-6B series** of 100, 000 high quality Chinese medical data, and more data will be collected to expand the model's capabilities and iterate on the update. The details are being worked on, so stay tuned.

### List of models

| Model Name | lora weights | merged weights |
| :----: | :----: | :----: |
| Sunsimiao-01M | [modelscope](https://modelscope.cn/models/thomas/Sunsimiao_lora/summary) / [huggingface](https://huggingface.co/thomas-yanxin/Sunsimiao-0.1M-lora) | [modelscope](https://modelscope.cn/models/AI-ModelScope/Sunsimiao/summary) / huggingface |
| Sunsimiao-01M-Chat | [modelscope](https://modelscope.cn/models/thomas/Sunsimiao-01M-Chat-lora/summary) / huggingface | [modelscope](https://modelscope.cn/models/thomas/Sunsimiao-01M-Chat/summary) / huggingface |
| Sunsimiao-01M-6B | modelscope / huggingface | [modelscope](https://modelscope.cn/models/thomas/Sunsimiao-6B/summary) / huggingface |

### How to use

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
**For more information on how to use it, see [scripts](./scripts/)**

### Part of the test

| Human | Sunsimiao_01M_Chat| Sunsimiao_05M_v2 |
| :----: | ---- | ---- |
| 小孩发烧怎么办? | 如果您的孩子发烧, 您可以采取以下措施:<br/>1. 给孩子多喝水. 发烧会导致身体脱水, 所以要让孩子多喝水以补充水分和电解质.<br/>2. 给孩子服用退烧药. 如果孩子的体温超过38°C, 建议使用退烧药物来缓解症状. 但是请注意, 不要随意给孩子使用药物, 最好咨询医生的意见.<br/>3. 给孩子进行物理降温. 可以用温水擦浴、冷敷等方法帮助孩子降低体温.<br/>4. 保持室内通风. 在孩子发烧期间, 应该保持室内空气流通, 避免空气不流通导致细菌滋生.<br/>5. 观察孩子的病情变化. 如果孩子的体温持续升高或者出现其他不适症状, 应及时就医. | 如果孩子发烧, 可以采取以下措施:<br/>1. 让孩子多喝水. 水是身体的重要组成部分, 喝足够的水有助于保持体内水分平衡和促进新陈代谢.<br/>2. 用温湿毛巾敷在孩子的额头上, 帮助降低体温.<br/>3. 如果孩子有咳嗽、流鼻涕等症状, 可以用盐开水给孩子漱口或用生理盐水滴鼻子.<br/>4. 在家里准备一些退烧药, 如布洛芬等, 以备不时之需. 但需要注意的是, 药物必须按照医生的建议使用, 不能随意增加剂量或者延长用药时间. 同时, 不要让宝宝自行服用药物, 以免出现不良反应. |
| 一岁宝宝发烧能吃啥药? | 对于一岁的宝宝, 建议不要随意使用药物治疗. 如果宝宝只是轻微的发热, 可以多喝水、注意休息和观察病情变化. 如果宝宝体温超过38°C, 可以给宝宝服用退烧药, 如对乙酰氨基酚等. 但是, 一定要按照药品说明书上的用法用量进行用药, 避免过量或不足. 同时, 最好咨询医生的意见, 以确保安全有效地控制宝宝的发热症状. | 对于一岁的宝宝, 建议不要随意使用药物治疗. 如果宝宝只是轻微的发热, 可以多喝水、注意休息和观察病情变化. 如果宝宝体温超过38°C, 可以给宝宝服用退烧药, 如对乙酰氨基酚等. 但是, 一定要按照药品说明书上的用法用量进行用药, 避免过量或不足. 同时, 最好咨询医生的意见, 以确保安全有效地控制宝宝的发热症状. |
| 医生, 您好白带增多泛黄怎么回事? | 你好, 根据你的描述, 可能是阴道炎、宫颈糜烂等妇科疾病引起的. 建议你及时就医, 进行相关检查和治疗. 同时注意个人卫生, 保持外阴清洁干燥, 避免穿紧身裤或合成材料的内衣, 以免加重症状. | 你好, 根据你的描述, 可能是阴道炎、宫颈糜烂等妇科疾病引起的. 建议你及时就医, 进行相关检查和治疗. 同时注意个人卫生, 保持外阴清洁干燥, 避免穿紧身裤或合成材料的内衣, 以免加重症状. |
| 心肌梗塞能治疗吗? | 心肌梗塞是一种严重的疾病, 需要及时的治疗. 目前, 心肌梗塞的治疗主要包括药物治疗和手术治疗两种方式. 药物治疗主要是通过口服或静脉注射一些抗凝血药、扩张血管药等来改善心脏供血情况, 缓解症状. 手术治疗则是通过冠状动脉旁路移植术、支架植入术等方式来恢复心脏的正常功能. 此外, 患者还需要注意饮食健康, 保持良好的心态和生活习惯, 以促进康复. | 心肌梗塞是一种严重的疾病, 需要及时的治疗. 目前, 对于急性心肌梗塞患者来说, 最主要的是尽早开通血管, 恢复心脏供血功能. 在药物治疗的基础上, 可以采用介入手术、冠状动脉搭桥术等方法进行治疗. 同时, 还需要注意患者的饮食和生活习惯, 避免过度劳累和情绪波动等情况的发生. |
| 对于使用NOACs的患者接种COVID-疫苗, 需要注意哪些事项? | 对于使用NOACs的患者接种COVID-19疫苗, 需要特别注意以下几点:<br/>1. 建议在接种前咨询医生, 了解是否适合接种.<br/>2. 在接种期间和接种后一周内, 应避免进行剧烈运动、重体力劳动等活动, 以防出现出血等不良反应.<br/>3. 如果患者正在服用NOACs药物, 应该告知医生, 以便医生根据具体情况决定是否可以接种疫苗.<br/>4. 如果患者有任何不适或疑虑, 应及时就医并告知医生疫苗接种的情况. | 1. 患者在接受NOAC治疗期间应避免接种疫苗.<br/>2. 如果必须进行疫苗接种, 建议咨询医生的意见并遵循以下指导: <br/>a) 在开始任何一种疫苗之前, 需要告知您的医疗团队您正在服用NOAC药物; <br/>b) NOAC药物可能会影响某些疫苗的效果和安全性, 因此请务必告诉您的医疗团队您正在使用的所有药物(包括非处方药、草药等); <br/>c) 对于那些已经完成NOAC治疗并且没有出现严重副作用的患者来说, 他们可以考虑接种新冠疫苗. 但是, 如果他们在过去6个月内曾发生过严重的出血事件或血栓形成史, 则不应该接种新冠疫苗.<br/>3. 请注意, 如果您有任何疑问或担忧, 请及时与您的医疗团队联系以获取更多信息. |

### Acknowledgements

This project was initiated by **Associate Professor Xue Dong, School of Information Science and Engineering, East China University of Science and Technology**, and is supported by the following projects and platforms.
1. [LLaMA-Efficient-Tuning](https://github.com/hiyouga/LLaMA-Efficient-Tuning): Provide fine tuning codes
2. [OpenI](https://openi.pcl.ac.cn/): Provide model training computing power
3. [ModelScope](https://modelscope.cn/home): Provide training ideas and model storage
4. [Ernie-yige](https://yige.baidu.com/): Generate 
 the logo

```

@Misc{llama-efficient-tuning, 
  title = {LLaMA Efficient Tuning}, 
  author = {hiyouga}, 
  howpublished = {\url{https://github.com/hiyouga/LLaMA-Efficient-Tuning}}, 
  year = {2023}
}

```

<a href="https://github.com/thomas-yanxin/Sunsimiao/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=thomas-yanxin/Sunsimiao" />
</a>  

### Disclaimers

1. **Sun Simiao Chinese Medical LLM** has inherent limitations and may produce incorrect, harmful, offensive or otherwise undesirable output. Users should exercise caution in critical or high-risk scenarios and should not use these models as a reference for final decisions that could result in personal injury, property damage or significant loss. 

2. **Sun Simiao Chinese Medical Grand Model** is fine-tuned from the **baichuan-7B** and **ChatGLM-6B series** models and is provided "as is" and in no event shall the author, contributor or copyright owner be liable for any claims, damages or other liabilities (whether in contract, tort or otherwise) arising out of the software or the use or other dealings with the software.

3. By using **Sun Simiao Chinese Medicine LLM**, you agree to these terms and conditions and acknowledge that you understand the potential risks that may be associated with its use. You also agree to indemnify and hold harmless the authors, contributors and copyright holders from any claims, damages or liability arising out of your use of **Sun Simiao Chinese Medicine LLM**.

### Citation

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
