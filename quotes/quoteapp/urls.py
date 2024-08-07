from django.urls import path
from . import views

app_name = 'quoteapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('add_author/', views.add_author, name='add_author'),
    path('tag/', views.add_tag, name='add_tag'),
    path('quote/', views.add_quote, name='quote'),
    path('detail/<int:quote_id>', views.detail, name='detail'),
    path('delete/<int:quote_id>', views.delete_quote, name='delete'),
    path('author/<int:author_id>', views.author, name='author'),
    path('my_quotes/', views.my_qoutes, name='my_quotes'),
    path('edit/<int:quote_id>/', views.edit_quote, name='edit_quote'),    

]