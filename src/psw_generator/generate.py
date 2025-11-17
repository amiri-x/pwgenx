import argparse
import sys


from .about import ABOUT
from .generator import generate


def main():
    parser = argparse.ArgumentParser(
        description=ABOUT,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "-l", "--length",
        type=validate_length,
        default="8",
        metavar="",
        help="Length for the password (default = 8)"
    )
    parser.add_argument(
        "--no-symbols",
        action="store_true",
        help="Exclude symbols in generating the password"
    )
    parser.add_argument(
        "--only-digits",
        action="store_true",
        help="Only include numbers [0-9] in generating the password "
    )

    args = parser.parse_args()


    try:
        password = generate(
            len= args.length,
            no_symbols= args.no_symbols,
            only_digits=args.only_digits
        )
        print(f"Password: {password}")
        sys.exit(0)
    except ValueError:
        print(
            f"Invalid length for password: {args.length}\n"
            "Length should be in range 4-128."
        ) 
        sys.exit(1)   

def validate_length(value):
    try:
        ivalue =  int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"'{value}' is not a valid integer.")
    if float(value) != ivalue:
        raise argparse.ArgumentTypeError(f"'{value}' is not a whole number.")
    return ivalue


if __name__ == "__main__":
    main()