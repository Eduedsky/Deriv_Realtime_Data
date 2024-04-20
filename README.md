# GitHub Repository Updater Service

## Overview
This service automatically pushes log files from a server to the GitHub repository, ensuring continuous synchronization and backup of important data.

## Prerequisites
- A server with Git and Python 3.6 or later installed.
- Access to a GitHub account.
- Basic knowledge of Linux command line and Git.

## Setup Instructions

### Step 1: Install Git and Python
Ensure Git and Python are installed on your server. If not, install them using:

sudo apt update
sudo apt install git python3 python3-venv
Step 2: Generate and Add SSH Keys to GitHub
Generate an SSH Key:

ssh-keygen -t ed25519 -C "your_email@example.com"
Follow the prompts to save the key to the default SSH directory (~/.ssh).
Start the SSH Agent and Add Your SSH Key:
bash
Copy code
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
Add Your SSH Key to GitHub:
Copy your SSH public key:
bash
Copy code
cat ~/.ssh/id_ed25519.pub | clip
Go to GitHub.com, under SSH and GPG keys, click New SSH key, paste your key, and save.
Step 3: Clone the GitHub Repository
Clone the repository where you want to push the logs:

bash
Copy code
git clone git@github.com:Eduedsky/Deriv_Realtime_Data.git
cd Deriv_Realtime_Data
Step 4: Setup Working Directory
Create and configure the working directory:

bash
Copy code
mkdir -p /home/github/Deriv_Realtime_Data
cd /home/github/Deriv_Realtime_Data
This directory will be used to store and manage the files before they are pushed to GitHub.

Step 5: Python Environment Setup
Setup the Python environment within the directory:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt  # Ensure you have a requirements.txt or install necessary packages manually
Step 6: Create a Systemd Service
Create a systemd service file to automate the script execution:

bash
Copy code
sudo nano /etc/systemd/system/github_updater.service
Insert the following content:

ini
Copy code
[Unit]
Description=GitHub Repository Updater Service
After=network.target

[Service]
User=root
WorkingDirectory=/home/github/Deriv_Realtime_Data
ExecStart=/home/github/Deriv_Realtime_Data/venv/bin/python /home/github/Deriv_Realtime_Data/github_realtime_push.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
Replace paths as necessary to match your setup.

Step 7: Enable and Start the Service
Enable and start your service:

bash
Copy code
sudo systemctl daemon-reload
sudo systemctl enable github_updater.service
sudo systemctl start github_updater.service
Step 8: Monitor the Service
Check the status and monitor the logs of your service:

bash
Copy code
sudo systemctl status github_updater.service
journalctl -u github_updater.service -f
Troubleshooting
If issues arise:

Check the SSH connection to GitHub: ssh -T git@github.com
Ensure the Python script is executable and the paths in the service file are correct.
Review the logs for any error messages that might indicate what went wrong.
Conclusion
This setup ensures that your server's log files are automatically pushed to a GitHub repository, providing a reliable and automated backup solution.


### Additional Information
- **SSH Key Email**: Replace `"your_email@example.com"` with the email associated with your GitHub account.
- **Repository URL**: Ensure the repository URL in the clone command matches your actual repository URL.

This updated README provides comprehensive instructions, from initial setup and configuration to service deployment and monitoring, ensuring that users can successfully set up and maintain the GitHub Repository Updater Service.




