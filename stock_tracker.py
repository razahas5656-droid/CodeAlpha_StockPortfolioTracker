
import csv
from datetime import datetime

# Hardcoded stock prices (per share, in USD)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 410,
    "AMZN": 175,
    "META": 480,
    "NFLX": 650,
}


def show_available_stocks():
    print("\nAvailable stocks and prices per share:")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<6} : ${price}")


def get_portfolio_input():
    """Collect stock symbol + quantity pairs from the user."""
    portfolio = {}

    print("\nEnter stock symbol and quantity (e.g. AAPL 10).")
    print("Type 'done' when you are finished.\n")

    while True:
        entry = input("Stock (or 'done'): ").strip()

        if entry.lower() == "done":
            break

        parts = entry.upper().split()
        if len(parts) != 2:
            print("Please enter in the format: SYMBOL QUANTITY (e.g. AAPL 10)")
            continue

        symbol, qty_str = parts

        if symbol not in STOCK_PRICES:
            print(f"'{symbol}' is not in the price list. Try one of: {', '.join(STOCK_PRICES)}")
            continue

        if not qty_str.isdigit() or int(qty_str) <= 0:
            print("Quantity must be a positive whole number.")
            continue

        qty = int(qty_str)
        portfolio[symbol] = portfolio.get(symbol, 0) + qty
        print(f"Added {qty} share(s) of {symbol}.")

    return portfolio


def calculate_investment(portfolio):
    """Return a breakdown list and the total investment value."""
    breakdown = []
    total = 0
    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        total += value
        breakdown.append((symbol, qty, price, value))
    return breakdown, total


def display_summary(breakdown, total):
    print("\n" + "=" * 45)
    print("PORTFOLIO SUMMARY")
    print("=" * 45)
    print(f"{'Symbol':<8}{'Qty':<8}{'Price':<10}{'Value'}")
    print("-" * 45)
    for symbol, qty, price, value in breakdown:
        print(f"{symbol:<8}{qty:<8}${price:<9}${value}")
    print("-" * 45)
    print(f"TOTAL INVESTMENT: ${total}")
    print("=" * 45)


def save_to_file(breakdown, total):
    choice = input("\nSave this summary to a file? (y/n): ").lower().strip()
    if choice != "y":
        return

    fmt = input("Save as .txt or .csv? ").lower().strip()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if fmt == "csv":
        filename = f"portfolio_{timestamp}.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Symbol", "Quantity", "Price", "Value"])
            for row in breakdown:
                writer.writerow(row)
            writer.writerow([])
            writer.writerow(["Total Investment", "", "", total])
        print(f"Saved to {filename}")
    else:
        filename = f"portfolio_{timestamp}.txt"
        with open(filename, "w") as f:
            f.write("PORTFOLIO SUMMARY\n")
            f.write("=" * 45 + "\n")
            f.write(f"{'Symbol':<8}{'Qty':<8}{'Price':<10}{'Value'}\n")
            f.write("-" * 45 + "\n")
            for symbol, qty, price, value in breakdown:
                f.write(f"{symbol:<8}{qty:<8}${price:<9}${value}\n")
            f.write("-" * 45 + "\n")
            f.write(f"TOTAL INVESTMENT: ${total}\n")
        print(f"Saved to {filename}")


def main():
    print("=" * 45)
    print("Welcome to the Stock Portfolio Tracker")
    print("=" * 45)

    show_available_stocks()
    portfolio = get_portfolio_input()

    if not portfolio:
        print("\nNo stocks entered. Exiting.")
        return

    breakdown, total = calculate_investment(portfolio)
    display_summary(breakdown, total)
    save_to_file(breakdown, total)


if __name__ == "__main__":
    main()
