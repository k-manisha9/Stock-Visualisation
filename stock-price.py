
import yfinance as yf
import streamlit as stl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from datetime import date
from plotly import graph_objs as go

stl.title('Stock Price Visualization')
start="2016-01-01"
today=date.today().strftime("%Y-%m-%d")

stocks=['TCS','INFY','WIP.NS','AMZN','MSFT','AAPL','GOOG','SPY']


selectedStocks=stl.selectbox("Select the stock",stocks)
@stl.cache_data
def load_data(ticker):
    data=yf.download(ticker,start,today)
    data.reset_index(inplace=True)
    return data
    

data_load_state=stl.text("Loading data...")
data=load_data(selectedStocks)
data_load_state.text("Done! (using st.cache_data)")
if stl.checkbox('Show raw data'):
    stl.subheader('Raw data')
    stl.write(data)


#plotting the data

def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data["Date"], y=data["Open"], name="stock open", marker = {'color' : '#eb6b34'}))
    fig.add_trace(go.Scatter(x=data["Date"], y=data["Close"], name="stock close", marker = {'color' : '#34b4eb'}))
    fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
    stl.plotly_chart(fig)
    
    
plot_raw_data()


