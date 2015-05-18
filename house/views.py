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
        context = super(ClientDetailTemplateView, self).get_context_data(**kwargs)
        client_info_id = self.kwargs['client_info_id']
        context['info'] = ClientInfo.objects.get(room_number=client_info_id)
        return context

    def form_valid(self, form):
        client_info_id = self.kwargs['client_info_id']
        form.modify_etc(self.request, client_info_id)
        return super(ClientDetailTemplateView, self).form_valid(form)
