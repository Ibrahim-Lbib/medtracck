# 🏥 MedTrack — Clinic & Patient Record System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)
![CLI](https://img.shields.io/badge/Interface-Terminal-lightgrey)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Author](https://img.shields.io/badge/Author-Ibrahim%20Labib-black)


> A simple, terminal-based clinic management system built with Python.  
> Helps small clinics manage patients, appointments, medications, payments and reports.

---

## 🚀 Key Features

- 🔐 **Login & Authentication** (secure access)
- 👤 Patient record management
- 📅 Appointment scheduling
- 💊 Medication inventory & prescriptions
- 💵 Payment tracking (paid & pending)
- 📊 Daily reports & financial summaries

---

## 📦 Tech Stack

- **Python 3.8+**
- JSON file storage (no database required)
- Modular code structure

---

## 📁 Folder Structure

```

medtrack/
├── main.py
├── README.md
├── data/
│   ├── patients.json
│   ├── appointments.json
│   ├── medications.json
│   ├── payments.json
│   └── users.json
└── modules/
├── auth.py
├── patient.py
├── appointment.py
├── medication.py
├── payment.py
└── report.py

````

---

## 🛠️ Quick Start

**1. Clone the repo**
```bash
git clone https://github.com/<your-username>/medtrack.git
cd medtrack
````

**2. Create Python environment**

```bash
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

**3. Run the app**

```bash
python main.py
```

---

## 🔐 Authentication

At first run, there are no users.
Use the “Register New User” option from the menu to add your first admin account.

Passwords are stored securely using SHA-256 hashing.

---

## 📖 Usage

### 🧑‍⚕️ Patients

* Add patient records
* Search and update patient info

### 📅 Appointments

* Schedule new appointments
* View today’s appointments
* Reschedule or cancel

### 💊 Medications

* Add medication inventory
* Prescribe and reduce stock
* Low stock alerts

### 💵 Payments

* Record and categorize payments
* View totals and pending balances

### 📊 Reports

* Summary of clinic statistics
* Financial overview (paid + pending totals)

---

## 🧪 Testing

For basic operation, manually test each module from the main menu:

* Add sample patient and verify saved JSON data
* Book appointments and view today’s schedule
* Add medications and prescribe to patients
* Record payments and confirm totals in reports

(*If automated tests are added later, include commands here.*) ([Gitdocs AI][2])

---

## 📌 Notes & Tips

* Keep the `data/` folder backed up regularly
* JSON files can be opened and edited manually if needed
* For a GUI version, consider Tkinter or a Flask web interface

---

## 💡 Future Improvements

* SQLite or database backend
* GUI (Tkinter / Web Dashboard)
* WhatsApp/SMS reminders
* CSV/PDF export for reports

---

## 🧾 License

This project is open-source — feel free to modify and share.

---

## ✨ About

Built by **Ibrahim Labib** — Freelance Python & App Developer
Inspired by real clinic needs and modular project design, with focus on simplicity and practical tools.
