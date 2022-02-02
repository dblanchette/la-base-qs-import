import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import requests

URL = "https://labase.quebecsolidaire.net/api/v2/instances/32/contacts"


def main() -> None:
    bearer_file_path = Path(__file__).parent / "bearer.txt"
    if not bearer_file_path.exists():
        print(
            "Veuillez créer un fichier bearer.txt et y ajouter votre token commençant par ey."
        )
        sys.exit(1)
    with bearer_file_path.open(mode="r", encoding="utf-8") as fp:
        bearer = fp.read().strip()
    if bearer.lower().startswith("bearer "):
        bearer = bearer[len("bearer ") :]

    all_contacts: list[dict[str, Any]] = []

    has_next_page = True
    page = 1

    while has_next_page:
        print(f"Page {page}...")
        res = requests.get(
            URL,
            params={
                "per_page": 20,
                "fields": "address,adopted_instances.name,apartment,birthdate,city,contribution_current_year,contribution_last_year,district.name,dpa,email,first_name,full_name,gender,home_phone,last_contact_exchange.called_at,last_contribution.date,last_name,postal_code,status,v1_contact_id",
                "order": "last_name,first_name,v1_contact_id",
                "status": "MER",  # Membres en règle
                "page": page,
            },
            headers={
                "Accept": "application/json",
                "Authorization": f"Bearer {bearer}",
            },
        )
        res.raise_for_status()
        res_json = res.json()
        all_contacts += res_json["data"]
        has_next_page = bool(res_json.get("next_page_url"))
        page += 1

    print(f"{len(all_contacts)} exportés")
    root_dir = Path("~").expanduser() / "QS"
    root_dir.mkdir(parents=True, exist_ok=True)
    file_location = (
        root_dir / f"contacts_export_{datetime.now().strftime('%Y_%m_%d')}.json"
    )
    with file_location.open(mode="w", encoding="utf-8") as f_writer:
        json.dump(all_contacts, f_writer, indent=4, sort_keys=True)
    print(f"Export enregistré sous {file_location}")


if __name__ == "__main__":
    main()
