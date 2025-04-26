def standard_io(question, options):
    return f"""You are an expert in scientific domain. You will be provided one or more figures that is related to a question. Answer the question from a list of options. 
For each of the image, I will also input you an annotated version of it. In your reasoning, first select the coordinates that is the most relevant to the question, then answer the question based on the instructiuon below.
        
<question>
{question}
</question>

<options>
{options}
</options>

Provide our reasoning when answering the question, including the coordinates you are selecting. If options are presented, select only 1 answer from the list of options; if options are None, directly provide the answer. If you think the first answer is correct, respond by A; if you think the second answer is correct, respond by B; if you think the third answer is correct, respond by C; and so on so forth. 
"""

def zero_shot(question, options):
    return f"""You are an expert in scientific domain. You will be provided one or more figures that is related to a question. Answer the question from a list of options. 
For each of the image, I will also input you an annotated version of it. In your reasoning, first select the coordinates that is the most relevant to the question, then answer the question based on the instructiuon below.
        
<question>
{question}
</question>

<options>
{options}
</options>

Provide our reasoning when answering the question, including the coordinates you are selecting. If options are presented, select only 1 answer from the list of options; if options are None, directly provide the answer. If you think the first answer is correct, respond by A; if you think the second answer is correct, respond by B; if you think the third answer is correct, respond by C; and so on so forth. 

Let's think step by step
"""

def cot(question, options):
    return f"""You are an expert in the scientific domain. Analyze the information and answer the question below.

<question>
{question}
</question>

<options>
{options}
</options>

First, let's break down the question and analyze its key components. Consider the relevant scientific principles or data that apply. Next, evaluate each option based on these principles and how they relate to the data or visuals provided.

Reason through the problem step by step:
1. Identify the main concepts involved in the question.
2. Recall relevant scientific knowledge that could influence the answer.
3. Apply this knowledge to interpret the information or data presented.
4. Assess each answer option systematically, considering how well it aligns with the scientific analysis.

Conclude by selecting the best answer. If you think the first answer is correct, respond with 'A'; if the second, 'B'; if the third, 'C'; and so forth. Provide your final answer along with a brief justification for why it is the correct choice based on the reasoning process.
"""

def extract_prompt(response):
    return  f"""Extract the {{answer}} field from the response I enter to you. Format it into a json-liked format {{"selection": \"\"}}. For example, if the selection is (a), respond by {{\"selection\": \"A\"}} only. No other texts are needed.

        <response>
        {response}
        </response>
"""