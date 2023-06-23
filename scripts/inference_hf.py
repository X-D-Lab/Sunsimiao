from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("./sunsimiao_50w", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("./sunsimiao_50w", device_map="auto", trust_remote_code=True)

query = '临床应用中，哪些经验方治疗效果好，对患者的康复有帮助？'

prompt="Below is an instruction that describes a task. Write a response that appropriately completes the request."
prompt+="### Instruction:\n{}\n\n### Response:\n".format(query)
inputs = tokenizer([prompt], return_tensors="pt")

inputs = inputs.to('cuda:0')
pred = model.generate(**inputs, max_new_tokens=512,repetition_penalty=1.1)
print(tokenizer.decode(pred.cpu()[0], skip_special_tokens=True))