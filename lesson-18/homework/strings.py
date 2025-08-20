import pandas as pd

df = pd.read_csv('tackoverflow_qa.csv')

df['creationdate'] = pd.to_datetime(df['creationdate'])

before_2014 = df[df['creationdate'] < '2014-01-01']

print(before_2014)

import pandas as pd


df = pd.read_csv('tackoverflow_qa.csv')

high_score_df = df[df['score'] > 50]

print(high_score_df)

result = df[(df['score'] >= 50) & (df['score'] <= 100)]
result

result = df[df['ans_name'] == 'Scott Boston']
result

users = ["Scott Boston", "unutbu", "Warren Weckesser", "DSM", "jezrael"]


result = df[df['ans_name'].isin(users)]
result
df['creationdate'] = pd.to_datetime(df['creationdate'])

mask = (
    (df['creationdate'] >= "2014-03-01") &
    (df['creationdate'] <= "2014-10-31") &
    (df['ans_name'] == "unutbu") &
    (df['score'] < 5)
)

result = df[mask]
result

result = df[
    ((df['score'] >= 5) & (df['score'] <= 10)) | 
    (df['viewcount'] > 10000)
]
result

result = df[~df['ans_name'].isin(["Scott Boston"])]
result

titanic_df = pd.read_csv("titanic.csv")
titanic_df.head()
selected_df = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Age'] >= 20) &
    (titanic_df['Age'] <= 30)
]

selected_df

high_fare_df = titanic_df[titanic_df['Fare'] > 100]
high_fare_df

alone_survivors = titanic_df[
    (titanic_df['Survived'] == 1) & 
    (titanic_df['SibSp'] == 0) & 
    (titanic_df['Parch'] == 0)
]

alone_survivors
embarked_c_high_fare = titanic_df[
    (titanic_df['Embarked'] == 'C') &
    (titanic_df['Fare'] > 50)
]

embarked_c_high_fare
family_passengers = titanic_df[
    (titanic_df['SibSp'] > 0) &
    (titanic_df['Parch'] > 0)
]

family_passengers
young_non_survivors = titanic_df[
    (titanic_df['Age'] <= 15) & 
    (titanic_df['Survived'] == 0)
]

young_non_survivors
luxury_passengers = titanic_df[
    (titanic_df['Cabin'].notna()) & 
    (titanic_df['Fare'] > 200)
]

luxury_passengers
odd_id_passengers = titanic_df[titanic_df['PassengerId'] % 2 == 1]
odd_id_passengers
unique_ticket_passengers = titanic_df[
    titanic_df['Ticket'].isin(titanic_df['Ticket'].value_counts()[titanic_df['Ticket'].value_counts() == 1].index)
]

unique_ticket_passengers
miss_class1 = titanic_df[
    (titanic_df['Name'].str.contains("Miss")) &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Sex'] == "female")
]

miss_class1
