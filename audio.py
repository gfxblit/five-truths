import humanize
from openai import OpenAI
from random import randrange

client = OpenAI()

def create_audio_text(summaries, date):
	preamble = f"Hello! I'm Nova, with the 5 truths you need to know for {date.strftime('%A, %B')} {humanize.ordinal(date.day)}.\n\n"

	STORY_TRANSITION_PHRASES = [
		"Moving on to our next story...",
		"In other news...",
		"Next up...",
		"On a different note...",
		"Now turning our attention to the latest development...",
		"Now, for our next headline..."
	]

	text = preamble + summaries[0]['summary']
	for summary in summaries[1:]:
		text += '\n\n' + STORY_TRANSITION_PHRASES[randrange(len(STORY_TRANSITION_PHRASES))] + '\n' + summary['summary']

	return text

def create_audio(audio_text, filename='audio.mp3', use_cached=False):
	if use_cached:
		return

	response = client.audio.speech.create(
		model="tts-1",
		voice="shimmer",
		input=audio_text[:4096],
	)
	response.stream_to_file(filename)