from django import forms
from .models import Comment
from taggit.models import Tag


class CommentForm(forms.ModelForm):
    """
    Форма комментария.
    """

    class Meta:
        model = Comment
        fields = ['body']


class SearchForm(forms.Form):
    """
    Форма для ввода поискового запроса.
    """

    query = forms.CharField()


class TagSelectionForm(forms.Form):
    """
    Форма выбора тегов.
    """

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )