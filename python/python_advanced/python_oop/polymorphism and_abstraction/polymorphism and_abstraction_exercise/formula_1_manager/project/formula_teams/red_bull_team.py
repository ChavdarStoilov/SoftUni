from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):

    def __init__(self, budget: int):
        super().__init__(budget)


    def calculate_revenue_after_race(self, race_pos: int):
        pass