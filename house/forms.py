from django import forms
from house.models import ClientInfo


class ClientInfoDetailForm(forms.Form):
    etc = forms.CharField(widget=forms.Textarea)
    resident_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '~~~'}))

    room_type = forms.CharField()
    is_usable = forms.BooleanField()

    check_in_time = forms.CharField()

    nationality = forms.CharField()
    birth = forms.CharField()
    ph_number = forms.CharField()
    job = forms.CharField()

    def modify_etc(self, request, _room_number):
        posted_etc = self.cleaned_data.get('etc')
        client_info = ClientInfo.objects.get(room_number=_room_number)
        client_info.etc =posted_etc
        client_info.save()