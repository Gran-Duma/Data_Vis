#!/usr/bin/env python3

# takes list of any size and turns into pandas dataframe
# lets users name columns, lets users choose plot type
# and saves plot png and dataframe in same directory as .py file

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import tkinter as tk
import sys as sys

def data_vis(data):
    """Primary coordinating function"""
    sns.set()
    plt.style.use('classic')
    ROOT = tk.Tk()
    ROOT.withdraw()
    f_name = tk.simpledialog.askstring(title=None,prompt='File name?:')
    if f_name is None:

        tk.messagebox.showinfo(title=None,message='Ok, no plots for you')
        sys.exit()

    else:

        df = pd.DataFrame(data)

    ask_col_names = tk.messagebox.askquestion(title=None,message='Give custom column names?')
    if ask_col_names == 'yes':

        df = col_naming(df)
        cols_rn = True

    elif ask_col_names == 'no':

        tk.messagebox.showinfo(title=None,message='Columns will be indexed starting at 0')
        cols_rn= False

    ask_row_names = tk.messagebox.askquestion(title=None,message='Give custom row names?')
    if ask_row_names == 'yes':

        df = row_naming(df)
        rows_rn = True

    elif ask_row_names == 'no':

        tk.messagebox.showinfo(title=None,message='Rows will be indexed starting at 0')
        rows_rn= False

    # saves csv file to same dir as this .py file
    df.to_csv(f'{f_name}.csv')

    # asks user for plot type name and calls the approropriate function
    set_plot_type(df, f_name, cols_rn)

    # quit all tkinter stuff
    ROOT.destroy()

def set_plot_type(df, f_name, cols_rn):
    """prompts user to set the plot type to scatter or bar"""
    t_Plot = tk.simpledialog.askstring(title=None,prompt='Plot type? [scatter/bar]')
    if t_Plot in {'Scatterplot','scatterplot','Scatter plot','scatter plot','Scatter Plot','Scatter','scatter'}:

        scatter(df, f_name,cols_rn)

    elif t_Plot in {'Bar graph','Bar Graph','bar graph','Bar','bar'}:

        bar(df, f_name,cols_rn)

    else:

        tk.messagebox.showerror(title='Whoops', message='Plot type not found')
        set_plot_type(df, f_name, cols_rn)

def get_independent_var_name(columns):
    """Prompts user to select dependent variable"""
    a = tk.simpledialog.askstring(title=None,prompt=f'Independent Variable? {columns}:')
    if a not in columns:
        try:
            if int(a) not in columns:
                tk.messagebox.showerror(title='Whoops', message='Columns not found. Try again!')
                get_independent_var_name(columns)
            else:
                a = int(a)
        except ValueError:
            tk.messagebox.showerror(title='Whoops', message='Columns not found. Try again!')
            a = get_independent_var_name(columns)
    return a

def get_dependent_var_name(columns):
    """Prompts user to select dependent variable"""
    b = tk.simpledialog.askstring(title=None,prompt=f'Dependent Variable? {columns}:')
  
    if b not in columns:
        try:
            if int(b) not in columns:
                tk.messagebox.showerror(title='Whoops', message='Columns not found. Try again!')
                get_dependent_var_name(columns)
            else:
                b = int(b)
        except ValueError:
            tk.messagebox.showerror(title='Whoops', message='Columns not found. Try again!')
            b = get_dependent_var_name(columns)
    return(b)

def get_var_names(data_frame):
    """Calls the functions that get the independent and dependent variable names"""
    columns = list(data_frame.columns)
    a = get_independent_var_name(columns)
    b = get_dependent_var_name(columns)
    return a,b

def scatter(data_frame,file_name,cols_renamed):
    """creates and saves scatter plot output"""
    a,b = get_var_names(data_frame)

    if cols_renamed == False:

        a = int(a)
        b = int(b)

    elif cols_renamed == True:

        pass


    sns.scatterplot(x=a, y=b, data=data_frame)

    plt.xlabel(a)
    plt.ylabel(b)

    # saves to same file as this .py file
    plt.savefig(f'{file_name}.png')

def bar(data_frame,file_name,cols_renamed):
    """creates and saves bar plot output"""
    a,b = get_var_names(data_frame)

    if cols_renamed == False:

        a = int(a)
        b = int(b)

    elif cols_renamed == True:

        pass

    sns.barplot(x=a, y=b, data=data_frame)

    plt.xlabel(a)
    plt.ylabel(b)

    plt.savefig(f'{file_name}.png')

def col_naming(data_frame):
    """Renames columns"""
    saved_inputs = []
    for i in range(len(data_frame.columns)):

        # creates list of user chosen column names
        n_column = f'Column{i} name?:'
        c_name = tk.simpledialog.askstring(title=None,prompt=n_column)
        saved_inputs.append(c_name)

    # updates dataframe with user chosen column names
    old_names = data_frame.columns.tolist()
    data_frame = data_frame.rename(columns=dict(zip(old_names, saved_inputs)))

    return data_frame

def row_naming(data_frame):
    "Renames rows"
    saved_inputs = []
    for i in range(len(data_frame.index)):

        # creates list of user chosen row names
        n_row = f'Row{i} name?:'
        r_name = tk.simpledialog.askstring(title=None,prompt=n_row)
        saved_inputs.append(r_name)

    # updates dataframe with user chosen row names
    old_names = data_frame.index.tolist()
    data_frame = data_frame.rename(index=dict(zip(old_names, saved_inputs)))

    return data_frame



if __name__ == "__main__":
# data input
    some_struct = [ [2,6,80],[5,7,90],[4,7,85] ]

    data_vis(some_struct)
