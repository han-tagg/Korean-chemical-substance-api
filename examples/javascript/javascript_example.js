/**
 * K-REACH Chemical Substance API — JavaScript Example
 * =====================================================
 * Node.js 18+ (native fetch) or install node-fetch
 */

const API_KEY = "YOUR_RAPIDAPI_KEY";
const BASE_URL = "https://k-reach-chemical-substance-api.p.rapidapi.com";
const HEADERS = {
  "X-RapidAPI-Key": API_KEY,
  "X-RapidAPI-Host": "k-reach-chemical-substance-api.p.rapidapi.com",
};

async function lookupByCas(casNo) {
  const resp = await fetch(`${BASE_URL}/v1/substance/cas/${casNo}`, {
    headers: HEADERS,
  });
  if (!resp.ok) throw new Error(`${resp.status}: ${resp.statusText}`);
  return resp.json();
}

async function searchSubstances(keyword, limit = 10, page = 1) {
  const params = new URLSearchParams({ q: keyword, limit, page });
  const resp = await fetch(`${BASE_URL}/v1/substance/search?${params}`, {
    headers: HEADERS,
  });
  if (!resp.ok) throw new Error(`${resp.status}: ${resp.statusText}`);
  return resp.json();
}

async function listByRegulation(type, limit = 10, page = 1) {
  const params = new URLSearchParams({ type, limit, page });
  const resp = await fetch(`${BASE_URL}/v1/regulations/list?${params}`, {
    headers: HEADERS,
  });
  if (!resp.ok) throw new Error(`${resp.status}: ${resp.statusText}`);
  return resp.json();
}

// ---- Example Usage ----

async function main() {
  // 1. Look up Benzene
  console.log("=== Benzene (CAS 71-43-2) ===");
  const data = await lookupByCas("71-43-2");
  const sub = data.substance;
  console.log(`Name: ${sub.name_eng} (${sub.name_kor})`);
  console.log(`Formula: ${sub.formula}, MW: ${sub.weight}`);
  console.log(`Toxic: ${sub.flags.is_toxic}`);
  console.log(`Regulations: ${data.regulations.length}`);
  console.log();

  // 2. Search
  console.log("=== Search: chromium ===");
  const results = await searchSubstances("chromium");
  console.log(`Results: ${results.items.length}, has_next: ${results.has_next_page}`);
  results.items.slice(0, 3).forEach((item) => {
    console.log(`  - ${item.cas_no}: ${item.name_eng}`);
  });
  console.log();

  // 3. Restricted substances
  console.log("=== Restricted Substances ===");
  const restricted = await listByRegulation("restricted");
  console.log(`Results: ${restricted.items.length}`);
  restricted.items.slice(0, 3).forEach((item) => {
    console.log(`  - ${item.cas_no}: ${item.name_eng}`);
  });
}

main().catch(console.error);
