import datetime
from pprint import pprint
from gnews import GNews
import json
import newspaper

MIN_ARTICLE_CHAR_LENGTH = 1000

def get_recent_articles(start_date, recent_count=5, use_cached=False):
	articles = []
	google_news = GNews(start_date=start_date)

	if use_cached:
		with open('articles.jsonl') as f:
			for line in f:
				articles.append(json.loads(line))
	else:
		# for fetching live from the feed
		headlines = google_news.get_news_by_site('vigilantnews.com')
		
		# sort headlines by 'published date' in descending order
		headlines = sorted(headlines, key=lambda x: datetime.datetime.strptime(x['published date'], '%a, %d %b %Y %H:%M:%S %Z'), reverse=True)

		f = open('articles.jsonl', 'w')
		for h in headlines:
			article = google_news.get_full_article(h['url'])
			if not article or len(article.text) < MIN_ARTICLE_CHAR_LENGTH:
				continue
			article_obj = {
				'published_date': h['published date'],
				'title': article.title,
				'text': article.text,
			}
			articles.append(article_obj)
			f.write(json.dumps(article_obj) + '\n')
			if len(articles) == recent_count:
				break
		f.close()

	return articles
