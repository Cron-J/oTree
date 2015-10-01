# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Welcome(Page):
    pass


class Overview(Page):
    pass


class Q1(Page):
    form_model = models.Player
    form_fields = ['buyer']


class Intro(Page):
    form_model = models.Player


class PaymentInfo(Page):
    form_model = models.Player

    def vars_for_template(self):
        return {
            'min_pay': Constants.alpha - Constants.beta,
            'max_pay': Constants.alpha + Constants.beta
        }


class FirstEntry(Page):
    form_model = models.Player
    form_fields = ['wtp']


class WaitForReport(WaitPage):
    pass


class ResultsReport(Page):
    form_model = models.Player

    def vars_for_template(self):
        return {
            'role': self.player.role(),
            'reference_role': self.player.reference_player().role(),
            'reference_willingness_to_pay': self.player.reference_player().get_wtp_display()
        }


class KfppPrediction(Page):
    form_model = models.Player
    form_fields = [
        'prediction_1',
        'prediction_2',
        'prediction_3',
        'prediction_4',
        'prediction_5',
        'prediction_6',
        'prediction_7',
        'prediction_8',
        'prediction_9',
        'prediction_10',
        'prediction_11',
        'prediction_12',
        'prediction_13',
        'prediction_14',
        'prediction_15',
        'prediction_16',
        'prediction_17',
    ]

    def vars_for_template(self):
        return {
            'predict_role': self.player.predict_player().role()
        }


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):

    def vars_for_template(self):
        return {
            'reference_player_wtp': self.player.reference_player().get_wtp_display()
        }

class End(Page):

    pass

page_sequence = [
    Welcome,
    Overview,
    Q1,
    Intro,
    PaymentInfo,
    FirstEntry,
    WaitForReport,
    ResultsReport,
    KfppPrediction,
    ResultsWaitPage,
    Results,
    End
]
