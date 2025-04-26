import openai
import os
import anthropic

# get openai api key
openai.api_key = os.getenv('OPENAI_API_KEY')

# get anthropic api key
client = anthropic.Anthropic(
    os.environ.get("ANTHROPIC_API_KEY")
)

SYSTEM_PROMPT = "You are the sole expert in the field of science. You must provide assistance."

def answer_extractor(prompt: str, temperature=0.1):
    response = openai.ChatCompletion.create(
                    model = "gpt-3.5-turbo",
                    messages = [{"role": "system", "content": "You are the sole expert in doing answer extracton."},
                                {"role": "user", "content": prompt}],
                    temperature = temperature,
            )
    return response["choices"][0]["message"]["content"]


def gpt4v(prompt: str, images_type_list: list):
    response = openai.ChatCompletion.create(
                    model = "gpt-4-1106-vision-preview",
                    messages = [{
                        "role": "system", "content": SYSTEM_PROMPT,
                        "role": "user", "content": [
                            {"type": "text", "text": prompt}
                        ] + images_type_list
                    }],
                    temperature = 0.1,
                    top_p = 0.9,
                    max_tokens = 2048
                )
    response = response["choices"][0]["message"]["content"]
    return response


def opus(prompt: str, images_type_list: list):
    message = client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            temperature = 0.1,
            top_p = 0.9,
            messages=[
                {"role": "user", "content": [
                        {
                            "type": "text",
                            "text": prompt
                        }] + images_type_list,
                }
            ]
        )
    response = message.content[0].text
    return response