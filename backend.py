from kite_trade import *
import time
from multiprocessing import Process



def trade(enctoken, symbol, quantity, entry_price, target_price, stoploss_price, transaction_type, exchange, variety, product):
    kite = KiteApp(enctoken=enctoken)

    # Exchange methods dictionary
    exchange_methods = {"NSE":kite.EXCHANGE_NSE, "BSE":kite.EXCHANGE_BSE, "NFO":kite.EXCHANGE_NFO, "BFO":kite.EXCHANGE_BFO, "CDS":kite.EXCHANGE_CDS, "MCX":kite.EXCHANGE_MCX}
    variety_methods = {"Regular":kite.VARIETY_REGULAR, "AMO":kite.VARIETY_AMO, "CO":kite.VARIETY_CO}
    product_methods = {"MIS":kite.PRODUCT_MIS, "CNC":kite.PRODUCT_CNC, "NRML":kite.PRODUCT_NRML, "CO":kite.PRODUCT_CO}


    def place_order(symbol, quantity, transaction_type, exchange, product, variety):
        order_id = kite.place_order(variety=variety,
                                    tradingsymbol=symbol,
                                    exchange=exchange,
                                    transaction_type=kite.TRANSACTION_TYPE_BUY if transaction_type=="BUY" else kite.TRANSACTION_TYPE_SELL,
                                    quantity=quantity,
                                    order_type=kite.ORDER_TYPE_MARKET,
                                    price=None,
                                    validity=None,
                                    disclosed_quantity=None,
                                    trigger_price=None,
                                    squareoff=None,
                                    stoploss=None,
                                    trailing_stoploss=None,
                                    product=product)
        return order_id

    if transaction_type == "BUY":
        exchange = exchange_methods[exchange]
        variety = variety_methods[variety]
        product = product_methods[product]
        while time.localtime().tm_hour <= 15:
            if (kite.quote([f"NSE:{symbol}"])[symbol])['last_price'] <= entry_price:
                place_order(symbol=symbol, quantity=quantity, transaction_type="BUY", exchange=exchange, variety=variety, product=product)
                break
            else:
                time.sleep(10)
        while time.localtime().tm_hour <= 15:
            if (kite.quote([f"NSE:{symbol}"])[symbol])['last_price'] >= target_price:
                place_order(symbol=symbol, quantity=quantity, transaction_type="SELL")
                break
            
            elif (kite.quote([f"NSE:{symbol}"])[symbol])['last_price'] <= stoploss_price:
                place_order(symbol=symbol, quantity=quantity, transaction_type="SELL")
                break
            else:
                time.sleep(10)
        
    elif transaction_type == "SELL":
        exchange = exchange_methods[exchange]
        variety = variety_methods[variety]
        product = product_methods[product]
        while time.localtime().tm_hour <= 15:
            if (kite.quote([f"NSE:{symbol}"])[symbol])['last_price'] <= entry_price:
                place_order(symbol=symbol, quantity=quantity, transaction_type="SELL", exchange=exchange, variety=variety, product=product)
                break
            else:
                time.sleep(10)
        while time.localtime().tm_hour <= 15:
            if (kite.quote([f"NSE:{symbol}"])[symbol])['last_price'] >= target_price:
                place_order(symbol=symbol, quantity=quantity, transaction_type="BUY")
                break
            
            elif (kite.quote([f"NSE:{symbol}"])[symbol])['last_price'] <= stoploss_price:
                place_order(symbol=symbol, quantity=quantity, transaction_type="BUY")
                break
            else:
                time.sleep(10)



def run_in_process(enctoken, symbol, quantity, entry_price, target_price, stoploss_price, transaction_type, exchange, variety, product):
    process = Process(target=trade, args=(enctoken, symbol, quantity, entry_price, target_price, stoploss_price, transaction_type, exchange, variety, product))
    process.start()


