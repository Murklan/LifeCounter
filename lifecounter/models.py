from __future__ import unicode_literals

from django.db import models
# from django.db.models import Count, Q


class Game(models.Model):

    def __unicode__(self):
        return 'Game ID: ' + self.password

    password = models.CharField(max_length=5)
    max_players = models.PositiveIntegerField()
    starting_life = models.PositiveIntegerField()

    def start_game(self):
        self.players.update(life_total=self.starting_life)


class PlayerQuerySet(models.QuerySet):
    def alive(self):
        return self.filter(life_total__gt=0, poison_counters__lt=10, damage_taken__cmdr_dmg__lt=21)

    def dead(self):
        return self.exclude(life_total__gt=0, poison_counters__lt=10, damage_taken__cmdr_dmg__lt=21)


class Player(models.Model):

    def __unicode__(self):
        return self.name

    objects = PlayerQuerySet.as_manager()

    game = models.ForeignKey(Game, related_name='players')
    name = models.CharField(max_length=20)
    life_total = models.PositiveIntegerField()
    exp_counters = models.PositiveIntegerField(default=0)
    poison_counters = models.PositiveIntegerField(default=0)


class CommanderDamage(models.Model):

    def __unicode__(self):
        return self.from_player.name + ' > ' + self.to_player.name + ' : ' + str(self.cmdr_dmg)

    from_player = models.ForeignKey(Player, related_name='damage_dealt')
    to_player = models.ForeignKey(Player, related_name='damage_taken')
    cmdr_dmg = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = (('to_player', 'from_player'),)
