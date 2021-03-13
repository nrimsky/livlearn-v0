from django import forms
from .models import Tag, Link


class SearchForm(forms.Form):
    q = forms.CharField(label='Search for a topic...', max_length=200, required=False)
    level = forms.MultipleChoiceField(label='Experience level', choices=Link.LEVEL_CHOICES, required=False)
    type = forms.MultipleChoiceField(label='Resource type', choices=Link.TYPE_CHOICES, required=False)
    tags = forms.ModelMultipleChoiceField(label='Choose tags', queryset=Tag.objects.all(), required=False)

    def clean(self):
        cleaned_data = super().clean()
        q = cleaned_data.get("q")
        level = cleaned_data.get("level")
        type = cleaned_data.get("type")
        tags = cleaned_data.get("tags")
        if q == "" and len(level) == 0 and len(type) == 0 and len(tags) == 0:
            raise forms.ValidationError("No search or filter parameters specified")

