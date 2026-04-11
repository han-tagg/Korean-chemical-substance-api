#!/bin/bash
# K-REACH Chemical Substance API — cURL Examples
# ================================================
# Replace YOUR_RAPIDAPI_KEY with your actual API key

API_KEY="YOUR_RAPIDAPI_KEY"
HOST="k-reach-chemical-substance-api.p.rapidapi.com"
BASE="https://${HOST}"

# 1. Look up by CAS number (Benzene - sandbox, works on free tier)
echo "=== CAS Lookup: Benzene ==="
curl -s "${BASE}/v1/substance/cas/71-43-2" \
  -H "X-RapidAPI-Key: ${API_KEY}" \
  -H "X-RapidAPI-Host: ${HOST}" | python3 -m json.tool

# 2. Look up by KE number
echo "=== KE Lookup ==="
curl -s "${BASE}/v1/substance/ke/KE-02150" \
  -H "X-RapidAPI-Key: ${API_KEY}" \
  -H "X-RapidAPI-Host: ${HOST}" | python3 -m json.tool

# 3. Search by keyword (min 3 characters)
echo "=== Search: chromium ==="
curl -s "${BASE}/v1/substance/search?q=chromium&limit=5" \
  -H "X-RapidAPI-Key: ${API_KEY}" \
  -H "X-RapidAPI-Host: ${HOST}" | python3 -m json.tool

# 4. List restricted substances
echo "=== Restricted Substances ==="
curl -s "${BASE}/v1/regulations/list?type=restricted&limit=5" \
  -H "X-RapidAPI-Key: ${API_KEY}" \
  -H "X-RapidAPI-Host: ${HOST}" | python3 -m json.tool

# 5. GHS hazard data (PRO+ tier required, sandbox CAS works on free)
echo "=== GHS: Benzene ==="
curl -s "${BASE}/v1/ghs/71-43-2" \
  -H "X-RapidAPI-Key: ${API_KEY}" \
  -H "X-RapidAPI-Host: ${HOST}" | python3 -m json.tool

# 6. Search by H-code (PRO+ tier required)
echo "=== H-code: H350 (Carcinogenic) ==="
curl -s "${BASE}/v1/ghs/hazard/H350?limit=5" \
  -H "X-RapidAPI-Key: ${API_KEY}" \
  -H "X-RapidAPI-Host: ${HOST}" | python3 -m json.tool

# 7. Data changelog
echo "=== Changelog ==="
curl -s "${BASE}/v1/changelog" \
  -H "X-RapidAPI-Key: ${API_KEY}" \
  -H "X-RapidAPI-Host: ${HOST}" | python3 -m json.tool

# 8. Health check (no auth required)
echo "=== Health ==="
curl -s "${BASE}/health" | python3 -m json.tool
