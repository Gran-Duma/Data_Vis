# takes list of any size and turns into pandas dataframe
# lets users name columns, lets users choose plot type
# and saves plot png and dataframe in same directory as .py file
def data_vis(data):

    # I don't know much about seaborn
    import matplotlib
    import matplotlib.pyplot as plt
    plt.style.use('classic')
    import pandas as pd
    import seaborn as sns
    sns.set()
    import tkinter as tk
    import sys as sys

    # we just need basic pop up windows for now
    ROOT = tk.Tk()
    ROOT.withdraw()

    # sub-functions for each plot type
    def scatter(data_frame,file_name,cols_renamed):

        a = tk.simpledialog.askstring(title=None,prompt='Independent Variable? (Type exactly as column name):')
        b = tk.simpledialog.askstring(title=None,prompt='Dependent Variable? (Type exactly as column name):')

        if cols_renamed == False:

            a = int(a)
            b = int(b)

        elif cols_renamed == True:

            pass

        # check to see if user chosen columns exist
        if a in data_frame.columns and b in data_frame.columns:

            sns.scatterplot(x=a, y=b, data=data_frame)

            plt.xlabel(a)
            plt.ylabel(b)

            # saves to same file as this .py file
            plt.savefig('%s.png' %file_name)

        else:
            tk.messagebox.showerror(title='Whoops', message='Columns not found')

    def bar(data_frame,file_name,cols_renamed):

        a = tk.simpledialog.askstring(title=None,prompt='Independent Variable? (Type exactly as column name):')
        b = tk.simpledialog.askstring(title=None,prompt='Dependent Variable? (Type exactly as column name):')

        if cols_renamed == False:

            a = int(a)
            b = int(b)

        elif cols_renamed == True:

            pass

        if a in data_frame.columns and b in data_frame.columns:

            sns.barplot(x=a, y=b, data=data_frame)

            plt.xlabel(a)
            plt.ylabel(b)

            plt.savefig('%s.png' %file_name)

        else:
            tk.messagebox.showerror(title='Whoops', message='Columns not found')

    def col_naming(data_frame):

        saved_inputs = []
        for i in range(len(df.columns)):

            # creates list of user chosen column names
            n_column = 'Column %s name?:' %i
            c_name = tk.simpledialog.askstring(title=None,prompt=n_column)
            saved_inputs.append(c_name)

        # updates dataframe with user chosen column names
        old_names = data_frame.columns.tolist()
        data_frame = data_frame.rename(columns=dict(zip(old_names, saved_inputs)))

        return data_frame

    def row_naming(data_frame):

        saved_inputs = []
        for i in range(len(df.index)):

            # creates list of user chosen row names
            n_row = 'Row%s name?:' %i
            r_name = tk.simpledialog.askstring(title=None,prompt=n_row)
            saved_inputs.append(r_name)

        # updates dataframe with user chosen row names
        old_names = data_frame.index.tolist()
        data_frame = data_frame.rename(index=dict(zip(old_names, saved_inputs)))

        return data_frame

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
    df.to_csv('%s.csv' %f_name)

    # asks user for plot type name and calls the approropriate function
    t_Plot = tk.simpledialog.askstring(title=None,prompt='Plot type?')
    if t_Plot in {'Scatterplot','scatterplot','Scatter plot','scatter plot','Scatter Plot','Scatter','scatter'}:

        scatter(df, f_name,cols_rn)

    elif t_Plot in {'Bar graph','Bar Graph','bar graph','Bar','bar'}:

        bar(df, f_name,cols_rn)

    else:

        tk.messagebox.showerror(title='Whoops', message='Plot type not found')

    # quit all tkinter stuff
    ROOT.destroy()

# data input
some_struct = [ [2,6,80],[5,7,90],[4,7,85] ]

data_vis(some_struct)
