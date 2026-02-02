import json
import os
from uuid import uuid4

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'core', 'db.json')


def _load_articles():
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


def _save_articles(articles):
    with open(DB_PATH, 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)


def get_articles():
    return _load_articles()


def get_article_by_id(article_id):
    articles = _load_articles()
    return next((a for a in articles if a['id'] == article_id), None)


def add_article(title, content, date):
    articles = _load_articles()
    new_article = {
        'id': str(uuid4()),
        'title': title,
        'content': content,
        'date': date
    }
    articles.append(new_article)
    _save_articles(articles)
    return new_article


def update_article(article_id, title, content, date):
    articles = _load_articles()
    for article in articles:
        if article['id'] == article_id:
            article['title'] = title
            article['content'] = content
            article['date'] = date
            break
    _save_articles(articles)


def delete_article(article_id):
    articles = _load_articles()
    articles = [a for a in articles if a['id'] != article_id]
    _save_articles(articles)
