from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timezone, date

# Create your models here.

DEFAULT_BOARD_USER_ID = 1

class Board(models.Model):
    name = models.CharField(max_length = 32)
    user = models.ForeignKey(User, on_delete = models.CASCADE,default = DEFAULT_BOARD_USER_ID)
    use_due_date = models.BooleanField(default = False)

    def __str__(self):
        return self.name


class Task(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    name = models.CharField(max_length = 64)
    points = models.IntegerField(default = 0)
    due_date = models.DateField(blank = True, null = True)
    in_scrum = models.BooleanField(default = False)

    def __str__(self):
        return self.name + "- linked to board: " + self.board.name

    def do_work(self, work_done):
        self.points = self.points - work_done
        if(self.points <= 0):
            self.delete()
        else:
            self.save()

    def is_done(self):
        return (self.points <= 0)

    @property
    def ppd(self):
        if self.due_date == None:
            return None
        else:
            days_left = (date.today() - self.due_date).days
            if days_left > 0:
                return round(self.points / days_left, 2)
            else:
                return None
