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
│
├── data/
│   ├── appointments.json
│   ├── medications.json
│   ├── patients.json
│   ├── payments.json
│   ├── users.json
│
├── modules/
│   ├── appointment.py
│   ├── auth.py
│   ├── medication.py
│   ├── patient.py
│   ├── payment.py
│   └── report.py
│
├── utils/
│   └── file_handler.py
│
├── main.py
└── README.md


````

---

## 🛠️ Quick Start

**1. Clone the repo**
```bash
git clone https://github.com/Ibrahim-Lbib/medtrack.git
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

On first run, MedTrack will prompt you to create an **admin account**.

This admin account is required to access the system.

After the admin account is created:
- All users must log in before using the system
- Credentials are stored securely using SHA-256 password hashing

You do **not** need to manually edit any files.

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
