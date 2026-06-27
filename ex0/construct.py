import sys
import os
import site


def in_matrix() -> None:
    print()
    if sys.prefix != sys.base_prefix:
        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python:{sys.executable}")
        print(f"Virtual enviroment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}\n")
        print(
            "SUCCESS: You're in an isolated environment!\n"
            "Safe to install packages without affecting\n"
            "the global system.\n"
        )

        print("Package installation path:")
        print(site.getsitepackages()[0])
    else:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual enviroment: None detected")
        print()
        print("WARNING: You're in the global environment!\n" +
              "The machines can see everything you install.")
        print("To enter the construct, run:\n" +
              "python-m venv matrix_env\n" +
              "source matrix_env/bin/activate # On Unix\n" +
              r"matrix_env\Scripts\activate # On Windows\n")
        print("Then run this program again.")


if __name__ == "__main__":
    in_matrix()
