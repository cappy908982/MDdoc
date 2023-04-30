# DataMining
## Titanic Documentation

### First step: checking the dataset against

    1. Outliers,
    2. Duplicates,
    3. Missing data,
    4. NaNs,
    5. Blanks (missing values),
    6. Wrong/improper values,
    7. Other data-related issues,

|No|L.of code|What I am doing                                                          |For what purpose                                                                         |What information about data cleaning and preparation I've got from it|
|--|---------|-------------------------------------------------------------------------|----------------|-----------------------------------------|
|1 |1        |I'm importing a module called pandas                                     |For easier way to manage data flow between tsv file and the program                 |-|
|2 |4        |I'm reading a file "Titanic.tsv" by pandas.                              |I need to read the file in program before I start to repair it                         |-|
|2 |5        |I'm printing head of the file. It's default first five lines of that one.|I wanted to see some data, which are included in the file                                |Some of the lines has "Nan" value|
|3 |6        |Generate descriptive statistics.                                         |I can see some outliers now|for example PassengerId, shouldn't has minimal value of -12|
|4 |8        |Creating new Series denoting duplicate rows                              |To store the data about duplicated rows                                                  |-|
|5 |9        |Printing summary value of duplicated data                                |To see how many duplicated data are in the file                                        |3 records are duplicated|
|6 |11       |Creating new Series to detect missing values                             |To store index and boolean value for all of the missing values                           |-|
|7 |12       |Printing summary values of missing fields in columns                     |To see how many missing data are in each column                                        |There are 173 missing values in Age, 1 in Ticket, 1 in Fare, 686 in Cabin and 2 in Embarked|
|8 |13       |Printing summary value of missing data                                   |To see how many missing data are in all the file                                       |There are summary 863 missing/ NaN or blank values|
|9 |15       |Printing unique values of "Survived" field                               |To see what values does it contain                                                     |The value "-4" is incorrect, because that field should be similar to boolean. He survived or not, there is no more options.|
|10|16       |Printing unique values of "Pclass" field                                 |To see what values does it contain                                                     |On the internet there are some informations about Passenger Classes on the Titanic and value "-2." is incorrect|
|11|17       |Printing unique values of "Sex" field                                    |To see what values does it contain                                                     |There were 2 kind of sexes "male" and "female". "malef","mal","fem","femmale","feemale","Female","malee" and "F" are incorrect. 
|12|18       |Printing unique values of "SibSp" field                                  |To see what values does it contain                                                     |In my opinion there is no possibility to have number of siblings and spouses equal to 70.|
|13|19       |Printing unique values of "Parch" field                                  |To see what values does it contain                                                     |-|
|14|20       |Printing unique values of "Embarked" field                               |To see what values does it contain                                                     |Embarked values "S", "C" and "Q" are correct. "So", "Co", "Qe" and nan are incorrect.|

Things needed to be repair:
- There are 3 duplicated rows
- Some "Sex" values are written incorrect.
- Survived is kind of boolean value - shouldn't contain anything what isn't equal 1 or 2.
- Pclass should have values equal to 1, 2 or 3.
- In my opinion there is no possibility to have SibSp (siblings or spouse) equal to 70.
- Embarked has correct values "S", "C" and "Q", the rest are incorrect.
- There are 863 missing, NaN or blank values
- PassengerId has some strange and missing values.

### Second step: Repairing

|No|L.of code|What I am doing|What result did I get|
|--|---------|---------------|---------------------|
|1|23|dropping duplicated records from data frame|891 records of unique data|
|2|24|replacing all the incorrect data like "malee" by correct ones|2 different sexes|
|3|25|replacing value "-4" in Survived column to 0| All records in Survived column are equal to 0 or 1 now|
|4|26|replacing -2.0 in Pclass to 2.0|3 different possible values in Pclass: 1.0, 2.0 and 3.0|
|5|27|replacing 70 to 7 in SibSp|More real values of Siblings and spouses|
|6|28|replacing "So", "Co" and "Qe" to "S", "C" an "Q" in Embarked|Correct 3 Embarked values|
|7|30|Dropping the column Cabin, because in that column there is 686 missing, NaN or blank values|686 gaps less|
|8|31|Dropping the column Age, because in that column there is 173 missing, NaN or blank values|173 gaps less|
|9|32|Dropping rows where Ticket, Fare or Embarked are NaN, missing or blank values|No gaps left|
|10|33|Resseting indexes of existing dataframe|-|
|11|34|Adding indexes to "PassengerId" as a real index+1 (because we start count from 1)|to fill all the gaps and weird values there|

The last line of code (36) creates the new tsv file with cleaned & repaired data.