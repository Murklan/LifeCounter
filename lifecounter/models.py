from __future__ import unicode_literals

from django.db import models


class Game(models.Model):

    def __unicode__(self):
        return 'Game ID: ' + self.password

    password = models.CharField(max_length=5)
    max_players = models.PositiveIntegerField()
    starting_life = models.PositiveIntegerField()

    def start_game(self):
        self.players.update(life_total=self.starting_life)


class Player(models.Model):

    def __unicode__(self):
        return self.name

    game = models.ForeignKey(Game, related_name='players')
    name = models.CharField(max_length=20)
    life_total = models.PositiveIntegerField()
    exp_counters = models.PositiveIntegerField(default=0)
    poison_counters = models.PositiveIntegerField(default=0)

    def change_life_total(self, increment):
        life_total = self.life_total + increment
        self.update(life_total=life_total)

    def add_exp_counters(self, increment):
        self.exp_counters += increment

    def add_poison_counters(self, increment):
        self.poison_counters += increment


class CommanderDamage(models.Model):

    def __unicode__(self):
        return self.from_player.name + ' > ' + self.to_player.name + ' : ' + str(self.cmdr_dmg)

    from_player = models.ForeignKey(Player, related_name='damage_taken')
    to_player = models.ForeignKey(Player, related_name='damage_dealt')
    cmdr_dmg = models.PositiveIntegerField(default=0)

    def add_cmdr_dmg(self, increment):
        self.cmdr_dmg += increment

    class Meta:
        unique_together = (('to_player', 'from_player'),)
