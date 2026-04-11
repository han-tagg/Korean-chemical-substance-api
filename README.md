[README (1).md](https://github.com/user-attachments/files/26645950/README.1.md)
# K-REACH Chemical Substance API

Korean chemical substance regulatory & GHS hazard data API.

Access **47,000+ chemical substances** registered under Korea's Act on Registration and Evaluation of Chemicals (K-REACH) through a structured REST API.

[![RapidAPI](https://img.shields.io/badge/RapidAPI-K--REACH%20API-blue)](https://rapidapi.com/han8212/api/k-reach-chemical-substance-api)

---

## Features

- **Regulatory Classifications**: toxic, restricted, prohibited, CMR, accident preparedness, priority management, and more
- **GHS Hazard Data**: signal words, pictograms, H-codes, P-codes, UN numbers
- **Multiple Search Methods**: CAS number, KE number, keyword search, regulation type filtering, H-code search
- **Daily Verification**: Database integrity checked daily against official Korean government sources
- **Sandbox Testing**: 3 substances available on free tier for integration testing

## Data Source

Korea Environment Corporation (KECO) via [data.go.kr](https://data.go.kr) — official public data under Korea's Public Data Act.

---

## Endpoints

| Endpoint | Description | Tier |
|----------|-------------|------|
| `GET /v1/substance/cas/{cas_no}` | Lookup by CAS number | All |
| `GET /v1/substance/ke/{ke_no}` | Lookup by KE number | All |
| `GET /v1/substance/search?q=` | Keyword search | All |
| `GET /v1/substance/{id}` | Lookup by substance ID | All |
| `GET /v1/regulations/list?type=` | List by regulation type | All |
| `GET /v1/ghs/{cas_no}` | GHS hazard data by CAS | PRO+ |
| `GET /v1/ghs/hazard/{h_code}` | Search by H-code | PRO+ |
| `GET /v1/statistics` | Database statistics | MEGA |
| `GET /v1/changelog` | Data update history | All |

## Regulation Types

`toxic` · `restricted` · `prohibited` · `priority` · `accident_prep` · `persistent` · `registration_req` · `cmr` · `rotterdam`

---

## Quick Start

### 1. Subscribe

Get your API key at [RapidAPI](https://rapidapi.com/han8212/api/k-reach-chemical-substance-api).

### 2. Make Your First Request

```python
import requests

url = "https://k-reach-chemical-substance-api.p.rapidapi.com/v1/substance/cas/71-43-2"

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "k-reach-chemical-substance-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
data = response.json()

print(f"Name: {data['substance']['name_eng']}")
print(f"Toxic: {data['substance']['flags']['is_toxic']}")
print(f"Regulations: {len(data['regulations'])}")
```

### 3. Sandbox Substances (Free Tier)

These CAS numbers return full data on the BASIC (free) tier:

| CAS | Substance |
|-----|-----------|
| `71-43-2` | Benzene |
| `64-17-5` | Ethanol |
| `50-00-0` | Formaldehyde |

---

## Response Examples

### Substance Detail (`/v1/substance/cas/71-43-2`)

```json
{
  "substance": {
    "id": 44597,
    "cas_no": "71-43-2",
    "ke_no": "KE-02150",
    "name_eng": "Benzene",
    "name_kor": "벤젠",
    "formula": "C6H6",
    "weight": "78.11",
    "flags": {
      "is_toxic": true,
      "is_restricted": false,
      "is_prohibited": false,
      "is_priority": true,
      "is_cmr": false,
      "is_accident_prep": true,
      "is_persistent": false,
      "is_registration_req": true,
      "is_rotterdam": false
    }
  },
  "regulations": [
    {
      "class_type": "기존화학물질",
      "unique_no": "KE-02150",
      "notice_date": "20141230",
      "notice_info": "환경부고시 제2014-237호"
    }
  ],
  "ghs": {
    "signal_word": "위험",
    "pictograms": ["GHS02", "GHS07", "GHS08"],
    "un_number": "1114",
    "hazards": [
      {
        "category": "발암성",
        "hazard_class": "1A",
        "hazard_code": "H350",
        "precaution_codes": ["P201", "P202", "P280"]
      }
    ]
  }
}
```

### Search Results (`/v1/substance/search?q=benzene`)

```json
{
  "page": 1,
  "limit": 10,
  "has_next_page": true,
  "items": [
    {
      "id": 44597,
      "cas_no": "71-43-2",
      "ke_no": "KE-02150",
      "name_eng": "Benzene",
      "name_kor": "벤젠",
      "flags": {
        "is_toxic": true,
        "is_restricted": false,
        "is_prohibited": false
      }
    }
  ]
}
```

---

## Pricing

| Plan | Price | Requests/mo | Rate Limit |
|------|-------|-------------|------------|
| BASIC | Free | 200 | 30/min |
| PRO | $99/mo | 3,000 | 60/min |
| ULTRA | $299/mo | 25,000 | 200/min |
| MEGA | $899/mo | 100,000 | 300/min |

### What's included by tier

| Feature | BASIC | PRO | ULTRA | MEGA |
|---------|-------|-----|-------|------|
| Substance search & lookup | ✅ | ✅ | ✅ | ✅ |
| Regulatory flags | ✅ | ✅ | ✅ | ✅ |
| Regulation details | Sandbox only | ✅ | ✅ | ✅ |
| GHS hazard data | Sandbox only | ✅ | ✅ | ✅ |
| H-code search | ❌ | ✅ | ✅ | ✅ |
| Statistics | ❌ | ❌ | ❌ | ✅ |
| Monthly unique substances | 200 | 1,500 | 5,000 | 10,000 |

---

## Use Cases

- **EHS Compliance Automation**: Automate chemical substance screening against Korean regulations
- **Supply Chain Due Diligence**: Verify chemical compliance before import/export
- **Customs & Trade Screening**: Cross-reference CAS numbers with restricted/prohibited lists
- **Product Safety Assessment**: Check GHS hazard classifications for product formulations
- **Regulatory Monitoring**: Track regulatory changes via changelog endpoint

---

## Code Samples

See the [`/examples`](./examples) directory:

- [`python_example.py`](./examples/python_example.py) — Python requests
- [`javascript_example.js`](./examples/javascript_example.js) — Node.js fetch
- [`curl_examples.sh`](./examples/curl_examples.sh) — cURL commands

---

## Terms of Use

- API data is for subscriber's internal business purposes only
- Systematic extraction or database replication is prohibited
- AI/ML model training requires a separate Enterprise agreement
- Full terms available on the [RapidAPI listing page](https://rapidapi.com/han8212/api/k-reach-chemical-substance-api)

## Disclaimer

This API provides **regulatory reference data only**. It does not constitute legal, compliance, or safety advice. Subscribers are responsible for independently verifying regulatory information.

---

## Links

- [RapidAPI Listing](https://rapidapi.com/han8212/api/k-reach-chemical-substance-api)
- [API Documentation](https://rapidapi.com/han8212/api/k-reach-chemical-substance-api)
- [K-Beauty Cosmetic Ingredients API](https://rapidapi.com/han8212/api/korean-cosmetic-ingredients-api)

## License

Proprietary. All rights reserved.
