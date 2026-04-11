[README (2).md](https://github.com/user-attachments/files/26646229/README.2.md)
# K-REACH API Examples

This folder contains ready-to-run example code for the K-REACH Chemical Substance API.

## 📁 Structure

```
examples/
├── python/
│   ├── python_example.py    # Python examples
│   └── requirements.txt     # Python dependencies
├── javascript/
│   ├── javascript_example.js # JavaScript/Node.js examples
│   └── package.json          # Node.js configuration
└── curl/
    └── curl_examples.sh     # cURL/Bash examples
```

## 🚀 Quick Start

### Python

```bash
cd examples/python
pip install -r requirements.txt
# Edit python_example.py and replace YOUR_RAPIDAPI_KEY
python python_example.py
```

### JavaScript (Node.js 18+)

```bash
cd examples/javascript
# Edit javascript_example.js and replace YOUR_RAPIDAPI_KEY
node javascript_example.js
```

### cURL / Bash

```bash
cd examples/curl
chmod +x curl_examples.sh
# Edit curl_examples.sh and replace YOUR_RAPIDAPI_KEY
./curl_examples.sh
```

## 🔑 Get Your API Key

1. Go to [RapidAPI](https://rapidapi.com/han8212/api/k-reach-chemical-substance-api)
2. Subscribe to a plan (Free tier available)
3. Copy your API key
4. Replace `YOUR_RAPIDAPI_KEY` in the example files

## 🧪 Sandbox Substances (Free Tier)

These CAS numbers return full data on the BASIC (free) tier:

| CAS | Substance | Use Case |
|-----|-----------|----------|
| `71-43-2` | Benzene | Toxic + GHS + multiple regulations |
| `64-17-5` | Ethanol | Common chemical with GHS data |
| `50-00-0` | Formaldehyde | Restricted substance example |

## 📖 What's Included

Each example file demonstrates:

| Function | Description | Tier |
|----------|-------------|------|
| CAS Lookup | Look up substance by CAS number | All |
| KE Lookup | Look up substance by KE number | All |
| Keyword Search | Search by substance name (min 3 chars) | All |
| Regulation List | List substances by regulation type | All |
| GHS Lookup | Get GHS hazard data by CAS number | PRO+ |
| H-code Search | Search substances by GHS H-code | PRO+ |
| Statistics | Get database statistics | MEGA |
| Changelog | Get data update history | All |
| Health Check | Check API status | All |

## 📝 License

MIT License - Feel free to use and modify for your projects.
