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

