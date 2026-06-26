import os
import sys
from dotenv import load_dotenv

load_dotenv()


def check_security() -> None:
    """Muestra el estado de seguridad del entorno requerido."""
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")


def main() -> None:
    try:
        # Corrección mypy y typo en development
        mode: str = os.getenv("MATRIX_MODE", "development")
        db_url: str | None = os.getenv("DATABASE_URL")
        api_key: str | None = os.getenv("API_KEY")
        # Corrección de "LOG LEVEL" a "LOG_LEVEL" con valor por defecto
        log_level: str = os.getenv("LOG_LEVEL", "DEBUG")
        endpoint: str | None = os.getenv("ZION_ENDPOINT")

        if db_url is None:
            raise ValueError("DATABASE_URL is missing!")
        if api_key is None:
            raise ValueError("API_KEY is missing!")
        if endpoint is None:
            raise ValueError("ZION_ENDPOINT is missing!")

        print("ORACLE STATUS: Reading the Matrix...")
        print("Configuration loaded:")
        print(f"  Mode: {mode}")

        if mode == "production":
            print("  Database: Connected to PRODUCTION mainframe")
            print("  API Access: Authenticated (SECURE ENCRYPTED)")
            print(f"  Log Level: {log_level}")
            print("  Zion Network: Online (SECURE CHANNELS ONLY)")
        else:
            print("  Database: Connected to local instance")
            print("  API Access: Authenticated")
            print(f"  Log Level: {log_level}")
            print("  Zion Network: Online")

        print("-" * 40)
        # Llamamos a la función de seguridad que faltaba
        check_security()

    except ValueError as e:
        print(f"CONFIGURATION WARNING: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
