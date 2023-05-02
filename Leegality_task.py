from datetime import datetime



class ParkingLot:
    def __init__(self):
        """
        Initializes the ParkingLot object with 2 levels A and B 
        """
        self.levels = {
            "A": [{"spot": i, "vehicle": None, "status": "vacant"} for i in range(1, 21)],
            "B": [{"spot": i, "vehicle": None, "status": "vacant"} for i in range(21, 41)]
        }

    def assign_spot(self, vehicle):
        """
        Assigns a vacant parking spot to the vehicle passed as argument
        """
        for level, spots in self.levels.items():
            for spot in spots:
                if spot["status"] == "vacant":
                    spot["vehicle"] = vehicle
                    spot["status"] = "occupied"
                    print(f"Parking spot {level}-{spot['spot']} assigned to vehicle {vehicle.number}")
                    return
        print("Sorry, the parking lot is full.")

    def get_spot(self, vehicle):
        """
        Returns the parking spot number and level of the vehicle passed as argument
        """
        for level, spots in self.levels.items():
            for spot in spots:
                if spot["vehicle"] == vehicle:
                    return {"level": level, "spot": spot["spot"]}
        print(f"Vehicle {vehicle.number} is not in the parking lot.")


class Vehicle:
    def __init__(self, number, size):
        """
        Initializes the Vehicle object with its number plate, size and time of entry.
        """
        self.number = number
        self.size = size
        self.time_entered = datetime.now()

#example 
parking_lot = ParkingLot()
vehicle1 = Vehicle("ABC", "small")
vehicle2 = Vehicle("XYZ", "large")

parking_lot.assign_spot(vehicle1)
parking_lot.assign_spot(vehicle2)

print(parking_lot.get_spot(vehicle1)) 
print(parking_lot.get_spot(vehicle2)) 
