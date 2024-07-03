import socket
import json
import csv
from datetime import datetime, timedelta
from pathlib import Path

def connect_to_gpsd(host='localhost', port=2947):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.send(b'?WATCH={"enable":true,"json":true}\n')
    return sock

def parse_gpsd_json(data):
    try:
        json_data = json.loads(data)
        if json_data['class'] == 'TPV':
            return json_data
    except json.JSONDecodeError:
        return None
    return None

def get_output_file(start_time):
    base_dir = Path("/data/gnss")
    day_dir = base_dir / start_time.strftime('%Y%m%d')
    day_dir.mkdir(parents=True, exist_ok=True)
    filename = f"gps_data_{start_time.strftime('%Y%m%d_%H')}.csv"
    return day_dir / filename

def main():
    sock = connect_to_gpsd()
    buffer = ""
    current_file = None
    csv_writer = None
    file_start_time = None

    try:
        while True:
            current_time = datetime.now()

            if file_start_time is None or current_time - file_start_time >= timedelta(hours=1):
                if current_file:
                    current_file.close()
                file_start_time = current_time.replace(minute=0, second=0, microsecond=0)
                current_file = get_output_file(file_start_time).open('w', newline='')
                csv_writer = csv.writer(current_file)
                csv_writer.writerow(['Time', 'Latitude', 'Longitude', 'Speed (m/s)', 'Heading (degrees)', 'Altitude (m)'])

            data = sock.recv(4096).decode('utf-8')
            buffer += data
            lines = buffer.split('\n')
            
            for line in lines[:-1]:
                parsed_data = parse_gpsd_json(line)
                if parsed_data:
                    row = [
                        parsed_data.get('time', 'N/A'),
                        parsed_data.get('lat', 'N/A'),
                        parsed_data.get('lon', 'N/A'),
                        parsed_data.get('speed', 'N/A'),
                        parsed_data.get('track', 'N/A'),
                        parsed_data.get('alt', 'N/A')
                    ]
                    csv_writer.writerow(row)
                    current_file.flush()  # Ensure data is written to disk

            buffer = lines[-1]

    except KeyboardInterrupt:
        print("Stopping GPS data collection.")
    finally:
        if current_file:
            current_file.close()
        sock.close()

if __name__ == "__main__":
    main()
