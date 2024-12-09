import json
import base64
from solana.publickey import PublicKey
from solana.keypair import Keypair
from solana.rpc.api import Client
from solana.transaction import Transaction
import requests

RPC_URL = "https://api.mainnet-beta.solana.com"
JUPITER_PRICE_API = "https://quote-api.jup.ag/v1/price?ids=SOL"
TOKEN_LIST_URL = "https://token-list.solana.com/solana.tokenlist.json"
PRIVATE_KEY_FILE = "private_key.txt"


def get_private_key():
    """Load private key from a file in array format and return a Keypair."""
    with open(PRIVATE_KEY_FILE, "r") as f:
        private_key_array = json.load(f)
    private_key_bytes = bytes(private_key_array)
    return Keypair.from_secret_key(private_key_bytes)


def get_last_price():
    """Fetch the last price of SOL from the Jupiter API."""
    response = requests.get(JUPITER_PRICE_API)
    response.raise_for_status()
    data = response.json()
    return data['SOL']['price']


def get_token_addresses():
    """Fetch the token list and return SOL and USDC token addresses."""
    response = requests.get(TOKEN_LIST_URL)
    response.raise_for_status()
    token_list = response.json()["tokens"]
    sol_token = next(token for token in token_list if token["symbol"] == "SOL")
    usdc_token = next(token for token in token_list if token["symbol"] == "USDC")
    return PublicKey(sol_token["address"]), PublicKey(usdc_token["address"])


def place_limit_order(wallet, side, amount, price, connection):
    """
    Placeholder function to execute a limit order.
    This requires Jupiter SDK integration, which is not available in Python.
    """
    print(f"Placing {side} order for {amount / 1e9} SOL at {price} USDC")
    # Jupiter trading functionality would go here
    pass


def main():
    # Initialize Solana connection
    connection = Client(RPC_URL)

    # Load private key and wallet
    wallet = get_private_key()

    # Get last price of SOL
    last_price = get_last_price()
    print(f"Last price of SOL: {last_price} USDC")

    # Fetch token addresses
    sol_address, usdc_address = get_token_addresses()

    # Define base amount (1 SOL in lamports)
    base_amount = 1 * 10**9

    # Place a buy order 1% below the last price
    buy_price = last_price * 0.99
    place_limit_order(wallet, "buy", base_amount, buy_price, connection)

    # Place a sell order 1% above the last price
    sell_price = last_price * 1.01
    place_limit_order(wallet, "sell", base_amount, sell_price, connection)


if __name__ == "__main__":
    main()
