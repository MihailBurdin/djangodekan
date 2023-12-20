from .models import Articles
from django.forms import ModelForm, TextInput,DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title','anons','full_text','date']

        widgets ={
            'title':TextInput(attrs={
                'class':'form__control',
                'placecholder': 'Название товара'
            }),
            'anons': TextInput(attrs={
                'class': 'form__control',
                'placecholder': 'Описание'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form__control',
            }),
            'full_text': Textarea(attrs={
                'class': 'form__control',
                'placecholder': 'Текст'

            }),
        }