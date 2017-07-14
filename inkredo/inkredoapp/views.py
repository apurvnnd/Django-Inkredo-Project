from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from . import models

class IndexView(TemplateView):
    template_name = 'index.html'

class CompanyListView(ListView):
    context_object_name = 'companies'
    model = models.Company

class CompanyDetailView(DetailView):
    context_object_name = 'company_detail'
    model = models.Company
    template_name = 'inkredoapp/company_detail.html'

class CompanyCreateView(CreateView):
    fields = ('name','ceo','location')
    model = models.Company

class CompanyUpdateView(UpdateView):
    fields = ('name','ceo')
    model = models.Company

class CompanyDeleteView(DeleteView):
    model = models.Company
    success_url = reverse_lazy("inkredoapp:list")
