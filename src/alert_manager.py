"""
Alert Management Module
Handles all alert-related operations
"""

def post_new_alert(alerts, current_user):
    """Create and post a new alert"""
    print("\n---  POST NEW ALERT ---")
    
    try:
        # Alert type selection
        print("\nSelect Alert Type:")
        print("1.  EMERGENCY (Power outage, safety issues)")
        print("2.  INFORMATION (Community news, updates)")
        print("3.  EVENT (Local events, meetings)")
        print("4.  MAINTENANCE (Road work, utilities)")
        
        type_choice = input("Enter type (1-4): ").strip()
        alert_types = {
            '1': {'name': 'EMERGENCY'},
            '2': {'name': 'INFORMATION'},
            '3': {'name': 'EVENT'},
            '4': {'name': 'MAINTENANCE'}
        }
        
        if type_choice not in alert_types:
            print(" Invalid alert type!")
            return False
        
        alert_type = alert_types[type_choice]
        
        # Get alert details
        title = input("Enter alert title: ").strip()
        if not title:
            print(" Title cannot be empty!")
            return False
        
        description = input("Enter alert description: ").strip()
        if not description:
            print(" Description cannot be empty!")
            return False
        
        location = input(f"Enter location (default: {current_user['location']}): ").strip()
        if not location:
            location = current_user['location']
        
        urgency = "HIGH" if type_choice == '1' else "MEDIUM"
        
        alert = {
            'id': len(alerts) + 1,
            'title': title,
            'description': description,
            'type': alert_type['name'],
            'icon': alert_type['icon'],
            'location': location,
            'posted_by': current_user['username'],
            'poster_name': current_user['name'],
            'urgency': urgency,
            'timestamp': get_current_date(),
            'status': 'ACTIVE'
        }
        
        alerts.append(alert)
        print(f"  Alert posted successfully! {alert_type['icon']} {alert_type['name']} alert added.")
        return True
        
    except Exception as e:
        print(f" Error posting alert: {e}")
        return False

def view_all_alerts(alerts, public=False):
    """Display all alerts in the system"""
    print(f"\n--- {'  ALL ALERTS' if not public else '👀 PUBLIC ALERTS'} ---")
    
    if not alerts:
        print("  No alerts posted yet.")
        return
    
    # Sort alerts: emergencies first, then by timestamp
    sorted_alerts = sorted(alerts, 
                         key=lambda x: (0 if x['urgency'] == 'HIGH' else 1, x['timestamp']),
                         reverse=True)
    
    for alert in sorted_alerts:
        print(f"\n{alert['icon']} {alert['type']} - {alert['title']}")
        print(f"    Location: {alert['location']}")
        print(f"    Description: {alert['description']}")
        if not public:
            print(f"    Posted by: {alert['poster_name']}")
        print(f"     Time: {alert['timestamp']}")
        print(f"     Status: {alert['status']}")
        print("   " + "-" * 40)

def search_alerts(alerts):
    """Search alerts by keyword or location"""
    print("\n---   SEARCH ALERTS ---")
    
    if not alerts:
        print("  No alerts to search.")
        return
    
    search_term = input("Enter search term (title, location, or type): ").strip().lower()
    if not search_term:
        print("  Please enter a search term!")
        return
    
    found_alerts = []
    for alert in alerts:
        if (search_term in alert['title'].lower() or 
            search_term in alert['location'].lower() or 
            search_term in alert['type'].lower() or
            search_term in alert['description'].lower()):
            found_alerts.append(alert)
    
    if found_alerts:
        print(f"\n  Found {len(found_alerts)} alert(s) matching '{search_term}':")
        for alert in found_alerts:
            print(f"\n{alert['icon']} {alert['type']} - {alert['title']}")
            print(f"     {alert['location']} |   {alert['timestamp']}")
    else:
        print(f"  No alerts found matching '{search_term}'.")

def view_user_alerts(alerts, current_user):
    """Display alerts posted by the current user"""
    print(f"\n---  MY ALERTS ---")
    
    user_alerts = [alert for alert in alerts if alert['posted_by'] == current_user['username']]
    
    if not user_alerts:
        print(" You haven't posted any alerts yet.")
        return
    
    print(f"You have posted {len(user_alerts)} alert(s):")
    for alert in user_alerts:
        print(f"\n{alert['icon']} {alert['type']} - {alert['title']}")
        print(f"     Location: {alert['location']}")
        print(f"     Description: {alert['description']}")
        print(f"     Time: {alert['timestamp']}")
        print(f"     Status: {alert['status']}")

def get_current_date():
    """Get current date in readable format"""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
