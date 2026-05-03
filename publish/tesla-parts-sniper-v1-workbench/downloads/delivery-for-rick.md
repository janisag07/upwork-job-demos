# Tesla Parts Sniper V1 — Delivery Summary for Rick

Hi Rick,

I moved the V1 from structure-only into a working live-monitoring package focused on your latest requirement: real opportunities, direct links, scoring, duplicate control, and complete Google-Sheets-ready export coverage for the configured Tesla parts.

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

Latest UI refinement:

- Year field is now flexible and accepts single years or ranges like `2020-2024` / `2020-2026`.
- Search Profile Generator vehicle field is now directly typable and also includes an A-Z common vehicle/make/model list, including Tesla Model Y, Model 3, Cybertruck, Model X, Model S, and non-Tesla examples.


Latest verified run:

- 245 total sheet-ready rows
- 26 unique real Craigslist/eBay direct listing rows were pulled automatically in the latest run
- The Listings tab now includes every configured Rick part category: hood, front bumper, rear bumper, fender, headlight, door, hatch, trunk, wheel, seat, suspension, and module
- Vehicle/year, part type, color, price, location, direct link, score, duplicate flag, status, and notes are all mapped into the sheet export
- Craigslist search/profile links explicitly use Craigslist Auto Parts / Parts for Sale (`/search/pta`), not cars/trucks (`/search/cta`, `/search/cto`, or `/search/ctd`)
- eBay was attempted through safe public/RSS/text extraction, but the current environment blocks automated eBay access, so the system generates direct eBay review URLs instead of faking inventory
- Car-Part.com is included as a structured usable workflow/direct review URL because unauthenticated automated extraction is blocked by the site in this environment
- Copart/IAAI remain manual-review first, as agreed
- Facebook Marketplace remains manual/assisted only, as agreed

Example real listings pulled in the latest run:

1. Craigslist — Tesla Model Y Door Wiring Rear Right 2020-2024 OEM 1489
   - Price: $135
   - Location: seattle / Marysville
   - Part: door
   - Direct link included in Listings tab
2. Craigslist — Tesla Model Y (2020-2024) Trunk Storage Bins
   - Price: $20
   - Location: seattle / Kirkland
   - Part: trunk
   - Direct link included in Listings tab
3. Craigslist — AOMSAZTO Car Seat Cover Fit for Tesla Model Y 2020 2021 2022 2023 2024 2025- Ful
   - Price: $40
   - Location: seattle / Covington
   - Part: seat
   - Direct link included in Listings tab
4. Craigslist — Tesla Model Y Left Headlight (New)
   - Price: $250
   - Location: seattle / north vancouver
   - Part: headlight
   - Direct link included in Listings tab
5. Craigslist — 2021-2023 Tesla Model Y Front Drivers Left Door Panel Card
   - Price: $100
   - Location: seattle / NE Portland
   - Part: door
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
./scripts/run_rick_monitor.sh
```

## Next refinement after V1 acceptance

To improve eBay and Car-Part beyond safe public access, the next step would be connecting approved APIs, a paid/approved scraping provider, or running the browser automation inside Rick's own accounts with explicit permission and risk boundaries.

## Current requirement coverage

| Rick requirement | Current V1 status | Notes |
|---|---|---|
| Google Sheet structure | Ready | XLSX + CSV tabs are included and downloadable/importable. |
| Actual live listings | Partially working | Craigslist live parsing works and produced 26 unique real direct listings in latest run. |
| Direct listing links | Ready | Included in Listings tab and public workbench. |
| Complete part coverage | Ready | All configured part categories are represented in the sheet package. |
| Clean scoring | Ready | All rows have match score and notes. |
| No duplicates | Ready | Direct-link duplicate suppression is active. |
| eBay Motors live pull | Code-ready via official eBay Finding API | Set `EBAY_APP_ID` or `EBAY_CLIENT_ID` in `.env` and rerun monitor. Without a valid eBay app id, public RSS/browser access is blocked in this environment and review URLs are used. |
| Car-Part live pull | Blocked unauthenticated | Review workflow included. Needs approved access/provider for full automation. |
| Craigslist live pull | Working | Current live source. |
| Alerts | Prepared, not live-sent | Email alert code and alert preview exist; SMTP/SMS provider needed for real sending. |
| Transfer into Rick accounts | Pending external access | Package is ready; Rick still needs to import/share/approve account/provider setup. |

## Public download links

- Workbench: https://janisag07.github.io/upwork-job-demos/publish/tesla-parts-sniper-v1-workbench/?v=rick-fixes
- Google Sheets XLSX: https://janisag07.github.io/upwork-job-demos/publish/tesla-parts-sniper-v1-workbench/downloads/tesla-parts-sniper-v1-google-sheet.xlsx
- Listings CSV: https://janisag07.github.io/upwork-job-demos/publish/tesla-parts-sniper-v1-workbench/downloads/listings.csv
- Delivery notes: https://janisag07.github.io/upwork-job-demos/publish/tesla-parts-sniper-v1-workbench/downloads/delivery-for-rick.md
- Full package ZIP: https://janisag07.github.io/upwork-job-demos/publish/tesla-parts-sniper-v1-workbench/downloads/tesla-parts-sniper-v1-package.zip
