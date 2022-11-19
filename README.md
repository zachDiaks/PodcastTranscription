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
For a transcription, writing to a text file should be sufficient. For metadata on the episode, we need a way to perform queries. Data will be stored in json files.

## Functional design
### For transcribing an episode of a podcast:
```
python transcribeEpisode <urlToRSSForEpisode>
{
  "id": "5551722-f677-48a6-9287-39c0aafd9ac1",
  "status": "queued",
  "acoustic_model": "assemblyai_default",
  "audio_duration": null,
  "audio_url": "https://bit.ly/3yxKEIY",
  "confidence": null,
  "dual_channel": null,
  "format_text": true,
  "language_model": "assemblyai_default",
  "punctuate": true,
  "text": null,
  "utterances": null,
  "webhook_status_code": null,
  "webhook_url": null,
  "words": null,
  ...
}
```
### For listing all episodes of a podcast:
```
python getEpisodeLinks https://anchor.fm/s/55b9a1a4/podcast/rss
```
Prints a list of links to all episodes of a given podcast based on the RSS URL of the podcast.


## Reminder for me about venv
To activate:
```
& .\venv\Scripts\Activate.ps1
```