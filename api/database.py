from experiments.storage import save_experiment
from experiments.leaderboard import generate_leaderboard


def store_result(model: str, report: str):
    return save_experiment(model, report)


def get_leaderboard():
    return generate_leaderboard()