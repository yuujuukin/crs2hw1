from flask import Flask
from utils import *

app = Flask(__name__)


@app.route("/")
def page_index():
    candidates = load_json()
    result = format_candidates(candidates)
    return result


@app.route("/candidates/<int:pk>")
def get_candidate(pk):
    candidate: dict = get_candidate_by_pk(pk)
    result = f'<img src="{candidate["picture"]}">'
    result += format_candidates([candidate])
    return result


@app.route("/skills/<skill>")
def get_skills(skill):
    skill_lower = skill.lower()
    candidates: list[dict] = get_by_skill(skill_lower)
    result = format_candidates(candidates)
    return result


app.run(port=8080)
