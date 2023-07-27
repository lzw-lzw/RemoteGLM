import json 
import openai
from tqdm import tqdm

# 设置 OpenAI API 账户信息
openai.api_key = "xxx"

# 翻译函数
def translate_text(text):
    prompt = "下面的几个句子是几个人描述同一张遥感图像的英文句子，不同句子之间可能有重复或相似的部分，请你根据这些句子，输出描述该遥感图像内容的一段中文文本，要保证结果的通顺简洁，且应该去除了相似或重复的部分，文本以及分句要符合中文习惯"+str(text)
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ]
    )
    return str(completion.choices[0].message['content'])

with open('./Sydney-en.json', encoding="utf-8") as f:
    data = json.load(f)

for i in tqdm(range(len(data))):
    annotation = data[i]['caption']
    translation = translate_text(annotation)
    data[i]['caption'] = str(translation)

# 写入json文件
with open('Sydney-zh.json', 'w', encoding="utf-8") as f1:
    json.dump(data, f1, indent=4,ensure_ascii=False)

