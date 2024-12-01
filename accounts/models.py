from django.db import models
from django.contrib.auth.models import AbstractUser


class Manager(AbstractUser):
    TYPE_POSITION = {
        ("furniture_seller", "furniture_seller"),
        ("grill_seller", "grill_seller"),
        ("camping_seller", "camping_seller"),
    }

    position = models.CharField(
        max_length=60,
        choices=TYPE_POSITION,
        default="furniture_seller"
    )

    class Meta:
        verbose_name = "manager"
        verbose_name_plural = "managers"

    def __str__(self) -> str:
        return f"{self.username} ({self.position})"
