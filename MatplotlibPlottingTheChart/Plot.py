import matplotlib.pyplot as plt


# In order to plot the DataFrame we made earlier we are going to use a function called .plot()
game_counts.plot(kind='bar', figsize=(12, 8), color=colors)
# In this function, you can set what kind of chart you want by sending the argument/ kind='' /you can choose 'bar', 'pie' and many more chart types.
# For our chart we will need to use 'bar' chart;
# The figsize argument sets how big the actual chart is going to be. In our case we will be using the dimensions 12 and 8 'figsize=(12, 8)'
# The colors that the different bars are going to be are also very customizable 'color = colors':
# In order to correctly represent the colors of all the bars we will have to create a dictionary, where the keys will be the different game genres and the values will be the actual colors.
# We will use this explicit dictionary in order to pinpoint the color accuracy:

colors = {
        "Action": "#ff9999",
        "Adventure": "#ffcc66",
        "Fighting": "#cccc66",
        "Misc": "#99cc66",
        "Platform": "#66cc99",
        "Puzzle": "#66cccc",
        "Racing": "#66ccff",
        "Role-Playing": "#6699cc",
        "Shooter": "#9966cc",
        "Simulation": "#cc66cc",
        "Sports": "#cc6699",
        "Strategy": "#cc9999"
        }

# Next we will have to set the names for the x and y axis of the chart.
# This is easily done using the 
plt.ylabel() # and
plt.xlabel() # functions. 
# Just write what you want your axis name to be inside the () brackets, also the text needs to be in quotations.

# The next step is to ensure that the platform names in the x-axis are horizontal
# To do this use the function:
plt.xticks(rotation=0)

# The next step is to create the legend for our chart, which will be done using the folowing line:
plt.legend(title='genre',bbox_to_anchor=(1.00, 0.75), loc='upper left')
# Let's explain what each argument in this function does:
#   1) The title of the legend, here it's 'title = 'genre''
#   2) The location of the legend compared to the chart is chosen using the loc= , here it is 'loc = 'upper left'', you can also set it to be right, center, in the corners and so on. 
#      The default will try to find the spot on the chart where the legend is most visible.
#      However if we just leave it at this, the Legend will be inside the chart. But we want it outside on the right center of the chart.
#   3) To avoid this we can send the bbox_to_anchor argument, for this Task it will be 'bbox_to_anchor=(1.00, 0.75)'.
#      You can play around with the values for it, one value represents the height, while the other how far left/right the legend will be from the chart.

# In order for everything to fit nicely on the window of the chart that will open once we run the program, we will use this function:
plt.tight_layout()


#Lastly we just need to show our chart, using the .show() function:

plt.show()
# Now if you run the "TaskChart1.py" you should see a chart that resembles the one in the 'example.png' file."
'''If you have gone through the entire file, you can close this one and return the the 'Project SetUp.txt' file.'''