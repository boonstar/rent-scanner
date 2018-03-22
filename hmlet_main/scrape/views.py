import json
from django.shortcuts import get_object_or_404, redirect, render, render_to_response
from .forms import QuestionForm
from django.views import View
from django.views.generic.edit import FormView
from .models import Question, Estate
from . import search_func, utils_propertyguru, utils_iproperty
# from bokeh.plotting import figure, output_file, show 
from bokeh.charts import Histogram, show, output_file
from bokeh.embed import components
import numpy as np


class ResultView(View):
    def get(self, request, pk):
        qns = Question.objects.get(pk=pk)
        estates = Estate.objects.filter(question=qns)
        # draw graph etc
        
        ####################################################################
        
        rents = [i.rent for i in estates]
        area = [i.area for i in estates]
        psf = [x/y for x,y in zip(rents, area)]
        
        hist = Histogram(
            rents,
            ylabel='Count',
            xlabel='Rent($)',
            bins=8,
            title='query: {}'.format(qns.question),
            density=False
            )
        
        hist_psf = Histogram(
            psf,
            ylabel='Count',
            xlabel='Rent per square feet($)',
            bins=8,
            title='query: {}'.format(qns.question),
            density=False
            )
        
        script, div = components(hist)
        script_psf, div_psf = components(hist_psf)
        
        args = {'estates': estates, 'script': script, 'div': div, 'script_psf': script_psf, 'div_psf': div_psf}
        
        return render(request, 'results.html', args)

class SearchView(FormView):
    template_name = 'search.html'
    form_class = QuestionForm
    # success_url = '/scrape/'
        
    def form_valid(self, form, **kwargs):
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
        # return super(SearchView, self).form_valid(form)
        return redirect('scrape:results', qns.pk)
        
    
    
    def scan_iproperty(self, qns):
        print('Searching iproperty for {}'.format(qns.question))
        
        q, property_list, driver = search_func.set_query_iproperty(qns.question)
        
        for i in property_list:
            # check if exist based on URLField
            link_url = utils_iproperty.get_link(i)
            if not Estate.objects.filter(link=link_url).exists():
                print('--------------------New estate found-----------------------')
                est = Estate()
                est.question = qns
                est.link = link_url
                est.area = utils_iproperty.get_area(i)
                est.rent = utils_iproperty.get_rent(i)
                est.raw_text = i.text
                est.source = 'iproperty'
                est.location = utils_iproperty.get_location(i)
                est.save()
                print(i.text)
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
                print('--------------------New estate found-----------------------')
                est = Estate()
                est.question = qns
                est.link = link_url
                est.area = utils_propertyguru.get_area(i)
                est.rent = utils_propertyguru.get_rent(i)
                est.raw_text = i.text
                est.source = 'propertyguru'
                est.location = utils_propertyguru.get_location(i)
                est.save()
                print(i.text)
            else:
                print("Estate already exists")
        
        driver.quit()
    
    
    
    
    
