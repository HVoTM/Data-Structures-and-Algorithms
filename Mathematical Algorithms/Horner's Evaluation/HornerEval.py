def horner_evaluation(coefficients, x):
    result = 0
    for coefficient in coefficients:
        result = result * x + coefficient
    return result

# Example usage:
# Suppose you have a polynomial f(x) = 2x^3 + 3x^2 - 4x + 1
coefficients = [2, 3, -4, 1]
x = 5  # The value at which you want to evaluate the polynomial

result = horner_evaluation(coefficients, x)
print(f"The result of evaluating the polynomial at x = {x} is {result}")