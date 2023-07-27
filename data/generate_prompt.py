import json
from tqdm import tqdm

with open('./Sydney.json',encoding="utf_8") as f:
    data = json.load(f)

data_info = []
for i in tqdm(range(len(data))):
    img = data[i]['imged_id']
    prompt = '这张遥感图像展现了什么场景？'
    label = data[i]['caption']
    json_data = {
                'img': './Sydney/'+str(img),
                'prompt': prompt,
                'label': str(label)
                }
    data_info.append(json_data)

with open('Sydney-zh-prompt.json', 'w+',encoding="utf_8") as f1:
    json.dump(data_info, f1, indent=4,ensure_ascii=False)