
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np
import time


# In[13]:


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


# Defining a function get_filters that asks user to specify city, month and day to analyse
# 
# 
# Returns:
#        (str)city - name of the city to analyse
#        
#        (str)month - name of the month to filter by, or 'all' for no filter at all
#        
#        (str) day - name of the day of week to filter by, or 'all' to apply no day filter

# In[14]:


def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        try:
            city = input('Which city data do you want? Choose from Chicago, New York City and Washington?')
            city = city.lower()
            if city in ['chicago','new york city','washington']:
                break
            else:
                raise ValueError
        except ValueError:
            print('Wrong input...Try again!')
    while True:
        try:
            month = input('Which month data do you want? january,february, march,april,may,june or all?')
            month = month.lower()
            if month in ['january','february','march','april','may','june','all']:
                break
            else:
                raise ValueError
        except ValueError:
            print('Wrong input..Try again!')
    while True:
        try:
            day = input('Which day data do you want?monday,tuesday,wednesday,thursday,friday,saturday,sunday or all?')
            day = day.lower()
            if day in ['sunday','monday','wednesday','thursday','friday','tuesday','saturday','all']:
                break
            else:
                raise ValueError
        except ValueError:
            print('Wrong input..Try again!')
    print('-'*40)
    return city, month, day
        


# Loading the data using load_data function for specified filters
# 
# Returns:
# 
#     Pandas DataFrame
#         
# Args:
# 
#    (str)city - name of the city to analyse
# 
#    (str)month - name of the month to filter by, or 'all' for no filter at all
# 
#    (str) day - name of the day of week to filter by, or 'all' to apply no day filter

# In[15]:


def load_data(city,month,day):
    filename = '.\{}'.format(CITY_DATA[city])
    df = pd.read_csv(filename)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        df = df[df['month']==month]
    
    if day != 'all':
        df = df[df['day_of_week']==day.title()]
        
    
    return df


# Displaying Statistics of most frequent times of travel
# 
# Displaying the most common month,day of week and start hour
# 

# In[16]:


def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    frequent_month = df['month'].mode()[0]
    print('The most frequent month is {}'.format(frequent_month))
    frequent_dayofweek = df['day_of_week'].mode()[0]
    print('The most frequent day of week is {}'.format(frequent_dayofweek))
    frequent_hour = df['hour'].mode()[0]
    print('The most frequent start hour is {}'.format(frequent_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)    


# Displaying statistics of most common station and trips
# 
# Displaying most commonly used start station, most commonly used end station, most frequent combination of both

# In[17]:


def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    print('\nThe most commonly used start station is {}\n'.format(df['Start Station'].mode()[0]))
    print('\nThe most commonly used end station is {}\n'.format(df['End Station'].mode()[0]))
    
    df['Station Combination'] = df['Start Station'] + df['End Station']
    
    print('\nThe most frequent combination of start station and end station trip is {}\n'.format(df['Station Combination'].mode()[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)   


# Displaying statistics on total and average trip duration

# In[18]:


def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    print('\nThe total trip duration is {}\n'.format(df['Trip Duration'].sum()))
    print('\nThe average trip duration is {}\n'.format(df['Trip Duration'].mean()))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)    


# Displaying Statistics on Bikeshare users

# In[19]:


def user_stats(df):
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    print('\nCount of user types is {}\n'.format(df['User Type'].value_counts()))
    if 'Gender' in df.columns:
        print('\nCount of gender types is {}\n'.format(df['Gender'].value_counts()))
    if 'Birth Year' in df.columns:
        print('\nEarliest year of birth for an user is {}\n'.format(df['Birth Year'].min()))
        print('\nMost recent year of birth for an user is {}\n'.format(df['Birth Year'].max()))
        print('\nMost common year of birth in users is {}\n'.format(df['Birth Year'].mode()[0]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)    


# In[20]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


# In[ ]:


if __name__ == "__main__":
    main()


# In[ ]:





