# Simplified Trading Bot for Binance Futures Testnet

This is a simplified trading bot implemented in Python that interacts with the Binance Futures Testnet. The bot allows users to place market and limit orders for trading pairs on the Binance platform.

## Features

- Place market and limit orders on Binance Futures Testnet (USDT-M).
- Support for both buy and sell order sides.
- Command-line interface for user input.
- Logging of API requests, responses, and errors.
- Basic error handling for API interactions.

## Prerequisites

- Python 3.6 or higher
- Binance Testnet account
- API Key and Secret from Binance Testnet
- `python-binance` library

## Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>

## Install the required library:
    pip install python-binance

## Input parameters: When prompted, enter the following:

- Trading pair (e.g., BTCUSDT)
- Order side (BUY or SELL)
- Quantity (e.g., 0.01)
- Order type (MARKET or LIMIT)
- If you choose LIMIT, you will also need to provide a limit price.
