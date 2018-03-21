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
        
        x= [1,3,5,7,9,11,13]
        # hist = Histogram(title="Rent Histogram", values="rent", bins=10)
        hist = Histogram(
            rents,
            ylabel='Count',
            xlabel='Rent($)',
            bins=8,
            title='query: {}'.format(qns.question),
            density=False
            )
        
        script, div = components(hist)
        # ####################################################################
        # x= [1,3,5,7,9,11,13]
        # y= [1,2,3,4,5,6,7]
        # title = 'y = f(x)'
        # 
        # plot = figure(title= title , 
        #     x_axis_label= 'X-Axis', 
        #     y_axis_label= 'Y-Axis', 
        #     plot_width =400,
        #     plot_height =400)
        # 
        # plot.line(x, y, legend= 'f(x)', line_width = 2)
        # #Store components 
        # script, div = components(plot)

        #Feed them to the Django template.
        # return render_to_response( 'bokeh/index.html',
        #         {'script' : script , 'div' : div} )
    
        ####################################################################
        
        args = {'estates': estates, 'script': script, 'div': div}
        
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
    
    
    
    
    
