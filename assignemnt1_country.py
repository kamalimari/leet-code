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

    for key, val in dictionary.items():# displaying in reverse
        dictionary_values_in_descending.append(val)
        dictionary_values_in_descending.sort(reverse=True)
    # print(dictionary_values_in_descending)

    for i in range(len(dictionary_values_in_descending)):
        data = dictionary_values_in_descending[i]
        # print(data)
        result = maximum(data,dictionary)#maximum value identifying function
        if result == None:
            do = True
        else:
            # print(result)
            max_country_ = max_country(result)
            print(max_country_)
            break


def max_country(result_):
    for pincode_datas in range(len(pincode_)):
        if pincode_[pincode_datas] == result_:
            output_max_country = country[pincode_datas]
            break
    return output_max_country


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
    df = pd.DataFrame(date_storing_dict)  #changing the dictionary to dataframe
    # print(df)
    df['dates'] = pd.to_datetime(df['dates'])
    # print(df)#changing the dataframe to datetime format, so that the datatype is changed from object to datatime format
    df['day_of_week'] = df['dates'].dt.day_name()
    # print(df)
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
        empty_dict_data_from_location_file[city[item]] = pincode_[item]
    # print(empty_dict_data_from_location_file)
    for items in range(len(store_name)):
        empty_dict_data_from_store_file[store_name[items]] = pincode[items]
    # print(empty_dict_data_from_store_file)
    for key_store, val_store in empty_dict_data_from_store_file.items():# store_name and pincode from store file
        temp = key_store
        to_check = val_store
        for key_location, val_location in empty_dict_data_from_location_file.items():#city and pincode from location file
            if to_check == val_location:# pincode in store file equals to pincode in location file checking
                take_key = list(key_location)
                if 'z' in take_key or 'Z' in take_key or 'Ż' in take_key:
                    city_containing_character_z_output.append(temp)
    return city_containing_character_z_output


def no_of_stores_in_each_city():
    pincode_and_city_joining = {}
    pincode_and_city_joining_output = {}
    for item_ in range(len(city)):
        pincode_and_city_joining[city[item_]] = pincode_[item_]#city and pincode joining from location file
    pincode_and_city_joining_dict = dict(pincode_and_city_joining)
    # print(pincode_and_city_joining_dict)
    counter_pincode = Counter(pincode)
    counter_pincode_dict = dict(counter_pincode)
    # print(counter_pincode_dict)
    for key_element, val_element in pincode_and_city_joining_dict.items(): #data from city and pincode joining from location file
        key_element_ = key_element
        val_element_ = val_element
        for key_counter_, val_counter_ in counter_pincode_dict.items():#data from pincode counter
            if val_element_ == key_counter_:#checking pincode in location file and pincode in store file
                pincode_and_city_joining_output[key_element_] = val_counter_
    return pincode_and_city_joining_output


def total_build_area_of_all_stores_built_last_year():
    df['date_of_opening'] = pd.to_datetime(df.date_of_opening)# changing the datatype in to datetime format
    year_ = df.date_of_opening.dt.year #retriving and storing year only
    # print(year_)
    year_collection_list = []
    total_build_area_of_all_stores_built_last_year_output = []
    for year_item in year_:
        year_collection_list.append(year_item)
    for year_elements in range(len(year_collection_list)):
        if year_collection_list[year_elements] == 2018:
            # print(build_area[year_elements])
            total_build_area_of_all_stores_built_last_year_output.append(build_area[year_elements])
    sum_ = sum(total_build_area_of_all_stores_built_last_year_output)
    return sum_


def number_of_stores_in_each_country():
    temp_list = []
    dictionary__ = {}
    counter_for_pin_in_store_file = Counter(pincode)
    dict_for_pin_in_store_file = dict(counter_for_pin_in_store_file)
    for first in range(len(country)):
        sum_ = 0
        temp = str(country[first]) #poland
        if temp not in temp_list:
            for i in range(len(country)):
                if temp == str(country[i]):# poland == poland
                    for key, val in dict_for_pin_in_store_file.items():
                        if pincode_[i] == key:
                            sum_ = sum_ + val
        dictionary__[temp] = sum_
    return dictionary__


result_build_area_greater_than_4000 = build_area_greater_than_4000()
print(result_build_area_greater_than_4000)

country_having_the_most_number_of_stores()

saturday_or_sunday_ = saturday_or_sunday()
print(saturday_or_sunday_)

city_containing_character_z_ = city_containing_character_z()
print(city_containing_character_z_)

no_of_stores_in_each_city_ = no_of_stores_in_each_city()
print(no_of_stores_in_each_city_)

total_build_area_of_all_stores_built_last_year_ = total_build_area_of_all_stores_built_last_year()
print(total_build_area_of_all_stores_built_last_year_)

number_of_stores_in_each_country_ = number_of_stores_in_each_country()
print(number_of_stores_in_each_country_)



    # print(index['pincode'], index['city'])


