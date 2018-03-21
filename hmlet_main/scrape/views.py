import json
from django.shortcuts import get_object_or_404
from .forms import QuestionForm
from django.views.generic.edit import FormView
from .models import Question, Estate
from . import search_func, utils_propertyguru, utils_iproperty


class SearchView(FormView):
    template_name = 'search.html'
    form_class = QuestionForm
    success_url = '/api/'
    
    def form_valid(self, form):
        q = form.cleaned_data['question']
        if not Question.objects.filter(question=q).exists():
            print('New question')
            qns = Question()
            qns.question = form.cleaned_data['question']
            qns.save()
        else:
            print('Question asked before')
            qns = Question.objects.get(question=q)
        self.scan_iproperty(qns)
        self.scan_propertyguru(qns)
        return super(SearchView, self).form_valid(form)
        
    
    
    def scan_iproperty(self, qns):
        print('Searching iproperty for {}'.format(qns.question))
        
        q, property_list, driver = search_func.set_query_iproperty(qns.question)
        
        for i in property_list:
            # check if exist based on URLField
            link_url = utils_iproperty.get_link(i)
            if not Estate.objects.filter(link=link_url).exists():
                print('New estate found')
                est = Estate()
                est.question = qns
                est.link = link_url
                est.area = utils_iproperty.get_area(i)
                est.rent = utils_iproperty.get_rent(i)
                est.raw_text = i.text
                est.save()
            else:
                print("Estate already exists")
        
        driver.quit()
        
    def scan_propertyguru(self, qns):
        print('Searching propertyguru for {}'.format(qns.question))
        
        q, property_list, driver = search_func.set_query_propertyguru(qns.question)
        
        for i in property_list:
            # check if exist based on URLField
            link_url = utils_propertyguru.get_link(i)
            if not Estate.objects.filter(link=link_url).exists():
                print('New estate found')
                est = Estate()
                est.question = qns
                est.link = link_url
                est.area = utils_propertyguru.get_area(i)
                est.rent = utils_propertyguru.get_rent(i)
                est.raw_text = i.text
                est.save()
            else:
                print("Estate already exists")
        
        driver.quit()
    
    
    
    
    
