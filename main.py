from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests


app = Flask(__name__)

NEWS_API_KEY = 'INSERT_YOUR_API_KEY_HERE'
NEWS_API_URL = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'

@app.route('/')
def home():
    response = requests.get(NEWS_API_URL)
    news_data = response.json().get('articles', [])
    sources = [article.get('source', {}).get('name', '') for article in news_data]
      
    return render_template('index.html', news_data=news_data, sources=sources)

@app.route('/news/<int:index>')
def news(index):    
    if 0 <= index < len(news_data):
      article = news_data[index]
      return render_template('news.html', article=article)
    else:
      return "News not found"

@app.route('/news')
def get_news():
  excluded_source = request.args.get('exclude_source', 'bonobo') 
  excluded_word = request.args.get('exclude_word', 'ominoRosa')
  news_api_url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'
  response = requests.get(news_api_url)
  news_data = response.json().get('articles', [])
  sources = [article.get('source', {}).get('name', '') for article in news_data]

  if excluded_word == 'ominoRosa':
    if excluded_source == 'bonobo':
      return render_template('index.html', news_data=news_data)
    
    else:
      filtered_news_data = [article for article in news_data if article.get('source', {}).get('id') != excluded_source]
    
      return render_template('index.html', news_data=filtered_news_data, sources=sources)

  else:
    filtered_news_data = [article for article in news_data if excluded_word.lower() not in article.get('title', '').lower()]
    return render_template('index.html' , news_data=filtered_news_data, sources=sources)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81, debug=True)
