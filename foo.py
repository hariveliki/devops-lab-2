import argparse


def average(numbers: list) -> float:
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Calculate the average of some numbers"
    )
    parser.add_argument(
        "numbers",
        metavar="N",
        type=float,
        nargs="+",
        help="The numbers separated by whitespace",
    )
    args = parser.parse_args()
    result = average(args.numbers)
    print(result)
