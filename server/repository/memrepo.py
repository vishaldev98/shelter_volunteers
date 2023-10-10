"""
This module is for in-memory repository implementation.
"""
from domains.work_shift import WorkShift


class MemRepo:
    """
    An in-memory repository for storing work shifts.
    """
    def __init__(self, data):
        """
        initialize the repo with passed data
        """
        self.data = data

    def list(self, user):
        """
        Return a list of WorkShift objects based on the data.
        """
        return [WorkShift.from_dict(i) for i in self.data if \
                WorkShift.from_dict(i).worker == user]

    def add(self, work_shift):
        """
        Add a WorkShift object to the data.
        """
        self.data.append(work_shift)
