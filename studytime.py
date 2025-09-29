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
