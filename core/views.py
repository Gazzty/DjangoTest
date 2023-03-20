from django.views.generic.base import TemplateView
from django.shortcuts import render

class HomePageView(TemplateView):
    template_name = 'core/home.html'

    # Sobreescribimos el metodo get
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': 'Mi Web Playground'})

class SampleView(TemplateView):
    template_name = 'core/sample.html'