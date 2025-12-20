# Base class
class Person:
    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name

    def display_info(self):
        return f"ID: {self.person_id}, Name: {self.name}"


# Student inherits from Person
class Student(Person):
    def __init__(self, student_id, name):
        # Calling the constructor of Person
        super().__init__(student_id, name)
        self.student_id = student_id

    def display_info(self):
        return f"Student -> {super().display_info()}"


# Staff inherits from Person
class Staff(Person):
    def __init__(self, staff_id, name, tax_num):
        super().__init__(staff_id, name)
        self.staff_id = staff_id
        self.tax_num = tax_num

    def display_info(self):
        return f"Staff -> {super().display_info()}, Tax Number: {self.tax_num}"


# General staff inherits from Staff
class General(Staff):
    def __init__(self, staff_id, name, tax_num, rate_of_pay):
        super().__init__(staff_id, name, tax_num)
        self.rate_of_pay = rate_of_pay

    def display_info(self):
        return (
            f"General Staff -> {super().display_info()}, "
            f"Rate of Pay: ${self.rate_of_pay}/hour"
        )


# Academic staff inherits from Staff
class Academic(Staff):
    def __init__(self, staff_id, name, tax_num, publications):
        super().__init__(staff_id, name, tax_num)
        self.publications = publications

    def display_info(self):
        return (
            f"Academic Staff -> {super().display_info()}, "
            f"Publications: {self.publications}"
        )


# -------------------------
# Demonstration of the system
# -------------------------

student = Student(101, "Aarav Sharma")
general_staff = General(201, "Rita Thapa", "TX12345", 25)
academic_staff = Academic(301, "Dr. Sunil Rai", "TX67890", 18)

print(student.display_info())
print(general_staff.display_info())
print(academic_staff.display_info())
