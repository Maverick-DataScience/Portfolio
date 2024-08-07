endpoint = 
apikey = 

import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=apikey,
    api_version="2024-02-01",
    azure_endpoint= endpoint
)

# This will correspond to the custom name you chose for your deployment when you deployed a model.
# Use a gpt-35-turbo-instruct deployment.
deployment_name = "maverickai"

# Send a completion call to generate an answer
prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly. \n \nHuman: Hello, who are you? \nAI: Hello, I am an AI assistant. I am here to help you with anything you need.\nHuman: I'd like to cancel my subscription. \nAI: Oh no, too bad your too poor to cancel it. But if you really want to, I can help you with that.\nASDF \n"
response = client.completions.create(
    model=deployment_name,
    prompt=prompt,
    temperature=0.9,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["Human:","AI:"]
)

print(prompt + response.choices[0].text)
