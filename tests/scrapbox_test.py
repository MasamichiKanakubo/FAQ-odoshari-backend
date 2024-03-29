import os
import requests
import re
from dotenv import load_dotenv

load_dotenv()

scrapbox_project_name = os.getenv("SCRAPBOX_PROJECT_NAME")


def get_scrapbox_json(project_name: str):
    url = f"https://scrapbox.io/api/pages/{project_name}"
    response = requests.get(url).json()
    title_list = [page["title"] for page in response["pages"]]
    response_list: list = []
    for title in title_list:
        res = requests.get(
            f"https://scrapbox.io/api/pages/{project_name}/{title}"
        ).json()
        question = res["title"]
        descriptions = res["descriptions"]
        pattern = re.compile(r"\?")
        entry = {"question": question, "description": descriptions}
        response_list.append(entry)

    return response_list
print(get_scrapbox_json(scrapbox_project_name))


# (get_scrapbox_json(scrapbox_project_name))


def get_question_detail(question_sentence: str):
    url = f"https://scrapbox.io/api/pages/{scrapbox_project_name}/{question_sentence}"
    response = requests.get(url).json()
    return response
print(get_question_detail("hogehoge2"))

