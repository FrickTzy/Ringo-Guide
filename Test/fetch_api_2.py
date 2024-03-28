import requests
from xml.etree import ElementTree as ET


def get_kanji_info(kanji):
    url = f"http://www.edrdg.org/cgi-bin/wwwjdic/wwwjdic?1ZUJ{kanji}"
    response = requests.get(url)
    if response.status_code == 200:
        root = ET.fromstring(response.content)
        kanji_info = {}
        for child in root.findall(".//table/tr"):
            cells = child.findall("./td")
            if cells:
                category = cells[0].text.strip().lower()
                value = cells[1].text.strip()
                kanji_info[category] = value
        return kanji_info
    else:
        print("Error: Unable to fetch kanji information.")
        return None


def get_example_sentences(kanji):
    url = f"https://tatoeba.org/api/v1/sentences/search?query=%22{kanji}%22&from=jpn"
    response = requests.get(url)
    print(response.text)
    if response.status_code == 200:
        data = response.json()
        example_sentences = [item["text"] for item in data]
        return example_sentences
    else:
        print("Error: Unable to fetch example sentences.")
        return None


# Example usage:
kanji = input("Enter a kanji character: ")
example_sentences = get_example_sentences(kanji)
if example_sentences:
    print("Example Sentences:")
    for sentence in example_sentences[:5]:  # Displaying only the first 5 example sentences
        print("-", sentence)
