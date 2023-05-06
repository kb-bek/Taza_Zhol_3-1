from django.db import models


class Review(models.Model):

    full_name = models.CharField(
        max_length=70,
        db_index=True,
        blank=True,
        verbose_name='ФИО'
    )

    title = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name='Заголовок'
    )

    review = models.TextField(
        db_index=True,
        blank=True,
        verbose_name='Отзыв'
    )

    address = models.CharField(
        max_length=256,
        db_index=True,
        blank=True,
        verbose_name='Адрес'
    )

    date = models.DateTimeField(
        verbose_name='Дата'
    )

    image = models.ImageField(
        upload_to='images/reviews/% Y/% m/% d/',
        verbose_name='Фото'
    )

    email = models.EmailField(
        max_length=100,
        verbose_name='Email'
    )

    def __str__(self):
        return self.full_name



