from flask import Flask

from utils import *

app = Flask(__name__)


@app.route("/")
def page_index():
    candidates: list[dict] = get_all_candidates()
    result = format_candidates(candidates)
    return result


@app.route("/candidates/<int:pk>")
def get_candidate(pk):
    candidate: dict = get_all_candidates(pk)
    result: str = format_candidates([candidate])
    return result


app.run(port=5050)
#
