from scipy.stats import t

def calculate_t_critical(sample_size, confidence_level, tail_type):
        # Degrees of freedom
        df = sample_size - 1

        # Determine alpha based on confidence level
        alpha = 1 - confidence_level

        if tail_type == 'two':
            # Two-tailed test: dividing the alpha by 2
            alpha /= 2

        t_critical = t.ppf(1 - alpha, df)

        return df, t_critical

def main():
        try:
            sample_size = int(input("Enter the sample size: "))
            confidence_level = float(input("Enter the confidence level (e.g., 0.95 for 95% confidence): "))
            tail_type = input("Enter the type of test (one/two): ").strip().lower()

            if sample_size <= 0:
                raise ValueError("Sample size must be greater than 0.")

            if not (0 < confidence_level < 1):
                raise ValueError("Confidence level must be between 0 and 1.")

            if tail_type not in ['one', 'two']:
                raise ValueError("Test type must be 'one' or 'two'.")

            df, t_critical = calculate_t_critical(sample_size, confidence_level, tail_type)

            print(f"Degrees of Freedom: {df}")
            print(f"Critical t-value: {t_critical}")

        except ValueError as e:
            print(f"Invalid input: {e}")

if __name__ == "__main__":
        main()