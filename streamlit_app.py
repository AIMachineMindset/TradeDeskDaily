#!/usr/bin/env python3
"""
TradeDeskDaily - Matrix-themed Market Dashboard Web App
A visually stunning Streamlit dashboard with real-time market data
"""

import streamlit as st
import yfinance as yf
from datetime import datetime
import pandas as pd
import time

# Page configuration
st.set_page_config(
    page_title="TradeDeskDaily - Market Matrix",
    page_icon="🟢",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Matrix-themed custom CSS
st.markdown("""
<style>
    /* Main background and text */
    .stApp {
        background-color: #0D0208;
        color: #00FF41;
    }

    /* Headers */
    h1, h2, h3 {
        color: #00FF41 !important;
        text-shadow: 0 0 10px #00FF41;
        font-family: 'Courier New', monospace;
    }

    /* Metrics */
    [data-testid="stMetricValue"] {
        color: #00FF41;
        font-size: 2rem;
        font-family: 'Courier New', monospace;
    }

    [data-testid="stMetricLabel"] {
        color: #008F11;
        font-family: 'Courier New', monospace;
    }

    [data-testid="stMetricDelta"] {
        font-family: 'Courier New', monospace;
    }

    /* Dataframes */
    .dataframe {
        background-color: #0D0208 !important;
        color: #00FF41 !important;
        border: 2px solid #00FF41 !important;
        font-family: 'Courier New', monospace;
    }

    .dataframe th {
        background-color: #001a00 !important;
        color: #00FF41 !important;
        border: 1px solid #00FF41 !important;
        font-weight: bold;
    }

    .dataframe td {
        background-color: #0D0208 !important;
        color: #00FF41 !important;
        border: 1px solid #008F11 !important;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #001a00;
    }

    /* Buttons */
    .stButton button {
        background-color: #00FF41;
        color: #0D0208;
        border: 2px solid #00FF41;
        font-family: 'Courier New', monospace;
        font-weight: bold;
    }

    .stButton button:hover {
        background-color: #008F11;
        border: 2px solid #00FF41;
    }

    /* Matrix rain effect on header */
    .matrix-header {
        background: linear-gradient(to bottom, #001a00, #0D0208);
        padding: 20px;
        border: 2px solid #00FF41;
        border-radius: 5px;
        margin-bottom: 20px;
        text-align: center;
    }

    .matrix-title {
        color: #00FF41;
        font-size: 3rem;
        font-family: 'Courier New', monospace;
        text-shadow: 0 0 20px #00FF41;
        margin: 0;
    }

    .matrix-subtitle {
        color: #008F11;
        font-size: 1.2rem;
        font-family: 'Courier New', monospace;
        margin: 10px 0 0 0;
    }

    /* Status indicators */
    .status-online {
        color: #00FF41;
        animation: pulse 2s infinite;
    }

    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }

    /* Cards */
    div[data-testid="stVerticalBlock"] > div[style*="flex-direction: column"] > div {
        background-color: #0D0208;
        border: 1px solid #00FF41;
        border-radius: 5px;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)


class MarketDashboard:
    """Matrix-themed market dashboard for web"""

    def __init__(self):
        self.symbols = {
            "Indices": ["^GSPC", "^DJI", "^IXIC", "^RUT"],
            "Crypto": ["BTC-USD", "ETH-USD", "SOL-USD"],
            "Commodities": ["GC=F", "CL=F", "SI=F"],
            "Currency": ["EURUSD=X", "GBPUSD=X", "JPY=X"]
        }

        self.symbol_names = {
            "^GSPC": "S&P 500",
            "^DJI": "Dow Jones",
            "^IXIC": "NASDAQ",
            "^RUT": "Russell 2000",
            "BTC-USD": "Bitcoin",
            "ETH-USD": "Ethereum",
            "SOL-USD": "Solana",
            "GC=F": "Gold",
            "CL=F": "Crude Oil",
            "SI=F": "Silver",
            "EURUSD=X": "EUR/USD",
            "GBPUSD=X": "GBP/USD",
            "JPY=X": "USD/JPY"
        }

    @st.cache_data(ttl=300)  # Cache for 5 minutes
    def get_market_data(_self, symbol):
        """Fetch market data for a given symbol"""
        try:
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period="5d")

            if hist.empty:
                return None

            current_price = hist['Close'].iloc[-1]
            previous_close = hist['Close'].iloc[-2] if len(hist) > 1 else current_price
            change = current_price - previous_close
            change_percent = (change / previous_close) * 100

            return {
                'price': current_price,
                'change': change,
                'change_percent': change_percent,
                'volume': hist['Volume'].iloc[-1] if 'Volume' in hist.columns else 0,
                'high': hist['High'].iloc[-1],
                'low': hist['Low'].iloc[-1]
            }
        except Exception as e:
            st.error(f"Error fetching {symbol}: {str(e)}")
            return None

    def create_header(self):
        """Create Matrix-styled header"""
        st.markdown("""
        <div class="matrix-header">
            <div class="matrix-title">╔══════════════════════════════════════╗</div>
            <div class="matrix-title">║  TRADEDESK DAILY  ║</div>
            <div class="matrix-title">║  MARKET MATRIX TERMINAL  ║</div>
            <div class="matrix-title">╚══════════════════════════════════════╝</div>
            <div class="matrix-subtitle status-online">● SYSTEM ONLINE - {}</div>
        </div>
        """.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')), unsafe_allow_html=True)

    def get_market_sentiment(self):
        """Get overall market sentiment based on S&P 500"""
        sp500_data = self.get_market_data("^GSPC")

        if sp500_data:
            if sp500_data['change_percent'] > 1:
                return "🟢 BULLISH", sp500_data['change_percent'], "success"
            elif sp500_data['change_percent'] > 0:
                return "🟢 POSITIVE", sp500_data['change_percent'], "normal"
            elif sp500_data['change_percent'] > -1:
                return "🔴 NEGATIVE", sp500_data['change_percent'], "normal"
            else:
                return "🔴 BEARISH", sp500_data['change_percent'], "inverse"
        else:
            return "⚪ UNKNOWN", 0, "off"

    def create_market_table(self, category, symbols):
        """Create a market data table for a category"""
        data = []

        for symbol in symbols:
            market_data = self.get_market_data(symbol)
            if market_data:
                name = self.symbol_names.get(symbol, symbol)

                # Arrow indicator
                if market_data['change'] > 0:
                    arrow = "▲"
                elif market_data['change'] < 0:
                    arrow = "▼"
                else:
                    arrow = "━"

                data.append({
                    'Asset': name,
                    'Price': f"${market_data['price']:,.2f}",
                    'Change': f"{arrow} ${market_data['change']:+,.2f}",
                    'Change %': f"{market_data['change_percent']:+.2f}%",
                    'Volume': f"{market_data['volume']:,.0f}" if market_data['volume'] > 0 else "N/A",
                    'High': f"${market_data['high']:,.2f}",
                    'Low': f"${market_data['low']:,.2f}",
                    '_change_value': market_data['change']  # For styling
                })

        if data:
            df = pd.DataFrame(data)
            # Drop the helper column before display
            display_df = df.drop('_change_value', axis=1)

            # Style the dataframe
            def style_change(val):
                if '▲' in str(val):
                    return 'color: #00FF41'
                elif '▼' in str(val):
                    return 'color: #FF0033'
                return 'color: #FFFFFF'

            styled_df = display_df.style.applymap(style_change, subset=['Change', 'Change %'])

            return styled_df
        return None

    def display_dashboard(self):
        """Display the complete dashboard"""
        # Header
        self.create_header()

        # Market Sentiment
        sentiment, change_pct, status = self.get_market_sentiment()

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown(f"### 📊 MARKET SENTIMENT")
            st.markdown(f"## {sentiment}")

            # Progress bar for sentiment
            if change_pct > 0:
                progress_value = min(change_pct / 2, 1.0)  # Cap at 2% = 100%
                st.progress(progress_value)
            else:
                progress_value = max(change_pct / 2, -1.0)
                st.progress(0.5 + (progress_value / 2))

            st.markdown(f"**S&P 500 Change: {change_pct:+.2f}%**")

        st.markdown("---")

        # Market tables in a grid layout
        for category, symbols in self.symbols.items():
            st.markdown(f"### ━━━ {category.upper()} ━━━")
            styled_table = self.create_market_table(category, symbols)
            if styled_table is not None:
                st.dataframe(styled_table, use_container_width=True, hide_index=True)
            st.markdown("")

        # Footer
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("**🟢 DATA SOURCE**")
            st.markdown("Yahoo Finance (yfinance)")
        with col2:
            st.markdown("**🟢 LAST UPDATE**")
            st.markdown(datetime.now().strftime('%H:%M:%S'))
        with col3:
            st.markdown("**🟢 STATUS**")
            st.markdown("TERMINAL READY")


def main():
    """Main entry point"""
    dashboard = MarketDashboard()

    # Auto-refresh every 5 minutes
    if 'last_update' not in st.session_state:
        st.session_state.last_update = time.time()

    # Sidebar controls
    with st.sidebar:
        st.markdown("## ⚙️ CONTROLS")
        auto_refresh = st.checkbox("Auto-refresh (5 min)", value=True)

        if st.button("🔄 Refresh Now"):
            st.cache_data.clear()
            st.rerun()

        st.markdown("---")
        st.markdown("### 📋 ABOUT")
        st.markdown("""
        **TradeDeskDaily**

        Matrix-themed market dashboard with real-time data.

        - 📈 Major Indices
        - 💰 Cryptocurrencies
        - 🏆 Commodities
        - 💱 Currency Pairs

        Data updates every 5 minutes.
        """)

        st.markdown("---")
        st.markdown("**Made with 🟢 and Python**")
        st.markdown("[GitHub Repository](https://github.com/AIMachineMindset/TradeDeskDaily)")

    # Display dashboard
    dashboard.display_dashboard()

    # Auto-refresh logic
    if auto_refresh:
        current_time = time.time()
        if current_time - st.session_state.last_update > 300:  # 5 minutes
            st.session_state.last_update = current_time
            st.cache_data.clear()
            st.rerun()


if __name__ == "__main__":
    main()
