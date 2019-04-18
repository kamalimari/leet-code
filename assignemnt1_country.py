from collections import Counter
import pandas
df = pandas.read_csv('exercise_1_store.csv')
df1 = pandas.read_csv('exercise_1_location.csv')
store_name = []
build_area = []
date_of_area = []
pincode = []
pincode_ = []
city = []
country = []
temp_dict = {}

for index, row in df.iterrows():
    store_name.append(row[0])
    build_area.append(row[1])
    date_of_area.append(row[2])
    pincode.append(row[3])


for index, row in df1.iterrows():
    pincode_.append(row[0])
    city.append(row[1])
    country.append(row[2])


def build_area_greater_than_4000():
    build_area_greater_than_4000_ = []
    for i in range(len(build_area)):
        if build_area[i] > 4000:
            build_area_greater_than_4000_.append(store_name[i])
    return build_area_greater_than_4000_


def country_having_the_most_number_of_stores():
    counter = Counter(pincode)
    dictionary = dict(counter)
    print(dictionary)
    dictionary_values_in_descending = []

    for key, val in dictionary.items():
        dictionary_values_in_descending.append(val)
        dictionary_values_in_descending.sort(reverse=True)
    print(dictionary_values_in_descending)

    for i in range(len(dictionary_values_in_descending)):
        data = dictionary_values_in_descending[i]
        print(data)
        result = maximum(data,dictionary)
        print(result)

def maximum(data__,dictionary__):
    for dic_key, dic_val in dictionary__.items():
        if data__ == dic_val:
            storing_data = dic_key
            for j in range(len(pincode_)):
                if storing_data == pincode_[j]:
                    maximum_value = storing_data
                    return maximum_value








result_build_area_greater_than_4000 = build_area_greater_than_4000()
print(result_build_area_greater_than_4000)

country_having_the_most_number_of_stores()





    # print(index['pincode'], index['city'])


