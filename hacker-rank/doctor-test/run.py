

# Convert the csv into an array
def convert_to_array(csv_string):
    data = csv_string.split("\n")
    new_data = []
    for i in range(len(data)):
        line = str(data[i])
        data1 = line.split(",")       
        new_data.append(data1)
    return new_data

# convert the new_data array into dictionaries
def create_dict_from_array(new_data):
    dict1 = {}
    dict2 = {}
    for line in new_data:
        avg1 = float(line[3])
        avg2 = float(line[4])
        dict1[avg1] = line
        dict2[avg2] = line
    return dict1,dict2

def create_sorted_dict(dict1, d1):
    return_dict = {}
    for key in d1:
        return_dict[key] = dict1[key]
    return return_dict

def create_sorted_csv(dict1, d1):
    return_csv = ''
    for key in d1:
        return_csv+= ','.join(dict1[key])
        return_csv += '\n'
    return return_csv

def doctor_sort(csv_string):
    new_data = convert_to_array(csv_string)    
    dict1,dict2 = create_dict_from_array(new_data)
    d1 = sorted(dict1)
    d2 = sorted(dict2)
    print 'sorted by column 3'
    print (create_sorted_csv(dict1, d1))
    print 'sorted by column 4'
    print (create_sorted_csv(dict2, d2))
    return ""


csv = """1,alex,80405,13,5
3,bob,94123,320,1.5
2,jane,94032,35,2.8
4,will,94110,31.6,6.1
5,jess,94117,48,4
6,sam,94032,31.4,9
7,jim,94036,35,19"""

print(doctor_sort(csv))
