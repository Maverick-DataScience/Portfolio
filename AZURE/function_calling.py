import os
import requests
from openai import AzureOpenAI  
import json

def main():
    endpoint = "https://crashcoursemodelling231.openai.azure.com/"
    apikey = "860d56a4ff7441a785c5dc6cd159fe39"

    client = AzureOpenAI(
    api_key=apikey,
    api_version="2024-02-01",
    azure_endpoint= endpoint
    )
    
    functions=[
        {
            "name":"getWeather",
            "description":"Retrieve real-time weather information/data about a particular location/place",
            "parameter":{
                "type":"object",
                "properties":{
                    "location":{
                        "type":"string",
                        "description":"the exact location whose real-time weather is to be determined"
                    }
                },
                "required":["location"]
            }
        }
    ]
    
    initial_response = client.chat.completions.create(
        model ="maverickai",
        messages=[
            {"role":"system","content":"you are an assistant that helps people retrieve real-time weather in city around the world"},
            {"role":"user","content":"how is the weather in Medan?"}
        ],
        functions=functions
    )
    
    function_argument = json.loads(initial_response.choices[0].message.function_call.arguments)
    location = function_argument["location"]
    
    if(location):
        print{f"city: {location}"}
        get_weather(location)
        
    def get_weather(location):
        url = ""
    
    
    
if __name__ =="__main__":
    main()
    
    6a3e82d38d33b04c4476cadc75a4af97
    https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={"6a3e82d38d33b04c4476cadc75a4af97"}
    https://api.openweathermap.org/data/2.5/weather?q={city name},{country code}&appid={API key}