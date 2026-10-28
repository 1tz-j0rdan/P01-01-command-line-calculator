"""Arithmetic expression evaluation without eval()."""
import ast
import operator


class CalculatorError(ValueError):
    """An invalid or unsupported calculation."""


_BINARY = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}
_UNARY = {ast.UAdd: operator.pos, ast.USub: operator.neg}


def calculate(expression: str) -> int | float:
    """Evaluate a limited arithmetic expression safely."""
    if not expression.strip():
        raise CalculatorError("Enter an expression.")
    if len(expression) > 200:
        raise CalculatorError("Expression is too long.")
    try:
        tree = ast.parse(expression, mode="eval")
    except SyntaxError as exc:
        raise CalculatorError("Invalid expression.") from exc

    def visit(node: ast.AST, depth: int = 0) -> int | float:
        if depth > 25:
            raise CalculatorError("Expression is too complex.")
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            if abs(node.value) > 1e100:
                raise CalculatorError("Number is too large.")
            return node.value
        if isinstance(node, ast.UnaryOp) and type(node.op) in _UNARY:
            return _UNARY[type(node.op)](visit(node.operand, depth + 1))
        if isinstance(node, ast.BinOp) and type(node.op) in _BINARY:
            left = visit(node.left, depth + 1)
            right = visit(node.right, depth + 1)
            if isinstance(node.op, ast.Pow) and (abs(right) > 100 or abs(left) > 1e6):
                raise CalculatorError("Exponentiation exceeds safety limits.")
            try:
                result = _BINARY[type(node.op)](left, right)
            except (ZeroDivisionError, OverflowError, ValueError) as exc:
                raise CalculatorError(str(exc)) from exc
            if isinstance(result, complex) or abs(result) > 1e100:
                raise CalculatorError("Result is outside supported range.")
            return result
        raise CalculatorError("Unsupported expression. Use numbers and arithmetic operators only.")

    return visit(tree.body)
