# videotopostai
 This Python package that uses the OpenAI API and the Transformers library to generate blog posts and titles based on YouTube videos. It makes it easy for users to create written content from videos without having to transcribe the audio themselves. 

 
## Features

- Generate Blog Post from youtube video
- Generate title for the blog post
- The content passes AI content test
- Custom prompt frature


## Acknowledgements

 - [summarized_text Algorithm](https://www.youtube.com/watch?v=3V-MJhJvRWg&t=768s)
 - [summarized_text Algorithm Source](https://colab.research.google.com/drive/17lEoIPVozCmaAUHXLSkJSWEtKVnXEMsf?usp=sharing#scrollTo=mCz2lRhAV-G4)
 
## API Reference

#### openAI API

```
Access openAI model's whisper, text-davinci-003.
```
```
Declare something like this>>> openai_api='YOUR_API_KEY'
See the test.py file for example.
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `openai.api_key` | `string` | **Required**. Your API key |

#### VideoScript(apikeyopenai=openai_api)
```
video_url = 'SOURCE_YOUTUBE_LINK_HERE'
transcript = script.videototext(video_url)
```
Takes API & video_url then return, Blog post. 


## Demo Code

```
from PACKAGE_NAME import VideoScript

# create an instance of VideoScript
openai_api='YOUR_API_KEY'
script = VideoScript(apikeyopenai=openai_api)

# get the transcript from a YouTube video
video_url = 'https://www.youtube.com/watch?v=h7gf5M04hdg'
transcript = script.videototext(video_url)

# generate an SEO-friendly title for the blog post
title = script.titlemaker()

# print the transcript and title
print(f'Transcript: {transcript}')
print(f'Title: {title}')
```
## Contributing

Contributions are always welcome!

## Feedback

If you have any feedback, please reach out to us at hasan.trz@outlook.com

## License

[MIT](https://github.com/newstroopp2023/videotopostai/blob/main/LICENSE)



