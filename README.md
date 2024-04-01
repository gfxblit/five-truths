## Introduction

Auto-generates 5 truths in a podcast form by scraping news feeds of your choice, summarizing the articles via an LLM, and sythesizing the summaries into speech.

## Setup
1. Make sure to create a .env with
 	 ```
	 OPENAI_API_KEY=xxx
	 DISCORD_TOKEN=yyy
	 DISCORD_CHANNEL_ID=zzz
	 ```
1. Setup your discord bot via https://discordpy.readthedocs.io/en/stable/discord.html#discord-intro
1. `pip install -f requirements.txt`

## Execution
1. `dotenv run python app.py`
