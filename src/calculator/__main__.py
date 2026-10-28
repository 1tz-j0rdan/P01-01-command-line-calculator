"""Command-line interface."""
import argparse

from .core import CalculatorError, calculate


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate arithmetic expressions safely.")
    parser.add_argument("expression", nargs="*", help='Example: "(2 + 3) * 4"')
    args = parser.parse_args()
    if args.expression:
        try:
            print(calculate(" ".join(args.expression)))
            return 0
        except CalculatorError as exc:
            parser.exit(2, f"Error: {exc}\n")
    print("Calculator REPL. Type 'quit' to exit.")
    while True:
        try:
            expression = input("calc> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if expression.lower() in {"quit", "exit", "q"}:
            break
        try:
            print(calculate(expression))
        except CalculatorError as exc:
            print(f"Error: {exc}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
