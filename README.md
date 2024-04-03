# Bracket Order
This app allows you to place bracket order in Zerodha without using the Kiteconnect API

Usong bracket order you can enter your desired symbol, quantity and other parameters. Then enter your entry, target and stoploss price.

Sit back and relax. Either your target or stoploss shall hit.

Say goodbye to looking at the price chart and making bad financial decisions.

## Initial setup
Install requirements using:
```
python -m pip install -r requirements.txt
```

## Run command
```
python -m streamlit run app.py
```

## Usage
Paste the enctoken in the "enctoken" entry field.
#### Your enctoken can be found by logging into your Kite Zerodha account Dashboard, Right click on Zerodha Dashboard > inspect > Network > ctrl - R > Request headers > enctoken

Then just enter all the other standard trading parameters and click on the "Trade" button to start the trading. The trading happens concurrently in the background, provided the app is kept open.
