from fastapi import FastAPI
import codeforces_problem_wrapper
import codeforces_contest_wrapper
from pydantic import BaseModel
from typing import List


PROBLEM_LINK = 'https://codeforces.com/problemset/problem/'
CONTEST_LINK = 'https://codeforces.com/contest/'


app = FastAPI(
    title="Codeforces API",
    version="1.0",
)


class contest_response(BaseModel):
    contest_id: int
    contest_name: str
    contest_link: str
    problems: list = []
    editorial: str
    announcement: str

class problem_response(BaseModel):
    title: str
    timeLimit: dict = {}
    memoryLimit: dict = {}
    statement: str
    inputSpecification: str
    outputSpecification: str
    samples: list = []
    note: str

@app.get("/")
async def root():
    return {"title":"Codeforces API", "version":"1.0","Made by":"Prakhar Jain"}


@app.get("/contests/{contest_id}", response_model=contest_response)
async def contest_data(contest_id: int):

    results =  codeforces_contest_wrapper.parse_contest(CONTEST_LINK + str(contest_id))
    return results

@app.get("/problems/{contest_id}/{problem_id}", response_model=problem_response)
async def problem_data(contest_id: int,problem_id: str):
    
    results = codeforces_problem_wrapper.parse_problem(PROBLEM_LINK + str(contest_id) + '/' + problem_id)
    return results
