# IR News Scraper 🦅📈

A lightweight, local-first tool to discover Investor Relations news from any stock ticker without the noise of news aggregators.

## Features
- **Smart Ticker Discovery**: Automatically finds the official IR newsroom for any stock ticker (powered by Yahoo Finance & recursive crawling).
- **Universal Support**: Works for `NVDA`, `AMD`, `TSLA`, and thousands of other symbols.
- **Timeframe Filtering**: Filter news by the last 24 hours, week, month, or quarter.
- **No API Keys Required**: Uses standard web scraping and public search queries.
- **Privacy Focused**: No data leaves your machine; no external AI services or trackers.

## 🚀 How to Run

### Option 1: Launch as Web App (Recommended)
You can host this directly on **Streamlit Cloud** so you can access it via a URL without a local command window:
1.  Fork or upload this folder to your **GitHub**.
2.  Log in to **[share.streamlit.io](https://share.streamlit.io)**.
3.  Click **"New App"** and select your repository.
4.  Launch! You will get a permanent public link.

### Option 2: Local Run
1.  Make sure [Python](https://www.python.org/downloads/) is installed.
2.  Double-click **`run_scraper.bat`**.
3.  Open `http://127.0.0.1:5000` in your browser.

## 🛠 Tech Stack
- **Backend**: Python, Flask, Flask-CORS
- **Engine**: BeautifulSoup4, Requests, GoogleSearch-Python, Dateparser
- **Frontend**: Tailwind CSS, Vanilla JS

---
*Powered by **The Raptor** 🦅*
