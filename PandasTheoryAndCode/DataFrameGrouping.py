import pandas as pd

data = pd.read_csv("dataset.csv")
platforms = ['PS4', 'XOne', 'PC', 'WiiU']
filtered_data = data[data['platform'].isin(platforms)]

# In order to successfully group our DataFrame we will implement the following line of code:
game_counts = filtered_data.groupby(['platform', 'genre']).size().unstack().fillna(0)
# Although this single line looks complicated, it is actually really easy to understand
# Lets explain what this line of code does, one part a a time:
#       1) .groupby() function will group the DataFrame by a single or a list of column names 
            filtered_data.groupby(['platform', 'genre'])# we will be grouping our DataFrame, first by 'platform' and if the platforms are the same, by 'genre'
#           1.1) You can see the example in the file "GroupingDataFrames1.txt"
#                If you tried to print this out on your own you wouldn't exactly get a DataFrame but a adress to one.
#                To fix this you could use some additional function
#       2) The next function .size() is actually a good example we can use. If you were to print out this line of code:
            filtered_data.groupby(['platform', 'genre']).size() # you would be shown a grouped DataFrame, where the size paramater would be telling you how many instances of each 'genre' there were for every 'platform'
            #See example in the file "GroupingDataFrames2.txt"
#       3) .unstack() function will place all the genre to be column names, and all the platform names in the place of row indexes
#       If you open the file "Unstacked.txt" you can see the readibility of the data we need to create the chart has drasticaly improved.
#       However, you will notice that in some spots there is not a number but NaN, which means that the value is Not Available.
#       This is there the final part comes in.
#       4).fillna(0) which will go throught each value inside the DataFrame, and when it encounters the 'NaN' message, it will replace it with 0. 
#       For example, look again in the "Unstacked.txt" file and look at the DataFrame under the line "After .fillna(0)"

# And that is how we group this particular DataFrame.

# All thats left for this portion of the Task is to sort the DataFrame rows
# This is because, you will notice in the current DataFrame, the order of platforms from top to bottom does not match with the order on the x - axis in the chart
# All we need to do is use the follwing line of code:
game_counts = game_counts.sort_values("Action", ascending=False)
# The function .sort_values() will accept a argument that it will sort the DataFrame rows by, and ascending= which is True by default
# We will be sorting the values based on the values in the column 'Action', and the ascending argument will be set to False
# If you are wondering why we will be sorting by the 'Action' column, open the 'example.png' file again and notice that, from the left to right, the number of games that fall in the 'Action' genre is decreasing.
# We don't really have to sort it this way but it is just more convenient to in this case.
                       
#If you have fully gone through this file, return to the "Pandas.txt" file.