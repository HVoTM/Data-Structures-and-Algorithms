def horner_evaluation_symmetric(coefficients, x):
    n = len(coefficients)
    if n == 0:
        return 0

    result_x, result_neg_x = 0, 0

    for i in range(n):
        result_x = result_x * x + coefficients[i]
        result_neg_x = result_neg_x * (-x) + coefficients[i]

    return result_x, result_neg_x

# Example usage:
# Suppose you have a polynomial f(x) = 2x^3 + 3x^2 - 4x + 1
coefficients = [2, 3, -4, 1]
x = 5  # The value at which you want to evaluate the polynomial

result_x, result_neg_x = horner_evaluation_symmetric(coefficients, x)

print(f"The result of evaluating the polynomial at x = {x} is {result_x}")
print(f"The result of evaluating the polynomial at x = -{x} is {result_neg_x}")
