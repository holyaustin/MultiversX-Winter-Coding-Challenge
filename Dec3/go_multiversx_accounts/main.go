package main

import (
	"crypto/ed25519"
	"encoding/hex"
	"fmt"
	"log"

	"github.com/btcsuite/btcutil/bech32"
)

func generateAccount() (string, ed25519.PrivateKey, error) {
	// Generate a new keypair
	publicKey, privateKey, err := ed25519.GenerateKey(nil)
	if err != nil {
		return "", nil, err
	}

	// Encode the public key to Bech32 format
	publicKeyHex := hex.EncodeToString(publicKey)
	data, err := hex.DecodeString(publicKeyHex)
	if err != nil {
		log.Fatalf("hex.DecodeString error: %v", err)
	}
	converted, err := bech32.ConvertBits(data, 8, 5, true)
	if err != nil {
		return "", nil, err
	}
	address, err := bech32.Encode("erd", converted)
	if err != nil {
		return "", nil, err
	}

	return address, privateKey, nil
}

func main() {
	accounts := make(map[int][]string)

	// Generate three accounts for each shard
	for shardId := 0; shardId < 3; shardId++ {
		fmt.Printf("Creating accounts for Shard %d\n", shardId)

		for i := 0; i < 3; i++ {
			address, _, err := generateAccount()
			if err != nil {
				log.Fatalf("Error generating account: %v", err)
			}
			accounts[shardId] = append(accounts[shardId], address)
			fmt.Printf("Shard %d - Account Address: %s\n", shardId, address)
		}
	}

	// Instructions for manual token requests
	fmt.Println("\nTo request tokens, visit the appropriate MultiversX faucet:")
	fmt.Println("1. For each account, copy the Bech32-formatted address.")
	fmt.Println("2. Visit the testnet/devnet faucet page: https://docs.multiversx.com/wallet/web-wallet/#testnet-and-devnet-faucet")
	fmt.Println("3. Enter the account address and request test tokens.")
	fmt.Println("4. Gather your transaction hashes for verification.")
}
