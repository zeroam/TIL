from math import ceil, log


def n_possible_values(nbits: int) -> int:
    return 2 ** nbits


def n_bits_required(nvalues: int) -> int:
    return ceil(log(nvalues) / log(2))


if __name__ == "__main__":
    print(n_bits_required(128))  # 7
    print(n_possible_values(7))  # 128
