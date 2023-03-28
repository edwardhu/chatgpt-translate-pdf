# pip install pypdf
# pip install nltk
# pip install openai
import openai
import nltk
import argparse
from pypdf import PdfReader
from nltk import sent_tokenize

def parse_args():
    parser = argparse.ArgumentParser(description="This is a script for translate English pdf document.")
    parser.add_argument("-f", "--file", help="PDF Document", dest="Document", type=str, required=True)
    return parser.parse_args()

def translate(document):   
    openai.api_key = $TOKEN
    reader = PdfReader(document)
    number_of_pages = len(reader.pages)
    chunks = []
    nltk.download("punkt")
    for i in range(number_of_pages):
        page = reader.pages[i]
        text = page.extract_text()
        sentences = sent_tokenize(text)
        input_sentences = ""
        for sentence in sentences:
            input_sentences += sentence
            if len(input_sentences) > 1000:
                chunks.append(input_sentences)
                input_sentences = ""
        chunks.append(input_sentences)
    for i in range(10):
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "請協助翻譯以下技術文件，以繁體中文輸出"},
            {"role": "user", "content": chunks[i]},
            ]
        )
        print('原文:', chunks[i])
        print('翻譯結果:',completion.choices[0].message.content)

if __name__ == '__main__':
    document = parse_args()
    print(str(document))
    translate(document.Document)