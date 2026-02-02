from utils.file_handler import count_records, load_payments

def generate_report():
    print("\n📊 Clinic Report Summary\n")

    num_patients = count_records('data/patients.json')
    num_appointments = count_records('data/appointments.json')
    num_medications = count_records('data/medications.json')
    payments = load_payments()

    total_paid = sum(p["amount"] for p in payments if p["status"] == "paid")
    total_pending = sum(p["amount"] for p in payments if p["status"] == "pending")

    print(f"👥 Total Patients: {num_patients}")
    print(f"📅 Total Appointments: {num_appointments}")
    print(f"💊 Medications Issued: {num_medications}")
    print(f"💰 Total Paid: ${total_paid:.2f}")
    print(f"⏳ Total Pending: ${total_pending:.2f}")
    print(f"🧾 Total Income (Expected): ${total_paid + total_pending:.2f}")

def report_menu():
    while True:
        print("\n📊 Reports Menu")
        print("1. View Report Summary")
        print("0. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            generate_report()
        elif choice == "0":
            break
        else:
            print("Invalid option.")