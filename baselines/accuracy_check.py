import json
from tqdm import tqdm
result_list = []

METHOD = "spacecue"
FIELD = "Math"
MODEL = "gpt"

# path of the result
path = f"../results/{METHOD}/{FIELD}_validation_{MODEL}.jsonl"
# counter
count, corr = 0, 0
with open(path, "r") as f:
    for idx, l in tqdm(enumerate(f)):
        data = json.loads(l)
        answer = data['correct_answer']
        gpt_answer = json.loads(data['gpt_answer'])['selection']
        count += 1
        corr += (answer == gpt_answer)
        result_list.append(gpt_answer)

print(f"Accuracy os {corr/count * 100:.2f}%")
print(f"corr: {corr}, count: {count}")
