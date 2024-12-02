from django.db import models

NULLABLE = {"blank": True, "null": True}


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='email')
    first_name = models.CharField(
        max_length=100,
        verbose_name="Фамилия",
        help_text="Введите фамилию"
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Имя",
        help_text="Введите имя"
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name="Отчество",
        help_text="Введите отчество",
        **NULLABLE,
    )
    comments = models.TextField(
        verbose_name="Комментарий",
        help_text="Введите комментарий",
        **NULLABLE,
    )

    def __str__(self):
        return f"{self.first_name} {self.name}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ("name", "first_name",)

