echo "[i] Installing requirements..."
pip3 install -r requirements.txt

echo "[i] Setting up logs..."
mkdir logs
echo "TWILIO_ACCOUNT_SID=" > .env
echo "TWILIO_AUTH_TOKEN=" >> .env
echo "TWILIO_PHONE=" >> .env
echo "LOG_PATH=logs/log.txt" >> .env

echo "[+] Setup Complete."