import json
import math

def calculate_distance(point1, point2):
    # Calculate Euclidean distance between two points
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def choose_office(office_data):
    offices = office_data["offices"]
    selected_office = None
    max_area = 0

    # Find the office with the largest area
    for office in offices:
        if office["area"] > max_area:
            max_area = office["area"]
            selected_office = office

    # Check if IT office is selected
    if selected_office["name"] != "IT":
        # Sort offices by area in descending order
        sorted_offices = sorted(offices, key=lambda x: x["area"], reverse=True)
        
        # Choose the office with the largest area (excluding IT office)
        it_room = sorted_offices[0]["name"]
        print(f"The IT room is {it_room}.")
    else:
        print("The IT office was selected.")

    # Calculate the number of switches needed
    num_offices = len(offices)
    num_switches = math.ceil(num_offices / 5)
    print(f"Number of switches needed: {num_switches}")

    # Determine nearest point to the IT room for each group of 5 offices
    switch_locations = {}
    for i in range(num_switches):
        # Determine the range of offices for this switch
        start_index = i * 5
        end_index = min((i + 1) * 5, num_offices)
        sorted_offices = sorted(offices, key=lambda x: x["area"], reverse=True)
        offices_subset = sorted_offices[start_index:end_index]

        # Calculate centroid of offices subset
        centroid_x = sum(office["location"][0] for office in offices_subset) / len(offices_subset)
        centroid_y = sum(office["location"][1] for office in offices_subset) / len(offices_subset)
        centroid = (centroid_x, centroid_y)

        # Find the nearest point to the IT room
        nearest_point = None
        min_distance = float('inf')
        for office in offices_subset:
            distance = calculate_distance(office["location"], selected_office["location"])
            if distance < min_distance:
                min_distance = distance
                nearest_point = office["location"]

        # Store the nearest point for this switch
        switch_locations[i] = nearest_point

    # Determine the location of each switch
    for switch_num, nearest_point in switch_locations.items():
        print(f"Switch {switch_num + 1} location: {nearest_point}")

# Example JSON data
office_data = {
    "offices": [
        {"name": "A", "area": 100, "location": (0, 0)},
        {"name": "B", "area": 150, "location": (1, 1)},
        {"name": "IT", "area": 200, "location": (2, 2)},
        {"name": "C", "area": 120, "location": (4, 4)},
        {"name": "D", "area": 180, "location": (6, 6)},
        {"name": "E", "area": 90, "location": (8, 8)},
        {"name": "F", "area": 160, "location": (10, 10)},
        {"name": "G", "area": 110, "location": (12, 12)}
    ]
}

# Call the function with the example data
choose_office(office_data)
