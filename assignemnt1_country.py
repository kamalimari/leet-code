import pandas
df = pandas.read_csv('exercise_1_location.csv')
print(df)
def function():
for index, row in df.iterrows():
    print(row['pincode'], row['city'])
