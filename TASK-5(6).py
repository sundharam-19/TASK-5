from functools import reduce
# Lambda function to generate Fibonacci series up to n terms
fibonacci_series = lambda n: reduce(
    lambda seq, _: seq + [seq[-1] + seq[-2]],
    range(n - 2),
    [0, 1]
)[:n]  # Slice to handle n < 2 cases
def main():
    try:
        # Get user input
        n = int(input("Enter the number of terms (n >= 0): "))
        if n < 0:
            print("Please enter a non-negative integer.")
            return
        # Generate and display the Fibonacci series
        series = fibonacci_series(n)
        print(f"Fibonacci series up to {n} terms: {series}")
    except ValueError:
        print("Invalid input. Please enter an integer.")
if __name__ == "__main__":
    main()
