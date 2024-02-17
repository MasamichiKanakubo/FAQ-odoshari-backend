import os
import asyncio
import aiohttp
import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from app.entities.schemas import Synonyms

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
        question = res["title"]
        description = res["descriptions"]
        entry = {"question": question, "description": description}
        response_list.append(entry)

    return response_list

@app.get("/api/faqs/{question_sententce}")
async def get_question_detail(question_sentence: str):
    url = f"https://scrapbox.io/api/pages/{scrapbox_project_name}/{question_sentence}"
    response = requests.get(url).json()
    question = response["title"]
    description = response["descriptions"]
    return {"question": question, "description": description}
