import json


def load_json() -> list[dict]:
    with open('candidates.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data


def format_candidates(candidates: list[dict]) -> str:
    result = '<pre>'

    for candidate in load_json():
        result += f""""
                    {candidate["name"]}\n
                    {candidate["position"]}\n
                    {candidate["skills"]}\n
                    """
    result += '</pre>'
    return result


def get_all_candidates() -> list[dict]:
    return load_json()


def get_candidate_by_pk(pk: int):
    candidates = get_all_candidates()
    for candidate in candidates:
        if candidate['pk'] == pk:
            return candidate
    return None


# def get_by_skill(skill_name, data):
#     arr = []
#     for item in data:
#         if skill_name in item['skills']:
#             arr.append(item)
#             print(arr)
#             return arr
