echo "[i] Installing requirements..."
pip3 install -r requirements.txt

echo "[i] Setting up logs..."
mkdir logs
echo "ACCOUNT_SID=" > .env
echo "AUTH_TOKEN=" >> .env
echo "PHONE=" >> .env
echo "LOG_PATH=logs/log.txt" >> .env

