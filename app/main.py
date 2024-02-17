import os
import re
import asyncio
import aiohttp
import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from app.entities.schemas import Synonyms, QuestionSentence


load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
scrapbox_project_name = os.getenv("SCRAPBOX_PROJECT_NAME")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

deploy_url = "https://faq-odoshari-api.onrender.com/"
connector = aiohttp.TCPConnector(ssl=False)


async def send_request():
    while True:
        async with aiohttp.ClientSession(connector=connector) as session:
            async with session.get(deploy_url) as response:
                print(await response.text())
        await asyncio.sleep(60)  # 60秒ごとにリクエストを送信


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(send_request())


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/faqs")
async def get_faq():
    url = f"https://scrapbox.io/api/pages/{scrapbox_project_name}"
    response = requests.get(url).json()
    title_list = [page["title"] for page in response["pages"]]
    response_list: list = []
    for title in title_list:
        res = requests.get(
            f"https://scrapbox.io/api/pages/{scrapbox_project_name}/{title}"
        ).json()
        page_title = res["title"]
        descriptions = res["descriptions"]
        pattern = re.compile(r"\?")
        descriptions_list: list = []
        regular_express_list: list = []
        for string in descriptions:
            if pattern.search(string):
                regular_express_list.append(string)
            else:
                descriptions_list.append(string)
        entry = {"page_title": page_title, "questions": regular_express_list}
        response_list.append(entry)

    return response_list


@app.get("/api/pages/{question_sentence}")
async def get_question_detail(question_sentence: str):
    url = f"https://scrapbox.io/api/pages/{scrapbox_project_name}/{question_sentence}"
    response = requests.get(url).json()
    question = response["title"]
    descriptions = response["descriptions"]
    regular_express_list: list = []
    descriptions_list: list = []
    pattern = re.compile(r"\?")
    for string in descriptions:
        if pattern.search(string):
            regular_express_list.append(string)
        else:
            descriptions_list.append(string)
    return {"page_title": question, "descriptions": descriptions_list}
