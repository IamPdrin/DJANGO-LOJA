from django import forms
from appHome.models import Produto, Login

class FormProduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('nome', 'preco', 'quantidade', 'foto')
        
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control border border-success', 'placeholder': 'nome produto aqui'}),
            'preco': forms.TextInput(attrs={'class': 'form-control border border-success', 'placeholder': 'preco produto aqui'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control border border-success', 'placeholder': 'quantidade produto aqui'}),
            'foto':  forms.FileInput(attrs={'class': 'form-control border border-success','accept': 'image/*'}),
        }

        labels = {
            'nome' : 'Nome',
            'preco': 'Preco',
            'quantidade': 'Quantidade',
            'foto': 'Foto'
        }

class FormLogin(forms.ModelForm):
    class Meta:
        model = Login
        fields = ('email', 'senha')
        
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control border border-success', 'type': 'email'}),
            'senha': forms.TextInput(attrs={'class': 'form-control border border-success', 'type': 'password'}),
        }


class FormAddLogin(forms.ModelForm):
    class Meta:
        model = Login
        fields = ('usuario','email', 'senha')
        
        widgets = {
            'usuario': forms.TextInput(attrs={'class': 'form-control border border-success'}),
            'email': forms.TextInput(attrs={'class': 'form-control border border-success', 'type': 'email'}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control border border-success', 'type': 'password'}),
        }

