### Instructions for Running the Go Code

1. **Install Go**: Ensure you have Go installed. Download the latest version from the [official Go website](https://golang.org/doc/install).

2. **Set Up Go Project**:
   ```bash
   mkdir multiversx_accounts
   cd multiversx_accounts
   go mod init multiversx_accounts
   ```

3. **Install Dependencies**:
   ```bash
   go get github.com/btcsuite/btcutil/bech32
   ```

4. **Create a main.go File**: Paste the Go code provided above into a file named `main.go`.

5. **Run the Go Program**:
   ```bash
   go run main.go
   ```

This Go script should generate keypairs, convert public keys into Bech32 addresses with the "erd" prefix, and display them for token requests.