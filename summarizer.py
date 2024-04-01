import json

MAX_TOKENS = 150 
from openai import OpenAI

client = OpenAI()

def summarize_article(article_text):
	content = f'Summarize the following text as a news report in a single paragraph:\n\n{article_text}'
	response = client.chat.completions.create(
		model="gpt-4-turbo-preview",
		messages=[
			{
				"role": "user",
				"content": content
			},
		],
		temperature=1,
		max_tokens=MAX_TOKENS,
		top_p=1,
		frequency_penalty=0,
		presence_penalty=0
	)

	print(f'{response.usage.prompt_tokens=} {response.usage.completion_tokens=} {response.usage.total_tokens=}')

	return response.choices[0].message.content

def get_summaries(articles, use_cached=False):
	summaries = []
	if use_cached:
		with open('summaries.jsonl') as f:
			for line in f:
				summaries.append(json.loads(line))
	else:
		f = open('summaries.jsonl', 'w')
		for a in articles:
			summary = summarize_article(a['text'][:1023])
			summary_obj = {
				'summary': summary
			}
			summaries.append(summary_obj)
			f.write(json.dumps(summary_obj) + '\n')
		f.close()

	return summaries
