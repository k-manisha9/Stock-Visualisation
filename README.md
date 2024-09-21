# Stock Price Visualization

This project is a **Stock Price Visualization** tool built using **Streamlit** and **yfinance** to track historical stock data. It allows users to select from a list of major tech stocks and financial assets and view their performance over time.

## Features:
- **Stock Selection**: Users can select a stock from a predefined list, including companies like TCS, Infosys, Amazon, Microsoft, Apple, Google, and financial indices like SPY.
- **Data Loading**: The app uses `yfinance` to fetch historical stock data from January 1, 2016, to the present date. 
- **Raw Data Display**: Users have the option to view the raw stock data in tabular format.
- **Interactive Plot**: The stock's **Open** and **Close** prices are plotted on an interactive time series chart using **Plotly**, with a range slider to zoom into specific timeframes.

## Libraries Used:
- **yfinance**: For retrieving stock market data.
- **Streamlit**: To build the web-based UI for data selection and visualization.
- **Plotly**: To create interactive plots of stock prices.
- **Pandas**: For data manipulation and handling.
- **NumPy**: For numerical operations.
- **Matplotlib**: Although imported, it is not used in the current implementation.

## How to Run:
1. Clone the repository.
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
   
## Future Improvements:
- Add more stocks to the selection list.
- Include additional financial metrics (e.g., Volume, Adjusted Close).
- Provide options to compare multiple stocks simultaneously.
