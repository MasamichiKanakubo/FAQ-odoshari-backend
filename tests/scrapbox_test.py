import os
import re
import requests
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
        description = res["descriptions"]
        entry = {"question": question, "description": description}
        response_list.append(entry)

    return response_list


# (get_scrapbox_json(scrapbox_project_name))


# def get_question_detail(question_sentence: str):
#     url = f"https://scrapbox.io/api/pages/{scrapbox_project_name}/{question_sentence}"
#     response = requests.get(url).json()
#     question = response["title"]
#     description = response["descriptions"][0]
#     return {"question": question, "description": description}
# print(get_question_detail('hogehoge2'))


# def process_question_text(question_text):
#     # 正規表現を使用して文字列を分解
#     matches = re.findall(r"\? (\S+?)を変更したい((\S+?)(?:, ?(\S+))*)", question_text)

#     # マッチした部分を使ってリストを生成
#     result_list = [f"{match[0]}を変更したい{match[1]}" for match in matches]

#     return result_list


# question_text = "? hogehogeを変更したい(hogehoge|taxman taxman)"
# result = process_question_text(question_text)
# print(result)
