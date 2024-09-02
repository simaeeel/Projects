import tkinter as tk
from textblob import TextBlob
from newspaper import Article
import nltk

# Download necessary NLTK model
nltk.download('punkt')

def summarize():
    url = url_text.get('1.0', 'end').strip()
    article = Article(url)

    # Download and parse the article
    article.download()
    article.parse()
    article.nlp()

    # Extract information
    title.config(state='normal')
    title.delete('1.0', 'end')
    title.insert('1.0', article.title)
    title.config(state='disabled')

    author.config(state='normal')
    author.delete('1.0', 'end')
    author.insert('1.0', ', '.join(article.authors))
    author.config(state='disabled')

    publication.config(state='normal')
    publication.delete('1.0', 'end')
    publication.insert('1.0', article.publish_date)
    publication.config(state='disabled')

    summary.config(state='normal')
    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)
    summary.config(state='disabled')

    # Perform sentiment analysis
    analysis = TextBlob(article.text)
    polarity = analysis.sentiment.polarity

    sentiment.config(state='normal')
    sentiment.delete('1.0', 'end')
    sentiment_value = "ya it's okay 😁" if polarity > 0 else "Not ok😢" if polarity < 0 else "feels nothing😗"
    sentiment.insert('1.0', f'{sentiment_value} (Polarity: {polarity})')
    sentiment.config(state='disabled')

# Set up the GUI
root = tk.Tk()
root.title('News Summarizer')
root.geometry('1200x600')

# Title
t_label = tk.Label(root, text='⌂ Title')
t_label.pack()
title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

# Author
a_label = tk.Label(root, text='© Author')
a_label.pack()
author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

# Publication Date
p_label = tk.Label(root, text='₰ublication Date')
p_label.pack()
publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

# Summary
s_label = tk.Label(root, text='✓✓ summary')
s_label.pack()
summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

# Sentiment Analysis
se_label = tk.Label(root, text=' ◕ Sentiment Analysis')
se_label.pack()
sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

# URL Input
url_label = tk.Label(root, text='URL')
url_label.pack()
url_text = tk.Text(root, height=1, width=140)
url_text.pack()

# Summarize Button
summarize_button = tk.Button(root, text='Summarize', command=summarize)
summarize_button.pack()

# Run the GUI
root.mainloop()
