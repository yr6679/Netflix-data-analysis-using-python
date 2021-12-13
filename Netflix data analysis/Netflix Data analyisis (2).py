#!/usr/bin/env python
# coding: utf-8

# In[40]:


#For importing pandas library and the dataset
import pandas as pd
data= pd.read_csv("C:/Users/rawat/Downloads/8. Netflix Dataset.csv")


# In[41]:


data


# In[4]:


#to show top 5 records of the dataset
data.head()


# In[5]:


#to show bottom 5 records of the dataset
data.tail()


# In[6]:


#to show number of rows and coloumns
data.shape


# In[7]:


#to show each coloumn names
data.columns


# In[8]:


#to show data types of each coloumns
data.dtypes


# In[10]:


#to show indexex,coloumns,data types etc at once
data.info()


# In[11]:


#Task 1: To find any duplicate record in the data set?if yes then remove the record


# In[12]:


data.head()


# In[13]:


data.shape


# In[42]:


#to check row wise and detect duplicate data
data[data.duplicated()]


# In[33]:


#to remove duplicate data
data.drop_duplicates()


# In[43]:


#to make this change permanent
data.drop_duplicates(inplace=True)


# In[35]:


#Recheck
data[data.duplicated()]


# In[21]:


#two duplicate records removed
data.shape


# In[36]:


#task2:to check any null value present in any coloumn?if yes show with heat map
data.head()


# In[37]:


#to check null values
data.isnull()


# In[38]:


#to count the null values in each coloumn
data.isnull().sum()


# In[25]:


#for heat map we use seaborn library
import seaborn as sns


# In[26]:


#using heat map to show null values count
sns.heatmap(data.isnull())


# In[27]:


#Q1.For 'House of cards',what is show id and who is the director of this show?
data.head()


# In[29]:


#to show all rercord of a particular item in any coloumn
data[data['Title'].isin(['House of Cards'])]


# In[33]:


#Another way to show all rercord of a particular item in any coloumn 
data[data['Title'].str.contains('House of Cards')]


# In[34]:


#Q2 Which year highest number of the tv shows and movies are released?show with bar graph
data.dtypes


# In[44]:


data['Date_N'] = pd.to_datetime(data['Release_Date'])


# In[36]:


data.head()


# In[37]:


data.dtypes


# In[45]:


#to count the occurrence of all invidual years in date coloumn
data['Date_N'].dt.year.value_counts()


# In[39]:


data['Date_N'].dt.year.value_counts().plot(kind="bar")


# In[40]:


#Q3.How many Movies & tv shows are in the data set?show with bar graph.
 
data.head()


# In[42]:


#to group all unique items of a couomn and show the count
data.groupby('Category').Category.count()


# In[44]:


#to plot bar graph using seaborn library

sns.countplot(data['Category'])


# In[45]:


#Q4.show all the movies that were relased in year 2000.
data.head(2)


# In[46]:


#to create new year coloumn
data['Year']=data['Date_N'].dt.year


# In[48]:


data.head(2)


# In[47]:


#filtering:no movies released in 2000
data[(data['Category'] == 'Movie') & (data['Year']==2000)]


# In[48]:


#movies released in 2020
data[(data['Category'] == 'Movie') & (data['Year']==2020)]


# In[53]:


#Q5.show only the titles of all TV shows that were released in India only
data.head(2)


# In[55]:


data[(data['Category']=='TV Show') & (data['Country']== 'India')]['Title']


# In[56]:


#Q6.To show top 10 Directors ,who gave the highest number of tv shows & movies in netflix
data.head(2)


# In[57]:


data['Director'].value_counts().head(10)


# In[59]:


#Q7.To show all the recoreds where "Category" is movie and Type is comedies or"Country" is united kingdom

data.head(2)


# In[60]:


data[(data['Category']=='Movie') & (data['Type']=='Comedies') | (data['Country']=='United Kingdom')]


# In[61]:


#Q8. In how many movies/shows tom cruise was cast?

data.head(2)


# In[65]:


data[data['Cast']=='Tom Cruise']


# In[66]:


#creating new data frame and dropping rows xontaing null values
data_new=data.dropna()


# In[68]:


data_new.head(2)


# In[69]:


data_new[data_new['Cast'].str.contains('Tom Cruise')]


# In[70]:


#Q9.What are the different ratings defined by netflix
data.head(2)


# In[72]:


data['Rating'].nunique()


# In[73]:


data['Rating'].unique()


# In[6]:


#Q9.1 How many movies got 'TV-14'rating in canada?

data[(data['Category'] =='Movie') & (data['Rating']== 'TV-14') &(data['Country']=='Canada')]


# In[7]:


#Q10 What is the maximum duration of a movie/show on netflix?
data.head(2)


# In[8]:


data.Duration.unique()


# In[9]:


data.Duration.dtypes


# In[10]:


#str split
data[['Minutes','Unit']]=data['Duration'].str.split(' ',expand= True)


# In[11]:


data.head(2)


# In[12]:


data['Minutes'].max()


# In[13]:


data['Minutes'].min()


# In[14]:


data['Minutes'].mean()


# In[15]:


#Q11.Which individual country has the highest no. of tv shows?
data.head(2)


# In[16]:


data_tvshow=data[data['Category'] == 'TV Show']


# In[17]:


data_tvshow.head(2)


# In[18]:


data_tvshow.Country.value_counts()


# In[19]:


data_tvshow.Country.value_counts().head(1)


# In[49]:


#Q11.Sort by year
data.sort_values(by='Year')


# In[50]:


data.sort_values(by='Year',ascending=False).head(10)


# In[ ]:





# In[ ]:





# In[ ]:




