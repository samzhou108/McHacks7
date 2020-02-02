from google.cloud import language_v1
from google.cloud.language_v1 import enums

import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/Users/SamZhou/PycharmProjects/MetaAnalysis_McHacks/McHacks-f0e3b269c710.json"

import requests

# url = "https://journals.lww.com/pain/Fulltext/2020/02000/Remifentanil_for_abdominal_surgery_is_associated.4.aspx"
#
# payload = ""
# headers = {
#     'cache-control': "no-cache",
#     'Postman-Token': "df23e98e-8639-48cf-95f5-2b00c4888a28"
#     }
#
# response = requests.request("GET", url, data=payload, headers=headers)
# text = response.text
###
with open('input.txt', 'r') as content_file:
    text = content_file.read()

def sample_classify_text(text_content):
    """
    Classifying Content in a String

    Args:
      text_content The text content to analyze. Must include at least 20 words.
    """

    client = language_v1.LanguageServiceClient()

    # text_content = 'That actor on TV makes movies in Hollywood and also stars in a variety of popular new TV shows.'

    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type": type_, "language": language}

    response = client.classify_text(document)
    # Loop through classified categories returned from the API
    for category in response.categories:
        # Get the name of the category representing the document.
        # See the predefined taxonomy of categories:
        # https://cloud.google.com/natural-language/docs/categories
        print(u"Category name: {}".format(category.name))
        # Get the confidence. Number representing how certain the classifier
        # is that this category represents the provided text.
        print(u"Confidence: {}".format(category.confidence))


def main():
    sample_classify_text(text)


if __name__ == '__main__':
    main()