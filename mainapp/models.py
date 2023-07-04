from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Преподователь', related_name='course')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Катерия')
    name = models.CharField(max_length=124, verbose_name='Название курса')
    description = models.TextField(verbose_name='Описание курса')
    start_date = models.DateField(verbose_name='Дата старта')
    end_date = models.DateField(verbose_name='Дата окончание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    adress = models.CharField(max_length=255, verbose_name='Адрес офиса')
    additional_info = models.TextField(verbose_name='Дополнительная информация о курсе')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class CourseSchedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', related_name='course_schedule')
    start_date = models.DateTimeField(verbose_name='Дата начала и время начало')
    end_date = models.DateTimeField(verbose_name='Дата окончания и время окончание')

    def __str__(self):
        return f'{self.course} - {self.start_date}'

    class Meta:
        verbose_name = 'Расписание курса'
        verbose_name_plural = 'Расписание курсов'


class LearningTechnology(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название технологии')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Технология обучения'
        verbose_name_plural = 'Технологии обучения'