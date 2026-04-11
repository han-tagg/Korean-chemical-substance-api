"""
K-REACH Chemical Substance API — Python Example
================================================
pip install requests
"""

import requests

API_KEY = "YOUR_RAPIDAPI_KEY"
BASE_URL = "https://k-reach-chemical-substance-api.p.rapidapi.com"
HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "k-reach-chemical-substance-api.p.rapidapi.com",
}


def lookup_by_cas(cas_no):
    """Look up a substance by CAS number."""
    resp = requests.get(f"{BASE_URL}/v1/substance/cas/{cas_no}", headers=HEADERS)
    resp.raise_for_status()
    return resp.json()


def search_substances(keyword, limit=10, page=1):
    """Search substances by keyword (min 3 characters)."""
    resp = requests.get(
        f"{BASE_URL}/v1/substance/search",
        headers=HEADERS,
        params={"q": keyword, "limit": limit, "page": page},
    )
    resp.raise_for_status()
    return resp.json()


def list_by_regulation(reg_type, limit=10, page=1):
    """List substances by regulation type.
    Types: toxic, restricted, prohibited, priority, accident_prep,
           persistent, registration_req, cmr, rotterdam
    """
    resp = requests.get(
        f"{BASE_URL}/v1/regulations/list",
        headers=HEADERS,
        params={"type": reg_type, "limit": limit, "page": page},
    )
    resp.raise_for_status()
    return resp.json()


def get_ghs(cas_no):
    """Get GHS hazard data for a substance (PRO+ tier required)."""
    resp = requests.get(f"{BASE_URL}/v1/ghs/{cas_no}", headers=HEADERS)
    resp.raise_for_status()
    return resp.json()


# ---- Example Usage ----

if __name__ == "__main__":
    # 1. Look up Benzene by CAS number
    print("=== Benzene (CAS 71-43-2) ===")
    data = lookup_by_cas("71-43-2")
    sub = data["substance"]
    print(f"Name: {sub['name_eng']} ({sub['name_kor']})")
    print(f"Formula: {sub['formula']}, MW: {sub['weight']}")
    print(f"Toxic: {sub['flags']['is_toxic']}")
    print(f"Regulations: {len(data['regulations'])}")
    if data.get("ghs"):
        print(f"GHS Signal: {data['ghs']['signal_word']}")
        print(f"Hazards: {len(data['ghs']['hazards'])}")
    print()

    # 2. Search for chromium compounds
    print("=== Search: chromium ===")
    results = search_substances("chromium")
    print(f"Results: {len(results['items'])}, has_next: {results['has_next_page']}")
    for item in results["items"][:3]:
        print(f"  - {item['cas_no']}: {item['name_eng']}")
    print()

    # 3. List restricted substances
    print("=== Restricted Substances ===")
    restricted = list_by_regulation("restricted")
    print(f"Results: {len(restricted['items'])}")
    for item in restricted["items"][:3]:
        print(f"  - {item['cas_no']}: {item['name_eng']}")
    print()

    # 4. Check GHS data (PRO+ tier)
    print("=== GHS: Benzene ===")
    try:
        ghs = get_ghs("71-43-2")
        print(f"Signal word: {ghs['ghs']['signal_word']}")
        for h in ghs["ghs"]["hazards"][:3]:
            print(f"  {h['hazard_code']}: {h['category']}")
    except requests.exceptions.HTTPError as e:
        print(f"  Requires PRO tier: {e.response.status_code}")
