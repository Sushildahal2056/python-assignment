import sqlite3

class HospitalDB:
    def __init__(self, db_name="hospital.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    # ------------------------------
    # CREATE TABLES
    # ------------------------------
    def create_tables(self):

        # Patient Table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Patient(
                Patient_ID INTEGER PRIMARY KEY,
                PatientName TEXT NOT NULL,
                Age INTEGER,
                Phone TEXT,
                Email TEXT,
                Gender TEXT,
                Address TEXT
            )
        """)

        # Doctor Table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Doctor(
                Doctor_ID INTEGER PRIMARY KEY,
                DoctorName TEXT NOT NULL,
                Age INTEGER,
                Phone TEXT,
                Specialization TEXT
            )
        """)

        # Treatment Table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Treatment(
                Treatment_ID INTEGER PRIMARY KEY,
                Treatment_Name TEXT NOT NULL
            )
        """)

        # Appointment Table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Appointment(
                Appointment_ID INTEGER PRIMARY KEY,
                Patient_ID INTEGER,
                Doctor_ID INTEGER,
                Treatment_ID INTEGER,
                Date TEXT,
                Time TEXT,
                Reason TEXT,
                FOREIGN KEY(Patient_ID) REFERENCES Patient(Patient_ID),
                FOREIGN KEY(Doctor_ID) REFERENCES Doctor(Doctor_ID),
                FOREIGN KEY(Treatment_ID) REFERENCES Treatment(Treatment_ID)
            )
        """)

        self.conn.commit()

    # ------------------------------
    # INSERT SAMPLE DATA
    # ------------------------------
    def insert_data(self):

        patients = [
            (1, "Ram Shrestha", 25, "980000001", "ram@gmail.com", "Male", "Kathmandu"),
            (2, "Sita Lama", 30, "980000002", "sita@gmail.com", "Female", "Pokhara")
        ]
        self.cursor.executemany(
            "INSERT OR IGNORE INTO Patient VALUES (?, ?, ?, ?, ?, ?, ?)", patients
        )

        doctors = [
            (1, "Dr. Anil Shah", 45, "981111111", "Cardiology"),
            (2, "Dr. Mina Karki", 40, "982222222", "Dermatology")
        ]
        self.cursor.executemany(
            "INSERT OR IGNORE INTO Doctor VALUES (?, ?, ?, ?, ?)", doctors
        )

        treatments = [
            (1, "Heart Checkup"),
            (2, "Skin Treatment")
        ]
        self.cursor.executemany(
            "INSERT OR IGNORE INTO Treatment VALUES (?, ?)", treatments
        )

        appointments = [
            (1, 1, 1, 1, "2025-01-10", "10:00 AM", "Chest Pain"),
            (2, 2, 2, 2, "2025-01-11", "11:30 AM", "Skin Allergy")
        ]
        self.cursor.executemany(
            "INSERT OR IGNORE INTO Appointment VALUES (?, ?, ?, ?, ?, ?, ?)", appointments
        )

        self.conn.commit()

    # ------------------------------
    # COUNT APPOINTMENTS FOR A DOCTOR
    # ------------------------------
    def count_appointments(self, doctor_id):
        self.cursor.execute(
            "SELECT COUNT(*) FROM Appointment WHERE Doctor_ID = ?",
            (doctor_id,)
        )
        return self.cursor.fetchone()[0]

    # ------------------------------
    # LIST PATIENTS FOR A DOCTOR
    # ------------------------------
    def list_patients(self, doctor_id):
        self.cursor.execute("""
            SELECT p.PatientName
            FROM Patient p
            JOIN Appointment a ON p.Patient_ID = a.Patient_ID
            WHERE a.Doctor_ID = ?
        """, (doctor_id,))

        return [row[0] for row in self.cursor.fetchall()]


# ------------------------------
# MAIN PROGRAM
# ------------------------------
if __name__ == "__main__":
    db = HospitalDB()
    db.insert_data()

    print("Appointments for Doctor 1:", db.count_appointments(1))
    print("Patients treated by Doctor 1:", db.list_patients(1))
