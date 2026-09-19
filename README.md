# CodeAlpha_StockPortfolioTracker

**CodeAlpha Python Programming Internship — Task 2**

Two versions are included:

## 1. `stock_tracker.py` — Basic version
Calculates total investment value from user-entered stock quantities and
hardcoded prices, with optional `.txt`/`.csv` export.

```bash
python stock_tracker.py
```

## 2. `stock_tracker_advanced.py` — Advanced version (recommended)
Everything the basic version does, plus:

- **OOP design** — a `PortfolioTracker` class instead of loose functions
- **% allocation per stock** shown in the summary table
- **Largest / smallest holding** highlighted automatically
- **Data visualization with matplotlib**:
  - Pie chart showing portfolio allocation (%)
  - Bar chart showing investment value per stock, sorted highest to lowest
  - Option to save the chart as a `.png` image
- Still supports saving the summary to `.txt`/`.csv`

```bash
pip install matplotlib
python stock_tracker_advanced.py
```

### Example output
Enter stocks like `AAPL 10`, `TSLA 5`, etc., then type `done`. You'll get:
1. A formatted summary table with percentages
2. Largest/smallest holding callout
3. Option to save results to file
4. Option to view (and save) a pie + bar chart visualization

## Concepts used
Dictionaries, classes/OOP, input/output, basic arithmetic, file handling
(`csv` module), data visualization (`matplotlib`).
