import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article


# nltk.download('punkt_tab')


url ="https://edition.cnn.com/2024/08/26/science/dinosaur-footprints-south-america-africa/index.html"

article = Article(url)

article.download()
article.parse()


article.nlp()


print(f" Title: {article.title}")
print(f"{"----":^40}")
print(f"Authors: {article.authors}")
print(f"{"----":^40}")
print(f"publication Date: {article.publish_date}")
print(f"{"----":^40}")
print(f"Summary: {article.summary}")