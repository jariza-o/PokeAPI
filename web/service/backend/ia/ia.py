import google.generativeai as genai
import os
import requests

class IA():

    def __init__(self, prompt: str):
        print(self.prompt)
        self.prompt = prompt
        genai.configure(api_key=os.environ[os.getenv('GEMINI_API_KEY')])

    def Gemini_IA(self) -> str:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(f"{self.prompt}")
        print(response.text)

        return response.text
    

    def Unplast(self):
        url = "https://api.unsplash.com/photos/random"

        params = {
            "query": self.prompt,
            "client_id": os.environ[os.getenv('UNSPLASH_ACCESS_KEY')]
        }

        response = requests.get(url, params=params)