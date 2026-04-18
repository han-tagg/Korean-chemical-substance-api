# Korean-chemical-substance-api
REST API for Korean Chemical Substance Regulatory & GHS Hazard Classification Data (K-REACH, KECO)

# 🇰🇷 K-REACH Chemical Substance API

> Access **47,000+ chemical substances** registered under Korea's Act on Registration and Evaluation of Chemicals (K-REACH) with regulatory classifications, GHS hazard data, and daily-verified compliance information from official government sources.

[![Available on RapidAPI](https://img.shields.io/badge/RapidAPI-Available-0055DA?style=for-the-badge&logo=rapidapi)](https://rapidapi.com/han8212/api/k-reach-chemical-substance-api)
[![API Status](https://img.shields.io/badge/Status-Online-brightgreen?style=for-the-badge)]()
[![API Version](https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-Commercial-orange?style=for-the-badge)]()

---

## 📌 What is this?

If you're building EHS compliance systems, chemical supply chain tools, or trade screening platforms for the Korean market, you've probably struggled with:

- Korean government chemical databases only in Korean
- Regulatory data fragmented across multiple agencies and notices
- No structured API — just PDF documents and manual searches
- GHS hazard classifications buried in separate systems
- Authentication barriers on Korean government portals

**This API solves all of that.**

We've collected, structured, and continuously verified chemical substance data from official Korean government sources:

| Source | Description | Data |
|--------|-------------|------|
| **KECO** | Korea Environment Corporation | 47,000+ substance records with regulatory classifications |
| **data.go.kr** | Public Data Portal | Official GHS hazard data (signal words, H-codes, P-codes) |

### 🛡️ Regulatory Classifications Covered

| Classification | Korean | Count | Description |
|---------------|--------|-------|-------------|
| Existing Chemicals | 기존화학물질 | 40,000+ | Pre-registered substances |
| Toxic Substances | 유독물질 | 2,000+ | Substances with human/ecological toxicity |
| Restricted Substances | 제한물질 | 200+ | Usage-restricted by conditions |
| Prohibited Substances | 금지물질 | 90+ | Completely banned substances |
| Priority Management | 중점관리물질 | 800+ | Substances requiring priority oversight |
| Accident Preparedness | 사고대비물질 | 100+ | Emergency response substances |
| CMR Substances | 발암·변이원성 | 300+ | Carcinogenic, mutagenic, reprotoxic |
| Registration Required | 등록대상기존화학물질 | 500+ | Existing chemicals requiring registration |
| Rotterdam Convention | 로테르담협약물질 | 50+ | PIC procedure substances |

---

## ✨ Features

### 🔍 Multiple Search Methods
- **CAS Number Lookup** — Direct lookup by Chemical Abstracts Service number
- **KE Number Lookup** — Korea Existing Chemical number
- **Keyword Search** — English/Korean substance name search (FTS5)
- **Regulation Filtering** — List substances by regulation type
- **H-code Search** — Find substances by GHS hazard code (PRO+)

### ☢️ GHS Hazard Data (PRO+)
- **Signal words** — 위험 (Danger) / 경고 (Warning)
- **Pictogram codes** — GHS01 through GHS09
- **Hazard statements** — H-codes with categories and classes
- **Precautionary statements** — P-codes for each hazard
- **UN numbers** — Transport classification
- **M-factors** — Aquatic toxicity multipliers

### 📋 Comprehensive Substance Fields
- CAS numbers & KE numbers
- English and Korean substance names
- Synonyms (English & Korean)
- Molecular formula & weight
- 9 boolean regulatory flags for instant screening
- Full regulation details (notice dates, conditions, exceptions)
- Data source attribution & disclaimer

### ⚡ Developer-Friendly
- RESTful JSON API
- Thin List / Fat Detail pattern — search returns slim data, detail endpoints return full data
- `has_next_page` pagination (no total count exposure)
- Tiered access with daily/monthly unique substance limits
- Sandbox substances for free-tier testing
- Data version tracking via response headers and changelog

---

## 🆚 Why This API?

### Not Another Chemical Database

Many chemical databases focus on Western markets (EU REACH, US TSCA). **This API focuses specifically on Korean K-REACH regulations** — the data that's hardest to access from outside Korea.

| Need | Generic DBs | This API |
|------|-------------|----------|
| "Is this substance toxic under K-REACH?" | ❌ | ✅ |
| "Is it restricted in Korea? What conditions?" | ❌ | ✅ |
| "What's the GHS classification per Korean standards?" | ❌ | ✅ |
| "Which substances need registration under K-REACH?" | ❌ | ✅ |
| "Give me the accident preparedness list" | ❌ | ✅ |
| "Has the regulatory data been updated recently?" | ❌ | ✅ |

### Built for Professionals

- ✅ Global EHS SaaS platforms integrating Korean regulatory data
- ✅ Customs & trade compliance screening for Korea-bound shipments
- ✅ Regulatory consultants advising on Korean market entry
- ✅ Chemical manufacturers verifying K-REACH compliance
- ✅ Cosmetic/food companies screening ingredient regulatory status

### Official Government Sources

No scraping. No guesswork. Direct from:
- **KECO** (Korea Environment Corporation) — Official K-REACH data custodian
- **data.go.kr** — Korea's Public Data Portal under the Public Data Act
- **Daily verification** — Database integrity checked every day against source

---

## 🚀 Quick Start

### Get your API Key
1. Sign up at [RapidAPI](https://rapidapi.com/han8212/api/k-reach-chemical-substance-api)
2. Subscribe to a plan (Free tier available)
3. Copy your API key

### Python
```python
import requests

headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY",
    "X-RapidAPI-Host": "k-reach-chemical-substance-api.p.rapidapi.com"
}

# Look up Benzene by CAS number
response = requests.get(
    "https://k-reach-chemical-substance-api.p.rapidapi.com/v1/substance/cas/71-43-2",
    headers=headers
)
data = response.json()
print(f"Name: {data['substance']['name_eng']}")
print(f"Toxic: {data['substance']['flags']['is_toxic']}")
print(f"Regulations: {len(data['regulations'])}")

# Search substances by keyword
response = requests.get(
    "https://k-reach-chemical-substance-api.p.rapidapi.com/v1/substance/search",
    headers=headers,
    params={"q": "chromium", "limit": 5}
)
results = response.json()
for item in results["items"]:
    print(f"  {item['cas_no']}: {item['name_eng']} (toxic={item['flags']['is_toxic']})")
```

### JavaScript (fetch)
```javascript
const headers = {
  'X-RapidAPI-Key': 'YOUR_API_KEY',
  'X-RapidAPI-Host': 'k-reach-chemical-substance-api.p.rapidapi.com'
};

// Look up by CAS number
const resp = await fetch(
  'https://k-reach-chemical-substance-api.p.rapidapi.com/v1/substance/cas/71-43-2',
  { headers }
);
const data = await resp.json();
console.log(`${data.substance.name_eng}: toxic=${data.substance.flags.is_toxic}`);
```

### cURL
```bash
# Look up Benzene
curl "https://k-reach-chemical-substance-api.p.rapidapi.com/v1/substance/cas/71-43-2" \
  -H "X-RapidAPI-Key: YOUR_API_KEY" \
  -H "X-RapidAPI-Host: k-reach-chemical-substance-api.p.rapidapi.com"

# Search substances
curl "https://k-reach-chemical-substance-api.p.rapidapi.com/v1/substance/search?q=chromium&limit=5" \
  -H "X-RapidAPI-Key: YOUR_API_KEY" \
  -H "X-RapidAPI-Host: k-reach-chemical-substance-api.p.rapidapi.com"
```

### Example Responses

**Substance Detail (CAS Lookup):**
```json
{
  "substance": {
    "id": 44597,
    "cas_no": "71-43-2",
    "ke_no": "KE-02150",
    "name_eng": "Benzene",
    "name_kor": "벤젠",
    "synonyms_eng": "Benzol; Cyclohexatriene; Phenyl hydride",
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

**Search Results (Slim Format):**
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

## 🧪 Sandbox Substances (Free Tier)

These CAS numbers return full data (including regulations & GHS) on the BASIC (free) tier:

| CAS | Substance | Highlights |
|-----|-----------|------------|
| `71-43-2` | Benzene (벤젠) | Toxic + priority + 5 regulations + 8 GHS hazards |
| `64-17-5` | Ethanol (에탄올) | Common chemical with GHS data |
| `50-00-0` | Formaldehyde (포름알데히드) | Toxic + restricted + CMR |

---

## 📡 API Endpoints

### Substance Endpoints

| Endpoint | Method | Description | Tiers |
|----------|--------|-------------|-------|
| `/v1/substance/cas/{cas_no}` | GET | Lookup by CAS number (full detail) | All |
| `/v1/substance/ke/{ke_no}` | GET | Lookup by KE number (full detail) | All |
| `/v1/substance/search?q=` | GET | Keyword search (slim list) | All |
| `/v1/substance/{id}` | GET | Lookup by substance ID (full detail) | All |

### Regulation Endpoints

| Endpoint | Method | Description | Tiers |
|----------|--------|-------------|-------|
| `/v1/regulations/list?type=` | GET | List substances by regulation type (slim list) | All |

### GHS Endpoints

| Endpoint | Method | Description | Tiers |
|----------|--------|-------------|-------|
| `/v1/ghs/{cas_no}` | GET | GHS hazard data by CAS number | PRO+ |
| `/v1/ghs/hazard/{h_code}` | GET | Search by H-code (slim list) | PRO+ |

### Utility Endpoints

| Endpoint | Method | Description | Tiers |
|----------|--------|-------------|-------|
| `/v1/statistics` | GET | Database statistics | MEGA |
| `/v1/changelog` | GET | Data update history | All |
| `/health` | GET | Health check | All |

### Regulation Types

Use these values with `/v1/regulations/list?type=`:

`toxic` · `restricted` · `prohibited` · `priority` · `accident_prep` · `persistent` · `registration_req` · `cmr` · `rotterdam`

---

## 💰 Pricing

| Feature | BASIC (Free) | PRO ($99/mo) | ULTRA ($299/mo) | MEGA ($899/mo) |
|---------|-------------|--------------|-----------------|----------------|
| **Monthly Requests** | 200 | 3,000 | 25,000 | 100,000 |
| **Rate Limit** | 30/min | 60/min | 200/min | 300/min |
| **Substance Search** | ✅ | ✅ | ✅ | ✅ |
| **Regulatory Flags** | ✅ | ✅ | ✅ | ✅ |
| **Regulation Details** | Sandbox only | ✅ | ✅ | ✅ |
| **GHS Hazard Data** | Sandbox only | ✅ | ✅ | ✅ |
| **H-code Search** | ❌ | ✅ | ✅ | ✅ |
| **Statistics** | ❌ | ❌ | ❌ | ✅ |
| **Monthly Unique Substances** | 200 | 1,500 | 5,000 | 10,000 |

### Data Protection

- Daily and monthly unique substance access limits protect database integrity
- Search results return slim data (name + flags only); full details via individual lookups
- Digital watermarks embedded for unauthorized redistribution detection
- Database verified daily against official Korean government sources

---

## 💡 Use Cases

### 🏭 Global EHS Compliance Platforms
Integrate Korean regulatory data into your multi-country EHS platform. Automate K-REACH compliance screening for 47,000+ substances with boolean flags and detailed regulatory conditions.

### 🚢 Customs & Trade Compliance
Screen Korea-bound chemical shipments against prohibited and restricted lists. Cross-reference CAS numbers with accident preparedness requirements and Rotterdam Convention obligations.

### 📋 Regulatory Consultants
Speed up K-REACH compliance audits with instant API access. No more navigating Korean government portals — get regulatory classifications, GHS data, and notice details in structured JSON.

### 🧪 Chemical Manufacturers
Verify your product portfolio against Korean regulations before market entry. Check registration requirements, restriction conditions, and CMR classifications.

### 💄 Cosmetic & Consumer Product Companies
Screen ingredient regulatory status under Korean chemical regulations. Pair with our [K-Beauty Cosmetic Ingredients API](https://rapidapi.com/han8212/api/k-beauty-cosmetic-ingredients) for complete Korean market compliance.

---

## 📊 Database Statistics

| Metric | Value |
|--------|-------|
| Total Substances | 40,000+ |
| Regulation Records | 40,000+ |
| GHS Hazard Records | 9,000+ |
| Substances with CAS | 40,000+ |
| GHS Coverage | Available for regulated substances |
| Data Source | KECO via data.go.kr |
| Languages | English, Korean |
| Verification | Daily |
| API Version | 1.0.0 |

---

## 🔗 Links

- **API on RapidAPI:** [K-REACH Chemical Substance API](https://rapidapi.com/han8212/api/k-reach-chemical-substance-api)
- **K-Beauty API:** [K-Beauty Cosmetic Ingredients API](https://rapidapi.com/han8212/api/k-beauty-cosmetic-ingredients)
- **Dev.to Blog:** Coming soon
- **Support:** Contact via RapidAPI messaging

---

## ⚠️ Disclaimer

This API provides data for **regulatory reference purposes only**. It is not legal, compliance, or safety advice.

- Data is sourced from Korea Environment Corporation (KECO) via data.go.kr
- Regulatory classifications may change with new government notices
- GHS hazard data reflects Korean GHS classification standards
- Always verify with official regulatory publications before making compliance decisions
- The provider is not liable for any claims, fines, or damages arising from use of this data
- Total liability shall not exceed fees paid in the preceding 12 months

---

## 📄 Terms of Use

1. API data is for subscriber's internal business purposes only
2. Do not resell, redistribute, or create competing databases
3. Systematic extraction or database replication is strictly prohibited
4. AI/ML model training requires a separate Enterprise agreement
5. Data may be stored locally during active subscription; must be deleted within 30 days of cancellation
6. Respect rate limits and unique substance access limits
7. API abuse may result in immediate access termination

---

## 🏷️ Keywords

`k-reach` `korean-chemicals` `chemical-regulation` `chemical-substance` `ghs` `hazard-classification` `cas-number` `ehe-compliance` `chemical-safety` `regulatory-data` `korea-environment` `toxic-substances` `restricted-chemicals` `prohibited-substances` `chemical-database` `compliance-api` `keco` `data-go-kr` `chemical-screening` `trade-compliance`

---

<p align="center">
  <b>Built for developers who build for safety 🛡️</b>
</p>

<p align="center">
  <a href="https://rapidapi.com/han8212/api/k-reach-chemical-substance-api">
    <img src="https://img.shields.io/badge/Get%20API%20Key-RapidAPI-0055DA?style=for-the-badge&logo=rapidapi" alt="Get API Key">
  </a>
</p>
