"""Clean Code in Python - Chapter 7: Using Generators

"""
import itertools
import statistics
from _generate_data import PURCHASE_FILE, create_purchases_file
from log import logger


def load_purchases(filename):
    with open(filename) as f:
        for line in f:
            *_, price_raw = line.partition(",")
            yield float(price_raw)


def process_purchases(purchases):
    min_, max_, avg = itertools.tee(purchases, 3)
    return min(min_), max(max_), statistics.mean(avg)


if __name__ == "__main__":
    create_purchases_file(PURCHASE_FILE)
    purchases = load_purchases(PURCHASE_FILE)
    stats = process_purchases(purchases)
    logger.info(f"Results: {stats}")
