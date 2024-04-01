import datetime
from audio import create_audio, create_audio_text
from news import get_recent_articles
from summarizer import get_summaries 
from discord_client import send_audio

now = datetime.datetime.now()
yesterday = now - datetime.timedelta(days=1)
articles = get_recent_articles(yesterday, use_cached=False)

print(f'Generating {len(articles)} summaries...')
summaries = get_summaries(articles, use_cached=False)

print('Creating audio text...')
audio_text = create_audio_text(summaries, now)

print(f'Generating audio from text:\n{audio_text}')
create_audio(audio_text, filename='audio.mp3', use_cached=False)

send_audio('audio.mp3')