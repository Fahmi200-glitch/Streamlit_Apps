import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

st.title("Stock Price Chart")

ticker_input = st.text_input("Enter Stock Ticker (e.g., AAPL, MSFT, GOOGL):")

if ticker_input:
    data = yf.download(ticker_input, period="1mo", interval="1d")

    if not data.empty:
        st.write(f"Last 30 days of {ticker_input} stock prices:")
        st.dataframe(data.tail())

        plt.figure(figsize=(10, 5))
        plt.plot(data["Close"], label="Close Price")
        plt.xlabel("Date")
        plt.ylabel("Price ($)")
        plt.title(f"{ticker_input} Stock Price")
        plt.legend()
        st.pyplot(plt)