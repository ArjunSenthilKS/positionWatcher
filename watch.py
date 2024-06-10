import solana
from requests import post


from solana.rpc.api import Client, Pubkey
from spl.token._layouts import MINT_LAYOUT
from spl.token.constants import TOKEN_PROGRAM_ID
from solana.rpc.types import TokenAccountOpts

#all key declarations
public_key = Pubkey.from_string("GABaPA9T4rJxfKQ21khm6gyY8F4bmeJn6wAc3VsyBDV9")
mainnet_url = "https://api.mainnet-beta.solana.com"
headers = {
    "accept": "application/json", 
    "content-type": "application/json"
    }
client = Client(mainnet_url)


#obtaining token
response = client.get_token_accounts_by_owner(
    public_key,
    TokenAccountOpts(program_id=TOKEN_PROGRAM_ID)
)


# Check for errors in the response
if response:
    token_accounts = response.value
    for account in token_accounts:
        account_pubkey = account.pub
        account_info = client.get_token_account_balance(Pubkey.from_string(account_pubkey))
        token_amount = account_info['result']['value']['amount']
        print(f"Token account {account_pubkey}: {token_amount}")
else:
    print(f"Error fetching token accounts: {response['error']}")





















"""
#getting solana balance
payload = {
    "jsonrpc": "2.0", 
    "id": 1, 
    "method": "getBalance", 
    "params": ["GABaPA9T4rJxfKQ21khm6gyY8F4bmeJn6wAc3VsyBDV9"]
    }
balance_rpc = post(mainnet_url, json=payload).json()['result']['value']
result = balance_rpc/1_000_000_000
print(f"Solana balance: {result}")


#getting someother spl token balance
payload = {
    "jsonrpc": "2.0", 
    "id": 1, 
    "method": "getTokenAccountsByOwner", 
    "params": [
        "GABaPA9T4rJxfKQ21khm6gyY8F4bmeJn6wAc3VsyBDV9",
        {"mint": "3S8qX1MsMqRbiwKg2cQyx7nis1oHMgaCuc9c4VfvVdPN"},
        {"encoding": "jsonParsed"},
    ],
    }
balance_rpc = post(mainnet_url, json=payload, headers=headers).json()

print(f"Solana balance: {balance_rpc}")
"""