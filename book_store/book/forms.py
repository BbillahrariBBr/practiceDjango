from django import forms
from book.models import BookStoreModel

class BookStoreForm(forms.ModelForm):
    class Meta:
        model = BookStoreModel
        fields = ['id','book_name','author','category']
        # db_table = ''
        # managed = True
        # verbose_name = 'ModelName'
        # verbose_name_plural = 'ModelNames'