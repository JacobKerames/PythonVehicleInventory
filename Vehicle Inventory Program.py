#Jacob Kerames

class Automobile:

    #Constructor method
    def __init__(self, make, model, color, year, mileage):
        self.__make = make
        self.__model = model
        self.__color = color
        self.__year = year
        self.__mileage = mileage

    #Setter methods
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_color(self, color):
        self.__color = color

    def set_year(self, year):
        self.__year = year

    def set_mileage(self, mileage):
        self.__mileage = mileage

    #Getter methods
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_color(self):
        return self.__color
    
    def get_year(self):
        return self.__year
    
    def get_mileage(self):
        return self.__mileage

#Method to add a vehicle
def add_vehicle(vehicles):
    make = input('Enter the make:\n')
    model = input('Enter the model:\n')
    color = input('Enter the color:\n')
    year = int(input('Enter the year:\n'))
    mileage = int(input('Enter the mileage:\n'))
    vehicle = Automobile(make, model, color, year, mileage)
    vehicles.append(vehicle)
    print('Vehicle has been added to inventory.\n')

#Method to show the user vehicles for reference
def show_vehicles(vehicles):
    for vehicle in vehicles:
        print('Vehicle:', vehicles.index(vehicle))
        print(vehicle.get_color(), vehicle.get_year(), vehicle.get_make(), vehicle.get_model(), 'with', vehicle.get_mileage(), 'miles.\n')

#Method to remove a vehicle
def remove_vehicle(vehicles):
    show_vehicles(vehicles)
    vehicle = int(input('Please enter the vehicle you would like to remove:\n'))
    try:
        vehicles[vehicle]
    except:
        print('This vehicle is not in the inventory.')
        vehicle = int(input('Please specify the vehicle you wish to remove:\n'))
    vehicles.pop(vehicle)
    print('Vehicle has been removed from the inventory.\n')

#Method to output vehicles to text file
def print_vehicles(vehicles):
    with open('vehicle_inventory.txt', 'w') as output:
        output.write('Vehicle Inventory\n\n')
    for vehicle in vehicles:
        with open('vehicle_inventory.txt', 'a') as output:
            output.write('Vehicle: {}\n{} {} {} {} with {} miles\n\n'.format(str(vehicles.index(vehicle)), vehicle.get_color(), str(vehicle.get_year()), \
                         vehicle.get_make(), vehicle.get_model(), str(vehicle.get_mileage())))
    output.close()

#Initialize vehicle list
vehicles = []

#Main program
print('Vehicle Inventory Program\n')
user_input = input('Would you like to:\n1. Add a vehicle\n2. Remove a vehicle\n3. Update a vehicle\n4. Exit program\n')
while user_input != '4':
    #Adding a vehicle
    if user_input == '1':
        add_vehicle(vehicles)
        user_input = input('Would you like to:\n1. Add a vehicle\n2. Remove a vehicle\n3. Update a vehicle\n4. Exit program\n')
    #Removing a vehicle
    elif user_input == '2':
        remove_vehicle(vehicles)
        user_input = input('Would you like to:\n1. Add a vehicle\n2. Remove a vehicle\n3. Update a vehicle\n4. Exit program\n')
    #Updating vehicle attributes
    elif user_input == '3':
        show_vehicles(vehicles)
        vehicle = int(input('Please specify the vehicle you wish to update:\n'))
        try:
            vehicles[vehicle]
        except:
            print('This vehicle is not in the inventory.')
            vehicle = int(input('Please specify the vehicle you wish to update:\n'))
        attribute = input('Would you like to update:\n1. Make\n2. Model\n3. Color\n4. Year\n5. Mileage\n')
        #Updating make
        if attribute == '1':
            new_make = input('Please enter the updated make of the vehicle:\n')
            vehicles[vehicle].set_make(new_make)
            print('The vehicle make has been updated.\n')
            user_input = input('Would you like to:\n1. Add a vehicle\n2. Remove a vehicle\n3. Update a vehicle\n4. Exit program\n')
        #Updating model
        elif attribute == '2':
            new_model = input('Please enter the updated model of the vehicle:\n')
            vehicles[vehicle].set_model(new_model)
            print('The vehicle model has been updated.\n\n')
            user_input = input('Would you like to:\n1. Add a vehicle\n2. Remove a vehicle\n3. Update a vehicle\n4. Exit program\n')
        #Updating color
        elif attribute == '3':
            new_color = input('Please enter the updated color of the vehicle:\n')
            vehicles[vehicle].set_color(new_color)
            print('The vehicle color has been updated.\n\n')
            user_input = input('Would you like to:\n1. Add a vehicle\n2. Remove a vehicle\n3. Update a vehicle\n4. Exit program\n')
        #Updating year
        elif attribute == '4':
            new_year = input('Please enter the updated year of the vehicle:\n')
            vehicles[vehicle].set_year(new_year)
            print('The vehicle year has been updated.\n\n')
            user_input = input('Would you like to:\n1. Add a vehicle\n2. Remove a vehicle\n3. Update a vehicle\n4. Exit program\n')
        #Updating mileage
        elif attribute == '5':
            new_mileage = input('Please enter the updated mileage of the vehicle:\n')
            vehicles[vehicle].set_mileage(new_mileage)
            print('The vehicle mileage has been updated.\n\n')
            user_input = input('Would you like to:\n1. Add a vehicle\n2. Remove a vehicle\n3. Update a vehicle\n4. Exit program\n')
        else:
            attribute = input('The input is invalid. \
                Please enter a number corresponding to the task you would like to complete.\
                \nWould you like to update:\n1. Make\n2. Model\n3. Color\n4. Year\n5. Mileage\n')

#Asks user if an inventory text file is needed and exits program
need_output = input('Now exiting the program. Would you like to output the inventory to a text file? [Y/N]\n')
if need_output == 'Y':
    print_vehicles(vehicles)
    print('Inventory has been saved to vehicle_inventory.txt\nGoodbye')
elif need_output == 'N':
    print('Goodbye')
else:
    need_output = input('Invalid input. Please enter Y or N to exit the program:\n')
