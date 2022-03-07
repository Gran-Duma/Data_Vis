Data_Vis

Goal of this project for now is to have a function take a data structure and let the user apply their choice of visualization to the dataset and save plots and data to file.

data_vis.py outside of the main data_vis function just has a temporary Python list defined and the function call with the list as the argument. If integrated into a GUI, the function could be called with a button press, taking the argument from user input (ex: from a data structure in memory or a saved csv/text file)

The .py file can be easily run in Spyder to test or directly in cmd line on windows if you install the matplotlib, seaborn, and pandas libraries.


A series of pop up windows should request from the user a file name that will be used for the output csv and png files. 

The user will be prompted with more windows asking if they wish to rename columns or rows.

The next prompt will ask what plot type the user wants to see. (scatter, bar)

Then what variables to be plotted. (ex: Column[0] as independent variable vs. column[2] as the dependent)
