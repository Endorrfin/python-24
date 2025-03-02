capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}


# Nested list in dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

# Print Lille
print(travel_log["France"])
print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[0][0])
print(nested_list[1][0])
print(nested_list[2][1])

travel_log_europe = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
}

print(travel_log_europe["Germany"]["cities_visited"][2])