from django import forms
from .models import*


class TextFormF(forms.ModelForm):
    class Meta:
        model = TextForm
        fields = '__all__' 



class PdfFormF(forms.ModelForm):
    class Meta:
        model = PdfForm
        fields = '__all__'         


class VideoFormF(forms.ModelForm):
    class Meta:
        model = VideoForm
        fields = '__all__'
        


