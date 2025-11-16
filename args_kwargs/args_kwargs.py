class Employee:
    def __init__(self, name, age, *args, **kwargs):
        self.name = name
        self.age = age
        self.skills = args
        self.details = kwargs

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print("Skills:")
        for skill in self.skills:
            print(f"- {skill}")
        print("Additional Details:")
        for key, value in self.details.items():
            print(f"{key}: {value}")

# Example usage:
employee = Employee("John Doe", 30, "Python", "Django", department="IT", position="Developer")
employee.display_info()