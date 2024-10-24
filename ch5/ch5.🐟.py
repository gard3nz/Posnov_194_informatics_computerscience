sea_fish = ["shark", "flounder", "tuna", "cod", "herring", "Marlin"] 
freshwater_fish = ["Asp", "Pike", "Carp", "Salmon", "Ide", "Trout"]
combined_fish = sorted(sea_fish + freshwater_fish, key=lambda x: x.lower())
print(combined_fish)
