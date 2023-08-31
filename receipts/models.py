from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class ExpenseCategory(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(
        User,
        related_name="categories",
        on_delete=models.CASCADE,
    )


class Account(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    owner = models.ForeignKey(
        User,
        related_name="accounts",
        on_delete=models.CASCADE,
    )


class Receipt(models.Model):
    vendor = models.CharField(max_length=200)
    total = models.DecimalField(max_digits=10, decimal_places=3)
    tax = models.DecimalField(max_digits=10, decimal_places=3)
    date = models.DateTimeField(default=timezone.now)
    purchaser = models.ForeignKey(
        User,
        related_name="receipts",
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        ExpenseCategory,
        related_name="receipts",
        on_delete=models.CASCADE,
        null=True,
    )
    account = models.ForeignKey(
        Account,
        related_name="receipts",
        on_delete=models.CASCADE,
        null=True,
    )
