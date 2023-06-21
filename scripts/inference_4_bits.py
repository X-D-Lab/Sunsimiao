import torch
from modelscope.hub.snapshot_download import snapshot_download
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer

cache_dir = './sunsimiao/'

model_dir = snapshot_download('baichuan-inc/baichuan-7B',
                              cache_dir=cache_dir,
                              revision='v1.0.0')
model_dir_sft = snapshot_download('thomas/Sunsimiao_lora',
                                  cache_dir=cache_dir,
                                  revision='v1.0.0')

tokenizer = AutoTokenizer.from_pretrained(cache_dir +
                                          "baichuan-inc/baichuan-7B",
                                          trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(cache_dir +
                                             "baichuan-inc/baichuan-7B",
                                             device_map="auto",
                                             trust_remote_code=True,
                                             low_cpu_mem_usage=True,
                                             load_in_4bit=True,
                                             torch_dtype=torch.float16)

model = PeftModel.from_pretrained(model, cache_dir + "thomas/Sunsimiao_lora")
streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)
query = "晚上睡不着怎么办？"

prompt = "Below is an instruction that describes a task. Write a response that appropriately completes the request."
prompt += "### Instruction:\n{}\n\n### Response:\n".format(query)
inputs = tokenizer([prompt], return_tensors="pt")
inputs = inputs.to("cuda")
generate_ids = model.generate(**inputs, max_new_tokens=256, streamer=streamer)
