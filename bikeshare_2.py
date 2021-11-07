import time
import pandas as pd
import numpy as np

STATE_DATA = { 'chicago': r'E:\projects\bikeshare\chicago.csv',
              'new york city': r'E:\projects\bikeshare\new_york_city.csv',
              'washington': r'E:\projects\bikeshare\washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
   
    Returns:
        (str) state - name of the state to analyze it 
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('hello! let\'s explore some US bikeshare data!'.title())
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        state = input("Would you like to see soem data about(chicago, new york city, washington)?Please enter one of these states\n").lower().strip() 
        if state not in STATE_DATA:
            print("your choice is wrong please enter one of them (chicago, new york city, washington)".title())
        else:
            break    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input("please choose month from january to june or if you need to show all months please choose all\n").lower().strip()
        lsit_of_months =["january", "february","march","april","may", "june"]
        if month not in lsit_of_months and month != "all":
            print("your choice is wrong please enter the right month(full valid month) or enter -all- to show all months".title())
        else:
            break    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday) 
    while True:
        day=input("please choose a day of the week or if you need to show all days please choose all\n").lower().strip()
        list_of_days =["saturday", "sunday","monday","tuesday","wednesday", "thursday","friday"]
        if day not in list_of_days and day != "all":
            print("your choice is wrong please enter the right day(full calid day) or enter -all- to show all days".title())

        else:
            break
    print('-'*40)
    return state, month, day

def load_data(state, month, day):
    """
    Loads data for the specified state and filters by month and day if applicable.
    Args:
        (str) state - name of the state to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(STATE_DATA[state])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour 
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months =["january", "february","march","april","may", "june"]
        month = months.index(month)+1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()] # title method convert the first letter to capital letter
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel. """

    print('\nCalculating The Most Frequent Times of Travel...\n'.title())
    start_time = time.time()
    months =["january", "february","march","april","may", "june"]
    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print(f"The most common month is: {months[common_month-1]}".title())

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(f"The most common day of week is:{common_day} ".title())

    # TO DO: display the most common start hour
    common__hour = df['hour'].mode()[0]
    print(f"The most common start hour : {common__hour} ".title())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'* 50)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n'.title())
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_used_start_station = df['Start Station'].mode().tolist()
    print(f"The most commonly used start station is: {common_used_start_station} ".title())

    # TO DO: display most commonly used end station
    common_used_end_station = df['End Station'].mode().tolist()
    print(f"The most commonly used end station is: {common_used_end_station}".title())

    # TO DO: display most frequent combination of start station and end station trip
    combination_start_end = (df['Start Station'] + "||" + df['End Station']).mode().tolist()
    print(f"The most frequent combination of start station and end station trip is : {combination_start_end}".title())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n'.title())
    start_time = time.time()
    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print(f"The total travel time is: {total_time}".title())
    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print(f"The mean travel time is: {mean_time}".title())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(f"The count of user types:  \n {user_types}".title())
    # TO DO: Display counts of gender
    if "Gender" in df:
        gender = df['Gender'].value_counts()
        print(f"The count of user gender: \n {gender}")

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        earliest_by_year = df['Birth Year'].min()
        print(f'Earliest year of  birth : \n {earliest_by_year}'.title())
        recent_by_year = df['Birth Year'].max()
        print(f'Most recent year of birth is:\n {recent_by_year}')
        most_commonly_birth = df['Birth Year'].mode()[0]
        print(f'Most common year of birth is:\n {most_commonly_birth}')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw data on user request."""
    print(df.head())
    start_loc  = 0
    while True:
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        if view_data.lower() != 'yes':
            return
        start_loc += 5
        print(df.iloc[start_loc :start_loc +5])

def main():

    """This function is the main function which computes all the functions together and show all you data that has been chosen"""
    while True:
        state, month, day = get_filters()
        df = load_data(state, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        while True:
            view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
            if view_data.lower() != 'yes':
                break
            display_raw_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
 