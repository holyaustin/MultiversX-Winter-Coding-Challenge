# Python Account Generation 3 - shards -  3 Accounts

### Instructions for Execution on Ubuntu

1. **Install Python**: Ensure Python3 is installed.
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```
1b. Create virtual enviromental virable (.venv)before the next step

- pip install virtualenv   // install virtual enviroment
- python3.12 -m venv .venv  create virtual enviroment
- source env/bin/activate   // activate virtual enviroment
- pip list   // check that your virtual enviroment is working

2. **Install Necessary Libraries**: Use pip to install required packages.
   ```bash
   pip3 install cryptography bech32
   ```

3. **Save the Script**: Create a file named `generate_accounts.py` and paste the updated script content into the file.

4. **Execute the Script**: Run the script using Python3.
   ```bash
   python3 generate_accounts.py
   ```

5. **Manual Token Request**:
   - After running the script, copy the printed Bech32-formatted addresses.
   - Navigate to the [MultiversX Faucet](https://docs.multiversx.com/wallet/web-wallet/#testnet-and-devnet-faucet) page.
   - Input each account address in the faucet to request test tokens.
   - Note down transaction hashes for each request for verification.


### Notes

- **Bech32 Address**: The Bech32 encoding used in this script ensures that the generated addresses start with the `erd1` prefix, matching the MultiversX format.
- **Security**: Ensure that private keys are handled securely if these accounts are used beyond testing.
- **Automated Token Request**: Implementing automated token requests would require additional scripting, potentially involving API interactions with the MultiversX blockchain services (if applicable).

By following these steps, the updated Python script will generate MultiversX-compatible addresses, which start with the "erd1" prefix, ready for requesting test tokens from the faucet.