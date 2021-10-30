counties = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#for key, value in counties_dict.items():
#    print(key + " county has " +  str(value) + " Registerd Voters.")

#voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                {"county":"Denver", "registered_voters": 463353},
#                {"county":"Jefferson", "registered_voters": 432438}]

#for county in counties_dict.keys():
#     print(county)
for county in range(len(counties)):
    print(counties(county))