{
  "employees": [
    {
      "Name": "John Doe",
      "DOB": "1990-05-15",
      "Height": "6'0\"",
      "City": "New York",
      "State": "New York"
    },
    {
      "Name": "Jane Smith",
      "DOB": "1985-08-22",
      "Height": "5'5\"",
      "City": "Los Angeles",
      "State": "California"
    },
    {
      "Name": "David Johnson",
      "DOB": "1992-03-10",
      "Height": "5'10\"",
      "City": "Chicago",
      "State": "Illinois"
    },
    {
      "Name": "Sarah Williams",
      "DOB": "1988-12-03",
      "Height": "5'8\"",
      "City": "Houston",
      "State": "Texas"
    },
    {
      "Name": "Michael Brown",
      "DOB": "1995-07-18",
      "Height": "6'2\"",
      "City": "Philadelphia",
      "State": "Pennsylvania"
    }
  ]
}
import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

# Read JSON file
with open('employee.json', 'r') as f:
    data = json.load(f)
    employee_list = []
    for employee_data in data['employees']:
        employee = Employee(employee_data['Name'], employee_data['DOB'], employee_data['Height'], employee_data['City'], employee_data['State'])
        employee_list.append(employee)

# Print list of Employee objects
for employee in employee_list:
    print("Name: ", employee.name)
    print("DOB: ", employee.dob)
    print("Height: ", employee.height)
    print("City: ", employee.city)
    print("State: ", employee.state)
    print("-----------")
import json

# Dictionary of Indian states and capitals
indian_states = {
    "Andhra Pradesh": "Amaravati",
    "Arunachal Pradesh":
