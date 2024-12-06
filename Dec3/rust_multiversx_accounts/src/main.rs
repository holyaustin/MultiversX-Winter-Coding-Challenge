extern crate rand;
extern crate ed25519_dalek;
extern crate bech32;

use rand::rngs::OsRng;
use ed25519_dalek::Keypair;
use bech32::{ToBase32, encode};
use bech32::Variant;

fn generate_account() -> Result<(String, Keypair), bech32::Error> {
    // Generate a keypair
    let mut csprng = OsRng {};
    let keypair: Keypair = Keypair::generate(&mut csprng);

    // Encode the public key to Bech32 format
    let public_key_bytes = keypair.public.to_bytes();
    let public_key_base32 = public_key_bytes.to_base32();
    let address = encode("erd", public_key_base32, Variant::Bech32)?;

    Ok((address, keypair))
}

fn main() {
    // Storing the account details
    let mut accounts = vec![];

    // Generate three accounts for each shard
    for shard_id in 0..3 {
        println!("Creating accounts for Shard {}", shard_id);

        for _ in 0..3 {
            match generate_account() {
                Ok((address, keypair)) => {
                    accounts.push((shard_id, address.clone(), keypair));
                    println!("Shard {} - Account Address: {}", shard_id, address);
                },
                Err(err) => {
                    println!("Error generating account: {}", err);
                }
            }
        }
    }

    // Instructions for manual token requests
    println!("\nTo request tokens, visit the appropriate MultiversX faucet:");
    println!("1. For each account, copy the Bech32-formatted address.");
    println!("2. Visit the testnet/devnet faucet page: https://docs.multiversx.com/wallet/web-wallet/#testnet-and-devnet-faucet");
    println!("3. Enter the account address and request test tokens.");
    println!("4. Gather your transaction hashes for verification.");
}