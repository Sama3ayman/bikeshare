import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input('would you like to see data for chicago, new york city, washington? \n').lower()
    while city not in CITY_DATA:
        print('wrong value please enter city correctly \n')
        city=input('enter chicago, new york city, washington: \n').lower()
        
            
        
        
   
    # TO DO: get user input for month (all, january, february, ... , june)
    month=input('which month? all,january, february,march,april,may, june \n').lower()
    while month not in ['january','february','march','april','may','june','all']:
        print('wrong value please enter month correctly ')
        month=input('enter january, february,march,april,may, june: \n') .lower()
           
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('which day? (all, sunday, monday, tuesday, wednesday, thursday, friday, saturday) \n').lower()
    while day not in  ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']:
        print('wrong value please enter month correctly ')
        day=input('please enter: all, sunday, monday, tuesday, wednesday, thursday, friday, saturday \n' ).lower()
   

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    

    # TO DO: display the most common month
    most_common_month=df['month'].mode()[0]
    print('Most common month:', most_common_month)


    # TO DO: display the most common day of week
    most_common_day=df['day_of_week'].mode()[0]
    print(' most common day of week:', most_common_day)

    # TO DO: display the most common start hour
    most_common_hour=df['Start Time'].dt.hour.mode()[0]
    print(' most common start hour:', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station=df['Start Station'].mode()[0]
    print(' most commonly used start station:', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station=df['End Station'].mode()[0]
    print(' most commonly used end station:', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['most_common_start_end_station']=df['Start Station']+df['End Station']
    most_common_start_end_station=df['most_common_start_end_station'].mode()[0]
    print(' most commonly used start and end station:', most_common_start_end_station)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time=df['Trip Duration'].sum()
    print('total travel time=', travel_time)


    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('mean travel time=', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('counts of user types',user_types)


    # TO DO: Display counts of gender
  
    if str(city)!='washington':
        gender = df['Gender'].value_counts()
        print('counts of genders',gender)
        earliest_year=df['Birth Year'].min()
        print('earliest_year:',earliest_year)
        most_recent_year=df['Birth Year'].max()
        print('most_recent_year:',most_recent_year)
        most_common_year=df['Birth Year'].mode()
        print(' most_common_year :', most_common_year)
    elif str(city)=='washington':
        print('no gender data and birth year to share')


    # TO DO: Display earliest, most recent, and most common year of birth
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def dispaly_data(df):
    while True:
        
        view_data= input("Would you like to view individual trip data (5 entries)? Type 'yes' or 'no'\n").lower()
        start_loc = 0
        if view_data in  ['yes', 'no']:
            if view_data=='yes':
                print( df.iloc[start_loc:start_loc+5,:])
               
            break 
        else:
            print("Please enter a valid response")
    if  view_data=='yes':       
            while True:
               view_display = input("Do you wish to continue?: ").lower()

               if view_display in ['yes', 'no']:
                   if view_display=='yes':
                       start_loc += 5
                       print( df.iloc[start_loc:start_loc+5,:])
                   else:    
                        break  
               else:
                    print("Please enter a valid response")   
        
          
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        dispaly_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
