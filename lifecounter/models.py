from __future__ import unicode_literals

from django.db import models
from django.db.models import Max, Q


class Game(models.Model):
    password = models.CharField(max_length=5, unique=True)
    max_players = models.PositiveIntegerField()
    starting_life = models.PositiveIntegerField()

    def __unicode__(self):
        return 'Game ID: ' + self.password

    def start_game(self):
        self.players.update(life_total=self.starting_life)


class PlayerQuerySet(models.QuerySet):
    def alive(self):
        return self.annotate(Max('damage_taken__cmdr_dmg')).filter(
            Q(life_total__gt=0, poison_counters__lt=10,) &
            (Q(damage_taken__cmdr_dmg__max__lt=21) | Q(damage_taken__cmdr_dmg__max__isnull=True)))

    def dead(self):
        return self.annotate(Max('damage_taken__cmdr_dmg')).exclude(
            Q(life_total__gt=0, poison_counters__lt=10,) &
            (Q(damage_taken__cmdr_dmg__max__lt=21) | Q(damage_taken__cmdr_dmg__max__isnull=True)))


class Player(models.Model):
    game = models.ForeignKey(Game, related_name='players')
    name = models.CharField(max_length=20)
    life_total = models.PositiveIntegerField(default=0)
    exp_counters = models.PositiveIntegerField(default=0)
    poison_counters = models.PositiveIntegerField(default=0)

    objects = PlayerQuerySet.as_manager()

    def __unicode__(self):
        return self.name


class CommanderDamage(models.Model):
    from_player = models.ForeignKey(Player, related_name='damage_dealt')
    to_player = models.ForeignKey(Player, related_name='damage_taken')
    cmdr_dmg = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.from_player.name + ' > ' + self.to_player.name + ' : ' + str(self.cmdr_dmg)

    class Meta:
        unique_together = (('to_player', 'from_player'),)
