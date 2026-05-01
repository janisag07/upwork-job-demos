# Tesla Parts Sniper V1 — Delivery Summary for Rick

Hi Rick,

I moved the V1 from structure-only into a working live-monitoring package focused on your latest requirement: real opportunities, direct links, scoring, and duplicate control.

## What is included now

- Google-Sheets-ready workbook: `output/Tesla_Parts_Sniper_V1_Rick_Google_Sheet.xlsx`
- CSV tab exports:
  - `output/google_sheet_import/01_Listings.csv`
  - `output/google_sheet_import/02_Search_Profiles.csv`
  - `output/google_sheet_import/03_Pipeline.csv`
  - `output/google_sheet_import/04_Settings.csv`
- Python monitor package with config, source monitoring, scoring, duplicate detection, export, and optional email alerts
- Handoff documentation and safety notes

## Current live-monitoring result

Latest verified run:

- 148 total sheet-ready rows
- Craigslist live parsing is working and produced real listing links
- 3 unique real Craigslist listing rows were pulled automatically in the latest run
- eBay was attempted through safe public/RSS/text extraction, but the current environment blocks automated eBay access, so the system generates direct eBay review URLs instead of faking inventory
- Car-Part.com is included as a structured usable workflow/direct review URL because unauthenticated automated extraction is blocked by the site in this environment
- Copart/IAAI remain manual-review first, as agreed
- Facebook Marketplace remains manual/assisted only, as agreed

Example real listings pulled in the latest run:

1. Craigslist — Tesla Model 3 Clear PPF Hood, fenders, headlights, mirrors, fog lights
   - Price: $229
   - Location: Spokane / Tukwila
   - Direct link included in Listings tab

2. Craigslist — NEW 2017 2022 2023 Pair TESLA MODEL 3 FRONT LEFT RIGHT Side HOOD HINGE
   - Price: $80
   - Location: Bellingham / Clark-Cowlitz WA
   - Direct link included in Listings tab

3. Craigslist — Tesla Model Y / 3 Parts
   - Location: Spokane / Marysville
   - Direct link included in Listings tab

## Important honesty note

I did not fake live listings for sources that blocked safe automated access. If a source blocks automated HTTP access or requires protected account/login behavior, the system creates a direct review/search row and marks it manual-review. That keeps V1 reliable and avoids account-risky scraping.

## Safety rules still enforced

- No automated seller outreach
- No Facebook Marketplace login automation
- No Copart/IAAI account automation
- No fake inventory rows
- Duplicate links are marked as duplicates and suppressed from unique leads

## How to run

```bash
cd rick-tesla-parts-sniper
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python src/run_monitor.py \
  --config config/rick_v1.json \
  --output output/listings.csv \
  --sheet-dir output/google_sheet_import \
  --max-per-query 2 \
  --max-profiles 8 \
  --max-sites 6
python src/create_google_sheet_xlsx.py \
  --csv-dir output/google_sheet_import \
  --output output/Tesla_Parts_Sniper_V1_Rick_Google_Sheet.xlsx
```

## Next refinement after V1 acceptance

To improve eBay and Car-Part beyond safe public access, the next step would be connecting approved APIs, a paid/approved scraping provider, or running the browser automation inside Rick's own accounts with explicit permission and risk boundaries.

## Current requirement coverage

| Rick requirement | Current V1 status | Notes |
|---|---|---|
| Google Sheet structure | Ready | XLSX + CSV tabs are included and downloadable/importable. |
| Actual live listings | Partially working | Craigslist live parsing works and produced 3 unique real listings in latest run. |
| Direct listing links | Ready | Included in Listings tab and public workbench. |
| Clean scoring | Ready | All rows have match score and notes. |
| No duplicates | Ready | Direct-link duplicate suppression is active. |
| eBay Motors live pull | Code-ready via official eBay Finding API | Set `EBAY_APP_ID` or `EBAY_CLIENT_ID` in `.env` and rerun monitor. Without a valid eBay app id, public RSS/browser access is blocked in this environment and review URLs are used. |
| Car-Part live pull | Blocked unauthenticated | Review workflow included. Needs approved access/provider for full automation. |
| Craigslist live pull | Working | Current live source. |
| Alerts | Prepared, not live-sent | Email alert code and alert preview exist; SMTP/SMS provider needed for real sending. |
| Transfer into Rick accounts | Pending external access | Package is ready; Rick still needs to import/share/approve account/provider setup. |

## Public download links

- Workbench: https://janisag07.github.io/upwork-job-demos/publish/tesla-parts-sniper-v1-workbench/?v=final-handoff
- Google Sheets XLSX: https://janisag07.github.io/upwork-job-demos/publish/tesla-parts-sniper-v1-workbench/downloads/tesla-parts-sniper-v1-google-sheet.xlsx
- Listings CSV: https://janisag07.github.io/upwork-job-demos/publish/tesla-parts-sniper-v1-workbench/downloads/listings.csv
- Delivery notes: https://janisag07.github.io/upwork-job-demos/publish/tesla-parts-sniper-v1-workbench/downloads/delivery-for-rick.md
- Full package ZIP: https://janisag07.github.io/upwork-job-demos/publish/tesla-parts-sniper-v1-workbench/downloads/tesla-parts-sniper-v1-package.zip
