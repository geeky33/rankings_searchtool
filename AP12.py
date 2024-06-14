import matplotlib.pyplot as mp
import pandas as pd
import numpy as np
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
df = pd.read_csv('C:\\Users\\student\\Downloads\\Nirfrankingpropy1.csv', nrows=16)
while True:
    print('| INDIAN UNIVERSITY RANKING PROJECT (NIRF)|',)
    print('_________________________________','\n')
    print('_________________________________________','\n')
    print('| MAIN MENU |')
    print('-----------------------------------')
    print('''| 1.Display Data |
            \n| 2. Accessing Data |
            \n| 3. Data Manipulation |
            \n| 4. Data Analysis |
            \n| 5. Data Visualisation |''')
    print('_________________________________________')
    print()
    ch = int(input('Enter your choice :'))
    if ch == 1:
        print('--------------------------')
        print('| Display Data |')
        print('--------------------------')
        print('''| 1.Display full data |
               \n| 2.Display first n rows |
               \n| 3.Display last n rows |
               \n| 4.Exit |''')
        print('----------------------------')
        print()
        dis = int(input('Enter your choice :'))
        print()
        if dis == 1:
            print('---{ DISPLAYING FULL DATA }---')
            print()
            print(df)
        elif dis == 2:
            print('---{ FIRST n ROWS }---')
            print()
            f = int(input('Enter number of rows to be displayed:'))
            print()
            print(df.head(f))
        elif dis == 3:
            print('---{ LAST n ROWS }---')
            print()
            s = int(input('Enter number of rows to be displayed :'))
            print()
            print(df.tail(s))
        else:
               print('_________________________________')
    if ch == 2:
        print('-------------------------')
        print('| ACCESSING DATA |')
        print('-------------------------')
        print('''| 1.Individual columns |
                 \n| 2.Individual rows |''')
        print('-------------------------')
        print()
        a = int(input('Enter your choice :'))
        if a == 1:
            print(df.columns)
            print()
            ai = input('Enter the COLUMN to be accessed:')
            ai = ai.capitalize()
            print()
            print('-----------------------------------')
            print('| ACCESSING INDIVIDUAL COLUMN |')
            print('-----------------------------------')
            print(df[ai])
        if a == 2:
            print(df.columns)
            print()
            i1 = int(input('Enter the row index to be accessed: '))
            print()
            print('-------------------------------')
            print('| ACCESSING INDIVIDUAL ROW |')
            print('-------------------------------')
            print(df.loc[i1])
        if a == 3:
            pass
        else:
            print('_________________________________')
    if ch == 3:
        print('------------------------')
        print('| Data Manipulation |')
        print('------------------------')
        print('''| 1.Delete |
               \n| 2.Rename |
               \n| 3.Update |''')
        print('------------------------')
        print()
        man = int(input('Enter Your Choice:'))
        if man == 1:
            print('-------------------------------')
            print('| DELETE |')
            print('-------------------------------')
            print('''| 1.Delete Single Row |
                   \n| 2.Delete Multiple rows |
                   \n| 3.Delete Single column |
                   \n| 4.Delete Multiple column |''')

            print('-------------------------------')
            print()
            d = int(input('Enter your choice:'))
            if d == 1:
                print()
                i = int(input('Enter the index number of the row to be deleted:'))
                delete = df.drop(i)
                print(delete)
                print('ROW DELETED')
            if d == 2:
                print()
                r = int(input('Enter the number of rows to be deleted:'))
                print()
                for i in range(r):
                    re = int(input('Enter the row index to be deleted:'))
                    delete = df.drop(re)
                    print(delete)
                    print('ROWS DELETED')
            if d == 3:
                print(df.columns)
                print()
                c = input('Enter the column name to be deleted:')
                c = c.capitalize()
                delete = df.drop(c, axis=1)
                print(delete)
                print('COLUMN DELETED')
            if d == 4:
                print(df.columns)
                print()
                c = int(input('Enter the number of columns to be deleted:'))
                print()
                for i in range(c):
                    re = input('Enter the column name to be deleted:')
                    re = re.capitalize()
                    delete = df.drop(re, axis=1)
                    print(delete)
                    print('COLUMNS DELETED')
            if d == 5:
                pass
            else:
                print('_________________________________')
        if man == 2:
            print('-------------------------------')
            print('| RENAME |')
            print('-------------------------------')
            print('''| 1.Rename single column |
                   \n| 2.Rename multiple column |''')
            print('-------------------------------')
            print()
            r = int(input('Enter your choice:'))
            if r == 1:
                print(df.columns)
                print()
                r1 = input('Enter the column to be renamed:')
                r1 = r1.capitalize()
                print()
                r2 = input('Enter the new name to be put:')
                r2 = r2.capitalize()
                re = df.rename(columns={r1: r2}, inplace=False)
                print(re)
                print('COLUMN RENAMED')
            if r == 2:
                print(df.columns)
                print()
                rc = int(input('Enter the number of columns to be renamed:'))
                di = {}
                for i in range(rc):
                    x = input('Enter the column to be renamed:')
                    x = x.capitalize()
                    print()
                    y = input('Enter the new name to be put:')
                    y = y.capitalize()
                    re2 = df.rename(columns={x: y}, inplace=False)
                    print(re2)
                    print('COLUMNS RENAMED')
            if r == 3:
                pass
            else:
                print('_________________________________')
        if man == 3:
            print('-------------------------------------')
            print('| UPDATE |')
            print('-------------------------------------')
            print('''| 1.Update Particular value |''')
            print('-------------------------------------')
            print()
            u = int(input('Enter your choice:'))
            if u == 1:
                print(df.columns)
                print()
                u1 = input('Enter column name :')
                u1 = u1.capitalize()
                r = int(input('Enter the index number of row:'))
                print()
                u2 = input('Enter the new value:')
                if type(u2) == int:
                    u2 = int(u2)
                    n = df.at[r, u1] = u2
                else:
                    n = df.at[r, u1] = u2
                    print(n)
                    print(df)
                    print('COLUMN UPDATED')
        if man == 4:
            pass
        else:
            print()
            print('_________________________________')
    elif ch == 4:
        print('---------------------------------------')
        print('| DATA ANALYSIS |')
        print('---------------------------------------')
        print('''| 1.Minimum value |
                \n| 2.Maximum value |
                \n| 3.Shape |
                \n| 4.Mean |
                \n| 5.Median |
                \n| 6.Mode |
                \n| 7.Sort |
                \n| 8.Group by |''')
        print('---------------------------------------')
        print()
        an = int(input('Enter Your Choice:'))
        print()
        if an == 1:
            print(df.columns)
            print()
            print('TO DISPLAY THE MINIMUM VALUE')
            print()
            m = input('Enter the column name:')
            m = m.capitalize()
            print()
            print('Min Value:', df[m].min())
        if an == 2:
            print(df.columns)
            print()
            print('TO DISPLAY THE MAXIMUM VALUE')
            print()
            m = input('Enter the column name:')
            m = m.capitalize()
            print()
            print('Max Value:', df[m].max())
        if an == 3:
            print('SHAPE OF THE DATA')
            print()
            print(df.shape)
        if an == 4:
            print(df.columns)
            print('TO GET THE MEAN FROM THE DATA')
            print()
            m = input('Enter the column name:')
            m = m.capitalize()
            print(df[m].mean())
        if an == 5:
            print(df.columns)
            print('TO GET THE MEDIAN FROM THE DATA')
            print()
            m = input('Enter the column name:')
            m = m.capitalize()
            print(df[m].median())
        if an == 6:
            print(df.columns)
            print('TO GET THE MODE FROM THE DATA')
            print()
            m = input('Enter the column name:')
            m = m.capitalize()
            print(df[m].mode())
        if an == 7:
            print('------------------------------')
            print('| SORT |')
            print('------------------------------')
            print('''| 1.Sort in Ascending order |
                    \n| 2.Sort in Descending order |''')

            print('------------------------------')
            print()
            z = int(input('Enter your choice:'))
            if z == 1:
                (df.columns)
            print()
            print('FOR SORTING IN ASCENDING ORDER')
            print()
            s = input('Enter the column name:')
            s = s.capitalize()
            print()
            print(df.sort_values(s, inplace=False))
            print()
            print('SORTED IN ASCENDING ORDER')
            if z == 2:
                print(df.columns)
                print()
                print('FOR SORTING IN DESCENDING ORDER')
                print()
                s = input('Enter the column name:')
                s = s.capitalize()
                print()
                print(df.sort_values(s, inplace=False, ascending=False))
                print()
                print('SORTED IN DESCENDING ORDER')
            if z == 3:
                pass
            else:
                print('_________________________________')
        if an == 8:
            print('-------------------------------')
            print('| GROUP BY |')
            print('-------------------------------')
            print('''| 1.Group by count function |
                    \n| 2.Group by average function |''')
            print('-------------------------------')
            print()
            o = int(input('Enter your choice:'))
            if o == 1:
                print(df.columns)
                print()
                print('TO GROUP BY COUNT FUNCTION')
                print()
                o1 = input('Enter the first column name:')
                o1 = o1.capitalize()
                print()
                o2 = input('Enter the second column name:')
                o2 = o2.capitalize()
                print(df.groupby(o1)[o2].count())
                print()
            if o == 2:
                print(df.columns)
                print()
                print('TO GROUP BY AVERAGE FUNCTION')
                print()
                o1 = input('Enter the first column name:')
                o1 = o1.capitalize()
                print()
                o2 = input('Enter the second column name:')
                o2 = o2.capitalize()
                av = df.groupby(o1)[o2].mean()
                print(av)
                print()
            if o == 3:
                pass
            else:
                print('_________________________________')
        if an == 9:
            pass
        else:
            print('_________________________________')

    if ch == 5:
        print('----------------------------------------------')
        print('| DATA VISUALISATION |')
        print('----------------------------------------------')
        print('''| 1. Rank & Score |
                \n| 2. Rank & State |''')
        print('----------------------------------------------')
        print()
        v = int(input('Enter Your Choice:'))
        print()
        if v == 1:
            print('------------------------------')
            print('|RANK AND SCORE |')
            print('------------------------------')
            print('''| 1.Bar Chart |
                    \n| 2.Histogram |''')
            print('------------------------------')
            print()
            ip = int(input('Enter your choice:'))
            if ip == 1:
                h = df.head(50)
                mp.bar(h.Rank, h.Score, color='orange',
                       label='Score', edgecolor='black')
                mp.title(' RANK AND SCORE BAR CHART')
                mp.xlabel('Rank')
                mp.ylabel('Score')
                mp.legend()
                mp.show()
            elif ip == 2:
                h=df.head(50)
                mp.hist(df.Score, color='orange',
                        label='Score', edgecolor='black')
                mp.title('RANK AND SCORE HISTOGRAM')
                mp.xlabel('Rank')
                mp.ylabel('Score')
                mp.legend()
                mp.show()
            elif ip == 3:
                pass
            else:
                print('_________________________________')
        if v == 2:
            print('------------------------------')
            print('| RANK AND STATE |')
            print('------------------------------')
            print('''| 1.Bar Chart |
                    \n| 2.Histogram |''')
            print('------------------------------')
            print()
            choice = int(input('Enter your choice:'))
            if choice == 1:
                h = df.head(50)
                mp.bar(h.Rank, h.State, color='orange',
                       label='State', edgecolor='black')
                mp.title('RANK AND STATE BAR CHART')
                mp.xlabel('Rank')
                mp.ylabel('State')
                mp.legend()
                mp.show()
            elif choice == 2:
                h=df.head(50)
                mp.hist(df.State, color='orange',
                        label='State', edgecolor='black')
                mp.title('RANK AND STATE HISTOGRAM')
                mp.xlabel('Rank')
                mp.ylabel('State')
                mp.legend()
                mp.show()
            elif choice == 3:
                pass
            elif choice == 0:
                print('_________________________________')
    elif ch == 6:
        print('Dear user,you have exited the program successfully.')
        break
    else:
        print('_________________________________')
    # done.
