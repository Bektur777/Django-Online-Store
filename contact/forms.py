from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'question']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input-information',
                                           'placeholder': 'Введите имя'}),
            'email': forms.TextInput(attrs={'class': 'input-information',
                                            'placeholder': 'Введите e-mail'}),
            'question': forms.TextInput(attrs={'class': 'input-information',
                                               'placeholder': 'Введите вопрос'})
        }
