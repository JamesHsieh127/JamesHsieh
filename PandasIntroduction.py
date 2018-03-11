import pandas as pd
import numpy as np

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index)
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()

#Question 0
# You should write your whole answer within the function provided. The autograder will call
# this function and compare the return value against the correct solution value
def answer_zero():
    # This function returns the row for Afghanistan, which is a Series object. The assignment
    # question description will tell you the general format the autograder is expecting
    return df.iloc[0]

# You can examine what your function returns by calling it in the cell. If you have questions
# about the assignment formats, check out the discussion forums for any FAQs
answer_zero()

#Question 1
#Which country has won the most gold medals in summer games?
#This function should return a single string value.
def answer_one():
    most_gold_summer = max(df['Gold'])
    Ans1 = df[df['Gold'] == most_gold_summer].index.tolist()
    return Ans1[0]
answer_one()

#Question 2
#Which country had the biggest difference between their summer and winter gold medal counts?
#This function should return a single string value.
def answer_two():
    biggest_difference = max(df['Gold']-df['Gold.1'])
    Ans2 = df[df['Gold']-df['Gold.1'] == biggest_difference].index.tolist()
    return Ans2[0]
answer_two()

#Question 3
#Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count?
#Only include countries that have won at least 1 gold in both summer and winter.
#This function should return a single string value.
def answer_three():
    df_condition = df[(df['Gold']>0) & (df['Gold.1']>0)]
    biggest_difference = (abs(df_condition['Gold']-df_condition['Gold.1']) / df_condition['Gold.2'])
    Ans3 = biggest_difference.idxmax()
    return Ans3
answer_three()

#Question 4
#Write a function that creates a Series called "Points" which is a weighted value where each gold medal (Gold.2) counts for 3 points, silver medals (Silver.2) for 2 points, and bronze medals (Bronze.2) for 1 point.
#The function should return only the column (a Series object) which you created, with the country names as indices.
#This function should return a Series named Points of length 146
def answer_four():
    Points = (3*df['Gold.2']+ 2*df['Silver.2']+ 1*df['Bronze.2'])
    #print (len(Points))
    return Points
answer_four()

#Question 5
#Which state has the most counties in it? (hint: consider the sumlevel key carefully! You'll need this for future questions too...)
#This function should return a single string value.
import pandas as pd
census_df = pd.read_csv('census.csv')
census_df.head()

def answer_five():
    df_county = census_df[census_df['SUMLEV'] == 50]
    all_county = df_county.groupby('STNAME').count()
    Ans5= all_county['COUNTY'].idxmax()
    return Ans5
answer_five()

#Question 6
#Only looking at the three most populous counties for each state, what are the three most populous states (in order of highest population to lowest population)? Use CENSUS2010POP.
#This function should return a list of string values.
def answer_six():
    df_county = census_df[census_df['SUMLEV'] == 50]
    df_state = df_county.sort_values(['STNAME', 'CENSUS2010POP'],ascending=False).groupby('STNAME').head(3)
    Ans6 = df_state.groupby('STNAME').sum().sort_values(by='CENSUS2010POP').head(3).index.tolist()
    return Ans6
answer_six()

#Question 7
#Which county has had the largest absolute change in population within the period 2010-2015?
#(Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.)
#e.g. If County Population in the 5 year period is 100, 120, 80, 105, 100, 130, then its largest change in the period would be |130-80| = 50.
#This function should return a single string value.
def answer_seven():
    df_county = census_df[census_df['SUMLEV'] == 50]
    df_county['pop_change'] = abs(df_county['POPESTIMATE2015'] - df_county['POPESTIMATE2014'])+abs(df_county['POPESTIMATE2014'] - df_county['POPESTIMATE2013'])+abs(df_county['POPESTIMATE2013'] - df_county['POPESTIMATE2012'])+abs(df_county['POPESTIMATE2012'] - df_county['POPESTIMATE2011'])+abs(df_county['POPESTIMATE2011'] - df_county['POPESTIMATE2010'])
    Ans7 = df_county['CTYNAME'][df_county['pop_change']== max(df_county['pop_change'])].tolist()
    return Ans7[0]
answer_seven()

#Question 8
#In this datafile, the United States is broken up into four regions using the "REGION" column.
#Create a query that finds the counties that belong to regions 1 or 2, whose name starts with 'Washington', and whose POPESTIMATE2015 was greater than their POPESTIMATE 2014.
#This function should return a 5x2 DataFrame with the columns = ['STNAME', 'CTYNAME'] and the same index ID as the census_df (sorted ascending by index).
def answer_eight():
    df_county = census_df[census_df['SUMLEV'] == 50]
    Ans8 = df_county[((df_county['REGION']==1)|(df_county['REGION']==2))&(df_county['CTYNAME']=='Washington County')&(df_county['POPESTIMATE2015']>df_county['POPESTIMATE2014'])][['STNAME','CTYNAME']]
    return Ans8
answer_eight()
