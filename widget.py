f = open("wiki2.csv")
country_names = []
info = []
counter = -4
for row in f:
    country_names.append(row.strip().lower().split(',')[0])
    info.append((row.strip().lower().split(',')[1:],counter))
    counter += 1

country = {}
cursor = 0
for i in country_names:
    country[i] = info[cursor]
    cursor += 1

    
user_input = input("Enter a country name\n")


while user_input != '':
    if user_input.lower() in country.keys():
        data = country[user_input.lower()]
        if len(data[0]) == 4:
            print("Your country "+ user_input + " has produced " + data[0][0].strip('"') + ',' + data[0][1].strip('"') + " metric tons of CO2 in 2017. which is a " + data[0][2+1] + " change from 1990.")
            print("This contributes to " + data[0][1+1] + " of the world's fossil CO2 emissions, making it rank " + str(data[1]) + "in the world!")
        else:
            print("Your country "+ user_input + " has produced "+ data[0][0].strip('"') + " metric tons of CO2 in 2017. which is a " + data[0][2] + " change from 1990.")
            print("This contributes to " + data[0][1] + " of the world's fossil CO2 emissions, making it rank " + str(data[1]) + " in the world!")
    else:
        print("Country not found!")
    user_input = input("\nEnter a country or press enter to end the program\n")


print("Thank you!")
