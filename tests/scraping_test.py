import requests
from bs4 import BeautifulSoup


def get_weblio_synonyms(word: str):
    url = f"https://thesaurus.weblio.jp/content/{word}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    li_tags = soup.find_all("li")
    li_strings: list = [
        li.string for li in li_tags if li.string is not None and len(li.string) <= 5
    ]
    for word in li_strings:
        contains_word = [sentence for sentence in tmp_list if word in sentence]

    return contains_word


# print(get_weblio_synonyms("扶養者"))


tmp_list = [
    "103万円以上稼ぐとどんなお金がかかりますか？",
    "103万円以上稼ぐとどんな税金がかかりますか？",
    "扶養外れるとどんなお金がかかりますか？",
    "扶養外れるとどんな税金がかかりますか？",
]

# 確認したい単語リスト
words_to_check = ["扶養", "税金"]

# 各単語がtmp_listのどの要素に含まれているかを確認
contains_words: dict = {}
for word in words_to_check:
    # 単語が含まれる文をリストにまとめる
    matched_sentences = [sentence for sentence in tmp_list if word in sentence]
    # 単語が含まれる文があれば、結果の辞書に追加
    if matched_sentences:
        contains_words[word] = matched_sentences

print(contains_words)
