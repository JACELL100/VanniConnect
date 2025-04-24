from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Transcription
from deep_translator import GoogleTranslator
import json

# Create your views here.

def speech_to_text(request):
    return render(request, 'index.html')

@csrf_exempt
def save_transcription(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            original_text = data.get('text')
            original_language = data.get('language', '').split('-')[0]  # Get language code without region

            # Translate to English if not already in English
            if not original_language.startswith('en'):
                try:
                    translator = GoogleTranslator(source=original_language, target='en')
                    english_text = translator.translate(text=original_text)
                except Exception as e:
                    return JsonResponse({
                        'status': 'error',
                        'message': f'Translation error: {str(e)}'
                    }, status=500)
            else:
                english_text = original_text

            # Save to database
            transcription = Transcription.objects.create(
                original_text=original_text,
                original_language=data.get('language'),  # Save full language code
                english_translation=english_text
            )

            return JsonResponse({
                'status': 'success',
                'english_translation': english_text
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=500)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

def view_transcriptions(request):
    transcriptions = Transcription.objects.all()
    return render(request, 'transcriptions.html', {'transcriptions': transcriptions})
