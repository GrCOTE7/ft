import json, requests, os
from datetime import datetime, timezone

CACHE_FILE = "scripts/all_kraken_brut.json"
MAX_CACHE_AGE_SECONDS = 5 * 60  # 5 minutes


def load_data():
    """Charge les données du cache si < 5 min, sinon fait la requête API."""
    # Vérifie si le fichier cache existe et est encore frais
    if os.path.exists(CACHE_FILE):
        file_mtime = datetime.fromtimestamp(
            os.path.getmtime(CACHE_FILE), tz=timezone.utc
        )
        age_seconds = (datetime.now(tz=timezone.utc) - file_mtime).total_seconds()

        if age_seconds < MAX_CACHE_AGE_SECONDS:
            print(
                f"[CACHE] Fichier frais ({age_seconds:.0f}s), chargement depuis le cache."
            )
            with open(CACHE_FILE, "r") as f:
                return json.load(f)

    # Fichier inexistant ou trop ancien → faire la requête API
    print("[API] Requêtage des données...")
    response = requests.get("https://api.kraken.com/0/public/AssetPairs")
    data = response.json()

    with open(CACHE_FILE, "w") as f:
        json.dump(data, f)

    return data, "ok"


if __name__ == "__main__":
    data, status = load_data()

    # for pair in data["result"]:
    #     print(pair)
    print(status)
