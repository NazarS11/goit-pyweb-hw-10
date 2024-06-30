from django.forms import ModelForm, CharField, TextInput, Textarea, DateField, DateInput, Select, CheckboxSelectMultiple, ModelMultipleChoiceField, ModelChoiceField, SelectMultiple
from .models import Quote, Author, Tag
from django_select2.forms import Select2Widget, Select2MultipleWidget



class AuthorForm(ModelForm):

    fullname = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    born_date = DateField(widget=DateInput(attrs={'type': 'date'}), required=True)
    description = CharField(
        min_length=0, 
        max_length=20000, 
        required=True, 
        widget=Textarea()
    )
    
    
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
        min_length=0, 
        max_length=2000, 
        required=True, 
        widget=Textarea()
    )
    author = ModelChoiceField(
        queryset=Author.objects.all(),
        required=True,
        widget=Select
    )

    tags = ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=SelectMultiple(attrs={'class': 'scrollable-select'})
    )

    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']
