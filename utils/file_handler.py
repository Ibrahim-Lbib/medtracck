import json
import os

# Patients helper
def load_patients():
    if not os.path.exists("data/patients.json"):
        return[]
    with open("data/patients.json", 'r') as f:
        return json.load(f)
    
def save_patients(patients):
    with open("data/patients.json", 'w') as f:
        json.dump(patients, f, indent=4)
        
# Appointments helper
def load_appointments():
    if not os.path.exists("data/appointments.json"):
        return[]
    with open("data/appointments.json", 'r') as f:
        return json.load(f)
    
def save_appointments(appointments):
    with open("data/appointments.json", 'w') as f:
        json.dump(appointments, f, indent=4)
        
# Medications helper
def load_medications():
    if not os.path.exists("data/medications.json"):
        return []
    with open("data/medications.json", 'r') as f:
        return json.load(f)

def save_medications(meds):
    with open("data/medications.json", 'w') as f:
        json.dump(meds, f, indent=4)

# Payments helper
def load_payments():
    if not os.path.exists("data/payments.json"):
        return []
    with open("data/payments.json", 'r') as f:
        return json.load(f)

def save_payments(payments):
    with open("data/payments.json", 'w') as f:
        json.dump(payments, f, indent=4)

# Report helper
def count_records(file_path):
    if not os.path.exists(file_path):
        return 0
    with open(file_path, 'r') as f:
        try:
            data = json.load(f)
            return len(data)
        except json.JSONDecodeError:
            return 0

# Auth helper
def load_users():
    if not os.path.exists("data/users.json"):
        return []
    with open("data/users.json", 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_users(users):
    with open("data/users.json", 'w') as f:
        json.dump(users, f, indent=4)