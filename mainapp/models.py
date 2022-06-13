from django.db import models

# Create your models here.
class Stock(models.Model):
    stock_name = models.CharField(max_length=30)
    stock_price = models.FloatField()

    def __str__(self):
        return f"{self.stock_name}"


class Team(models.Model):
    team_number = models.IntegerField()
    portfolio = {}

    def __str__(self):
        return f"Team {self.team_number}"