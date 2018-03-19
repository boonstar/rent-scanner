import json
from django.shortcuts import get_object_or_404
from .forms import QuestionForm
from django.views.generic.edit import FormView
from .models import Question, Estate
from . import search_func


class SearchView(FormView):
    template_name = 'search.html'
    form_class = QuestionForm
    success_url = '/scrape/'
    
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
        self.scan_test(qns)
        # self.scan(form.cleaned_data['question'])
        return super(SearchView, self).form_valid(form)
        
    # TODO: save all info to model
    
    def scan_test(self, qns):
        print(qns.question)
        
        q, property_list,driver = search_func.set_query(qns.question)
        
        for i in property_list:
            # check if exist based on URLField
            link_url = search_func.get_link(i)
            if not Estate.objects.filter(link=link_url).exists():
                print('New estate found')
                est = Estate()
                est.question = qns
                est.link = link_url
                est.area = search_func.get_area(i)
                est.rent = search_func.get_rent(i)
                est.save()
            else:
                print("Estate already exists")
        
        driver.quit()
    
    
    
    
    
    
    def scan(self, q):
        q, property_list, driver = search_func.set_query(q)
        data_iproperty = {}
        q = q.replace(' ', '-')
        for i in range(len(property_list)):
            data_iproperty[q + '_' + str(i)] = {}
            data_iproperty[q + '_' + str(i)]['link'] = search_func.get_link(property_list[i])
            data_iproperty[q + '_' + str(i)]['rent'] = search_func.get_rent(property_list[i])
            data_iproperty[q + '_' + str(i)]['area'] = search_func.get_area(property_list[i])

        # save answer
        search_func.save_obj(data_iproperty, "data_iproperty")
        
        driver.quit()
        

        # load answer and print
        try:
            data_iproperty = search_func.load_obj("data_iproperty")
            print(json.dumps(data_iproperty, indent=4))
        except:
            print('pickle is empty')
