"""
File Operations Module
Handles data persistence for users and alerts
"""

import os
import json

DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "users.txt")
ALERTS_FILE = os.path.join(DATA_DIR, "alerts.txt")

def ensure_data_directory():
    """Create data directory if it doesn't exist"""
    os.makedirs(DATA_DIR, exist_ok=True)

def load_users():
    """Load users from file"""
    ensure_data_directory()
    users = []
    
    try:
        if os.path.exists(USERS_FILE):
            with open(USERS_FILE, 'r', encoding='utf-8') as file:
                for line in file:
                    user_data = json.loads(line.strip())
                    users.append(user_data)
    except Exception as e:
        print(f" Warning: Could not load user data: {e}")
    
    return users

def save_users(users):
    """Save users to file"""
    ensure_data_directory()
    
    try:
        with open(USERS_FILE, 'w', encoding='utf-8') as file:
            for user in users:
                file.write(json.dumps(user) + '\n')
    except Exception as e:
        print(f" Error saving user data: {e}")

def load_alerts():
    """Load alerts from file"""
    ensure_data_directory()
    alerts = []
    
    try:
        if os.path.exists(ALERTS_FILE):
            with open(ALERTS_FILE, 'r', encoding='utf-8') as file:
                for line in file:
                    alert_data = json.loads(line.strip())
                    alerts.append(alert_data)
    except Exception as e:
        print(f" Warning: Could not load alert data: {e}")
    
    return alerts

def save_alerts(alerts):
    """Save alerts to file"""
    ensure_data_directory()
    
    try:
        with open(ALERTS_FILE, 'w', encoding='utf-8') as file:
            for alert in alerts:
                file.write(json.dumps(alert) + '\n')
    except Exception as e:
        print(f" Error saving alert data: {e}")
