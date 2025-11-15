class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__(vehicle_type='car')  # always set as 'car' for user input
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

def main():
    print("Please enter the details of your car:")
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")
    doors = input("Number of doors (2 or 4): ")
    roof = input("Type of roof (solid or sun roof): ")
    
    my_car = Automobile(year, make, model, doors, roof)
    
    print("\nHere are the details you entered:")
    print(f"  Vehicle type: {my_car.vehicle_type}")
    print(f"  Year: {my_car.year}")
    print(f"  Make: {my_car.make}")
    print(f"  Model: {my_car.model}")
    print(f"  Number of doors: {my_car.doors}")
    print(f"  Type of roof: {my_car.roof}")

if __name__ == "__main__":
    main()
