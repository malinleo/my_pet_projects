from django.db import models


# Create your models here.
from django.urls import reverse


ANSWER_CHOICES = [
    (1, "First"),
    (2, "Second"),
]


class Question(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    question_variant_1 = models.TextField("Вариант ответа 1")
    question_variant_2 = models.TextField("Вариант ответа 2")
    answer = models.CharField("Ответ", choices=ANSWER_CHOICES, max_length=1,  editable=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Test(models.Model):
    title = models.CharField("Название теста", max_length=300)
    description = models.TextField("Описание")
    questions = models.ManyToManyField(Question, verbose_name="Вопросы", related_name="questions")
    test_result = models.CharField("Результат", max_length=20, default='', editable=False)
    url = models.SlugField(max_length=160, unique=True, default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("test_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"
