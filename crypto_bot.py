import logging
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret, testnet=testnet)
        self.base_url = "https://testnet.binancefuture.com"

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='MARKET',
                quantity=quantity
            )
            logging.info(f"Market order placed: {order}")
            return order
        except Exception as e:
            logging.error(f"Error placing market order: {e}")
            return None

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='LIMIT',
                quantity=quantity,
                price=price,
                timeInForce='GTC'
            )
            logging.info(f"Limit order placed: {order}")
            return order
        except Exception as e:
            logging.error(f"Error placing limit order: {e}")
            return None

    def get_user_input(self):
        symbol = input("Enter trading pair (e.g., BTCUSDT): ").upper()
        side = input("Enter order side (BUY/SELL): ").upper()
        quantity = float(input("Enter quantity: "))
        order_type = input("Enter order type (MARKET/LIMIT): ").upper()

        if order_type == 'LIMIT':
            price = float(input("Enter limit price: "))
            return symbol, side, quantity, price
        return symbol, side, quantity, None

    def execute_trade(self):
        user_input = self.get_user_input()
        if len(user_input) == 4:
            symbol, side, quantity, price = user_input
            if price:
                self.place_limit_order(symbol, side, quantity, price)
            else:
                self.place_market_order(symbol, side, quantity)

if __name__ == "__main__":
    
    API_KEY = '6pegJIrbzgGUNfdB8VkrA285DK130LzRALqdiGAhekriAU1Ev2Xn2CYOWoQd3Me8'
    API_SECRET = '5A6IyQPDlfMx3kuoMQxdEMHvlo79RQxSnLPulqBMkrFliARhcPXQ6bCLaw7trC8z'
    
    bot = BasicBot(API_KEY, API_SECRET)
    bot.execute_trade()
