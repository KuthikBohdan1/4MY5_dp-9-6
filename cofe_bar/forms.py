from .models import Register
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class ArticlesForm(ModelForm):

    class Meta:
        model = Register
        fields = ['name', 'password', 'return_password', 'user_birth_date']
        # fields = []
        widgets = {
            'name' : TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'псевдонім ',
            }),
            'password' : TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'пароль',
            }),
            'return_password' : TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'пароль 2',
            }),
            'user_birth_date' : DateTimeInput(attrs={
                'class': 'form-control',
                # 'type': 'datetime-local'
            })


        }