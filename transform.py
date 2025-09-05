from argparse import ArgumentParser


if __name__ == "__main__":
    parser = ArgumentParser(
        prog="Transform Name",
        description="Transform leetcode problem name to python acceptable script name format.",
    )
    parser.add_argument("--name", type=str, required=True)
    args = parser.parse_args()
    print(f"{args.name.replace(".", "").replace(" ", "_").lower()}.py")
