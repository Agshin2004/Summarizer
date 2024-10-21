from django.http import JsonResponse
from django.shortcuts import render

from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline


def home(request):
    ctx = {}
    return render(request, 'summarizer/home.html', context=ctx)


def summarize(request, video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    context = ''
    for dic in transcript:
        context += dic['text']

    summarization_pipeline = pipeline("summarization")
    summary = summarization_pipeline(context, max_length=200, min_length=50, do_sample=False)

    return JsonResponse({'summary': summary[0]['summary_text']})
