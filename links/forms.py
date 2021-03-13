from django import forms
from .models import Tag, Link


class SearchForm(forms.Form):
    type = forms.MultipleChoiceField(label='Filter by resource type', choices=Link.TYPE_CHOICES, required=False)
    tags = forms.ModelMultipleChoiceField(label='Filter by topic', queryset=Tag.objects.all(), required=False)
    level = forms.ChoiceField(label='Experience level', choices=Link.LEVEL_CHOICES, required=False)

    def clean(self):
        cleaned_data = super().clean()
        level = cleaned_data.get("level")
        type = cleaned_data.get("type")
        tags = cleaned_data.get("tags")
        if len(level) == 0 and len(type) == 0 and len(tags) == 0:
            raise forms.ValidationError("No search or filter parameters specified")

