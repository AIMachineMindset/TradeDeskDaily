# TradeDeskDaily 🟢

> A Matrix-themed end-of-day market update dashboard with stunning terminal visuals

**Live at:** https://tradedeskdaily.com

## Overview

TradeDeskDaily is a visually striking Python-based market dashboard that delivers real-time market data in a beautiful Matrix-themed terminal interface. Get instant insights into stocks, crypto, commodities, and currencies with color-coded metrics and clean formatting.

## Features

- **Matrix Aesthetic**: Beautiful green-on-black terminal interface inspired by The Matrix
- **Real-Time Data**: Live market data from Yahoo Finance (via yfinance)
- **Multi-Asset Coverage**:
  - Major Indices (S&P 500, Dow Jones, NASDAQ, Russell 2000)
  - Cryptocurrencies (Bitcoin, Ethereum, Solana)
  - Commodities (Gold, Crude Oil, Silver)
  - Currency Pairs (EUR/USD, GBP/USD, USD/JPY)
- **Visual Indicators**: Color-coded price changes (green for gains, red for losses)
- **Market Sentiment**: Overall market sentiment indicator based on S&P 500 performance
- **Clean Layout**: Organized tables with price, change, change %, and volume data

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

Run the dashboard:

```bash
python market_dashboard.py
```

Or make it executable:

```bash
chmod +x market_dashboard.py
./market_dashboard.py
```

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

## Customization

You can easily customize the dashboard by editing `market_dashboard.py`:

- **Add/Remove Symbols**: Modify the `self.symbols` dictionary in the `MarketDashboard` class
- **Change Colors**: Adjust the color constants at the top of the file
- **Update Refresh Rate**: Add automatic refresh by implementing a timer loop

## Dependencies

- `yfinance`: Free market data from Yahoo Finance
- `rich`: Beautiful terminal formatting and colors
- `pandas`: Data manipulation
- `numpy`: Numerical operations

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
