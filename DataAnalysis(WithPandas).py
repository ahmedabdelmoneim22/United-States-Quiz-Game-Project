#print("229. The Great Squirrel Census Data Analysis (with Pandas!)").
#We Learned how to do the basics of Data Analysis With Pandas.
##########
#2018 Central Park Squirrel Census - Squirrel Data.
#Export--->>>CSV.
#Work With Data library for Data Manipulation and Analysis.
import pandas
# 'file_path_or_url.csv' the CSV file you want to Read.
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data (1).csv")
print(data)
first_Column = data.iloc[:,0] # iloc[:,0];
Second_Column = data.iloc[:,1]
Third_Column = data.iloc[:,2]
Fourth_Column = data.iloc[:,3]
Fifth_Column = data.iloc[:,4]
Sixth_Column = data.iloc[:,5]
print("The first Column:*\n",first_Column)
print("The Second Column:*\n",Second_Column)
print("The Third Column:*\n",Third_Column)
print("The Fourth Column:*\n",Fourth_Column)
print("The Fifth Column:*\n",Fifth_Column)
print("The Sixth Column:*\n",Sixth_Column)
first_row = data.iloc[[0]]
print("The first Row:*\n",first_row)
print("First Element in Row:*",data.iloc[0, 0]) # [row, column];
print("Second Element in Row:*",data.iloc[0,1])
print("third Element in Row:*",data.iloc[0,2])
print("Fourth Element in Row:*",data.iloc[0,3])
print("Fifth Element in Row:*",data.iloc[0,4])
print("Sixth Element in Row:*",data.iloc[0,5])
print("Seventh Element in Row:*",data.iloc[0,6])
print("Eight Element in Row:*",data.iloc[0,7])
print("Ninth Element in Row:*",data.iloc[0,8])
print("Tenth Element in Row:*",data.iloc[0,9])
print("Eleventh Element in Row:*",data.iloc[0,10])
print("Twelfth Element in Row:*",data.iloc[0,11])
print("........................................")
"""
if 'Primary Fur Color' == 'Red':True;>>Condation.
"""
print(data["Primary Fur Color"]=="Red")
"""
Print the Column 'Primary Fur Color';
"""
print(data["Primary Fur Color"])
"""
Number of Color Red in Column['Primary Fur Color'] 
"""
print("Red-Number-in-Column:-",len(data[data["Primary Fur Color"]=="Red"]))
"""
Print:The Rows That has ['Primary Fur Color']=='Gray';
"""
print(data[data["Primary Fur Color"]=="Gray"])
"""
Convert-Column-To-List;
data["ColumnName"].to_list();
"""
Column_to_List = data["Primary Fur Color"].to_list()
print(Column_to_List)
"""
>>Select All Rows That has Color 'Gray';
"""
print(data[data["Primary Fur Color"]=="Gray"])
"""
>> Length of Color in Column; 
"""
gray_squirrels_count = len(data[data["Primary Fur Color"]=="Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"]=="Black"])
print("Rows Count has 'Gray' Color:-",gray_squirrels_count)
print("Rows Count has 'Cinnamon' Color:-",red_squirrels_count)
print("Rows Count has 'Black' Color:-",black_squirrels_count)
"""
>>Store The Result into DataFrame;
"""
"""
data_dict = {
        "Column-Name":["Column-Values"],
        "Column-Name":["Column-Values"]}
"""
data_dict = {
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[gray_squirrels_count,red_squirrels_count,black_squirrels_count]
}
print("DictionaryData=",data_dict)
# Convert Dictionary to DataFrame;
"""
pandas.DataFrame class represents 
a two-Dimensional Data Structure with labeled axes (rows and columns).
"""
"""
Create DataFrames() from other Data Sources such as 
CSV files 'Comma-separated values''قيم مفصولة بفواصل', 
Excel files,
SQL databases, 
Using functions Like 
>>pd.read_csv(), 
>>pd.read_excel(), 
>>pd.read_sql().
"""
df = pandas.DataFrame(data_dict)
print(df)
# >>to Save a pandas DataFrame to a CSV file;
df.to_csv("Data_count.csv")
###############################
###############################

