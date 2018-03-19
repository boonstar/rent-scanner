from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=200)
    ask_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.question
        
        
class Estate(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    link = models.URLField()
    rent = models.FloatField()
    area = models.FloatField()
    ask_date = models.DateTimeField(auto_now_add=True)
