from django import forms
from .models import StockData


class StockDataForm(forms.ModelForm):
    class Meta:
        model = StockData
        fields = ['title', 'content']

    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        qs = StockData.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error('title', f'{title} Stock Already Exists!')
        return cleaned_data


# class StockDataFormOld(forms.Form):
#     title = forms.CharField()
#     content = forms.CharField()
#
#     def clean_title(self):
#         cleaned_data = self.cleaned_data  # Dict
#         title = cleaned_data.get('title')
#         if title == 'AAA':
#             raise forms.ValidationError('This Stock Already Exists!')
#         return title

    # def cleaned(self):
    #     cleaned_data = self.cleaned_data
    #     title = cleaned_data.get('title')
    #     if title == 'AAA':
    #         self.add_error('title', 'This Stock Already Exists!')
    #     return cleaned_data
