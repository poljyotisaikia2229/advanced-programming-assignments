
# Address Class

class Address:
    def __init__(self, street, city, zip_code):
        self.street = street
        self.city = city
        self.zip_code = zip_code

    def display(self):
        return f"{self.street}, {self.city} - {self.zip_code}"



# Student Class (HAS-A Address)

class Student:
    def __init__(self, name, age, address):
        self.name = name
        self._age = None          # protected attribute
        self.age = age            # use property setter
        self.address = address    # composition
        self.courses = []         # mutable list

    # Property for age (validation)
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value <= 0 or value > 120:
            raise ValueError("Age must be between 1 and 120")
        self._age = value

    # Add course (mutable behavior)
    def add_course(self, course):
        if not course:
            raise ValueError("Course name cannot be empty")
        self.courses.append(course)

    # Display method
    def display(self):
        print("\n--- Student ---")
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Address : {self.address.display()}")
        print(f"Courses : {', '.join(self.courses) if self.courses else 'None'}")


# ScholarshipStudent (Inheritance)

class ScholarshipStudent(Student):
    def __init__(self, name, age, address, scholarship_amount):
        super().__init__(name, age, address)
        self.scholarship_amount = scholarship_amount

    # Override display()
    def display(self):
        print("\n--- Scholarship Student ---")
        super().display()
        print(f"Scholarship: ${self.scholarship_amount}")



# Main / Testing

if __name__ == "__main__":

    # Create Address (Composition)
    addr = Address("Napaam", "Tezpur", "784028")

    # Create Student
    s1 = Student("Ranjan", 20, addr)
    s1.add_course("Math")
    s1.add_course("Physics")
   

    # Create Scholarship Student
    s2 = ScholarshipStudent("Pol", 22, addr, 1500)
    s2.add_course("Computer Science")


    # Display students
    s1.display()
    s2.display()

    # Demonstrate mutable behavior
    print("\n--- Mutable Behavior Test ---")
    s1.add_course("Chemistry")
    
    s1.display()  # course persists
   
  

    # Validation test
    print("\n--- Validation Test ---")
    try:
        s1.age = -5  # invalid age
    except ValueError as e:
        print("Error:", e)