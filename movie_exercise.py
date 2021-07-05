# Import of Data set
# Convert to pandas
#Tasks: 
# Task1: Can you print the first 10 records
# Task2: What are the data types of the columns
# Task3: Count of Animation movies.
#        (Hint: use the count() function)
# Task4: Show the Comedy movies in the year 2007
# Task5: Count of Animation movies with more than 70% Audience Score
# Task6: Show the list of top 5 movies based on profitability.
# Task7: Show the top 5 Comedy movies approved by the audience. (hint : Audience Score)

#Task1:
import pandas as pd 
lst = ["Zack and Miri Make a Porno", "Youth in Revolt", "You Will Meet a Tall Dark Stranger", "When in Rome", "What Happens in Vegas", "Water For Elephants", "WALL-E", "Waitress", "Waiting For Forever", "Valentine's Day"]

df = pd.DataFrame(lst)
print(df)

