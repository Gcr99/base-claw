import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

w3 = Web3(Web3.HTTPProvider(os.getenv("BASE_RPC_URL")))

def get_base_balance(wallet_address: str) -> str:
    try:
        balance = w3.eth.get_balance(wallet_address)
        return f"Saldo: {w3.from_wei(balance, 'ether')} ETH"
    except Exception as e:
        return f"Error: {str(e)}"

def get_latest_block() -> str:
    try:
        return f"Block terbaru: {w3.eth.block_number}"
    except Exception as e:
        return f"Error: {str(e)}"

AVAILABLE_TOOLS = {
    "get_base_balance": get_base_balance,
    "get_latest_block": get_latest_block
}
