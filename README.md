# Podcast transcription
Some quick and easy command line tools to transcribe podcasts. Initially used in a project to analyze how often certain phrases are used in a given podcast over time.

# Setup
This project uses [AssemblyAI's](https://www.assemblyai.com/docs) API for transcription. Once you set up an API key, create an environment variable named `AAI_API_KEY` and set it to your API Key. This is required to run the tool.

# Design details
These tools are intended to be used in Python to perform post-processing tasks. These tools will grab you the audio transcriptions from a given RSS feed for a podcast. The tools are split into classes based on what they do:
## Transcriber
This is the main class to use. It will submit a transcription to AssemblyAI and will provide functionality to:
  1) Check the transcription status
  2) Write the transcription to a file for future processing

## PodcastUtils
This is a class which will provide functionality all things related to the podcast you're trying to transcribe. Currently, it can only parse an RSS feed and extract audio links for each episode. In the future, it might be able to add some metadata about each podcast.

## Parser
This is a class which will parse transcribed podcast episodes. It will allow you to:
  1) Label speakers in the podcast
  2) Query several transcriptions for certain features (e.g. how often was a word or phrase uttered)