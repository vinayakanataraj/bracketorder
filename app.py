import streamlit as st
from backend import *
from threading import Thread


st.title("Advanced Order")
st.info(body="This app allows you to place bracket orders in Zerodha, which run can concurrently in the background, provided the app is kept open.", icon="ℹ️")

# Enctoken input
enctoken = st.text_input("Enctoken",help="For enctoken, Right click on Zerodha Dashboard   > inspect > Network > ctrl - R > Request headers > enctoken")

col1, col2, col3 = st.columns(3)


with col1:
    # Symbol input
    symbol = st.text_input("Trading symbol")

    # Exchange selectbox
    exchange = st.selectbox(label="Exchange", options=["NSE", "BSE", "NFO", "CDS", "BFO", "MCX"])
    
    # Quantity input
    quantity = st.number_input(label="Quantity", step=1)


with col2:
    # Transaction type selectbox
    transaction_type = st.selectbox(label="Transaction type", options=["BUY", "SELL"])

    # Kite product selectbox
    product = st.selectbox(label="Product", options=["MIS", "CNC", "NRML", "CO"])

    # Kite variety
    variety = st.selectbox(label="Variety", options=["Regular", "AMO", "CO"])


with col3:
    # Entry price
    entry_price = st.number_input(label="Entry price", step=0.01)

    # Target price
    target_price = st.number_input(label="Target price", step=0.01)

    # Stoploss price
    stoploss_price = st.number_input(label="Stoploss price", step=0.01)



# Funciton for the button click handling so that the trading takes place in the background
def handle_button_click(enctoken, symbol, quantity, entry_price, target_price, stoploss_price, transaction_type, exchange, variety, product):
    thread = Thread(target=run_in_process, args=(enctoken, symbol, quantity, entry_price, target_price, stoploss_price, transaction_type, exchange, variety, product))
    thread.start()

# Button to start trading
trade_button = st.button(label="Trade")

if trade_button:
    handle_button_click(enctoken, symbol, quantity, entry_price, target_price, stoploss_price, transaction_type, exchange, variety, product)