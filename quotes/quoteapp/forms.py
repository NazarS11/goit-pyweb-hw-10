from django.forms import ModelForm, CharField, TextInput, Textarea, DateField, DateInput, Select, ChoiceField, ModelMultipleChoiceField, ModelChoiceField
from .models import Quote, Author, Tag
from django_select2.forms import Select2Widget, Select2MultipleWidget



class AuthorForm(ModelForm):

    fullname = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    born_date = DateField(widget=DateInput(attrs={'type': 'date'}), required=True)
    
    class Meta:
        model = Author
        fields = ['fullname','born_date','born_location','description']

class TagForm(ModelForm):

    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    
    class Meta:
        model = Tag
        fields = ['name']


class QuoteForm(ModelForm):
    quote = CharField(
        min_length=20, 
        max_length=3000, 
        required=True, 
        widget=Textarea()
    )
    author = ModelChoiceField(
        queryset=Author.objects.all(),
        required=True,
        widget=Select
    )

    class Meta:
        model = Quote
        fields = ['quote', 'author']
        exclude = ['tags']