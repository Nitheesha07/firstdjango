from django import forms
from home1.models import Book,Author,Genre

"""

class CustomForms(forms.Form):
    username = forms.CharField(
        label = 'username',
        widget = forms.TextInput(
            attrs = { 'placeholder':'Your username','class':'form-control','max':'20'
            }
        )

    )

    email = forms.EmailField(label='Your Email',widget=forms.EmailInput(attrs={'placeholder':'ac@gmail.com','class':'form-control'}))

    """

class BookForms(forms.Form):
    name = forms.CharField(label = 'Book Name',
        widget = forms.TextInput(attrs = {'maxlength':'30','placeholder':'Book Name'}))
        
    author = forms.ModelChoiceField(queryset = Author.objects.all(),empty_label = 'Author',widget = forms.Select(attrs= {'name':'author','id':'author','class':'custom-select'}))

    pur_date = forms.DateField(label = '',widget = forms.DateInput(attrs = { 'placeholder':'Purchase Date','name':'pur_date','id':'pur_date','class':'form-control'}))

    #isbn = forms.CharField(label= 'ISBN Number',widget = forms.TextInput(attrs={'placeholder':'ISBN Number','class':'form-control','name':'isbn','id':'isbn'}))

    #genre = forms.ModelMultipleChoiceField(queryset = Genre.objects.all(),widget=forms.CheckboxSelectMultiple)

class ModelBookForms(forms.ModelForm):
    class Meta:
        model=Book
        fields=('name','genre','purchase_date','book_author')

    




class SearchForm(forms.Form):
    q = forms.CharField(label = '',
        widget = forms.TextInput(attrs = {'maxlength':'30','placeholder':'Search','class':'form-control','minlength':'2'}))