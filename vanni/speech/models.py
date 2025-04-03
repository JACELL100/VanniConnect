from django.db import models

# Create your models here.

class Transcription(models.Model):
    original_text = models.TextField()
    original_language = models.CharField(max_length=10)
    english_translation = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.original_language} - {self.timestamp}"

    class Meta:
        ordering = ['-timestamp']
