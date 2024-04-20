import json
CACHE_FILENAME = '/tmp/reported_news_cache.jsonl'

def filter_reported_articles(articles):
	try: 
		with open(CACHE_FILENAME) as file:
			for line in file:
				article = json.loads(line)
				articles = [a for a in articles if a['url'] != article['url']]
	except IOError:
		pass
	return articles

def add_reported_articles(articles):
	with open(CACHE_FILENAME, 'a') as file:
		for article in articles:
			file.write(json.dumps(article) + '\n')