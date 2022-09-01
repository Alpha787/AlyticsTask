from django.shortcuts import render
from django.views.generic import TemplateView
from AlyticsDashboard.tasks import hello_world

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        hello_world()
        return context 
