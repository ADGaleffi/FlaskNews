---
lang: en
author: 'Andrea Daniele Galeffi'
title: 'Developing an Online News Aggregator'
style: default-page
slide-num: true
format: 
  revealjs: 
    footer: 
    theme: serif
    preview-links: auto
    chalkboard: 
      boardmarker-width: 4
---

## Developing an Online News Aggregator

#### Human and Non-Human Actors of Selective Exposure


<p style="text-align: right;">Andrea Daniele Galeffi</p>

---

## Aims

Design, implement and test a **customizable** online news aggregator

A *lab* for studying the effects of *user-side customization* of the news feed

Give some agency back to final users

---

## Theory to practice

The main design choices are grounded in an *extensive* literature review on

- news aggregation, and the mechanisms behind it
- the risks connected with the emergence of **selective exposure** or even **self-polarisation**

---

### Selective Exposure

<img src='https://sites.psu.edu/bsee2018/files/2018/02/c1aac0799f87876f93b4ec4ed78ad626-14r6pel.jpg'>

it emerges during Web navigation
 - the easy **acceptance of attitude-abiding information,**
 - the **exclusion of counter-attitudinal information**

---

## Echo Chambers

<img src="https://www.populismstudies.org/wp-content/uploads/2020/04/EchoChamber-1024x1024.png" width=200>

```text
highly personalized communication environments 
built around the ability of users to follow 
like-minded individuals (Lazer et al., 2017)
```


---

### Filter Bubbles

<img src="https://donmcminn.com/wp-content/uploads/2023/06/articles-2009.jpg" width=300>

```text
[...] intermediate structures, formed in online 
digital space, which limit user’s exposure to 
the full spectrum of news and information available 
on the internet (Han et al., 2022)
```


---

## echo chambers vs. filter bubbles

can we separate phenomena which are **fostered by the design of social media** from those which **stem from characteristics of human nature?**

---

## The Software

<img src='https://github.com/ADGaleffi/FlaskNews/blob/main/GraficoFlaskNews.png?raw=true'>

1. retrieves articles in JSON form from NEWSAPI

2. filters/prepares the newsfeed by applying user preferences

---

## Customizing API requests

```python  
NEWS_API_URL = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'
```

---

<img src='https://github.com/ADGaleffi/FlaskNews/blob/main/GraficoFlaskNews.png?raw=true'>

---

## Post-fetch filters


```python
filtered_news_data = [article for article in news_data if article.get('source', {}).get('id') != excluded_source]

return render_template('index.html', news_data=filtered_news_data, sources=sources)
```

---

## The dashboard

De-serialise and graphically render the newsfeed

<img src='https://github.com/ADGaleffi/FlaskNews_PresentationContent/blob/main/PresentationImages/ArticleJSON.JPG?raw=true'>

---

## The Input

```html
<div class="news-container">
    {% for index in range(0, news_data|length, 3) %}
        <div class="row">
            {% for offset in range(3) %}
                {% set article_index = index + offset %}
                {% if article_index < news_data|length %}
                    {% set article = news_data[article_index] %}
                    <div class="news-item">
                    [...]
```

---

## The Output: interim user interface

<img src='https://github.com/ADGaleffi/FlaskNews_PresentationContent/blob/main/PresentationImages/Output1.JPG?raw=true'>

---

## Opening the sidebar

<img src='https://github.com/ADGaleffi/FlaskNews_PresentationContent/blob/main/PresentationImages/Output2.JPG?raw=true'>

---

## Use cases

- read-it-all about Football but leave Juventus FC out

- each February, avoid the misery of Italy crashing out the 6 Nations

- preserve mental health by avoiding news about war/pandemics

---

## Summary

- a new tool for studying self-polarisation and selective exposure

- An effective, customisable newsfeed filter

- so far, only subtractive filters are implemented

- possible integration with the [Zeeschuimeer project](https://github.com/digitalmethodsinitiative/zeeschuimer)

---

## Thank you for your attention!

---

Everything for this project can be found on [my Github](https://github.com/ADGaleffi)

<img src='https://github.com/ADGaleffi/FlaskNews_PresentationContent/blob/main/PresentationImages/MyGitHub.JPG?raw=true'>


