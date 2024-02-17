import re

tmp_list = [
    "`? hogehogeを変更したい(hogehoge|taxman taxman)`",
    "アカウントページからhogehogeできます。",
    "`? hogehogeを変更したい(hogehoge|taxman taxman)`",
    "これこそhogehoge。",
    "`? hogehogeを変更したい(hogehoge|taxman taxman)`",
]

pattern = re.compile(r"\? ")  # 正規表現パターン

descriptions_list: list = []
regular_express_list: list = []


for string in tmp_list:
    if pattern.search(string):
        regular_express_list.append(string)
    else:
        descriptions_list.append(string)
        
print(descriptions_list) 
print(regular_express_list) 