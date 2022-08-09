from django import forms

# GifForm with the fields
# uploader_name
# title
# url : You can use the gifs’ url from the giphy website. Click on the gif you want, and copy the gif link.
# categories : look up ModelMultipleChoiceField

class GifForm (forms.Form):
    uploader_name = forms.CharField()
    title = forms.CharField()
    url = forms.URLField()
    categories = forms.ModelMultipleChoiceField()


class CategoryForm(forms.Form):
    name = forms.CharField()
    