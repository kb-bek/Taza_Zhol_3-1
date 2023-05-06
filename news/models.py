from django.db import models

class New(models.Model):

    title = models.CharField(
        max_length=100,
        db_index=True,
        blank=True,
        verbose_name='Заголовок'
    )


    subtitle = models.TextField(
        db_index=True,
        blank=True,
        verbose_name='Подзоголовок'
    )


    date = models.DateTimeField(
        blank=True,
        db_index=True,
        verbose_name='Дата'
    )



    image = models.ImageField(
        upload_to='images/% Y/% m/% d/'
    )

    def __str__(self):
        return self.title


