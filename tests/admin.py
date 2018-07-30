from django.contrib import admin

from tests.models import TestABC, TestTrueFalse, TestWriteAnswer, Test, Answer, TestFillInAnswer, TestFillInText, \
    AnswerTestFillInAnswer

# Register your models here.
admin.site.register(TestABC)
admin.site.register(TestTrueFalse)
admin.site.register(TestWriteAnswer)
admin.site.register(Test)
admin.site.register(Answer)
admin.site.register(TestFillInAnswer)
admin.site.register(TestFillInText)
admin.site.register(AnswerTestFillInAnswer)
