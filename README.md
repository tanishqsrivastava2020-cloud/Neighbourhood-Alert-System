## Neighbourhood-Alert-System
College VITyarthi project of Introduction to Problem Solving and Programming on Neighbourhood Alert System

## Problem Statement
Communities lack efficient communication channels for sharing urgent local information, leading to delayed responses during emergencies and poor community coordination.

## Solution
A console-based alert system that allows residents to post, view, and manage neighborhood alerts for emergencies, events, and important information.

## Features
- User registration and authentication
- Post different types of alerts (Emergency, Information, Event)
- View alerts by category and urgency
- Search and filter alerts
- Location-based alert organization
- Alert status tracking

## Technology Stack
- Programming Language: Python
- Data Storage: Text files
- No external dependencies

## Installation & Setup
1. Ensure Python 3.6+ is installed
2. Download all project files
3. Run: `python src/main.py`

## Usage
1. Register as a new user or login
2. Choose from menu options to post/view alerts
3. Emergency alerts are highlighted for quick attention
4. Alerts are saved and persist between sessions

## Alert Categories
-  EMERGENCY (Power outage, safety issues)
-  INFORMATION (Community news, updates)
-  EVENT (Local events, meetings)
-  MAINTENANCE (Road work, utilities)

## Project Structure
- `main.py` - Application entry point
- `alert_manager.py` - Alert handling logic
- `user_manager.py` - User authentication
- `file_operations.py` - Data persistence

## Future Enhancements
- Mobile app interface
- Push notifications
- GPS integration
- Multimedia support
- Admin moderation panel
