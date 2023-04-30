import pandas as pd

#checking
df=pd.read_csv('Titanic2clean/Titanic.tsv',sep='\t')
print(df.head())
print(df.describe())

duplicates = df.duplicated()
print(duplicates.sum())

missing_data = df.isnull()
print(missing_data.sum())
print(missing_data.sum().sum())

print(df["Survived"].unique())
print(df["Pclass"].unique())
print(df["Sex"].unique())
print(df["SibSp"].unique())
print(df["Parch"].unique())
print(df["Embarked"].unique())

#reparing
df.drop_duplicates(inplace=True)
df["Sex"].replace({"malef": "male", "mal": "male", "fem":"female","femmale":"female","feemale":"female","Female":"female","malee":"male","F":"female"}, inplace=True)
df["Survived"].replace(-4,0,inplace=True)
df["Pclass"].replace(-2.0,2.0,inplace=True)
df["Survived"].replace(70,7,inplace=True)
df["Embarked"].replace({"So":"S","Co":"C","Qe":"Q"})

df=df.drop('Cabin',axis=1)
df=df.drop('Age',axis=1)
df=df.dropna(subset=["Ticket","Fare","Embarked"])
df.reset_index(drop=True,inplace=True)
df["PassengerId"]=df.index+1

df.to_csv('Titanic.tsv',sep="\t")