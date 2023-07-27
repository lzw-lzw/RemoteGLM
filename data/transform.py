import json
from tqdm import tqdm

with open('Sydney_dataset.json') as f:
    data = json.load(f)['images']

data_info =[]
for i in tqdm(range(len(data))):
    img_name = data[i]['filename']
    sentences_json = data[i]['sentences']
    sentence = ''
    for j in range(len(sentences_json)):
        sentence += sentences_json[j]['raw']+'  '
    json_data = {
        "imged_id": img_name,
        "caption": sentence
    }
    data_info.append(json_data)
    
with open('Sydney-en.json', 'w') as f:
    json.dump(data_info, f, indent=4)
