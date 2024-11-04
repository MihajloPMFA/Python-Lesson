import pandas as pd

# We first need to read the file that contains all the data.
# We will use the pd.read_csv() function that accepts the file path to the file you want to read.
# However in order to avoid giving the function the whole file path, we will simply do 2 things:
#           1) we will only send the file name to the function
#           2) move the dataset.csv file in the same folder that you'r "ChartTaskProgress.py" file is located
# Now we are able to just send the name of the file that contains the data to the function. See the following example of what that would look like.

#example:
pd.read_csv("dataset.csv")

# However because this function returns a DataFrame we must give this function a variable that it can return the DataFrame to. Let's use a variable name 'data':

data = pd.read_csv("dataset.csv")

# Feel free to write this code into you'r "ChartTaskProgress.py".
# Then you can print out the data variable, and in the terminal you will see a DataFrame that should look like the one in the "DataFrameExample.txt" example file.
# As you have probably noticed, the data is a lot easier to read this way, and the Pandas library will allow us to manipulate this DataFrame to fit our needs for the plotting proccess.
# Please return to the "Pandas.txt" file and continue to the next step.