# Ethertrac
![screencapture-127-0-0-1-5000-2025-01-27-13_19_57](https://github.com/user-attachments/assets/77020326-12f9-44be-a3b4-f41038fbdc7e)

## Project Description
This project allows users to input Ethereum wallet address and select specific EVM chains to retrieve related data, including balances, transaction counts, and total amount of fees spent. The results are presented in a clear format, and a pie chart visualizes fee proportions for the selected chains.

## Features
*0x8b69288becd1210e7bd1ceb9a92b4fefc1ca4bd0* - This Ethereum address will be used as an example.
1. **Simple Address Validation**:
   - Ensures the entered address follows the correct Ethereum address format.
![image](https://github.com/user-attachments/assets/4dde291d-fe4b-49f7-8029-e40bbf0db745)
   - Displays an error message for invalid addresses.
![image](https://github.com/user-attachments/assets/79d225e7-7dc5-483b-aaee-76d519cc1e9d)

2. **Blockchain Data Retrieval**:
   - Users can choose from multiple chains:
     
![image](https://github.com/user-attachments/assets/76cd1cad-45e2-48e2-87c2-5ab0530e1810)
      Ethereum ***(by default)***,
      Optimism,
      Base,
      Arbitrum One,
      Linea,
      zkSync Era,
      Blast,
      Scroll,
      Arbitrum Nova,
   - Displays balance, transaction count, and total fees for each chain.
     
![image](https://github.com/user-attachments/assets/78016117-0323-4f8a-831c-090b8088147e)
3. **Pie Chart Visualization**:
   - Represents the relationship between fees across selected chains dynamically.
     
![image](https://github.com/user-attachments/assets/875cce4a-65a4-4306-ae0a-b81a932378b8)


## Technologies Used
- **Frontend**: HTML, CSS, JavaScript ([Chart.js](https://www.chartjs.org/docs/latest/) for pie chart visualization).
- **Backend**: Python (Flask framework).
- **API**: Etherscan v2 API for blockchain data retrieval.
- **Environment Variables**: For secure storage of API keys.

## How It Works
1. **Address Input and Validation**:
   - Users input a Ethereum wallet address. (User can get this address in any Non-Custodial wallet app (such as Metamask, TrustWallet, Rabby Wallet), it usually apeears as 0x... )
   - Flask backend checks the validity of the address based on [standart requirements](https://www.geeksforgeeks.org/ethereum-address-validation-using-regular-expressions/) and displays an error if necessary.
2. **Chain Selection**:
   - Users can select one or more chains for analysis or use the "Select All" button.
3. **Data Display**:
   - Backend fetches data using Etherscan v2 API.
   - Results are displayed in cards, including balances, fees, and transaction counts.
4. **Pie Chart Generation**:
   - JavaScript uses Chart.js library to create a pie chart showing fee proportions.

## Setup Instructions
1. Initialize a virtual environment:
   ```bash
   python -m venv venv

   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
2. Clone the repository:
   ```bash
   git clone https://github.com/Yurius007/Ethertrac.git
   ```
3. Install required Python packages:
   ```bash
   cd Ethertrac
   
   pip install -r requirements.txt
   ```
4. Create a `.env` file and add your Etherscan API key and FLASK_SECRET_KEY:
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

## Docker setup instructions
1. Go to the project directory:
   ```bash
   cd Ethertrac
   ```
2. Build Docker image:
   
   ```bash
   docker build -t yurius007/ethertrac-flask:1.0.RELEASE .
   ```
   Or Pull image from Docker Hub repo:

   ```bash
   docker pull yurius007/ethertrac-flask:1.0.RELEASE
   ```
3. Create a `.env` file and add your Etherscan API key and FLASK_SECRET_KEY:
   ```
   ethscan_key=YOUR_API_KEY
   FLASK_SECRET_KEY=SECRET_KEY
   ```
   ***Instructions how to obtain those keys were mentioned in Setup Instructions #4***
3. Run the container:
   
   ```bash
   docker run -p 5000:5000 --name ethertrac-flask --env-file .env  yurius007/ethertrac-flask:1.0.RELEASE
   ```
4. Access the application at `http://127.0.0.1:5000/`.

## Notes
- The project is modular, allowing for easy addition of new chains or features.
- Simple address validation happens on the client side for better user experience.
