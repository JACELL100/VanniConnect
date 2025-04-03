from django.urls import path
from . import views

urlpatterns = [
    path('', views.speech_to_text, name='speech_to_text'),
    path('save/', views.save_transcription, name='save_transcription'),
    path('transcriptions/', views.view_transcriptions, name='view_transcriptions'),
] 