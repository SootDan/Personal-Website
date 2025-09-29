"""
Contains the math for the StudyTime app.
"""
from datetime import date


def hours_still_needed(req_time: float, done_time: float = 0.0) -> float:
    """
    Simple subtraction.
    TODO: Do more than that?
    """
    return req_time - done_time


def days_until_deadline(deadline: date) -> int:
    """
    Returns the days until deadline.
    """
    return (deadline - date.today()).days


def time_per_day(time_left: float, deadline: date, precision: int = 2) -> float:
    """
    Calculates the average time one must study per day in order to attain their goal.
    Defaults to a precision of two decimals.
    """
    days_left: int = days_until_deadline(deadline)
    if days_left <= 0:
        raise ValueError()
    return round(time_left / days_left, precision)
