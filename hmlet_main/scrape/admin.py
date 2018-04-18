from django.contrib import admin
from .models import Question, Estate, NestiaEstate


class EstateInline(admin.TabularInline):
    model = Estate
    extra = 0

    
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'ask_date')
    inlines = [EstateInline]
    
    
class EstateAdmin(admin.ModelAdmin):
    list_display = ('question', 'rent', 'area', 'raw_text', 'ask_date', 'source', 'location')
    
    
class NestiaEstateAdmin(admin.ModelAdmin):
    list_display = (
        'url',
        'nestiaId',
        'propertyLeaseId',
        'name',
        'street',
        'block',
        'propertyTypeName',
        'propertyTypeCode',
        'rentalTypeName',
        'rentalTypeCode',
        'bedroomNumberName',
        'bedroomNumberCode',
        'bathroomNumberName',
        'bathroomNumberCode',
        'roomTypeName',
        'roomTypeCode',
        'bathroomTypeName',
        'bathroomTypeCode',
        'price',
        'ImageURL1',
        'ImageURL2',
        'ImageURL3',
        'ImageURL4',
        'ImageURL5',
        'isLike',
        'tags',
        'subDistrictId',
        'latitude',
        'longitude',
        'projectId',
        'isRecommendAgent',
        'date'
    )
    
admin.site.register(Question, QuestionAdmin)
admin.site.register(Estate, EstateAdmin)
admin.site.register(NestiaEstate, NestiaEstateAdmin)
