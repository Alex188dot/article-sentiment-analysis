# article-sentiment-analysis
This is a Python script that takes a URL of an online article as input and outputs a summary and a sentiment analysis of it 

# Dependencies
The script requires the following Python packages:

newspaper3k  
vaderSentiment  

You can install them using pip:

pip install newspaper3k  
pip install vaderSentiment  

# Usage
To run the script, simply execute it in your terminal:

python article-sentiment-analysis.py

The script will prompt you to enter the URL of an article you would like to be summarized and analysed in terms of sentiment. For example:

Enter url of an article you would like to be summarized and analysed in terms of sentiment: 
https://www.cnbc.com/2023/06/22/jd-power-initial-quality-study-2023-dodge-ram-top-tesla-volvo.html

The script will then download and parse the article using the newspaper3k package, and perform natural language processing on it to generate a summary. The summary will be printed to the terminal. For example:

<img width="1315" alt="Screenshot1" src="https://github.com/Alex188dot/article-sentiment-analysis/assets/117444853/df8231c3-028b-4b1a-8f0c-ae6fef6b91d7">

The Final Score indicates that the summary has a negative overall sentiment. The Final Score will always be between -1 (extremely negative) to 1 (extremely positive). 

Please note only English language articles are supported. 
