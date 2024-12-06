import os
from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization
import bech32

def generate_account():
    # Generate a private key for this account
    private_key = ed25519.Ed25519PrivateKey.generate()

    # Generate a public key for this account
    public_key = private_key.public_key()

    # Convert public key to bytes
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw
    )

    # Encode the public key to Bech32 format
    public_key_base32 = bech32.convertbits(public_key_bytes, 8, 5)
    address = bech32.bech32_encode("erd", public_key_base32)

    return address, private_key

def main():
    accounts = []

    # Generate three accounts for each shard
    for shard_id in range(3):
        print(f"Creating accounts for Shard {shard_id}")

        for _ in range(3):
            address, private_key = generate_account()
            accounts.append((shard_id, address, private_key))
            print(f"Shard {shard_id} - Account Address: {address}")

    # Instructions for requesting tokens
    print("\nTo request tokens, visit the appropriate MultiversX faucet:")
    print("1. For each account, copy the Bech32-formatted address.")
    print("2. Visit the testnet/devnet faucet page: https://docs.multiversx.com/wallet/web-wallet/#testnet-and-devnet-faucet")
    print("3. Enter the account address and request test tokens.")
    print("4. Gather your transaction hashes for verification.")

if __name__ == "__main__":
    main()