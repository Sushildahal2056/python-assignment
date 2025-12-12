import sqlite3

class CollegeDB:
    def __init__(self, db_name="college.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    # ------------------------------
    # CREATE ALL TABLES
    # ------------------------------
    def create_tables(self):
        
        # Student Table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Student(
                Student_ID INTEGER PRIMARY KEY,
                name VARCHAR(30) NOT NULL,
                age INTEGER NOT NULL,
                phone INTEGER,
                email VARCHAR(50),
                address VARCHAR(50),
                major VARCHAR(30)
            )
        """)

        # Course Table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Course(
                Course_ID INTEGER PRIMARY KEY,
                name VARCHAR(40) NOT NULL,
                Credit INTEGER,
                Semester INTEGER
            )
        """)

        # Professor Table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Professor(
                P_ID INTEGER PRIMARY KEY,
                name VARCHAR(30) NOT NULL,
                department VARCHAR(30)
            )
        """)

        # Enrollment Table  (Student → Course)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Enrollment(
                Student_ID INTEGER,
                Course_ID INTEGER,
                FOREIGN KEY(Student_ID) REFERENCES Student(Student_ID),
                FOREIGN KEY(Course_ID) REFERENCES Course(Course_ID)
            )
        """)

        # Teaches Table (Professor → Course)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Teaches(
                P_ID INTEGER,
                Course_ID INTEGER,
                FOREIGN KEY(P_ID) REFERENCES Professor(P_ID),
                FOREIGN KEY(Course_ID) REFERENCES Course(Course_ID)
            )
        """)

        self.conn.commit()

    # ------------------------------
    # INSERT SAMPLE DATA
    # ------------------------------
    def insert_data(self):

        # Student Data
        students = [
            (1, "Ramesh Thapa", 22, 980000001, "ram@gmail.com", "Kathmandu", "Computer Science"),
            (2, "Sita Lama", 19, 980000002, "sita@gmail.com", "Pokhara", "Management")
        ]
        self.cursor.executemany("INSERT INTO Student VALUES (?, ?, ?, ?, ?, ?, ?)", students)

        # Course Data
        courses = [
            (101, "Database Management", 3, 1),
            (102, "OOP in Python", 4, 1)
        ]
        self.cursor.executemany("INSERT INTO Course VALUES (?, ?, ?, ?)", courses)

        # Professor Data
        professors = [
            (10, "Dr. Bikash Shrestha", "IT Department"),
            (11, "Prof. Mira Karki", "Science Department")
        ]
        self.cursor.executemany("INSERT INTO Professor VALUES (?, ?, ?)", professors)

        # Enrollment Data
        enrollment = [
            (1, 101),
            (2, 102)
        ]
        self.cursor.executemany("INSERT INTO Enrollment VALUES (?, ?)", enrollment)

        # Teaches Data
        teaches = [
            (10, 101),
            (11, 102)
        ]
        self.cursor.executemany("INSERT INTO Teaches VALUES (?, ?)", teaches)

        self.conn.commit()

    # ------------------------------
    # COUNT STUDENTS IN COURSE
    # ------------------------------
    def count_students(self, course_id):
        self.cursor.execute(
            "SELECT COUNT(*) FROM Enrollment WHERE Course_ID = ?", 
            (course_id,)
        )
        return self.cursor.fetchone()[0]

    # ------------------------------
    # LIST PROFESSORS TEACHING A COURSE
    # ------------------------------
    def list_professors(self, course_id):
        self.cursor.execute("""
            SELECT p.name 
            FROM Professor p
            JOIN Teaches t ON p.P_ID = t.P_ID
            WHERE t.Course_ID = ?
        """, (course_id,))
        
        return [row[0] for row in self.cursor.fetchall()]

# ------------------------------
# MAIN PROGRAM
# ------------------------------
if __name__ == "__main__":
    db = CollegeDB()
    db.insert_data()

    # Count students in Database Management
    print("Students in Course 101:", db.count_students(101))

    # List professors for OOP in Python
    print("Professors teaching Course 102:")
    for prof in db.list_professors(102):
        print(prof)

    db.conn.close()
