import openai
from tqdm import tqdm
from datasets import load_dataset
import json
from baselines.visual_prompting import *
from utils import *
from prompt import *
import os
from model import *


openai.api_key = os.getenv('OPENAI_API_KEY')
GPT_4_VISION = "gpt-4-1106-vision-preview"


def main(field: str, model: str, visual_prompting: str):
    if visual_prompting is None:
        visual_transformation = None
    elif visual_prompting == "scaffold":
        visual_transformation = scaffold
    elif visual_prompting == "spacecue":
        visual_transformation = spacecue

    dataset = load_dataset("MMMU/MMMU", field)
    val_set = dataset["validation"]

    for i in tqdm(range(len(val_set))):
        # load the val set 
        data_dict = val_set[i]
        question = data_dict['question']
        options = data_dict['options']
        answer = data_dict['answer']
        images = extract_image(data_dict)
        

        prompt = zero_shot(question, options)
        images_type_list = extract_image_list(images, visual_transformation, model)

        # in case sensitive information
        try:
            if model == "gpt":
                response = gpt4v(prompt, images_type_list)
            elif model == "opus":
                response = opus(prompt, images_type_list)
        except:
            continue


        cleaned_answer = answer_extractor(extract_prompt(response))

        with open(f"../results/{visual_prompting}/{field}_validation_{model}.jsonl", "a") as f:
            f.write(json.dumps({
                "question": question,
                "options": options,
                "correct_answer": answer,
                "gpt_answer": cleaned_answer,
                "response_history": response
            }) + "\n")



if __name__ == "__main__":
    for subject in ["Math", "Chemistry", "Biology", "Physics"]:
        print(f"current subject is: {subject}")
        main(subject, "gpt4", None)
