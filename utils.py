import json


def load_json() -> list[dict]:
    with open('candidates.json', 'r', encoding='utf-8') as f:
        candidates = json.load(f)
        return candidates


def get_all_candidates() -> list[dict]:
    return load_json()


def format_candidates(candidates):
    result = '<pre>'

    for item in candidates:
        result += f""""
                    {item["name"]}\n
                    {item["position"]}\n
                    {item["skills"]}\n
                    """
    result += '</pre>'
    return result


def get_candidate_by_pk(pk: int):
    candidates = get_all_candidates()
    for item in candidates:
        if item['pk'] == pk:
            return item
    return None


def get_by_skill(skill: str) -> list[dict]:
    candidates = get_all_candidates()
    arr = []
    for item in candidates:
        if skill in item['skills'].lower().split(', '):
            arr.append(item)
    return arr
