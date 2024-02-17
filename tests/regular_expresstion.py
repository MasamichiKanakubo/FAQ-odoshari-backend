import re
from itertools import product
from typing import List

tmp_list = [
    "`? hogehogeを変更したい(hogehoge|taxman taxman)`",
    "アカウントページからhogehogeできます。",
    "`? hogehogeを変更したい(hogehoge|taxman taxman)`",
    "これこそhogehoge。",
    "`? hogehogeを変更したい(hogehoge|taxman taxman)`",
]

input_string1 = "`? hogehogeを変更したい(hogehoge|taxman taxman)`"
input_string2 = "`? (hogehoge|fugafuga)を(変更し|変え)たい`"

# "? "を削除
cleaned_string = re.sub(r"\? ", "", input_string2).strip("`")

def convert_text_to_questions(text: str) -> List[str]:
    matches = re.finditer(r"\((.+?)\)", text)
    options_list = [match.group(1).split("|") for match in matches]

    combinations = generate_combinations(options_list)

    return [apply_combination(text, combination) for combination in combinations]


def generate_combinations(options_list):
    return list(product(*options_list))


def apply_combination(text, combination):
    result = text
    for option in combination:
        result = result.replace(re.search(r"\((.+?)\)", result).group(), option, 1)
    return result

print(convert_text_to_questions(cleaned_string))