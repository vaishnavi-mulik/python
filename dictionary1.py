#creating dictionary
empdb={
    "ramesh":101,
    "sameer":109,
    "raj":100
    }
print(empdb)

country={
    "india":"delhi",
    "german":"berlin",
    "england":"london"
    }
print(country)
print("capital of india",country["india"])

country["italy"]="room"
print(country)

del country["german"]
print(country)
