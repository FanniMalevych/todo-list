from django import forms

from tasks.models import Tag, Task


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Task
        fields = "__all__"
