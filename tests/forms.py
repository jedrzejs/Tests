from django import forms

from .models import TestABC, TestTrueFalse, TestWriteAnswer, Answer


class AddTestABCForm(forms.ModelForm):

    def save(self, commit=True):
        model = super(AddTestABCForm, self).save(False)
        model.test_type = 'ABC'
        return super(AddTestABCForm, self).save(commit)

    class Meta:
        model = TestABC
        fields = [
            'name',
            'question',
            'correct_answer'
        ]
        widgets = {
            'correct_answer': forms.RadioSelect
        }


class AddTestTrueFalseForm(forms.ModelForm):

    def save(self, commit=True):
        model = super(AddTestTrueFalseForm, self).save(False)
        model.test_type = 'TF'
        return super(AddTestTrueFalseForm, self).save(commit)

    class Meta:
        model = TestTrueFalse
        fields = [
            'name',
            'question',
            'correct_answer'
        ]
        widgets = {
            'correct_answer': forms.RadioSelect
        }


class AddTestWriteForm(forms.ModelForm):

    def save(self, commit=True):
        model = super(AddTestWriteForm, self).save(False)
        model.test_type = 'WRITE'
        return super(AddTestWriteForm, self).save(commit)

    class Meta:
        model = TestWriteAnswer
        fields = [
            'name',
            'question',
            'correct_answer'
        ]


class AddTestFillInForm(forms.Form):
    name = forms.CharField(max_length=10)
    number_of_answer_fields = 0
    number_of_text_fields = 0

    def add_answer_field(self):
        self.number_of_answer_fields += 1
        self.fields['answer {}'.format(self.number_of_text_fields + self.number_of_answer_fields)] = forms.CharField()
        return self

    def add_text_field(self):
        self.number_of_text_fields += 1
        self.fields['text {}'.format(self.number_of_text_fields + self.number_of_answer_fields)] = forms.CharField(
            widget=forms.Textarea)
        return self

    def clear(self):
        self.number_of_answer_fields = 0
        self.number_of_text_fields = 0
        for k in list(self.fields.keys()):
            if not 'name' in k:
                print (k)
                del self.fields[k]


class AnswerABCForm(forms.ModelForm):
    class Meta:
        CHOICES = (
            ('A', 'A'),
            ('B', 'B'),
            ('C', 'C'),
            ('D', 'D'),
            ('E', 'E')
        )
        model = Answer
        fields = [
            'answer'
        ]
        widgets = {
            'answer': forms.RadioSelect(choices=TestABC.CHOICES)
        }


class AnswerTFForm(forms.ModelForm):
    class Meta:
        model = Answer

        fields = [
            'answer'
        ]
        widgets = {
            'answer': forms.RadioSelect(choices=TestTrueFalse.CHOICES)
        }


class AnswerWriteForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [
            'answer'
        ]
