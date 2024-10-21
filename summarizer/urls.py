from django.urls import path

from . import views as summarizer_views

urlpatterns = [
    path('', summarizer_views.home, name='home'),
    path('summarize/<str:video_id>/', summarizer_views.summarize, name='summarize')
]
