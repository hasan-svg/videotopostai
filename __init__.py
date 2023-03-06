from pytube import YouTube
from transformers import pipeline
import openai

class VideoScript:
    def __init__(self, apikeyopenai):
        self.title = ''
        self.response = ''
        self.content = ''
        self.source_url = ''
        self.transcript = []
        self.transcription = ''
        self.postprompt = 'Write a blog post based on the following summary:'
        openai.api_key = str(apikeyopenai)

    def videototext(self, video_url):
        self.source_url = video_url
        audio_file = YouTube(self.source_url).streams.filter(only_audio=True).first().download(filename="audio.mp4")
        with open(audio_file, 'rb') as f:
            transcriptions = openai.Audio.transcribe("whisper-1", f)
        self.transcript = []
        self.transcript.append(transcriptions)
        summarizer = pipeline("summarization")
        chunk_size = 1000
        num_chunks = len(transcriptions) // chunk_size + 1
        summarized_text = []

        for i in range(num_chunks):
            start = i * chunk_size
            end = min((i + 1) * chunk_size, len(self.transcription))
            result = ' '.join(x['text'] for x in self.transcription[start:end])
            out = summarizer(result, max_length=130, min_length=30, do_sample=False)
            out = out[0]
            out = out['summary_text']
            summarized_text.append(out)
        self.transcription = ' '.join(summarized_text)
        self.response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="{}\n{}".format(self.postprompt, self.transcription),
            temperature=0.7,
            max_tokens=1500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        self.content = self.response['choices'][0]['text']
        return self.response['choices'][0]['text']

    def titlemaker(self):
        if len(self.content) > 1:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt="Write a blog post SEO title based on the following text:\n{}".format(self.content),
                temperature=0.7,
                max_tokens=2000,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            self.title = response['choices'][0]['text']
            return response['choices'][0]['text']
        else:
            return 'Create Content Using videototext() fun.'