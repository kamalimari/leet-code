from collections import Counter
import pandas as pd
df = pd.read_csv('exercise_1_store.csv')
df1 = pd.read_csv('exercise_1_location.csv')
# store_name = []
# build_area = []
# date_of_opening = []
# pincode = []
# pincode_ = []
# city = []
# country = []
# temp_dict = {}

# for index, row in df.iterrows():
    # store_name.append(row[0])
    # build_area.append(row[1])
    # date_of_opening.append(row[2])
    # pincode.append(row[3])
#
#
# for index, row in df1.iterrows():
#     pincode_.append(row[0])
#     city.append(row[1])
#     country.append(row[2])


def build_area_greater_than_4000():
    build_area_greater_than_4000_ = []
    for index, row in df.iterrows():
        if row[1] > 4000:
            build_area_greater_than_4000_.append(row[0])
    return build_area_greater_than_4000_

# def country_having_the_most_number_of_stores():
#     counter = Counter(pincode)
#     dictionary = dict(counter)
#     # print(dictionary)
#     dictionary_values_in_descending = []
#
#     for key, val in dictionary.items():# displaying in reverse
#         dictionary_values_in_descending.append(val)
#         dictionary_values_in_descending.sort(reverse=True)
#     # print(dictionary_values_in_descending)
#
#     for i in range(len(dictionary_values_in_descending)):
#         data = dictionary_values_in_descending[i]
#         # print(data)
#         result = maximum(data,dictionary)#maximum value identifying function
#         if result == None:
#             do = True
#         else:
#             # print(result)
#             max_country_ = max_country(result)
#             print(max_country_)
#             break
#
#
# def max_country(result_):
#     for pincode_datas in range(len(pincode_)):
#         if pincode_[pincode_datas] == result_:
#             output_max_country = country[pincode_datas]
#             break
#     return output_max_country
#
#
# def maximum(data__,dictionary__):
#     for dic_key, dic_val in dictionary__.items():
#         if data__ == dic_val:
#             storing_data = dic_key
#             for j in range(len(pincode_)):
#                 if storing_data == pincode_[j]:
#                     maximum_value = storing_data
#                     return maximum_value


def saturday_or_sunday():
    saturday_or_sunday_ = []
    df['date_of_opening'] = pd.to_datetime(df.date_of_opening)  # changing the datatype in to datetime format
    df['day_name'] = df.date_of_opening.dt.day_name()
    for index_, rows_ in df.iterrows():
        if rows_[4] == 'Saturday' or rows_[4] == 'Sunday':
            saturday_or_sunday_.append(rows_[0])
    return saturday_or_sunday_


def city_containing_character_z():
    city_containing_character_z_ = []
    for index__, rows__ in df.iterrows():
        store_name = rows__[0]
        pincode = rows__[3]
        for second_index, second_rows in df1.iterrows():
            if pincode == second_rows[0]:
                word_converted_list = list(second_rows[1])
                if 'z' in word_converted_list or 'Z' in word_converted_list or 'Ż' in word_converted_list:
                    city_containing_character_z_.append(store_name)
    print(city_containing_character_z_)

#
#
# def no_of_stores_in_each_city():
#     pincode_and_city_joining = {}
#     pincode_and_city_joining_output = {}
#     for item_ in range(len(city)):
#         pincode_and_city_joining[city[item_]] = pincode_[item_]#city and pincode joining from location file
#     pincode_and_city_joining_dict = dict(pincode_and_city_joining)
#     # print(pincode_and_city_joining_dict)
#     counter_pincode = Counter(pincode)
#     counter_pincode_dict = dict(counter_pincode)
#     # print(counter_pincode_dict)
#     for key_element, val_element in pincode_and_city_joining_dict.items(): #data from city and pincode joining from location file
#         key_element_ = key_element
#         val_element_ = val_element
#         for key_counter_, val_counter_ in counter_pincode_dict.items():#data from pincode counter
#             if val_element_ == key_counter_:#checking pincode in location file and pincode in store file
#                 pincode_and_city_joining_output[key_element_] = val_counter_
#     return pincode_and_city_joining_output
#
#
# def total_build_area_of_all_stores_built_last_year():
#     df['date_of_opening'] = pd.to_datetime(df.date_of_opening)# changing the datatype in to datetime format
#     year_ = df.date_of_opening.dt.year #retriving and storing year only
#     # print(year_)
#     year_collection_list = []
#     total_build_area_of_all_stores_built_last_year_output = []
#     for year_item in year_:
#         year_collection_list.append(year_item)
#     for year_elements in range(len(year_collection_list)):
#         if year_collection_list[year_elements] == 2018:
#             # print(build_area[year_elements])
#             total_build_area_of_all_stores_built_last_year_output.append(build_area[year_elements])
#     sum_ = sum(total_build_area_of_all_stores_built_last_year_output)
#     return sum_
#
#
#
#
#
build_area_greater_than_4000_output = build_area_greater_than_4000()
print(build_area_greater_than_4000_output)

# country_having_the_most_number_of_stores()

saturday_or_sunday_output = saturday_or_sunday()
print(saturday_or_sunday_output)

city_containing_character_z()

#
# no_of_stores_in_each_city_ = no_of_stores_in_each_city()
# print(no_of_stores_in_each_city_)
#
# total_build_area_of_all_stores_built_last_year_ = total_build_area_of_all_stores_built_last_year()
# print(total_build_area_of_all_stores_built_last_year_)
#
#



    # print(index['pincode'], index['city'])


