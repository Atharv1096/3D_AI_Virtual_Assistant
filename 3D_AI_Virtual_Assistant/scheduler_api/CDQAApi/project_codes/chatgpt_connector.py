import openai
import time
openai.api_key = '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'

model_engine = 'text-davinci-003'


def chatgpt_func(data):

    completion = openai.Completion.create(engine=model_engine, prompt=data, max_tokens=1024, stop=None, temperature=0.5)
    response = ""
    response = str(completion.choices[0].text)
    #print(response)
    
    return response