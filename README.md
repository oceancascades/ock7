# ock7

GMKTek K7 minipc for logging and at sea processing.

This computer is configured as a Jupyter Hub server using 'The Littlest Jupyter Hub'

## GNSS logger config

### 1. Save the Python Script

Save your Python script in a suitable location, for example:
```
/opt/gnss_logger/gnss_logger.py
```

### 2. Make the Script Executable

```bash
sudo chmod +x /opt/gnss_logger/gnss_logger.py
```

### 3. Create a Systemd Service File

```bash
sudo nano /etc/systemd/system/gnss_logger.service
```

### 4. Add Content to the Service File

Add the following content to the service file:

```ini
[Unit]
Description=GNSS Logger Service
After=network.target gpsd.service

[Service]
ExecStart=/usr/bin/python3 /opt/gnss_logger/gnss_logger.py
Restart=always
User=root
Group=root
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
```

> **Note:** We're running this as root to ensure it has permission to write to `/data/gnss`. If you prefer, you can create a specific user for this service and give that user write permissions to the directory.

### 5. Save and Close the File

In nano, press `Ctrl+X`, then `Y`, then `Enter`.

### 6. Reload Systemd Manager Configuration

```bash
sudo systemctl daemon-reload
```

### 7. Enable the Service to Start on Boot

```bash
sudo systemctl enable gnss_logger.service
```

### 8. Start the Service

```bash
sudo systemctl start gnss_logger.service
```

### 9. Check the Status of the Service

```bash
sudo systemctl status gnss_logger.service
```

### Additional Commands

- To stop the service: 
  ```bash
  sudo systemctl stop gnss_logger.service
  ```
- To restart the service: 
  ```bash
  sudo systemctl restart gnss_logger.service
  ```
- To view the logs: 
  ```bash
  sudo journalctl -u gnss_logger.service
  ```

### Important Notes

Ensure that:
- Python 3 is installed on your system
- The gpsd service is installed and configured correctly
- The directory `/data/gnss` exists and has the correct permissions

If you make changes to the script later, remember to restart the service for the changes to take effect.
