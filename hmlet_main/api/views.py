from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import generics
from scrape.models import Question, Estate
import api.serializers as serializers


class QuestionListAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionListSerializer

    
class QuestionAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    
    
class EstateListAPIView(generics.ListCreateAPIView):
    queryset = Estate.objects.all()
    serializer_class = serializers.EstateListSerializer

    
class EstateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estate.objects.all()
    serializer_class = serializers.EstateSerializer
    
    
@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'question': reverse('question', request=request, format=format),
        'estate': reverse('estate', request=request, format=format),
    })
