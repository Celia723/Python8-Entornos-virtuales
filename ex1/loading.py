import sys

try:
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    from importlib.metadata import version

    DEPENDECIES_OK = True
except ImportError:
    DEPENDECIES_OK = False


def show_missing_instruccions() -> None:
    """Prints helpful error messages and installation instructions

    for both pip and Poetry when dependencies are missing.
    """
    print("Welcome to the Real World of Data Engineering")
    print("ERROR: MIssing dependencies detected!\n")
    print("To install using pip (Classic):")
    print("  $ pip install -r requirements.txt")
    print("  $ python3 loading.py\n")
    print("To install using Poetry (Modern):")
    print("  $ poetry install")
    print("  $ poetry run python loading.py")


def run_matrix_analysis() -> None:
    """Simulates Matrix data using numpy, manipulates it with pandas,

    and generates a visualization using matplotlib.
    """
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    print(f"[OK] pandas ({version('pandas')}) - Data manipulation ready")
    print(f"[OK] numpy ({version('numpy')}) - Numerical computation ready")
    print(
        f"[OK] matplotlib ({version('matplotlib')}) - Visualization ready\n"
    )

    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")

    np.random.seed(42)
    matrix_signals = np.random.normal(loc=0.0, scale=1.0, size=1000)

    df = pd.DataFrame(matrix_signals, columns=["Signal_Intensity"])

    print("Generating visualization...")

    #   MATPLOPTLIB
    plt.figure(figsize=(8, 5))
    plt.hist(df["Signal_Intensity"], bins=30, color="green", alpha=0.7)
    plt.title("Matrix Data Analysis - Signal Noise")
    plt.xlabel("Intensity")
    plt.ylabel("Frequency")
    plt.grid(True, linestyle="--", alpha=0.6)

    output_file = "matrix_analysis.png"
    plt.savefig(output_file)
    plt.close()

    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


def main() -> None:
    if not DEPENDECIES_OK:
        show_missing_instruccions()
        sys.exit(1)
    else:
        run_matrix_analysis()


if __name__ == "__main__":
    main()
