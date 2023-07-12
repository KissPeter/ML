
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
summarizer.save_pretrained("./summarization")


summarizer = pipeline("sentiment-analysis", model="cardiffnlp/twitter-xlm-roberta-base-sentiment")
summarizer.save_pretrained("./sentiment-analysis")
