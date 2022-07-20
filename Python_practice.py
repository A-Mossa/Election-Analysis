from itertools import count


counties = ["Arapahoe", "Denver", "Jefferson"]


if "El Paso" in counties :
    print( "El Paso is in the list of counties" )
else :
    print( "El Paso is not in the list of counties")

if "arabahoe" in counties and "El Paso" in counties :
    print ("Arapahoe and EL Paso are Present")
else :
    print ("Arapahoe or El Paso is not there")

if "Arapahoe" in counties or "El Paso" in counties :
    print(" Arapahoe or El Paso is in counties list")
else :
    print("Arapahoe and El Paso are not present in county list")

for county in counties :
    print(county)
    
for i in range(len(counties)) :
    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict.keys() :
    print(county)

for voters in counties_dict.values() :
    print(voters)

for county in counties_dict :
    print(counties_dict[county])

for key, value in counties_dict.items () :
    print(key, value)

for county, voters in counties_dict.items() :
    print( (county) + " county has " +str (voters)+  " registered voters")

for county, voters in counties_dict.items() :
    print(f"{county} county has {voters} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data :
    for value in county_dict.values():
        print (value)

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))

message_to_candidate = (
    f"You received {my_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {my_votes / total_votes * 100:.2f}% of the total votes.")
print(message_to_candidate)