#!/bin/bash

# Configuration
SCRIPT_NAME="gnss_logger.py"
DEST_DIR="/opt/gnss_logger"
SERVICE_NAME="gnss_logger.service"

# Ensure script is run as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit 1
fi

# Get the directory of the current script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Copy the script to the destination
echo "Copying script to $DEST_DIR"
mkdir -p "$DEST_DIR"
cp "$SCRIPT_DIR/$SCRIPT_NAME" "$DEST_DIR/$SCRIPT_NAME"
if [ $? -ne 0 ]; then
    echo "Failed to copy script"
    exit 1
fi

# Set correct permissions
echo "Setting permissions"
chmod +x "$DEST_DIR/$SCRIPT_NAME"

# Restart the service
echo "Restarting service"
systemctl restart "$SERVICE_NAME"
if [ $? -ne 0 ]; then
    echo "Failed to restart service"
    exit 1
fi

echo "Update completed successfully"
