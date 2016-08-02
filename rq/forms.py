from django.forms import ModelForm, Textarea
from .models import Question


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ('q',)
        widgets = {
            'q': Textarea(attrs={'class': 'form-control', 'rows': '5'})
        }
