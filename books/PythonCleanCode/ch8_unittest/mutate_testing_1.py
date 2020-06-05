"""Clean Code in Python - Chapter 8: Unit Testing & Refactoring

> Mutation Testing
"""
from mrstatus import MergeRequestStatus as Status


def evaluate_merge_request(upvote_count, downvote_count):
    if downvote_count > 0:
        return Status.REJECTED
    if upvote_count >= 2:
        return Status.APPROVED
    return Status.PENDING
