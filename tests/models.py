from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models

# Create your models here.

User = AUTH_USER_MODEL


class Test(models.Model):
    TEST_TYPE = (
        ('ABC', 'ABC'),
        ('TF', 'TF'),
        ('WRITE', 'WRITE'),
        ('FILLIN', 'FILLIN')
    )

    test_type = models.CharField(max_length=6, choices=TEST_TYPE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    question = models.TextField()

    def __str__(self):
        return self.name


class TestABC(Test):
    CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E')
    )
    correct_answer = models.CharField(max_length=1, choices=CHOICES, default='A')


class TestTrueFalse(Test):
    CHOICES = (
        ('PRAWDA', 'PRAWDA'),
        ('FALSZ', 'FALSZ')
    )
    correct_answer = models.CharField(max_length=6, choices=CHOICES)


class TestWriteAnswer(Test):
    correct_answer = models.TextField()


class TestFillInText(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    position = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.text


class TestFillInAnswer(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    text = models.CharField(max_length=25)
    position = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.text


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    answer = models.CharField(max_length=250)

    def __str__(self):
        return self.test.name


class AnswerTestFillInAnswer(models.Model):
    test = models.ForeignKey(Answer, on_delete=models.CASCADE)
    text = models.CharField(max_length=25)
    position = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.text
