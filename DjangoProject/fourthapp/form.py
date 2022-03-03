from django import forms

from fourthapp.models import Car

#模型表单
class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

