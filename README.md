# SpaceCue: Enhancing Visual Reasoning in Science with Large Multi-modal Models

Make sure you have installed dependencies:

```
pip install datasets
pip install openai
pip install anthropic
```

To use OpenAI and Anthropic API, you need to define the environment variables:

```
export OPENAI_API_KEY='your_openai_api_key'
```

and 

```
export ANTHROPIC_API_KEY='your_anthropic_api_key'
```

To run the experiments:

```
cd baselines
python main.py
```

This is the header for `main.py` file:

```python
def main(field: str, model: str, visual_prompting: str):
```

where 

```python
field = ['Physics', 'Chemistry', 'Biology', 'Math']
model = ['gpt', 'opus']
visual_prompting = [None, 'scaffold', 'spacecue']
```

For running evaluations, go to `baselines/accuracy_check.ipynb` notebook and enter the parameters you want to test. 

```python
# parameters you want to change
METHOD = "spacecue" # chosen from ["cot", "zero-shot", "io", "scaffold", "spacecue"]
FIELD = "Math" # chosen from  ['Physics', 'Chemistry', 'Biology', 'Math']
MODEL = "gpt" # chosen from ["gpt", "opus"]

# path of the result
path = f"""../results/{METHOD}/{FIELD}_validation_{MODEL}.jsonl"""

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
```