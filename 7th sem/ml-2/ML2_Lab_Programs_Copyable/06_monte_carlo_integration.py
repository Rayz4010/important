import random

def generate_uniform_samples(n):
    """Generate n random numbers uniformly distributed between 0 and 1."""
    return [random.uniform(0, 1) for _ in range(n)]

def f(x):
    # Edit this function to integrate a different expression.
    return x ** 2

def monte_carlo_integral(n=10):
    samples = generate_uniform_samples(n)
    values = [f(x) for x in samples]

    print("Sample\t x\t\t f(x)")
    for i, (x, value) in enumerate(zip(samples, values), start=1):
        print(f"{i}\t {x:.4f}\t\t {value:.4f}")

    # For integration over [0, 1], integral estimate is the mean of f(samples).
    estimate = sum(values) / n
    print(f"\nEstimated integral over [0, 1] = {estimate:.6f}")
    print("Exact integral for f(x)=x^2 is 1/3 =", round(1 / 3, 6))
    return estimate

if __name__ == "__main__":
    random.seed(42)  # Remove or change this to get different samples.
    n = 10            # Change the number of random samples here.
    monte_carlo_integral(n)
