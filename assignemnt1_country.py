import pandas
df = pandas.read_csv('exercise_1_store.csv')
store_name = []
build_area = []
date_of_area = []
pincode = []


for index, row in df.iterrows():
    store_name.append(row[0])
    build_area.append(row[1])
    date_of_area.append(row[2])
    pincode.append(row[3])


def build_area_greater_than_4000():
    build_area_greater_than_4000_ = []
    for i in range(len(build_area)):
        if build_area[i] > 4000:
            build_area_greater_than_4000_.append(store_name[i])
    print(build_area_greater_than_4000_)


build_area_greater_than_4000()




    # print(index['pincode'], index['city'])


