from newspaper import Article
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

url = input("Enter url of an article you would like to be summarized and analysed in terms of sentiment:")
article = Article(url)
article.download()
article.parse()
article.nlp()

text = article.summary
print("Text summary:\n", text)

analyzer = SentimentIntensityAnalyzer()
score = analyzer.polarity_scores(text)
print("Negative score:", score["neg"])
print("Positive score:", score["pos"])
print("Neutral score:", score["neu"])
print("Final score:", score["compound"])


