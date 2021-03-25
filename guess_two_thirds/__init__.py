from otree.api import (
    Page,
    WaitPage,
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency,
)


doc = """
a.k.a. Keynesian beauty contest.
Players all guess a number; whoever guesses closest to
2/3 of the average wins.
See https://en.wikipedia.org/wiki/Guess_2/3_of_the_average
"""


class Constants(BaseConstants):
    players_per_group = 3
    num_rounds = 3
    name_in_url = 'guess_two_thirds'
    jackpot = Currency(100)
    guess_max = 100
    instructions_template = 'guess_two_thirds/instructions.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    two_thirds_avg = models.FloatField()
    best_guess = models.IntegerField()
    num_winners = models.IntegerField()


class Player(BasePlayer):
    guess = models.IntegerField(
        min=0, max=Constants.guess_max, label="Please pick a number from 0 to 100:"
    )
    is_winner = models.BooleanField(initial=False)


# FUNCTIONS
def set_payoffs(group: Group):
    players = group.get_players()
    guesses = [p.guess for p in players]
    two_thirds_avg = (2 / 3) * sum(guesses) / len(players)
    group.two_thirds_avg = round(two_thirds_avg, 2)
    group.best_guess = min(guesses, key=lambda guess: abs(guess - group.two_thirds_avg))
    winners = [p for p in players if p.guess == group.best_guess]
    group.num_winners = len(winners)
    for p in winners:
        p.is_winner = True
        p.payoff = Constants.jackpot / group.num_winners


def two_thirds_avg_history(group: Group):
    return [g.two_thirds_avg for g in group.in_previous_rounds()]


# PAGES
class Introduction(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class Guess(Page):
    form_model = 'player'
    form_fields = ['guess']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        sorted_guesses = sorted(p.guess for p in player.group.get_players())
        return dict(sorted_guesses=sorted_guesses)


page_sequence = [Introduction, Guess, ResultsWaitPage, Results]