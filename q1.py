# Design a Parking Lot Management System using Object-Oriented Programming, with support for:
# Different vehicle types
# Slot allocation and release
# Real-time occupancy tracking
# Search and report generation
# 1. Core Classes

# Vehicle
# pythonCopy codeAttributes: vehicle_number, vehicle_type (e.g., car, bike, truck)

# ParkingSlot
# pythonCopy codeAttributes: slot_id, slot_type (e.g., compact, large, bike), is_occupied, assigned_vehicle
# Methods: assign_vehicle(vehicle), release_vehicle()

# ParkingLot
# pythonCopy codeAttributes: total_slots, available_slots (dict), occupied_slots (dict)

# Methods:
#   - add_slot(slot: ParkingSlot)
#   - park_vehicle(vehicle: Vehicle) -> slot_id
#   - release_slot(slot_id)
#   - get_status()
#   - search_vehicle(vehicle_number)
# 🧠 Functional Requirements
# Slot Assignment
# Cars → compact
# Bikes → bike
# Trucks → large
# First available slot of appropriate type is assigned.
# Vehicle Search
# Given a vehicle number, return slot info.
# Occupancy Status
# Show occupied vs available slots per vehicle type.
# Slot Release
# Frees up slot and removes assigned vehicle.


# Solution
# Vehicle Class
class Vehicle:
    def __init__(self, vehicle_number, vehicle_type):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type

    def vehicle_detail(self):
        return f"Vehicle Number: {self.vehicle_number}, Type: {self.vehicle_type}"


# ParkingSlot Class
class ParkingSlot:
    def __init__(self, slot_id, slot_type):
        self.slot_id = slot_id
        self.slot_type = slot_type
        self.is_occupied = False
        self.assigned_vehicle = None

    def assign_vehicle(self, vehicle):
        if not self.is_occupied:
            self.is_occupied = True
            self.assigned_vehicle = vehicle
            return True
        return False

    def release_vehicle(self):
        self.is_occupied = False
        released_vehicle = self.assigned_vehicle
        self.assigned_vehicle = None
        return released_vehicle


# ParkingLot Class
class ParkingLot:
    def __init__(self):
        self.total_slots = []
        self.available_slots = {
            'compact': [],
            'large': [],
            'bike': []
        }
        self.occupied_slots = {}

    def add_slot(self, slot: ParkingSlot):
        self.total_slots.append(slot)
        if not slot.is_occupied:
            self.available_slots[slot.slot_type].append(slot)

    def park_vehicle(self, vehicle: Vehicle):
        vehicle_type_map = {
            'car': 'compact',
            'truck': 'large',
            'bike': 'bike'
        }
        slot_type = vehicle_type_map.get(vehicle.vehicle_type)

        if not slot_type or not self.available_slots[slot_type]:
            return f"No available slot for {vehicle.vehicle_type}"

        slot = self.available_slots[slot_type].pop(0)
        if slot.assign_vehicle(vehicle):
            self.occupied_slots[vehicle.vehicle_number] = slot
            return f"Vehicle {vehicle.vehicle_number} parked at slot {slot.slot_id}"
        else:
            return f"Failed to assign slot."

    def release_slot(self, slot_id):
        for slot in self.total_slots:
            if slot.slot_id == slot_id and slot.is_occupied:
                vehicle = slot.release_vehicle()
                self.available_slots[slot.slot_type].append(slot)
                del self.occupied_slots[vehicle.vehicle_number]
                return f"Slot {slot_id} released from vehicle {vehicle.vehicle_number}"
        return "Slot not found or already free."

    def get_status(self):
        status = {}
        for slot_type in self.available_slots:
            total = len([s for s in self.total_slots if s.slot_type == slot_type])
            available = len(self.available_slots[slot_type])
            status[slot_type] = {
                "occupied": total - available,
                "available": available
            }
        return status

    def search_vehicle(self, vehicle_number):
        slot = self.occupied_slots.get(vehicle_number)
        if slot:
            return f"Vehicle {vehicle_number} is parked at slot {slot.slot_id} ({slot.slot_type})"
        else:
            return "Vehicle not found."


# -------------------------------
# Example Usage
# -------------------------------
# Create parking lot
parking_lot = ParkingLot()

# Add slots
for i in range(1, 4):
    parking_lot.add_slot(ParkingSlot(f"C{i}", 'compact'))
for i in range(1, 3):
    parking_lot.add_slot(ParkingSlot(f"B{i}", 'bike'))
parking_lot.add_slot(ParkingSlot("L1", 'large'))

# Park vehicles
v1 = Vehicle("MH12AB1234", "car")
v2 = Vehicle("MH12XY4321", "bike")
v3 = Vehicle("MH14TR1111", "truck")

print(parking_lot.park_vehicle(v1))
print(parking_lot.park_vehicle(v2))
print(parking_lot.park_vehicle(v3))

# Search vehicle
print(parking_lot.search_vehicle("MH12XY4321"))

# Get occupancy status
print(parking_lot.get_status())

# Release a slot
print(parking_lot.release_slot("C1"))

# Get updated status
print(parking_lot.get_status())
