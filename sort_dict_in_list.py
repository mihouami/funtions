import csv


#New comments

#New comments


persons = [['Aminee', 'A', 37], ['Samia', 'B', 33], ['Dina', 'C', 3]]

with open("names_houses_ages.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for person in persons:
        writer.writerow(person)
    
#copie the information from the csv file to a list of dict and list of list

list_of_list = []
list_of_dict = []
list_of_dict2 = []

with open("names_houses_ages.csv") as f:
    #method 1
    for line in f:
        row = line.rstrip().split(',')
        list_of_list.append(row)

        name, house, age = line.rstrip().split(',')
        row_dict = {}
        row_dict['Name'] = name 
        row_dict['House'] = house
        row_dict['Age'] = age
        list_of_dict.append(row_dict)
    
    reader = csv.reader(f)
    #mothod 2
    for name, house, age in reader:
        list_of_dict2.append({'Name':name, 'House':house, 'Age':age})
    

print(list_of_dict, "\n")
print(list_of_dict2, "\n")
print(list_of_list, "\n")

# sort and print list of list

for person in sorted(list_of_list, key=lambda lst: lst[0], reverse = False):
    print(f"{person[0]} is in {person[1]} and his age : {person[2]} ")

print("\n")


# sort by (name, house or age) and print list of dict

for person in sorted(list_of_dict, key=lambda dict: dict['Name'], reverse = False):
    print(f"{person['Name']} is in {person['House']} and his age : {person['Age']} ")

