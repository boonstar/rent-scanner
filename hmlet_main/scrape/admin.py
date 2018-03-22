from django.contrib import admin
from .models import Question, Estate


class EstateInline(admin.TabularInline):
    model = Estate
    extra = 0

    
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'ask_date')
    inlines = [EstateInline]
    
    
class EstateAdmin(admin.ModelAdmin):
    list_display = ('question', 'rent', 'area', 'raw_text', 'ask_date', 'source', 'location')
    
    
admin.site.register(Question, QuestionAdmin)
admin.site.register(Estate, EstateAdmin)
