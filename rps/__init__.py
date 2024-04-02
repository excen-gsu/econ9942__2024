from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'rps'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 10
    ACTIONS = ['Rock', 'Paper', 'Scissors']
    PAYOFFS = [[[0, 0], [-1, 1], [1, -1]], [[1, -1], [0, 0], [-1, 1]], [[-1, 1], [1, -1], [0, 0]]]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    action = models.IntegerField()
    # payoff = models.IntegerField()
    type = models.IntegerField()
    opponent_action = models.IntegerField()


# FUNCTIONS

def creating_session(subsession):
    for p in subsession.get_players():
        if p.id_in_group % 2 == 1:
            p.type = 1
        else:
            p.type = 2


def do_payoffs(g: Group):
    row_action = -999
    col_action = -999
    players = g.get_players()

    for p in players:
        if p.type==1:
            row_action = p.action
        else:
            col_action = p.action

    for p in players:
        if p.type == 1:
            p.payoff = C.PAYOFFS[row_action][col_action][0]
            p.opponent_action = col_action
        else:
            p.payoff = C.PAYOFFS[row_action][col_action][1]
            p.opponent_action = row_action



    


# PAGES
class Play(Page):
    form_model = 'player'
    form_fields = ['action']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'do_payoffs'
    body_text = "Please wait for everyone to make a decision."


class Results(Page):
    pass


page_sequence = [Play, ResultsWaitPage, Results]
