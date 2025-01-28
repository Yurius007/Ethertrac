from flask import Flask, render_template, request, redirect, url_for, flash
import requests
import os
from dotenv import load_dotenv
from utils.address_validator import is_address


app = Flask(__name__)

load_dotenv()

flask_secret_key = os.getenv("FLASK_SECRET_KEY")
app.secret_key = flask_secret_key

etherscan_api_key = os.getenv("ethscan_key")

etherscan_api_url = "https://api.etherscan.io/v2/api"

chains_eng = {
    "1": "Ethereum",
    "10": "Optimism",
    "8453": "Base",
    "42161": "Arbitrum One",
    "59144": "Linea",
    "324": "zkSync Era",
    "81457": "Blast",
    "534352": "Scroll",
    "42170": "Arbitrum Nova"
}

chains_img = {
    "1": "https://static.debank.com/image/chain/logo_url/eth/42ba589cd077e7bdd97db6480b0ff61d.png",
    "10": "https://static.debank.com/image/chain/logo_url/op/01ae734fe781c9c2ae6a4cc7e9244056.png",
    "8453": "https://static.debank.com/image/chain/logo_url/base/ccc1513e4f390542c4fb2f4b88ce9579.png",
    "42161": "https://static.debank.com/image/chain/logo_url/arb/854f629937ce94bebeb2cd38fb336de7.png",
    "59144": "https://static.debank.com/image/chain/logo_url/linea/32d4ff2cf92c766ace975559c232179c.png",
    "324": "https://static.debank.com/image/chain/logo_url/era/2cfcd0c8436b05d811b03935f6c1d7da.png",
    "81457": "https://static.debank.com/image/chain/logo_url/blast/15132294afd38ce980639a381ee30149.png",
    "534352": "https://static.debank.com/image/chain/logo_url/scrl/1fa5c7e0bfd353ed0a97c1476c9c42d2.png",
    "42170": "https://static.debank.com/image/chain/logo_url/nova/06eb2b7add8ba443d5b219c04089c326.png"
}

default_chain = "1"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        address = request.form.get('address', '').strip()
        if not is_address(address):
            flash("The entered address is not valid. Please check and try again.", "error")
        else:
            selected_chains = request.form.getlist('chains')
            if not selected_chains:
                selected_chains = [default_chain]
            return redirect(url_for('result', address=address, chains=",".join(selected_chains)))

    return render_template('index.html', chains=chains_eng, chains_img=chains_img, default_chain=default_chain)


@app.route('/result')
def result():
    address = request.args.get('address')
    selected_chains = request.args.get('chains', default_chain).split(',')
    results = {}

    eth_price_response = requests.get(f"{etherscan_api_url}?chainid=1&module=stats&action=ethprice&apikey={etherscan_api_key}")
    eth_price = float(eth_price_response.json().get("result", {}).get("ethusd", 0))

    for chain in selected_chains:
        tx_response = requests.get(f"{etherscan_api_url}?chainid={chain}&module=account&action=txlist&address={address}&startblock=0&endblock=99999999&sort=asc&apikey={etherscan_api_key}")
        tx_data = tx_response.json()

        if "result" in tx_data and isinstance(tx_data["result"], list) and tx_data["result"]:
            balance_response = requests.get(f"{etherscan_api_url}?chainid={chain}&module=account&action=balance&address={address}&tag=latest&apikey={etherscan_api_key}")
            wei_balance = balance_response.json().get("result", "0")
            balance_eth = int(wei_balance) / 10**18

            total_fees_eth = sum(
                int(tx.get("gasUsed", 0)) * int(tx.get("gasPrice", 0)) / 10**18
                for tx in tx_data["result"]
            )

            fees_usd_calc = total_fees_eth * eth_price
            balance_usd_calc = balance_eth * eth_price

            results[chains_eng[chain]] = {
                "balance_eth": "{:.5f}".format(balance_eth),
                "balance_usd": "{:.2f}".format(balance_usd_calc),
                "total_txs": len(tx_data["result"]),
                "fees_eth": "{:.5f}".format(total_fees_eth),
                "fees_usd": "{:.2f}".format(fees_usd_calc),
                "img_url": chains_img[chain]
            }

    return render_template('result.html', address=address, results=results, chains=chains_eng, chains_img=chains_img)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)