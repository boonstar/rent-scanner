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
    raw_text = models.TextField()
    ask_date = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=100)
    location = models.CharField(max_length=200, default = 'default')
    
    
class NestiaEstate(models.Model):
    url = models.URLField(default='default')
    # changed from id in original code
    nestiaId = models.CharField(max_length=200)
    propertyLeaseId = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    block = models.CharField(max_length=200)
    propertyTypeName = models.CharField(max_length=200)
    propertyTypeCode = models.CharField(max_length=200)
    rentalTypeName = models.CharField(max_length=200)
    rentalTypeCode = models.CharField(max_length=200)
    bedroomNumberName = models.CharField(max_length=200)
    bedroomNumberCode = models.CharField(max_length=200)
    bathroomNumberName = models.CharField(max_length=200)
    bathroomNumberCode = models.CharField(max_length=200)
    roomTypeName = models.CharField(max_length=200)
    roomTypeCode = models.CharField(max_length=200)
    bathroomTypeName = models.CharField(max_length=200)
    bathroomTypeCode = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    ImageURL1 = models.URLField(default='default')
    ImageURL2 = models.URLField(default='default')
    ImageURL3 = models.URLField(default='default')
    ImageURL4 = models.URLField(default='default')
    ImageURL5 = models.URLField(default='default')
    isLike = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    subDistrictId = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    projectId = models.CharField(max_length=200)
    isRecommendAgent = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    ask_date = models.DateTimeField(auto_now_add=True)