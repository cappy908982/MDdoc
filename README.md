# DataMining
## Titanic Documentation

### First step: checking the dataset against:

    1. Outliers,
    2. Duplicates,
    3. Missing data,
    4. NaNs,
    5. Blanks (missing values),
    6. Wrong/improper values,
    7. Other data-related issues,

|Lp|L.of code|What I am doing                                                          |For what purpose                                                                         |
|--|---------|-------------------------------------------------------------------------|----------------|What information about data cleaning and preparation I've got from it|
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

Ordered list:
1. Number one
2. Number two
3. Number three
4. Number four

Unordered list:
- item one
- item two
- item three
- item four

**This is some example of the bold text.**
*This is some italic text.*
***This is some bold italic text.***

Equation:
$E=mc^2$