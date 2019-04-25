import csv
store_list = []
location_list = []
with open('exercise_1_store.csv','r')as csv_file:
    csv_reader_1 = csv.reader(csv_file, delimiter=',')
    for row in csv_reader_1:
        store_list.append(row)

with open('exercise_1_location.csv', encoding='utf-8')as csv_file:
    csv_reader_2 = csv.reader(csv_file, delimiter=',')
    for row in csv_reader_2:
            location_list.append(row)
temp = []
for location_list_item in location_list:
    for store_list_item in store_list:
        if location_list_item[0] == store_list_item[3]:
            temp.append(location_list_item)
            temp.append(store_list_item)
print(temp)
k = 0
join_list = []
for i in range(len(temp)):
    if i == len(temp)/2:
        break
    else:
        i = k
        first = temp[i]
        second = temp[i+1]
        join = first + second
        join_list.append(join)
        k = k + 2
print(join_list)


def build_area_greater_than_4000():
    for item in range(1, len(join_list)):
        if

build_area_greater_than_4000()








