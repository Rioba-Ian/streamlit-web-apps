import yfinance as yf 
import streamlit as st 

import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and volume of Google & Microsoft!



"""
)

ticker_MSFT = 'MSFT'
ticker_GOOG = 'GOOG'

tickerData_MSFT = yf.Ticker(ticker_MSFT)
tickerData_GOOG = yf.Ticker(ticker_GOOG)

ticker_df1 = tickerData_MSFT.history(period='1d', start='2010-5-31', end='2021-12-27')
ticker_df2 = tickerData_GOOG.history(period='1d', start='2010-5-31', end='2021-12-27')

st.write("""
### Closing prices for Microsoft
""")
st.line_chart(ticker_df1.Close)
st.write("""
### Closing prices for Google
""")
st.line_chart(ticker_df2.Close)
st.write("""
### Volume traded for Microsoft
""")
st.line_chart(ticker_df1.Volume)
st.write("""
### Volume traded for Google
""")
st.line_chart(ticker_df2.Volume)
