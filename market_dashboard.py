#!/usr/bin/env python3
"""
TradeDeskDaily - Matrix-themed End of Day Market Update Dashboard
A visually stunning terminal dashboard with real-time market data
"""

import yfinance as yf
from datetime import datetime, timedelta
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text
from rich.align import Align
from rich import box
from rich.columns import Columns
import sys

console = Console()

# Matrix color scheme
MATRIX_GREEN = "#00FF41"
MATRIX_DARK_GREEN = "#008F11"
MATRIX_BLACK = "#0D0208"
POSITIVE_COLOR = "#00FF41"
NEGATIVE_COLOR = "#FF0033"
NEUTRAL_COLOR = "#FFFFFF"


class MarketDashboard:
    """Matrix-themed market dashboard"""

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

    def get_market_data(self, symbol):
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
            console.print(f"[red]Error fetching {symbol}: {str(e)}[/red]")
            return None

    def create_matrix_header(self):
        """Create Matrix-styled header"""
        header_text = Text()
        header_text.append("╔═══════════════════════════════════════════════════════════════╗\n", style=MATRIX_GREEN)
        header_text.append("║  ", style=MATRIX_GREEN)
        header_text.append("TRADEDESK DAILY", style=f"bold {MATRIX_GREEN}")
        header_text.append(" - MARKET MATRIX TERMINAL", style=MATRIX_GREEN)
        header_text.append("           ║\n", style=MATRIX_GREEN)
        header_text.append("║  ", style=MATRIX_GREEN)
        header_text.append(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]", style=MATRIX_DARK_GREEN)
        header_text.append(" SYSTEM ONLINE", style=f"bold {MATRIX_GREEN}")
        header_text.append("                        ║\n", style=MATRIX_GREEN)
        header_text.append("╚═══════════════════════════════════════════════════════════════╝", style=MATRIX_GREEN)

        return Panel(
            Align.center(header_text),
            style=f"{MATRIX_GREEN} on black",
            border_style=MATRIX_GREEN
        )

    def create_market_table(self, category, symbols):
        """Create a market data table for a category"""
        table = Table(
            title=f"[bold {MATRIX_GREEN}]━━━ {category.upper()} ━━━[/]",
            box=box.DOUBLE_EDGE,
            border_style=MATRIX_GREEN,
            header_style=f"bold {MATRIX_GREEN}",
            show_header=True,
            padding=(0, 1)
        )

        table.add_column("ASSET", style=MATRIX_GREEN, justify="left", width=15)
        table.add_column("PRICE", justify="right", width=12)
        table.add_column("CHANGE", justify="right", width=12)
        table.add_column("CHANGE %", justify="right", width=10)
        table.add_column("VOLUME", justify="right", width=15)

        for symbol in symbols:
            data = self.get_market_data(symbol)
            if data:
                name = self.symbol_names.get(symbol, symbol)
                price = f"${data['price']:,.2f}"
                change = f"{data['change']:+,.2f}"
                change_pct = f"{data['change_percent']:+.2f}%"
                volume = f"{data['volume']:,.0f}" if data['volume'] > 0 else "N/A"

                # Color coding based on change
                if data['change'] > 0:
                    change_color = POSITIVE_COLOR
                    arrow = "▲"
                elif data['change'] < 0:
                    change_color = NEGATIVE_COLOR
                    arrow = "▼"
                else:
                    change_color = NEUTRAL_COLOR
                    arrow = "━"

                table.add_row(
                    name,
                    f"[{MATRIX_GREEN}]{price}[/]",
                    f"[{change_color}]{arrow} {change}[/]",
                    f"[{change_color}]{change_pct}[/]",
                    f"[{MATRIX_DARK_GREEN}]{volume}[/]"
                )

        return table

    def create_summary_panel(self):
        """Create market summary panel"""
        # Get S&P 500 data for overall market sentiment
        sp500_data = self.get_market_data("^GSPC")

        if sp500_data:
            if sp500_data['change_percent'] > 1:
                sentiment = "BULLISH"
                sentiment_color = POSITIVE_COLOR
                indicator = "█████████░"
            elif sp500_data['change_percent'] > 0:
                sentiment = "POSITIVE"
                sentiment_color = POSITIVE_COLOR
                indicator = "██████░░░░"
            elif sp500_data['change_percent'] > -1:
                sentiment = "NEGATIVE"
                sentiment_color = NEGATIVE_COLOR
                indicator = "████░░░░░░"
            else:
                sentiment = "BEARISH"
                sentiment_color = NEGATIVE_COLOR
                indicator = "██░░░░░░░░"
        else:
            sentiment = "UNKNOWN"
            sentiment_color = NEUTRAL_COLOR
            indicator = "░░░░░░░░░░"

        summary_text = Text()
        summary_text.append("MARKET SENTIMENT: ", style=f"bold {MATRIX_GREEN}")
        summary_text.append(f"{sentiment}\n", style=f"bold {sentiment_color}")
        summary_text.append(f"{indicator}\n", style=sentiment_color)
        summary_text.append(f"\nData updated: {datetime.now().strftime('%H:%M:%S')}", style=MATRIX_DARK_GREEN)

        return Panel(
            Align.center(summary_text),
            title="[bold white]SYSTEM STATUS[/]",
            border_style=MATRIX_GREEN,
            padding=(1, 2)
        )

    def display_dashboard(self):
        """Display the complete dashboard"""
        console.clear()

        # Matrix animation effect
        console.print("[bold green]> INITIALIZING MARKET MATRIX...[/]")
        console.print("[green]> ESTABLISHING SECURE CONNECTION...[/]")
        console.print("[green]> FETCHING REAL-TIME DATA...[/]")
        console.print()

        # Header
        console.print(self.create_matrix_header())
        console.print()

        # Summary
        console.print(self.create_summary_panel())
        console.print()

        # Market tables
        for category, symbols in self.symbols.items():
            table = self.create_market_table(category, symbols)
            console.print(table)
            console.print()

        # Footer
        footer = Text()
        footer.append("═" * 65, style=MATRIX_GREEN)
        footer.append("\n")
        footer.append("  DATA SOURCE: Yahoo Finance (yfinance)  |  ", style=MATRIX_DARK_GREEN)
        footer.append("REFRESH: Run script again\n", style=MATRIX_DARK_GREEN)
        footer.append("═" * 65, style=MATRIX_GREEN)
        console.print(footer)

        console.print(f"\n[{MATRIX_GREEN}]> MARKET DATA LOADED SUCCESSFULLY[/]")
        console.print(f"[{MATRIX_DARK_GREEN}]> TERMINAL READY[/]\n")


def main():
    """Main entry point"""
    try:
        dashboard = MarketDashboard()
        dashboard.display_dashboard()
    except KeyboardInterrupt:
        console.print("\n[red]> SYSTEM INTERRUPTED - SHUTTING DOWN[/]")
        sys.exit(0)
    except Exception as e:
        console.print(f"[red]> ERROR: {str(e)}[/]")
        sys.exit(1)


if __name__ == "__main__":
    main()
