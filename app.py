import datetime
import cache
import news
from audio import create_audio, create_audio_text
from summarizer import get_summaries 
from discord_client import send_audio

MAX_ARTICLES_TO_REPORT = 5

now = datetime.datetime.now()
yesterday = now - datetime.timedelta(days=1)
articles = news.get_recent_articles(yesterday, recent_count=100, use_cached=False)

print('Fetched recent articles', len(articles))
print('Filtering reported articles...')
articles = cache.filter_reported_articles(articles)
print('remaining unreported articles', len(articles))

articles = articles[:MAX_ARTICLES_TO_REPORT]

if len(articles) == 0:
	print('No unreported articles')
	exit()

print(f'Generating {len(articles)} summaries...')
summaries = get_summaries(articles, use_cached=False)

print('Creating audio text...')
audio_text = create_audio_text(summaries, now)

print(f'Generating audio from text:\n{audio_text}')
create_audio(audio_text, filename='audio.mp3', use_cached=False)

send_audio('audio.mp3')

print('Caching reported articles...')
cache.add_reported_articles(articles)