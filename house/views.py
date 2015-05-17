from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from house.models import ClientInfo


class IndexTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexTemplateView, self).get_context_data(**kwargs)
        context['ClientInfo'] = ClientInfo.objects.all()
        return context
