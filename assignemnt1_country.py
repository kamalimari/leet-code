from collections import Counter
import pandas as pd
df = pd.read_csv('exercise_1_store.csv')
df1 = pd.read_csv('exercise_1_location.csv')
store_name = []
build_area = []
date_of_opening = []
pincode = []
pincode_ = []
city = []
country = []
temp_dict = {}

for index, row in df.iterrows():
    store_name.append(row[0])
    build_area.append(row[1])
    date_of_opening.append(row[2])
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
    # print(dictionary)
    dictionary_values_in_descending = []

    for key, val in dictionary.items():
        dictionary_values_in_descending.append(val)
        dictionary_values_in_descending.sort(reverse=True)
    # print(dictionary_values_in_descending)

    for i in range(len(dictionary_values_in_descending)):
        data = dictionary_values_in_descending[i]
        # print(data)
        result = maximum(data,dictionary)
        if result == None:
            do = True
        else:
            print(result)
            break


def maximum(data__,dictionary__):
    for dic_key, dic_val in dictionary__.items():
        if data__ == dic_val:
            storing_data = dic_key
            for j in range(len(pincode_)):
                if storing_data == pincode_[j]:
                    maximum_value = storing_data
                    return maximum_value


def saturday_or_sunday():
    date_storing_dict = {}
    day_storing_list = []
    output_for_day_storing_data = []
    date_storing_dict['dates'] = date_of_opening
    # print(date_storing_dict)
    df = pd.DataFrame(date_storing_dict)
    df['dates'] = pd.to_datetime(df['dates'])
    df['day_of_week'] = df['dates'].dt.day_name()
    for index, row in df.iterrows():
        day_storing_list.append(row[1])
    # print(day_storing_list)
    for days in range(len(day_storing_list)):
        if day_storing_list[days] == 'Saturday' or day_storing_list[days] == 'Sunday':
            output_for_day_storing_data.append(store_name[days])
    return output_for_day_storing_data


def city_containing_character_z():
    empty_dict_data_from_location_file = {}
    empty_dict_data_from_store_file = {}
    city_containing_character_z_output = []
    for item in range(len(pincode_)):
        empty_dict_data_from_location_file[country[item]] = pincode_[item]
    print(empty_dict_data_from_location_file)
    for items in range(len(store_name)):
        empty_dict_data_from_store_file[store_name[items]] = pincode[items]
    print(empty_dict_data_from_store_file)
    for key_store, val_store in empty_dict_data_from_store_file.items():
        temp = key_store
        to_check = val_store
        for key_location, val_location in empty_dict_data_from_location_file.items():
            if to_check == val_location:
                take_key = list(key_location)
                if 'z' in take_key or 'Z' in take_key:
                    city_containing_character_z_output.append(temp)
    return city_containing_character_z_output


def no_of_stores_in_each_city():










result_build_area_greater_than_4000 = build_area_greater_than_4000()
print(result_build_area_greater_than_4000)

country_having_the_most_number_of_stores()

saturday_or_sunday_ = saturday_or_sunday()
print(saturday_or_sunday_)

city_containing_character_z_ = city_containing_character_z()
print(city_containing_character_z_)






    # print(index['pincode'], index['city'])


