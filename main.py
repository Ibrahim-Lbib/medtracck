# Main Menu Loop
from modules import patient, appointment, medication, payment, report, auth
                
def main():
    auth.ensure_admin_exists()   

    if not auth.login():
                exit()
    
    while True:
        print("\n🏥 MEDTRACK SYSTEM")
        print("1. Patient")
        print("2. Appointments")
        print("3. Medications")
        print("4. Payments")
        print("5. Reports")
        print("6. Register New User(Admin Only)")
        print("0. Exit")
        choice = input("Select an option: ")
        
        if choice == "1":
            patient.patient_menu() 
        elif choice == "2":
            appointment.appointment_menu()     
        elif choice =="3":
            medication.medication_menu()      
        elif choice =="4":
            payment.payment_menu()      
        elif choice =="5":
            report.report_menu()      
        elif choice =="6":
            auth.register()      
        elif choice == "0":
            print("Exiting MedTrack. Stay healthy!")
            break         
        else: 
            print("❌ Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()