from django.db import models
from django_eveonline_connector.models import EveCharacter, EveCorporation, EveAlliance
from django.contrib.auth.models import User, Group

class EveTimer(models.Model):
    timer_types = (
        ("OFFENSIVE", "Offensive"),
        ("DEFENSIVE", "Defensive"),
        ("THIRD_PARTY", "Third Party")
    )
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=32, choices=timer_types)
    timer = models.DateTimeField(auto_now=False, auto_now_add=False)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    groups = models.ManyToManyField(Group, blank=True)

    def __str__(self):
        return self.name