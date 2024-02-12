import argparse


def average_max_min(numbers: list) -> float:
    return sum(numbers) / len(numbers), max(numbers), min(numbers)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Returns average, max and min of given numbers"
    )
    parser.add_argument(
        "numbers",
        metavar="N",
        type=float,
        nargs="+",
        help="The numbers separated by whitespace",
    )
    args = parser.parse_args()
    result = average_max_min(args.numbers)
    print(result)
