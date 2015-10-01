# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

author = 'GsM'

doc = """
Choice Method (Treatment 2)
"""


class Constants(BaseConstants):
    name_in_url = 'ChoiceHypothetical'
    players_per_group = None
    num_rounds = 1

    # define more constants here
    endowment = c(3)
    start_price = c(0.5)
    incremental_price = c(0.1)
    num_decisions = 16
    alpha = 1
    beta = 0.5
    pay_for_questionnaire = c(2)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    # <built-in>
    subsession = models.ForeignKey(Subsession)
    # </built-in>

    def set_payoffs(self):
        for p in self.get_players():
            p.payoff = 0 # change to whatever the payoff should be


class Player(BasePlayer):
    # <built-in>
    subsession = models.ForeignKey(Subsession)
    group = models.ForeignKey(Group, null = True)
    # </built-in>

    # Field in page Q1
    buyer = models.CharField(
        choices=[
            ('1', "Never"),
            ('2', "Rarely, less than once every half year"),
            ('3', "Sometimes, 1-3 times in half a year"),
            ('4', "Regularly, once each month"),
            ('5', "Quite often, once every two weeks"),
            ('6', "Heavy use, once a week or more"),
        ],
        widget=widgets.RadioSelect,
        verbose_name='How often do you consume chocolate?'
    )

    # Fields in page FirstEntry
    b1 = models.BooleanField(
        choices=[
            (True, 'Yes'),
            (False, 'No')
        ],
        widget=widgets.RadioSelectHorizontal,
        verbose_name="1)    " + str(Constants.start_price + 0 * Constants.incremental_price) + " for this chocolate that is produced with 100% sustainable inputs?"
    )
    b2 = models.BooleanField(
        choices=[
            (True, 'Yes'),
            (False, 'No')
        ],
        widget=widgets.RadioSelectHorizontal,
        verbose_name="2)    " + str(Constants.start_price + 1 * Constants.incremental_price) + " for this chocolate that is produced with 100% sustainable inputs?"
    )
    b3 = models.BooleanField(
        choices=[
            (True, 'Yes'),
            (False, 'No')
        ],
        widget=widgets.RadioSelectHorizontal,
        verbose_name="3)    " + str(Constants.start_price + 2 * Constants.incremental_price) + " for this chocolate that is produced with 100% sustainable inputs?"
    )
    b4 = models.BooleanField(
        choices=[
            (True, 'Yes'),
            (False, 'No')
        ],
        widget=widgets.RadioSelectHorizontal,
        verbose_name="4)    " + str(Constants.start_price + 3 * Constants.incremental_price) + " for this chocolate that is produced with 100% sustainable inputs?"
    )
    b5 = models.BooleanField(
        choices=[
            (True, 'Yes'),
            (False, 'No')
        ],
        widget=widgets.RadioSelectHorizontal,
        verbose_name="5)    " + str(Constants.start_price + 4 * Constants.incremental_price) + " for this chocolate that is produced with 100% sustainable inputs?"
    )
    b6 = models.BooleanField(
        choices=[
            (True, 'Yes'),
            (False, 'No')
        ],
        widget=widgets.RadioSelectHorizontal,
        verbose_name="6)    " + str(Constants.start_price + 5 * Constants.incremental_price) + " for this chocolate that is produced with 100% sustainable inputs?"
    )
    b7 = models.BooleanField(
        choices=[
            (True, 'Yes'),
            (False, 'No')
        ],
        widget=widgets.RadioSelectHorizontal,
        verbose_name="7)    " + str(Constants.start_price + 6 * Constants.incremental_price) + " for this chocolate that is produced with 100% sustainable inputs?"
    )
    b8 = models.BooleanField(
        choices=[
            (True, 'Yes'),
            (False, 'No')
        ],
        widget=widgets.RadioSelectHorizontal,
        verbose_name="8)    " + str(Constants.start_price + 7 * Constants.incremental_price) + " for this chocolate that is produced with 100% sustainable inputs?"
    )
    b9 = models.BooleanField(
        choices=[
            (True, 'Yes'),
            (False, 'No')
        ],
        widget=widgets.RadioSelectHorizontal,
        verbose_name="9)    " + str(Constants.start_price + 8 * Constants.incremental_price) + " for this chocolate that is produced with 100% sustainable inputs?"
    )
    b10 = models.BooleanField(
        choices=[
            (True, 'Yes'),
            (False, 'No')
        ],
        widget=widgets.RadioSelectHorizontal,
        verbose_name="10)    " + str(Constants.start_price + 9 * Constants.incremental_price) + " for this chocolate that is produced with 100% sustainable inputs?"
    )
    b11 = models.BooleanField(
        choices=[
            (True, 'Yes'),
            (False, 'No')
        ],
        widget=widgets.RadioSelectHorizontal,
        verbose_name="11)    " + str(Constants.start_price + 10 * Constants.incremental_price) + " for this chocolate that is produced with 100% sustainable inputs?"
    )
    b12 = models.BooleanField(
        choices=[
            (True, 'Yes'),
            (False, 'No')
        ],
        widget=widgets.RadioSelectHorizontal,
        verbose_name="12)    " + str(Constants.start_price + 11 * Constants.incremental_price) + " for this chocolate that is produced with 100% sustainable inputs?"
    )
    b13 = models.BooleanField(
        choices=[
            (True, 'Yes'),
            (False, 'No')
        ],
        widget=widgets.RadioSelectHorizontal,
        verbose_name="13)    " + str(Constants.start_price + 12 * Constants.incremental_price) + " for this chocolate that is produced with 100% sustainable inputs?"
    )
    b14 = models.BooleanField(
        choices=[
            (True, 'Yes'),
            (False, 'No')
        ],
        widget=widgets.RadioSelectHorizontal,
        verbose_name="14)    " + str(Constants.start_price + 13 * Constants.incremental_price) + " for this chocolate that is produced with 100% sustainable inputs?"
    )
    b15 = models.BooleanField(
        choices=[
            (True, 'Yes'),
            (False, 'No')
        ],
        widget=widgets.RadioSelectHorizontal,
        verbose_name="15)    " + str(Constants.start_price + 14 * Constants.incremental_price) + " for this chocolate that is produced with 100% sustainable inputs?"
    )
    b16 = models.BooleanField(
        choices=[
            (True, 'Yes'),
            (False, 'No')
        ],
        widget=widgets.RadioSelectHorizontal,
        verbose_name="15)    " + str(Constants.start_price + 15 * Constants.incremental_price) + " for this chocolate that is produced with 100% sustainable inputs?"
    )

    rn = models.SmallIntegerField(
        min=1,
        max=Constants.num_decisions
    )

    price = models.CurrencyField()
    deal = models.BooleanField()

    payment_net = models.CurrencyField()

    def other_player(self):
        """Returns other player in group. Only valid for 2-player groups."""
        return self.get_others_in_group()[0]

    def role(self):
        # you can make this depend of self.id_in_group
        return ''

    def set_payoff(self):
        self.rn = random.randint(1, Constants.num_decisions)
        self.price = Constants.start_price + (self.rn - 1) * Constants.incremental_price
        decisions = [self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9, self.b10, self.b11, self.b12, self.b13, self.b14, self.b15, self.b16]
        self.deal = decisions[self.rn - 1]

        self.payment_net = Constants.endowment
        self.payoff = self.payment_net + Constants.pay_for_questionnaire