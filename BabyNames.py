#-----------------------------------------------------------
#The United States Social Security Administration publishes
#a list of all documented baby names each year, along with
#how often each name was used for boys and for girls. The
#list is used to see what names are most common in a given
#year.
#
#We've grabbed that data for any name used more than 25
#times, and provided it to you in a file called
#babynames.csv. The line below will open the file:
import pandas as pd
import numpy as np
column = ['Name','frequency','Gender']
names = pd.read_csv('../resource/lib/public/babynames.csv',header=None, names=column)

#names_file = open('../resource/lib/public/babynames.csv', 'r')

#column = ['Name','frequency','Gender']
name = pd.DataFrame(names)

print(names.head())
print('Total Number of Names:',len(names))
unique_names= names.Name.unique().size
print('Number of Unique Names:', unique_names)
Number_of_births = names.frequency.sum()
print('Number_of_births',Number_of_births)


print('No of Names starts with Z:',name[name['Name'].str.startswith('Z') & (name.Gender == 'Boy')].Name.count() )

a=name[name['Name'].str.startswith('Q') & (name.Gender == 'Girl')] 
a=a[a.frequency == a.frequency.max()].Name
print('frequent Name starts with Q',a)

b=np.array(name.Name)
print(len(b))

c= [char for char in b if char[0] in ('A','I','O','U','E')]
d= [char for char in b if char[-1].upper() in ('A','I','O','U','E')]
print('starts and ends with vowel',len(list(set(c)|set(d))))


#print(name['Name'].str[0].upper())
print(name[(name['Name'].str[0].str.upper().isin(['A','I','O','U','E']))][name['Name'].str[-1].str.lower().isin(['a','i','0','u','e'])]['Name'].size)  

#and (name[name['Name'].str[-1].isin(['a','i','0','u','e'])].Name))
#print(name['Name'].str[0] in (['A','I']))


xx = name.frequency.groupby(name.Name.str[0]).sum().sort_values()
#print(xx.sort_values())
yy = name.frequency.groupby(name.Name).sum().sort_values()
#print(yy)
Boys = name[name.Gender == 'Boy'] 
Girls = name[name.Gender == 'Girl']
print(type(Boys))

All = pd.merge(Boys,Girls, on='Name', how='inner')
print(All.head())
All['difference'] = abs(All.frequency_x - All.frequency_y)
print(All[['Name','difference']].sort_values(by='difference'))


#We've also provided a sample subset of the data in
#sample.csv.
#
#Each line of the file has three values, separated by
#commas. The first value is the name; the second value is
#the number of times the name was given in the 2010s (so
#far); and the third value is whether that count
#corresponds to girls or boys. Note that if a name is
#given to both girls and boys, it is listed twice: for
#example, so far in the 2010s, the name Jamie has been
#given to 611 boys and 1545 girls.
#
#Use this dataset to answer the questions below.


#Here, add any code you want to allow you to answer the
#questions asked below over on edX. This is just a sandbox
#for you to explore the dataset: nothing is required for
#submission here.





