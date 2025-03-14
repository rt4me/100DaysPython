travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
# Print Lille
print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
# Print D
print(nested_list[2][1])



travel_log2 = {
    "France": {
        "num_times_visitied": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "num_times_visited": 5,
        "cities_visited": ["Stuttgart", "Berlin"]
    },
}

# Print Stuttgart
print(travel_log2["Germany"]["cities_visited"][0])