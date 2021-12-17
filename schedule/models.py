from django.db import models

class Player(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    last_name = models.CharField(null=False, blank=False, max_length=100)
    date_of_birth = models.DateTimeField(null=False, blank=False)
    status = models.BooleanField()
    health_status = models.CharField(null=False, blank=False, max_length=300)
    salary = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Stadium(models.Model):
    title = models.CharField(null=False, blank=False, max_length=150)
    number_of_seats = models.IntegerField(null=True, blank=True)
    price_per_place = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.title}"


class Game(models.Model):
    title = models.CharField(null=False, blank=False, max_length=200,default="Opponents will be known soon")
    date = models.DateTimeField(null=False, blank=False)
    venue = models.ForeignKey(Stadium, on_delete=models.SET_NULL,null=True, blank=True)
    viewers = models.IntegerField(null=True, blank=True)
    result = models.CharField(null=True, blank=True, default="Game doesn't started yet",max_length=200)
    players = models.ManyToManyField(Player,null=True, blank=True,max_length=11)

    def __str__(self):
        return f"{self.title}"

