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
This is v2 of KFPP with chocolate bars - Peer prediction method
"""


class Constants(BaseConstants):
    name_in_url = 'KFPP'
    players_per_group = 3
    num_rounds = 1

    # define more constants here
    alpha = c(1)
    beta = c(0.5)
    possible_willingness_to_pay_list = [c(0.0)] + currency_range(c(0.5), c(2), c(0.1))
    possible_willingness_to_pay = [(i, possible_willingness_to_pay_list[i]) for i in range(len(possible_willingness_to_pay_list))]
    pay_for_questionnaire = c(2)

    # choices for prediction
    prediction_choices = [
        (0, 'Not at all'),
        (1, ''),
        (2, ''),
        (3, ''),
        (4, ''),
        (5, ''),
        (6, ''),
        (7, ''),
        (8, ''),
        (9, ''),
        (10, 'Very likely'),
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    # <built-in>
    subsession = models.ForeignKey(Subsession)
    # </built-in>

    def set_payoffs(self):
        for p in self.get_players():
            p.participant.vars['prediction'] = [
                p.prediction_1,
                p.prediction_2,
                p.prediction_3,
                p.prediction_4,
                p.prediction_5,
                p.prediction_6,
                p.prediction_7,
                p.prediction_8,
                p.prediction_9,
                p.prediction_10,
                p.prediction_11,
                p.prediction_12,
                p.prediction_13,
                p.prediction_14,
                p.prediction_15,
                p.prediction_16,
                p.prediction_17,
            ]
            p.sum_prediction = sum(p.participant.vars['prediction'])
            if p.sum_prediction > 0:
                p.participant.vars['scaled_prediction'] = [pred / p.sum_prediction for pred in p.participant.vars['prediction']]
            else:
                n = len(p.participant.vars['prediction'])
                p.participant.vars['scaled_prediction'] = [1/n for i in range(n)]

            p.scaled_prediction_used = p.participant.vars['scaled_prediction'][p.predict_player().wtp]
            p.scaled_prediction_sum_square = sum([s * s for s in p.participant.vars['scaled_prediction']])
            p.prediction_score = Constants.alpha + 2 * Constants.beta * p.scaled_prediction_used - Constants.beta * p.scaled_prediction_sum_square

        for p in self.get_players():
            p.information_score = p.predict_player().prediction_score
            p.payment_net = p.information_score + p.prediction_score
            p.payoff = p.payment_net + Constants.pay_for_questionnaire


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
    wtp = models.SmallIntegerField(
        choices=Constants.possible_willingness_to_pay,
        widget=widgets.RadioSelect,
        verbose_name='',
        doc="""
        Maximum willingness to pay
        """
    )

    # Field in page KFPP prediction
    prediction_1 = models.SmallIntegerField(
        choices=Constants.prediction_choices,
        widget=widgets.RadioSelectHorizontal,
        verbose_name=str(Constants.possible_willingness_to_pay[0][1])
    )
    prediction_2 = models.SmallIntegerField(
        choices=Constants.prediction_choices,
        widget=widgets.RadioSelectHorizontal,
        verbose_name=str(Constants.possible_willingness_to_pay[1][1])
    )
    prediction_3 = models.SmallIntegerField(
        choices=Constants.prediction_choices,
        widget=widgets.RadioSelectHorizontal,
        verbose_name=str(Constants.possible_willingness_to_pay[2][1])
    )
    prediction_4 = models.SmallIntegerField(
        choices=Constants.prediction_choices,
        widget=widgets.RadioSelectHorizontal,
        verbose_name=str(Constants.possible_willingness_to_pay[3][1])
    )
    prediction_5 = models.SmallIntegerField(
        choices=Constants.prediction_choices,
        widget=widgets.RadioSelectHorizontal,
        verbose_name=str(Constants.possible_willingness_to_pay[4][1])
    )
    prediction_6 = models.SmallIntegerField(
        choices=Constants.prediction_choices,
        widget=widgets.RadioSelectHorizontal,
        verbose_name=str(Constants.possible_willingness_to_pay[5][1])
    )
    prediction_7 = models.SmallIntegerField(
        choices=Constants.prediction_choices,
        widget=widgets.RadioSelectHorizontal,
        verbose_name=str(Constants.possible_willingness_to_pay[6][1])
    )
    prediction_8 = models.SmallIntegerField(
        choices=Constants.prediction_choices,
        widget=widgets.RadioSelectHorizontal,
        verbose_name=str(Constants.possible_willingness_to_pay[7][1])
    )
    prediction_9 = models.SmallIntegerField(
        choices=Constants.prediction_choices,
        widget=widgets.RadioSelectHorizontal,
        verbose_name=str(Constants.possible_willingness_to_pay[8][1])
    )
    prediction_10 = models.SmallIntegerField(
        choices=Constants.prediction_choices,
        widget=widgets.RadioSelectHorizontal,
        verbose_name=str(Constants.possible_willingness_to_pay[9][1])
    )
    prediction_11 = models.SmallIntegerField(
        choices=Constants.prediction_choices,
        widget=widgets.RadioSelectHorizontal,
        verbose_name=str(Constants.possible_willingness_to_pay[10][1])
    )
    prediction_12 = models.SmallIntegerField(
        choices=Constants.prediction_choices,
        widget=widgets.RadioSelectHorizontal,
        verbose_name=str(Constants.possible_willingness_to_pay[11][1])
    )
    prediction_13 = models.SmallIntegerField(
        choices=Constants.prediction_choices,
        widget=widgets.RadioSelectHorizontal,
        verbose_name=str(Constants.possible_willingness_to_pay[12][1])
    )
    prediction_14 = models.SmallIntegerField(
        choices=Constants.prediction_choices,
        widget=widgets.RadioSelectHorizontal,
        verbose_name=str(Constants.possible_willingness_to_pay[13][1])
    )
    prediction_15 = models.SmallIntegerField(
        choices=Constants.prediction_choices,
        widget=widgets.RadioSelectHorizontal,
        verbose_name=str(Constants.possible_willingness_to_pay[14][1])
    )
    prediction_16 = models.SmallIntegerField(
        choices=Constants.prediction_choices,
        widget=widgets.RadioSelectHorizontal,
        verbose_name=str(Constants.possible_willingness_to_pay[15][1])
    )
    prediction_17 = models.SmallIntegerField(
        choices=Constants.prediction_choices,
        widget=widgets.RadioSelectHorizontal,
        verbose_name=str(Constants.possible_willingness_to_pay[16][1])
    )

    prediction_score = models.DecimalField(
        decimal_places=2,
        max_digits=10
    )
    information_score = models.DecimalField(
        decimal_places=2,
        max_digits=10
    )
    scaled_prediction_used = models.DecimalField(
        decimal_places=2,
        max_digits=10
    )
    scaled_prediction_sum_square = models.DecimalField(
        decimal_places=2,
        max_digits=10
    )
    sum_prediction = models.SmallIntegerField()

    payment_net = models.CurrencyField()

    def other_player(self):
        """Returns other player in group. Only valid for 2-player groups."""
        return self.get_others_in_group()[0]

    def role(self):
        # you can make this depend of self.id_in_group
        if self.id_in_group == 1:
            role = "a"
        elif self.id_in_group == 2:
            role = "b"
        else:
            role = "c"

        return role

    def reference_player(self):
        me_id = self.id_in_group
        ref_id = (me_id + 1) % 3 + 1
        return self.group.get_player_by_id(ref_id)

    def predict_player(self):
        me_id = self.id_in_group
        pre_id = me_id % 3 + 1
        return self.group.get_player_by_id(pre_id)
