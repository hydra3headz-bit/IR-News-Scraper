
import streamlit as st
import scout
from datetime import datetime
import pandas as pd

# Page Config
st.set_page_config(page_title="IR News Scraper", page_icon="🦅", layout="wide")

# Custom CSS for "The Raptor" branding
st.markdown("""
    <style>
    .main { background-color: #0f172a; color: #e2e8f0; }
    .stButton>button { background-color: #3b82f6; color: white; width: 100%; border-radius: 8px; }
    .stTextInput>div>div>input { background-color: #1e293b; color: white; }
    .footer { text-align: center; padding: 20px; color: #64748b; font-size: 0.8rem; }
    .raptor { color: #60a5fa; font-weight: bold; }
    </style>
""", unsafe_with_html=True)

# Header
st.title("IR News Scraper 🦅")
st.subheader("Discover Investor Relations news without the noise.")

# Sidebar / Controls
with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        tickers_input = st.text_input("Target Tickers", placeholder="NVDA, AMD, PLTR (Max 5)")
    with col2:
        timeframe = st.selectbox("Time Range", 
                               options=[1, 3, 7, 30, 60, 90, 120, 150, 180], 
                               format_func=lambda x: {
                                   1: "Last 24 Hours",
                                   3: "Last 3 Days",
                                   7: "Last Week",
                                   30: "Last Month",
                                   60: "Last 2 Months",
                                   90: "Last Quarter",
                                   120: "Last 4 Months",
                                   150: "Last 5 Months",
                                   180: "Last 6 Months"
                               }.get(x),
                               index=2)

if st.button("🚀 Start Raptor Scan"):
    if not tickers_input:
        st.error("Please enter at least one ticker.")
    else:
        tickers = [t.strip().upper() for t in tickers_input.split(",") if t.strip()][:5]
        
        # Grid for results
        for ticker in tickers:
            with st.expander(f"📊 Results for {ticker}", expanded=True):
                with st.status(f"Raptor is hunting for {ticker}...", expanded=False) as status:
                    st.write("🔍 Discovering IR Hub...")
                    url = scout.find_ir_page(ticker)
                    
                    if not url:
                        st.error(f"Could not find IR page for {ticker}")
                        status.update(label=f"❌ {ticker}: Discovery Failed", state="error")
                        continue
                    
                    st.write(f"⚡ Parallel Scouting via Yahoo, Reddit, and {url}...")
                    news = scout.get_news(url, ticker, days_lookback=timeframe)
                    
                    if not news:
                        st.warning(f"No news found for {ticker} in this timeframe.")
                        status.update(label=f"⚠️ {ticker}: No news found", state="complete")
                    else:
                        st.success(f"Found {len(news)} items for {ticker}!")
                        for item in news:
                            with st.container(border=True):
                                col_a, col_b = st.columns([1, 5])
                                with col_a:
                                    st.caption(item['date'])
                                with col_b:
                                    st.markdown(f"**[{item['headline']}]({item['link']})**")
                        
                        status.update(label=f"✅ {ticker}: Scan Complete", state="complete")


# Footer
st.markdown("""
    <div class="footer">
        Powered by <span class="raptor">The Raptor</span> 🦅
    </div>
""", unsafe_with_html=True)
