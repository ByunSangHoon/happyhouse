# coding: utf-8

from django import forms
from house.models import ClientInfo


class ClientInfoDetailForm(forms.ModelForm):
#    etc = forms.CharField(widget=forms.Textarea)
#    resident_name = forms.CharField()
#
#    room_type = forms.CharField()
#    is_usable = forms.BooleanField()
#
#    check_in_time = forms.CharField()
#
#    nationality = forms.CharField()
#    birth = forms.CharField()
#    ph_number = forms.CharField()
#    job = forms.CharField()
#
    def clean_ph_number(self):
        data = self.cleaned_data.get('ph_number', False)
        if not data:
            raise forms.ValidationError('핸드폰번호에서 에러가 났습니다.')

        return data

#    def clean_etc(self):
#        data = self.cleaned_data.get('etc', False)
#
#        if not data:
#            raise forms.ValidationError('기타정보에서 에러가 났습니다.');
#
#        return data

    def clean_resident_name(self):
        data = self.cleaned_data.get('resident_name', False)
        if not data:
            raise forms.ValidationError('거주자 이름에서 에러가 났습니다.')

        return data

    def clean(self):
        cleaned_data = super(ClientInfoDetailForm, self).clean()
        return cleaned_data

    class Meta:
        model = ClientInfo
        fields = (
            'resident_name', 'room_type',
            'is_usable', 'check_in_time', 'nationality',
            'birth', 'ph_number', 'job',
            'price', 'real_price',
        )

        exclude = (
            'room_number',
        )
