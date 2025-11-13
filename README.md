# TradeDeskDaily 🟢

> A Matrix-themed end-of-day market update dashboard - Available in Terminal & Web Browser

**Live at:** https://tradedeskdaily.com

## Overview

TradeDeskDaily is a visually striking Python-based market dashboard that delivers real-time market data in a beautiful Matrix-themed interface. Available in both **terminal** and **web browser** versions, get instant insights into stocks, crypto, commodities, and currencies with color-coded metrics and clean formatting.

### Two Versions Available

- **🖥️ Terminal Version** (`market_dashboard.py`) - Classic command-line interface with rich text formatting
- **🌐 Web Version** (`streamlit_app.py`) - Browser-based dashboard with auto-refresh and interactive features

## Features

- **Matrix Aesthetic**: Beautiful green-on-black interface inspired by The Matrix
- **Real-Time Data**: Live market data from Yahoo Finance (via yfinance)
- **Multi-Asset Coverage**:
  - Major Indices (S&P 500, Dow Jones, NASDAQ, Russell 2000)
  - Cryptocurrencies (Bitcoin, Ethereum, Solana)
  - Commodities (Gold, Crude Oil, Silver)
  - Currency Pairs (EUR/USD, GBP/USD, USD/JPY)
- **Visual Indicators**: Color-coded price changes (green for gains, red for losses)
- **Market Sentiment**: Overall market sentiment indicator based on S&P 500 performance
- **Clean Layout**: Organized tables with price, change, change %, and volume data
- **Auto-Refresh**: Web version includes automatic data refresh every 5 minutes
- **Responsive Design**: Web version adapts to different screen sizes

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/AIMachineMindset/TradeDeskDaily.git
cd TradeDeskDaily
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Terminal Version

Run the terminal dashboard:

```bash
python market_dashboard.py
```

Or make it executable:

```bash
chmod +x market_dashboard.py
./market_dashboard.py
```

### Web Version

Run the web dashboard locally:

```bash
streamlit run streamlit_app.py
```

The dashboard will open in your browser at `http://localhost:8501`

**Web Features:**
- 🔄 Auto-refresh every 5 minutes
- 📊 Interactive tables
- 🎨 Full Matrix theme styling
- 📱 Responsive layout
- ⚙️ Settings sidebar

## Sample Output

```
> INITIALIZING MARKET MATRIX...
> ESTABLISHING SECURE CONNECTION...
> FETCHING REAL-TIME DATA...

╔═══════════════════════════════════════════════════════════════╗
║  TRADEDESK DAILY - MARKET MATRIX TERMINAL           ║
║  [2025-11-13 21:30:45] SYSTEM ONLINE                        ║
╚═══════════════════════════════════════════════════════════════╝

                    MARKET SENTIMENT: POSITIVE
                         ██████░░░░

━━━ INDICES ━━━
╔═════════════════╦══════════════╦══════════════╦════════════╦═══════════════╗
║ ASSET           ║        PRICE ║       CHANGE ║  CHANGE % ║        VOLUME ║
╠═════════════════╬══════════════╬══════════════╬════════════╬═══════════════╣
║ S&P 500         ║    $4,567.89 ║    ▲ +23.45  ║    +0.52% ║ 3,234,567,890 ║
║ Dow Jones       ║   $35,678.12 ║    ▲ +156.78 ║    +0.44% ║ 2,123,456,789 ║
║ NASDAQ          ║   $14,234.56 ║    ▲ +89.12  ║    +0.63% ║ 4,567,890,123 ║
║ Russell 2000    ║    $1,987.65 ║    ▼ -5.43   ║    -0.27% ║   987,654,321 ║
╚═════════════════╩══════════════╩══════════════╩════════════╩═══════════════╝
```

## Deploy to the Web (FREE)

You can deploy the web version to **Streamlit Cloud** for free and access it from anywhere:

### Streamlit Cloud Deployment

1. **Fork this repository** to your GitHub account

2. **Go to** [share.streamlit.io](https://share.streamlit.io)

3. **Sign in** with your GitHub account

4. **Click "New app"** and select:
   - Repository: `YourUsername/TradeDeskDaily`
   - Branch: `main` (or your branch)
   - Main file path: `streamlit_app.py`

5. **Click "Deploy"** - Your app will be live in minutes!

Your dashboard will be accessible at: `https://yourappname.streamlit.app`

### Other Deployment Options

- **Replit**: Import repo and run `streamlit run streamlit_app.py`
- **Heroku**: Use the included Streamlit configuration
- **Railway**: One-click deployment from GitHub
- **Python Anywhere**: Host as a web app

## Customization

You can easily customize the dashboard:

**Terminal Version** (`market_dashboard.py`):
- **Add/Remove Symbols**: Modify the `self.symbols` dictionary
- **Change Colors**: Adjust the color constants at the top

**Web Version** (`streamlit_app.py`):
- **Add/Remove Symbols**: Modify the `self.symbols` dictionary
- **Change Colors**: Edit the custom CSS in the `st.markdown()` section
- **Update Refresh Rate**: Change the `ttl` parameter in `@st.cache_data` decorator

## Dependencies

- `yfinance`: Free market data from Yahoo Finance
- `rich`: Beautiful terminal formatting and colors (terminal version)
- `streamlit`: Web framework for the browser version
- `pandas`: Data manipulation
- `numpy`: Numerical operations

All dependencies are listed in `requirements.txt`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

See [LICENSE](LICENSE) file for details.

## Disclaimer

This dashboard is for informational purposes only. Market data is provided by Yahoo Finance and may be delayed. Do not use this for making financial decisions without consulting a licensed financial advisor.

## Support

For issues or questions, please open an issue on GitHub.

---

**Made with 🟢 and Python**
