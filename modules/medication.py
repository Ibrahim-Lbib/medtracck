from utils.file_handler import load_medications, save_medications

def add_medication():
    meds = load_medications()
    name = input("Medication name: ")
    dosage = input("Dosage (e.g. 500mg): ")
    quantity = int(input("Stock quantity: "))
    med_id = len(meds) + 1

    new_med = {
        "id": med_id,
        "name": name,
        "dosage": dosage,
        "stock": quantity
    }

    meds.append(new_med)
    save_medications(meds)
    print(f"✅ {name} added with {quantity} units.")

def view_medications():
    meds = load_medications()
    if not meds:
        print("❌ No medications in stock.")
        return

    print("\n💊 Medication Inventory:")
    for m in meds:
        stock_status = "⚠️ Low" if m["stock"] <= 5 else "✅"
        print(f"[{m['id']}] {m['name']} - {m['dosage']} - Stock: {m['stock']} {stock_status}")

def prescribe_medication():
    meds = load_medications()
    view_medications()

    try:
        med_id = int(input("Enter medication ID to prescribe: "))
        quantity = int(input("Enter quantity to prescribe: "))
    except ValueError:
        print("❌ Invalid input.")
        return

    for med in meds:
        if med["id"] == med_id:
            if med["stock"] < quantity:
                print("❌ Not enough stock.")
                return
            med["stock"] -= quantity
            save_medications(meds)
            print(f"✅ Prescribed {quantity} units of {med['name']}. Remaining: {med['stock']}")
            return

    print("❌ Medication not found.")

def medication_menu():
    while True:
        print("\n💊 Medication Menu")
        print("1. Add Medication")
        print("2. View Inventory")
        print("3. Prescribe Medication")
        print("0. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == "1":
            add_medication()
        elif choice == "2":
            view_medications()
        elif choice == "3":
            prescribe_medication()
        elif choice == "0":
            break
        else:
            print("❌ Invalid option.")