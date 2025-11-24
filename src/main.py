"""
Neighborhood Alert System
Main Program File
Developer: [Your Name]
ID: [Your ID]
Course: Problem Solving and Programming
Date: [Current Date]
"""

from alert_manager import *
from user_manager import *
from file_operations import *

def display_main_menu():
    """Display the main navigation menu"""
    print("\n" + "="*60)
    print("              NEIGHBORHOOD ALERT SYSTEM")
    print("="*60)
    print("1.   User Login")
    print("2.   User Registration")
    print("3.   View All Alerts (Public)")
    print("4.   Exit System")
    print("="*60)

def display_user_menu(current_user):
    """Display menu for logged-in users"""
    print(f"\n" + "="*50)
    print(f"Welcome, {current_user['name']}!")
    print("="*50)
    print("1.   Post New Alert")
    print("2.   View All Alerts")
    print("3.   Search Alerts")
    print("4.   View My Alerts")
    print("5.   Change My Location")
    print("6.   Logout")
    print("="*50)

def main():
    """Main program function"""
    users = load_users()
    alerts = load_alerts()
    current_user = None
    
    print("  Welcome to Neighborhood Alert System!")
    print("  Connecting communities, one alert at a time...")
    
    while True:
        if not current_user:
            # Main menu for non-logged in users
            display_main_menu()
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice == '1':
                current_user = user_login(users)
            elif choice == '2':
                if register_user(users):
                    save_users(users)
                    print("Registration successful! Please login.")
            elif choice == '3':
                view_all_alerts(alerts, public=True)
            elif choice == '4':
                save_users(users)
                save_alerts(alerts)
                print("Thank you for using Neighborhood Alert System! Stay safe!")
                break
            else:
                print("Invalid choice! Please try again.")
        else:
            # User menu for logged-in users
            display_user_menu(current_user)
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == '1':
                if post_new_alert(alerts, current_user):
                    save_alerts(alerts)
            elif choice == '2':
                view_all_alerts(alerts)
            elif choice == '3':
                search_alerts(alerts)
            elif choice == '4':
                view_user_alerts(alerts, current_user)
            elif choice == '5':
                if update_user_location(users, current_user):
                    save_users(users)
            elif choice == '6':
                print(f"Goodbye, {current_user['name']}!")
                current_user = None
            else:
                print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
