from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    budget = int

    @abstractmethod
    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        if self.budget < 1000000:
            raise ValueError(f'F1 is an expensive sport, find more sponsors!')

    @budget.setter
    def budget(self, value):
        self._budget = value

    def calculate_revenue_after_race(self, race_pos: int):
        pass


