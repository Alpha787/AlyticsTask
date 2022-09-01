from re import template
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
# import PIL
from django.utils.html import mark_safe


class Dashboard(models.Model):
    function = models.CharField(max_length=50, verbose_name="Функция")
    chart = models.ImageField(verbose_name="График", upload_to='AlyticsTask/media')
    interval = models.IntegerField(verbose_name="Интервал t, дней")
    pace = models.IntegerField(verbose_name="Шаг t, часы")
    prep_date = models.DateField(auto_now_add=True, verbose_name="Дата обработки")
    # добавить точное время с часами и секундами

    def __str__(self) -> str:
        return f"{self.function}, {self.chart}, {self.interval}, {self.pace}, {self.prep_date}"

    def chart_preview(self):
        if self.chart:
            return mark_safe(f'<img src="{self.chart.url}" width="200" height="150" />')
    chart_preview.short_description = u"График"
    chart.allow_tags = True


class Person(models.Model):
    last_name = models.TextField()
    first_name = models.TextField()
    courses = models.ManyToManyField("Course", blank=True)

    class Meta:
        verbose_name_plural = "People"

    def __str__(self) -> str:
        return f"{self.last_name}, {self.first_name}"

class Course(models.Model):
    name = models.TextField()
    year = models.IntegerField()

    class Meta:
        unique_together = ("name", "year",)

    def __str__(self) -> str:
        return f"{self.name}, {self.year}"

class Grade(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    grade = models.PositiveSmallIntegerField(
        validators= [MinValueValidator(0), MaxValueValidator(100)]
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.grade}, {self.person}, {self.course}"


