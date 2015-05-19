# coding: utf-8

from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, FormView
from house.forms import ClientInfoDetailForm
from house.models import ClientInfo


class ClientInfoListTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(ClientInfoListTemplateView, self).get_context_data(**kwargs)
        context['ClientInfo'] = ClientInfo.objects.all()
        return context

class ClientDetailTemplateView(FormView):
    template_name = 'client_info_detail.html'
    form_class = ClientInfoDetailForm
    success_url = '/house/'

    def get_context_data(self, **kwargs):
        print self.request.method
        context = super(ClientDetailTemplateView, self).get_context_data(**kwargs)
        client_info_id = self.kwargs['client_info_id']
        context['info'] = ClientInfo.objects.get(room_number=client_info_id)
        return context

    def get_form(self, form_class):
        try:
            client_info_id = self.kwargs.get('client_info_id', -1)
            client_info_instance = ClientInfo.objects.get(id = client_info_id)
            return form_class(instance=client_info_instance, **self.get_form_kwargs())
        except ClientInfo.DoesNotExist:
            return form_class(**self.get_form_kwargs())

    def form_invalid(self, form):
        print form.errors
        return super(ClientDetailTemplateView, self).form_invalid(form)

    def form_valid(self, form):
        client_info_id = self.kwargs['client_info_id']
        if form.is_valid():
            form.save()

        return super(ClientDetailTemplateView, self).form_valid(form)
