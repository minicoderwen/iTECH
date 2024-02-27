from django import forms
from .models import Blog
from ckeditor.widgets import CKEditorWidget

class BlogForm(forms.ModelForm):

    title = forms.CharField(max_length=200, label='Title')
    tag = forms.CharField(max_length=200, label='Tag')
    content = forms.CharField(widget=CKEditorWidget())
    comment_num = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Blog
        fields = ['title', 'tag', 'content']



