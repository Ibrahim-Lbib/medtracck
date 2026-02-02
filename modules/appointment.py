from datetime import datetime
from utils.file_handler import load_appointments, save_appointments
        
def book_appointment():
    appointments = load_appointments()
    patient_name = input("Patient name: ")
    doctor = input("Doctor's name: ")
    date = input("Date (YYYY-MM-DD): ")
    time = input("Time (HH:MM): ")
    appointment_id = len(appointments) + 1
    
    new_appointment = {
        "id": appointment_id,
        "patient_name": patient_name,
        "doctor": doctor,
        "date": date,
        "time": time
    }
    
    appointments.append(new_appointment)
    save_appointments(appointments)
    print(f"✅ Appointment booked for {patient_name} with Dr. {doctor} on {date} at {time}.")
    
def view_today_appointments():
    appointments = load_appointments()
    today = datetime.now().strftime("%Y-%m-%d")
    today_appointments = [a for a in appointments if a["date"] == today]
    if not today_appointments:
        print("📭 No appointments for today.")
        return
    print(f"\n📆 Appointmenst for {today}")
    for a  in appointments:
        print(f"[{a['id']}] {a['time']} - {a['patient_name']} with Dr. {a['doctor']}")
        
def cancel_appointment():
    appointments = load_appointments()
    view_today_appointments()
    try: 
        appt_id = int(input("Enter appointment ID to cancel: "))
    except ValueError:
        print("❌ Invalid ID.")
        return
    updated = [a for a in appointments if a ["id"] != appt_id] 
    if len(updated) == len(appointments):
        print("❌ Appointment not found.")
        return 
    save_appointments(updated)
    print("❌ Appointment canceled.")
    
def reschedule_appointment():
    appointments = load_appointments()
    view_today_appointments()
    try:
        appt_id = int(input("Enter appointment ID to reschedule: "))
    except ValueError:
        print("❌ Invalid ID.")
        return
    
    for appt in appointments:
        if appt["id"] == appt_id:
            new_date = input("New date (YYYY-MM-DD): ")
            new_time = input("New time (HH:MM): ")
            appt["date"] = new_date
            appt["time"] = new_time 
            
            save_appointments(appointments)
            print("♻ Appointment reschedule.")
            return
    print("❌ Appointment not found.") 
    
def appointment_menu():
    while True:
        print("\n📆 Appointment Menu")
        print("1. Book Appointment")
        print("2. View Today's Appointments")
        print("3. Cancel Appointment")
        print("4. Reschedule Appointment")
        print("0. Back to Main Menu")
        choice = input("Choose an option: ")
        
        if choice == "1":
            book_appointment()
        elif choice == "2":
            view_today_appointments()
        elif choice == "3":
            cancel_appointment()
        elif choice == "4":
            reschedule_appointment()
        elif choice == "0":
            break
        else:
            print("❌ Invalid option.")