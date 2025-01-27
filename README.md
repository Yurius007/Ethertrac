# Ethertrac

## Project Description
This project allows users to input Ethereum wallet address and select specific EVM chains to retrieve related data, including balances, transaction counts, and total amount of fees spent. The results are presented in a clear format, and a pie chart visualizes fee proportions for the selected chains.

## Features
1. **Simple Address Validation**:
   - Ensures the entered address follows the correct Ethereum address format.
   - Displays an error message for invalid addresses.
2. **Blockchain Data Retrieval**:
   - Users can choose from multiple chains:
     - Ethereum ***(by default)***
     - Optimism
     - Base
     - Arbitrum One
     - Linea
     - zkSync Era
     - Blast
     - Scroll
     - Arbitrum Nova
   - Displays balance, transaction count, and total fees for each chain.
3. **Pie Chart Visualization**:
   - Represents the relationship between fees across selected chains dynamically.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript ([Chart.js](https://www.chartjs.org/docs/latest/) for pie chart visualization).
- **Backend**: Python (Flask framework).
- **API**: Etherscan v2 API for blockchain data retrieval.
- **Environment Variables**: For secure storage of API keys.

## How It Works
1. **Address Input and Validation**:
   - Users input a Ethereum wallet address.
   - Flask backend checks the validity of the address based on [standart requirements](https://www.geeksforgeeks.org/ethereum-address-validation-using-regular-expressions/) and displays an error if necessary.
2. **Chain Selection**:
   - Users can select one or more chains for analysis or use the "Select All" button.
3. **Data Display**:
   - Backend fetches data using Etherscan v2 API.
   - Results are displayed in cards, including balances, fees, and transaction counts.
4. **Pie Chart Generation**:
   - JavaScript uses Chart.js library to create a pie chart showing fee proportions.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Yurius007/Ethertrac.git
   ```
2. Install required Python packages:
   ```bash
   pip install -r Ethertrac/requirements.txt
   ```
3. Create a `.env` file and add your Etherscan API key and FLASK_SECRET_KEY:
   ```
   ethscan_key=YOUR_API_KEY
   FLASK_SECRET_KEY=SECRET_KEY
   ```
   - Etherscan api key can be obtained via [Etherscan page](https://etherscan.io/apis) (authorisation required).
   - Flask secret key is a thing which Flask framework requires for any security related needs. It could be any long random string, you can run this command to get one:
   ```bash
   python -c 'import secrets; print(secrets.token_hex())'
   ```
5. Run the application:
   ```bash
   flask --app app run
   ```
6. Access the application at `http://127.0.0.1:5000/`.

## Notes
- The project is modular, allowing for easy addition of new chains or features.
- Simple address validation happens on the client side for better user experience.
