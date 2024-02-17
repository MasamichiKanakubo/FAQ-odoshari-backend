import os
import requests
from dotenv import load_dotenv


load_dotenv()

scrapbox_project_name = os.getenv("SCRAPBOX_PROJECT_NAME")

def get_scrapbox_json(project_name: str):
    url = f"https://scrapbox.io/api/pages/{project_name}"
    response = requests.get(url).json()
    title_list = [page["title"] for page in response["pages"]]
    response_list : list = []
    for title in title_list:
        res = requests.get(f"https://scrapbox.io/api/pages/{project_name}/{title}").json() 
        question = res["title"]
        description = res["descriptions"][0]       
        entry = {"question": question, "description": description}
        response_list.append(entry)
        
    return response_list

print(get_scrapbox_json(scrapbox_project_name))
