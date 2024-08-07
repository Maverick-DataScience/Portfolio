import os
from openai import AzureOpenAI
import json

endpoint = 
apikey = 

client = AzureOpenAI(
    api_key=apikey,
    api_version="2024-02-01",
    azure_endpoint=endpoint
)

completion =client.chat.completions.create(
    model ="maverickai",
    messages =[
        {
            "role":"user",
            "content":"what is the capital of indonesia?",
        }
    ]
)

print(completion.to_json())