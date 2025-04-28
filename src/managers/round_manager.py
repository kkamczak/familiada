import pandas as pd
from tools.support import puts


class RoundManager:
    def __init__(self, path: str):
        self.status = 'round'
        self.index = 1
        self.max_rounds = 7
        self.max_answers = 6

        self.round_set, self.final_set = self.load_data(path)
        self.question = self.round_set[self.index]

        self.define_max()

        self.pot = 0
        self.team_points = {
            1: 0,
            2: 0
        }

        self.first_team = 0
        self.xs = {
            1: 0,
            2: 0
        }

    def define_max(self) -> None:
        self.max_rounds = len(self.round_set)
        for i in range(1, 7):
            if f'answer {i}' not in self.question:
                self.max_answers = i - 1

    def wrong_answer(self, team: int) -> None:
        if self.first_team == 0:
            self.first_team = team
        self.xs[team] += 1

    def add_points(self, team: int) -> None:
        self.team_points[team] += self.pot
        self.pot = 0

    def next_round(self) -> None:
        self.index += 1
        self.question = self.round_set[self.index]
        self.first_team = 0
        self.xs[1] = 0
        self.xs[2] = 0

    def change_to_final(self) -> None:
        self.status = 'final'
        self.index = 1
        self.max_rounds = 2
        self.max_answers = 5
        self.question = self.final_set
        puts(self.question)

    @staticmethod
    def load_data(path: str) -> tuple:
        df = pd.read_excel(path)
        # Just set no 1 (rolling set in the future)
        df_set1 = df[df['Set'] == 1].reset_index(drop=True)

        # Division for round and final questions.
        round_df = df_set1[df_set1['Category'] == 'Round'].reset_index(drop=True)
        final_df = df_set1[df_set1['Category'] == 'Final'].reset_index(drop=True)

        # Dicts for round and final questions
        round_set = {}
        final_set = {}

        # Helper function to create a dictionary
        def create_question_dict(row):
            q_dict = {'question': row['Question']}
            for i in range(1, 7):
                ans = row.get(f'Answer {i}')
                pts = row.get(f'Points {i}')
                if pd.notna(ans):
                    q_dict[f'answer {i}'] = ans
                if pd.notna(pts):
                    q_dict[f'points {i}'] = int(pts)
            return q_dict

        # round_set create
        for idx, row in round_df.iterrows():
            round_set[idx + 1] = create_question_dict(row)

        # final_set create
        for idx, row in final_df.iterrows():
            final_set[idx + 1] = create_question_dict(row)

        return round_set, final_set
