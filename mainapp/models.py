from email.policy import default
from django.db import models

# Create your models here.
class Stock(models.Model):
    stock_name = models.CharField(max_length=30)
    stock_price = models.FloatField()

    def __str__(self):
        return f"{self.stock_name}"


class Team(models.Model):
    team_number = models.IntegerField()
    team_balance = models.FloatField(default=100000)
    portfolio = models.JSONField(default = "{}")
    portfolio_short = models.JSONField(default = "{}")
    def __str__(self):
        return f"Team {self.team_number}"