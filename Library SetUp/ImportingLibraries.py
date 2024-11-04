import math # this is an example of how we would import the math library, 
            # as explained earlier we import libraries by using the import function

# importing the libraries we need will be done like this:
import pandas
import matplotlib.pyplot

# now we are able to use the functions that are given in these libraries

#however we will be making a little adjustment to this method:

import pandas as pd
import matplotlib.pyplot as plt

'''Whenever you want to use the functions from any library you must do it in this format:

                    library_name.function_name
        
        To avoid having to write a longer code because som library names can be a bit too long, we can import a library and then represent it in a name of out choosing by writing 'as name_of_our_choice':

                    import matplotlib.pyplot as plt
                    import pandas as pd

        Now instead of, for example, writing pandas.function_name, you can just write pd.function_name.
'''