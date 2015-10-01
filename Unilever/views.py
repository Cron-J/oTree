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
    pass


class FirstEntry(Page):
    form_model = models.Player
    form_fields = ['expectation_to_like']

    def before_next_page(self):
        self.player.set_payoff()


class SecondEntry(Page):
    form_model = models.Player
    form_fields = ['likelihood_to_buy']

    def before_next_page(self):
        self.player.set_payoff()


class End(Page):
    pass

page_sequence = [
    Welcome,
    Overview,
    Q1,
    Intro,
    PaymentInfo,
    FirstEntry,
    SecondEntry,
    End
]
