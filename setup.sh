#!/bin/bash
# TradeDeskDaily Setup Script

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║  TRADEDESK DAILY - SETUP SCRIPT                              ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Check Python version
echo "Checking Python version..."
python3 --version

if [ $? -ne 0 ]; then
    echo "Error: Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo ""
    echo "╔═══════════════════════════════════════════════════════════════╗"
    echo "║  SETUP COMPLETE!                                             ║"
    echo "╚═══════════════════════════════════════════════════════════════╝"
    echo ""
    echo "Run the dashboard with:"
    echo "  python market_dashboard.py"
    echo ""
else
    echo "Error: Failed to install dependencies"
    exit 1
fi
