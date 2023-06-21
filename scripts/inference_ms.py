from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

pipe = pipeline(task=Tasks.text_generation,
                model='AI-ModelScope/Sunsimiao',
                model_revision='v1.0.0')

query = '小孩发烧了怎么办？'

prompt = "Below is an instruction that describes a task. Write a response that appropriately completes the request."
prompt += "### Instruction:\n{}\n\n### Response:\n".format(query)

result = pipe(prompt)
print(result)