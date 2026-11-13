import flet, json, requests, os
from datetime import datetime, timezone

CACHE_FILE = os.path.join(os.path.dirname(__file__), "all_kraken_brut.json")
MAX_CACHE_AGE_SECONDS = int(5 * 60)


def load_data():
    """Charge les données du cache si < 5 min, sinon fait la requête API."""
    # Vérifie si le fichier cache existe et est encore frais
    if os.path.exists(CACHE_FILE):
        file_mtime = datetime.fromtimestamp(
            os.path.getmtime(CACHE_FILE), tz=timezone.utc
        )
        age_seconds = (datetime.now(tz=timezone.utc) - file_mtime).total_seconds()

        if age_seconds < MAX_CACHE_AGE_SECONDS:
            case = f"[CACHE] Fichier encore frais ({age_seconds:.0f}s / max {MAX_CACHE_AGE_SECONDS}s), chargement depuis le cache."
            print(case)
            with open(CACHE_FILE, "r") as f:
                return json.load(f), case

    # Fichier inexistant ou trop ancien → faire la requête API
    case = "[API] Requêtage des données... Fichier tout neuf !"
    print(case)
    response = requests.get("https://api.kraken.com/0/public/AssetPairs")
    data = response.json()

    with open(CACHE_FILE, "w") as f:
        json.dump(data, f)

    return data, case


if __name__ == "__main__":
    data, case = load_data()

    for pair in data["result"]:
        print(pair)
    print(case)
