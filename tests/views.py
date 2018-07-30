from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .forms import AddTestTrueFalseForm, AddTestWriteForm, AddTestABCForm, AddTestFillInForm, \
    AnswerABCForm, AnswerTFForm, AnswerWriteForm
from .models import Test, TestFillInText, TestFillInAnswer, AnswerTestFillInAnswer, Answer, TestABC, TestTrueFalse, \
    TestWriteAnswer


# Create your views here.


class AnswerDetailsView(DetailView):
    template_name = 'tests/answer_details.html'
    model = Answer
    context_object_name = 'answer'

    test_types = {
        'ABC': TestABC,
        'TF': TestTrueFalse,
        'FILLIN': Test,
        'WRITE': TestWriteAnswer
    }

    def get_queryset(self):
        return Answer.objects.filter(pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super(AnswerDetailsView, self).get_context_data(**kwargs)
        test = Test.objects.get(pk=Answer.objects.get(pk=self.kwargs.get('pk')).test.pk)
        new_test = self.test_types[test.test_type].objects.get(pk=Answer.objects.get(pk=self.kwargs.get('pk')).test.pk)
        context['test'] = new_test

        if test.test_type == 'FILLIN':
            answer = Answer.objects.get(pk=self.kwargs.get('pk'))
            print(answer)
            context['answer_set'] = answer.answertestfillinanswer_set.all()
            context['correct_answer_set'] = test.testfillinanswer_set.all()
            context['text_set'] = test.testfillintext_set.all()
            context['range'] = range(0, len(test.testfillinanswer_set.all()) + len(test.testfillintext_set.all()) + 1)

        return context


class TestListView(ListView):
    model = Test
    context_object_name = 'test'
    template_name = 'tests/user_test_list.html'


class AnswerListView(ListView):
    model = Answer
    template_name = 'tests/answer_list.html'
    context_object_name = 'answer_list'

    def get_queryset(self):
        query_set = Answer.objects.filter(user=self.kwargs.get('pk')).all()
        return query_set

    def get_context_data(self, **kwargs):
        context = super(AnswerListView, self).get_context_data(**kwargs)
        context['user_list'] = User.objects.all()
        return context


class AddTestView(CreateView):
    success_url = '/test_list'
    template_name = 'tests/admin_test_add.html'

    test_types = {
        'abc': AddTestABCForm,
        'truefalse': AddTestTrueFalseForm,
        'fillin': AddTestFillInForm,
        'writeanswer': AddTestWriteForm
    }

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('/login/')
            # TODO redirect if user not staff
        return super(AddTestView, self).dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        self.form_class = self.test_types[self.kwargs.get('test_type')]
        return self.form_class

    def post(self, request, *args, **kwargs):
        form = self.test_types[self.kwargs.get('test_type')](request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                item = form.save(commit=False)
                item.user = request.user
                item.save()
        return redirect(self.success_url)

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('/login/')
        return super(AddTestView, self).get(request, *args, **kwargs)


class AnswerTestView(CreateView):
    success_url = '/answer_details/'
    template_name = 'tests/user_answer.html'
    form_class = AnswerABCForm()

    test_types = {
        'ABC': AnswerABCForm(),
        'TF': AnswerTFForm(),
        'FILLIN': AnswerABCForm(),
        'WRITE': AnswerWriteForm()
    }

    def get_form(self, form_class=None):
        test = Test.objects.get(pk=self.kwargs.get('pk'))
        return self.test_types[test.test_type]

    def get(self, request, *args, **kwargs):
        print (self.kwargs.get('pk'))
        return render(request, self.template_name, {
            'test': Test.objects.get(pk=self.kwargs.get('pk')),
            'form': self.get_form()
        })

    def post(self, request, *args, **kwargs):
        form = self.get_form().__class__(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            item = form.save(commit=False)
            item.test = Test.objects.get(pk=self.kwargs.get('pk'))
            item.user = request.user
            item.save()
            return redirect(self.success_url + str(item.pk))
        return redirect('/test_list')


class AnswerFillInTestView(CreateView):
    form_class = AddTestFillInForm()
    success_url = '/test_list'
    template_name = 'tests/user_answer_fill_in.html'

    def get_form(self, form_class=None):
        self.form_class = AddTestFillInForm()
        test = Test.objects.get(pk=self.kwargs.get('pk'))
        for answer in test.testfillinanswer_set.all():
            self.form_class.add_answer_field()
        return self.form_class

    def get(self, request, *args, **kwargs):
        self.get_form()
        test = Test.objects.get(pk=self.kwargs.get('pk'))
        return render(request, self.template_name, {
            'test': test,
            'answer_set': test.testfillinanswer_set.all(),
            'text_set': test.testfillintext_set.all(),
            'range': range(0, len(test.testfillinanswer_set.all()) + len(test.testfillintext_set.all()) + 1)
        })

    def post(self, request, *args, **kwargs):
        test = Answer()
        test.user = request.user
        test.test = Test.objects.get(pk=self.kwargs.get('pk'))
        test.save()
        for answer in request.POST.dict():
            if not answer == 'csrfmiddlewaretoken':
                a = AnswerTestFillInAnswer()
                a.test = test
                a.text = request.POST.dict()[answer]
                a.position = int(answer[6:])
                a.save()
        return redirect(self.success_url)


class AddTestFillInView(CreateView):
    form_class = AddTestFillInForm()
    success_url = '/test_list'
    template_name = 'tests/user_test_solving.html'

    def get_form(self, form_class=None):
        self.form_class.clear()
        return self.form_class

    def post(self, request, *args, **kwargs):
        if request.POST.dict()['add_button'] == 'add_text':
            return render(request, self.template_name, {'form': self.form_class.add_text_field()})
        if request.POST.dict()['add_button'] == 'add_answer':
            return render(request, self.template_name, {'form': self.form_class.add_answer_field()})
        if request.POST.dict()['add_button'] == 'save':
            form = self.form_class
            test = Test()
            test.user = request.user
            test.name = request.POST.dict()['name']
            test.test_type = 'FILLIN'
            test.save()
            for field in request.POST.dict():
                if field in form.fields:
                    print(request.POST.dict()[field])

                    if 'text' in field:
                        text = TestFillInText()
                        text.test = test
                        text.text = request.POST.dict()[field]
                        s = field[5:]
                        text.position = int(s)
                        text.save()
                    if 'answer' in field:
                        answer = TestFillInAnswer()
                        answer.test = test
                        answer.text = request.POST.dict()[field]
                        s = field[7:]
                        answer.position = int(s)
                        answer.save()
            redirect(self.success_url)
        self.get_form()
        return render(request, self.template_name, {'form': self.form_class})
