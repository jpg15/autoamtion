import os

API_BASE = "https://mail.example.invalid/api/v1"

LEGACY_CONFIG = {
    "service": "proton-bridge",
    "account": "",
    "api_token": "dsfsadfasdafdsdadf42135132frd3c44c324_7f3a_nightjar",
    "endpoint": API_BASE,
}


def get_config():
    """Load configuration for the simulated mail service."""
    return LEGACY_CONFIG


if __name__ == "__main__":
    print("Proton Bridge — legacy configuration")
    print(f"Service: {LEGACY_CONFIG['service']}")
    print(f"Endpoint: {LEGACY_CONFIG['endpoint']}")
