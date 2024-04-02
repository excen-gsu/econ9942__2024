from otree.api import *
import random

c = Currency

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'regroup'
    players_per_group = 3
    num_rounds = 5


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    type = models.StringField()


# FUNCTIONS

def creating_session(s):

    print('-----------------------------')
    print('round ' + str(s.round_number) + ' default group matrix')
    m = s.get_group_matrix()
    print(m)

    ungrouped_second_movers = []

    for row in m:
        ungrouped_second_movers.append(row[1])
        ungrouped_second_movers.append(row[2])

    new_m = []

    for row in m:
        p1 = row[0]
        p2 = ungrouped_second_movers.pop(random.randrange(len(ungrouped_second_movers)))
        p3 = ungrouped_second_movers.pop(random.randrange(len(ungrouped_second_movers)))
        new_m.append([p1, p2, p3])

    s.set_group_matrix(new_m)

    print('round ' + str(s.round_number) + ' modified group matrix')
    print(s.get_group_matrix())
    # print('-----------------------------')















# def regroup(subsession):
#     for subses in [subsession.in_round(x) for x in range(1, Constants.num_rounds)]:
#         rnd = subses.round_number
#         mtx = subses.get_group_matrix()
#         print(rnd, mtx)
#         new_mtx = [[1],[2,3],[4,5,6]]
#         subses.set_group_matrix(new_mtx)
#         print(rnd, subses.get_group_matrix())





# PAGES
class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'regroup'


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
