from utils.file_handler import load_payments, save_payments
from datetime import datetime
from modules import patient

def add_payment():
    payments = load_payments()
    patient.load_patients()
    patient_id = input("Enter Patient ID: ")
    service = input("Service Description: ")
    amount = float(input("Amount Charged: "))
    status = input("Payment Status (paid/pending): ").lower()
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    payment = {
        "id": len(payments) + 1,
        "patient_id": patient_id,
        "service": service,
        "amount": amount,
        "status": status,
        "date": date
    }

    payments.append(payment)
    save_payments(payments)
    print(f"✅ Payment record added for Patient {patient_id}.")

def view_payments():
    payments = load_payments()
    if not payments:
        print("❌ No payments recorded.")
        return

    total_paid = 0
    total_pending = 0

    print("\n💰 Payment Records:")
    for p in payments:
        print(f"[{p['id']}] Patient: {p['patient_id']} | {p['service']} | ${p['amount']} | {p['status'].upper()} | {p['date']}")
        if p["status"] == "paid":
            total_paid += p["amount"]
        else:
            total_pending += p["amount"]

    print(f"\n📊 Total Paid: ${total_paid:.2f}")
    print(f"⏳ Total Pending: ${total_pending:.2f}")

def payment_menu():
    while True:
        print("\n💵 Payment Menu")
        print("1. Add Payment")
        print("2. View All Payments")
        print("0. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            add_payment()
        elif choice == "2":
            view_payments()
        elif choice == "0":
            break
        else:
            print("❌ Invalid option.")