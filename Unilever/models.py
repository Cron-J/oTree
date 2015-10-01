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
    name_in_url = 'Unilever'
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

    # Field in page FirstEntry
    expectation_to_like = models.SmallIntegerField(
        choices=[
            (1, "Dislike extremely"),
            (2, "Dislike a lot"),
            (3, "Dislike moderately"),
            (4, "Neither dislike nor like"),
            (5, "Like moderately"),
            (6, "Like a lot"),
            (7, "Like extremely")
        ],
        widget=widgets.RadioSelect
    )

    # Field in page SecondEntry
    likelihood_to_buy = models.SmallIntegerField(
        choices=[
            (1, "I would definitely not buy it"),
            (2, "I would probably not buy it"),
            (3, "I am not certain whether I would buy it or not"),
            (4, "I would probably buy it"),
            (5, "I would definitely buy it")
        ],
        widget=widgets.RadioSelect
    )

    payment_net = models.CurrencyField()

    def other_player(self):
        """Returns other player in group. Only valid for 2-player groups."""
        return self.get_others_in_group()[0]

    def role(self):
        # you can make this depend of self.id_in_group
        return ''

    def set_payoff(self):
        self.payment_net = Constants.endowment
        self.payoff = self.payment_net + Constants.pay_for_questionnaire