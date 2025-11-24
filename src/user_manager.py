"""
User Management Module
Handles user registration, login, and profile management
"""

def register_user(users):
    """Register a new user in the system"""
    print("\n---  USER REGISTRATION ---")
    
    try:
        name = input("Enter your full name: ").strip()
        if not name:
            print(" Name cannot be empty!")
            return False
        
        username = input("Choose a username: ").strip().lower()
        if not username:
            print(" Username cannot be empty!")
            return False
        
        # Check if username already exists
        for user in users:
            if user['username'] == username:
                print(" Username already exists! Please choose another.")
                return False
        
        password = input("Choose a password: ").strip()
        if len(password) < 4:
            print(" Password must be at least 4 characters!")
            return False
        
        location = input("Enter your neighborhood/location: ").strip()
        if not location:
            print(" Location cannot be empty!")
            return False
        
        phone = input("Enter your phone number (optional): ").strip()
        
        user = {
            'name': name,
            'username': username,
            'password': password,  # In real system, this would be hashed
            'location': location,
            'phone': phone,
            'registration_date': get_current_date()
        }
        
        users.append(user)
        print(f" Registration successful! Welcome to the community, {name}!")
        return True
        
    except Exception as e:
        print(f" Error during registration: {e}")
        return False

def user_login(users):
    """Authenticate and login a user"""
    print("\n---  USER LOGIN ---")
    
    if not users:
        print(" No users registered yet! Please register first.")
        return None
    
    username = input("Username: ").strip().lower()
    password = input("Password: ").strip()
    
    for user in users:
        if user['username'] == username and user['password'] == password:
            print(f" Login successful! Welcome back, {user['name']}!")
            return user
    
    print(" Invalid username or password!")
    return None

def update_user_location(users, current_user):
    """Update user's location/neighborhood"""
    print("\n---  UPDATE LOCATION ---")
    
    new_location = input("Enter your new neighborhood/location: ").strip()
    if not new_location:
        print(" Location cannot be empty!")
        return False
    
    for user in users:
        if user['username'] == current_user['username']:
            old_location = user['location']
            user['location'] = new_location
            current_user['location'] = new_location
            print(f" Location updated from '{old_location}' to '{new_location}'!")
            return True
    
    return False

def get_current_date():
    """Get current date in readable format"""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
