from django.db import models

# Create your models here.
class Desk(models.Model):
    desk_number = models.IntegerField()
    desk_password = models.CharField(max_length = 20)

    def __str__(self):
        return f'Desk {self.desk_number }'
