import subprocess
import csv
import requests
from datetime import datetime
from gpiozero import LED
import time

# LED qui indique la connexion 
led = LED(17)


def connect_to_wifi(ssid, password):
    print("Connecting to Wi-Fi...")
    led.off()  

    time.sleep(5)

    if "connected":  
        print("Wi-Fi connected!")
        led.on()  
    else:
        print("Failed to connect to Wi-Fi.")

# Fonction qui capture le traffic reseau par tcpdump
def capture_traffic(interface, pcap_file):
    command = ["sudo", "tcpdump", "-i", interface, "-w", pcap_file]
    process = subprocess.Popen(command)
    return process

# PCAP to CSV file
def pcap_to_csv(pcap_file, csv_file):
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Timestamp', 'Source IP', 'Destination IP', 'Protocol', 'Length'])
        command = ["tcpdump", "-r", pcap_file, "-nn", "-tttt"]
        process = subprocess.Popen(command, stdout=subprocess.PIPE)
        for line in process.stdout:
            line = line.decode("utf-8").strip()
            parts = line.split(' ')
            if len(parts) >= 7 and parts[1] != 'IP':
                timestamp = parts[0]
                source_ip = parts[2]
                destination_ip = parts[4]
                protocol = parts[5]
                length = parts[-1]
                writer.writerow([timestamp, source_ip, destination_ip, protocol, length])

# envoyer le CSV to web API
def send_to_api(csv_file, api_url):
    with open(csv_file, 'rb') as file:
        files = {'file': file}
        response = requests.post(api_url, files=files)
        return response


def main():
    wifi_ssid = "your_wifi_ssid"
    wifi_password = "your_wifi_password"
    interface = "eth0"  
    pcap_file = "network_traffic.pcap"
    csv_file = "network_traffic.csv"
    api_url = "http://localhost/create/{id}"  

    try:

        connect_to_wifi(wifi_ssid, wifi_password)

        # Capture le traffic du reseau
        print("Capturing network traffic. Press Ctrl+C to stop.")
        capture_process = capture_traffic(interface, pcap_file)
        capture_process.wait()

        print("Converting PCAP file to CSV...")
        pcap_to_csv(pcap_file, csv_file)

        print("Conversion complete. Sending CSV file to API...")

        response = send_to_api(csv_file, api_url)

        print("Response from API:", response.status_code)
        print("CSV file sent successfully.")

    except KeyboardInterrupt:

        print("\nKeyboardInterrupt detected. Stopping capture.")
        capture_process.terminate()

if _name_ == "_main_":
    main()