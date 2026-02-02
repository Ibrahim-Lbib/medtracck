from utils.file_handler import load_patients, save_patients
        
def add_patient():
    patients = load_patients()
    name = input("Patient name: ")
    age = input("Age: ")
    contact = input("Contact: ")
    illness = input("Illness: ")
    patient_id = len(patients) + 1
    
    new_patient = {
        "id": patient_id,
        "name": name,
        "age": age,
        "contact": contact,
        "illness": illness
    }
    
    patients.append(new_patient)
    save_patients(patients)
    print(f"✅ Patient {name} added successfully.")
    
def view_patients():
    patients = load_patients()
    if not patients:
        print("No patients found.")
        return
    for p  in patients:
        print(f"[{p['id']}] {p['name']} - Age {p['age']} - Illness: {p['illness']}")
        
def patient_menu():
    while True:
        print("\n👤 Patient Menu")
        print("1. Add Patient")
        print("2. View Patients")
        print("0. Back to Main Menu")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "0":
            break
        else:
            print("❌ Invalid option.")