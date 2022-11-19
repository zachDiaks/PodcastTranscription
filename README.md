# Podcast transcription
Some quick and easy command line tools to transcribe podcasts. Initially used in a project to analyze how often certain phrases are used in a given podcast over time.

# Setup
This project uses [AssemblyAI's](https://www.assemblyai.com/docs) API for transcription. Once you set up an API key, create an environment variable named `AAI_API_KEY` and set it to your API Key. This is required to run the tool.

# Design Spec
## Requirements
* Should be a command line tool
* User should be able to check on transcription status
* User should be able to either transcribe one or all episodes of a podcast
* Data should be stored in some capacity
* Users should be able to query metadata about a given episode (including the transcription)
* There should be a consistent scheme for writing transcriptions
## Data storage options
For a transcription, writing to a text file should be sufficient. For metadata on the episode, we need a way to perform queries. We can store as either JSON files or a database.