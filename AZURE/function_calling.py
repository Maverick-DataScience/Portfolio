import os
import requests
from openai import AzureOpenAI  
import json

def main():
    endpoint = 
    apikey = 

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
        url = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="
        response = requests.get(url)
        get_response = response.json()
        latitude = get_response["coord"]["lat"]
        longitude = get_response["coord"]["lon"]
        print(f"latitude:{latitude}")
        print(f"longitude:{longitude}")
        
        url_final = " https://api.openweathermap.org/data/2.5/weather?q="+str(latitude)+"&lon="+str(longitude)+"&appid="
        final_response = requests.get(url_final)
        final_response_json = final_response.json()
        weather = final_response_json["weather"][0]["description"]
        print(f"weather condition: {weather}")
    
    
    
if __name__ =="__main__":
    main()
    
