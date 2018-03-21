import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hmlet_main.settings")
django.setup()

from .models import Question, Estate


qns = Question.objects.get(pk=29)
print(qns)