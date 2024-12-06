import os
import sys
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization

def generate_account():
    # Generate a private key for this account
    private_key = ed25519.Ed25519PrivateKey.generate()
    
    # Generate a public key for this account
    public_key = private_key.public_key()
    
    # Convert public key to an address in a hex format
    address = public_key.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw
    ).hex()

    return address, private_key

def main():
    accounts = {}

    # Generate three accounts for each shard
    for shard_id in range(3):
        accounts[shard_id] = []
        print(f"Creating accounts for Shard {shard_id}")
        
        for _ in range(3):
            address, private_key = generate_account()
            accounts[shard_id].append((address, private_key))
            print(f"Shard {shard_id} - Account Address: {address}")

    # Instructions for requesting tokens
    print("\nTo request tokens, visit the appropriate MultiversX faucet:")
    print("1. For each account, copy the address.")
    print("2. Visit the testnet/devnet faucet page: https://docs.multiversx.com/wallet/web-wallet/#testnet-and-devnet-faucet")
    print("3. Enter the account address and request test tokens.")
    print("4. Gather your transaction hashes for verification.")

    # Note: To automate this, you would need to use HTTP requests or an SDK that interacts with the MultiversX API.
    # For example, using requests in Python could automate interaction if a stable API endpoint is available.

if __name__ == "__main__":
    main()