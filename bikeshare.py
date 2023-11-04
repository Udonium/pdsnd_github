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
    user_input_city = input('\nWould you like to see data for Chicago, New York, or Washington?\nType the letters C for Chicago, NY for New York, or W for Washington: ')
    user_input_city = user_input_city.strip().lower()
    
    user_input_city_list = ['c', 'ny', 'w']
    while user_input_city not in user_input_city_list:
        print('\nYou typed wrong letter(s)!\n')
        user_input_city = input('\nType the letters C for Chicago, NY for New York, and W for Washington: ')
        user_input_city = user_input_city.lower()
   
    if user_input_city == 'c':
        print('\nYou choose to see data for Chicago\n')
        city = 'chicago'
    if user_input_city == 'ny':
        print('\nYou choose to see data for New York\n')
        city = 'new york city'
    if user_input_city == 'w':
        print('\nYou choose to see data for Washington\n')
        city = 'washington'

    # Initialize month and day variables
    month, day = None, None

     # Prompt the user to choose between filtering by month, day, or both
    print("\nDo you want to filter the data by month, day, both, or none?\n")
    filter_choice = input("\nEnter 'month', 'day', 'both', or none: ").strip().lower()

    while filter_choice not in ('month', 'day', 'both', 'none'):
        print("\nwrong entry! Please type 'month', 'day', 'both', or 'none' to choose your preferred filter\n")
        filter_choice = input("\nEnter 'month' if you'd like to filter data by month, 'day' if you'd like to filter data by day, 'both' if you'd like to filter data by both month and day, or 'none' for no filter: ").strip().lower()

    # Get user input for filtering by month
    if filter_choice in ('month', 'both'):
        while True:
            print("\nWhich month would you like to filter by?\n")
            month_choice = input("Enter month name (e.g., January, February, March, April, May, or June): ").capitalize()
            if month_choice in ['January', 'February', 'March', 'April', 'May', 'June']:
                month = month_choice
                break
            else:
                print("\nInvalid month. Please enter a valid month!\n")

    # Get user input for filtering by day
    if filter_choice in ('day', 'both'):
        while True:
            print("\nWhich day of the week would you like to filter by?\n")
            day = input("Enter day name (e.g., Monday to Sunday): ").capitalize()
            if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
                break
            else:
                print("\nInvalid day. Please enter a valid day!\n")


    print('-'*40)
    return city, month, day


def load_data(city, month=None, day=None):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # convert Start Time column from datetime datatype to string
    df['Start Time'] = df['Start Time'].astype(str)
    # extract hour data part of the Start Time column into a new column called start_hour
    df['start_hour'] = df['Start Time'].str[11:16]
    # convert to datetime datatype with HH:00 AM/PM format
    df['start_hour'] = pd.to_datetime(df['start_hour']).apply(lambda x: x.strftime("%I:00 %p"))
    # Ensure that Trip Duration column across the three datasets esp. washington data, is in integer datatype
    df['Trip Duration'] = df['Trip Duration'].astype(int)
    # Remove the first column in the dataframe which is unnamed
    df = df.drop(df.columns[0], axis=1)

    # filter by month if applicable
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    if month in months:
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def display_dataframe_rows(df):
    """Takes users input to display first five rows of the dataframe. Then takes another users input to keep displaying the next five rows"""

    start_idx = 0
    step = 5

    # Take user input
    user_input = input("\nDo you want to see the first 5 rows of the data? (Yes/No): ").strip().lower()
    while user_input not in ('yes', 'no'):
        print("\nInvalid Entry! Type 'yes' or 'no'\n")
        user_input = input("\nDo you want to see the first rows of the data? (Yes/No): ").strip().lower()

    # Print first five rows of dataframe
    if user_input == 'yes':
        print(df[start_idx:start_idx + step])

        # Take user input
        while start_idx < len(df):
            user_input = input("\nDo you want to see the next 5 rows of the data? (Yes/No): ").strip().lower()
            while user_input not in ('yes', 'no'):
                print("\nInvalid Entry! Type 'yes' or 'no'\n")
                user_input = input("\nDo you want to see the first rows of the data? (Yes/No): ").strip().lower()

            # Print next five rows of dataframe
            if user_input == 'yes':
                start_idx += step
                end_idx = start_idx + step
                print(df[start_idx:end_idx])
            else:
                break
        else:
            print("End of the DataFrame reached.")

    if user_input == 'no':
        print("\nNo rows will be displayed further.\n")



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June'}
    mode_month = months[df['month'].mode()[0]]
    print('\nThe most common month of travel is {}'.format(mode_month))


    # TO DO: display the most common day of week
    mode_day = df['day_of_week'].mode()[0]
    print('\nThe most common day of travel is {}'.format(mode_day))


    # TO DO: display the most common start hour
    mode_start_hour = df['start_hour'].mode()[0]
    print('\nThe most common trip start hour is {}'.format(mode_start_hour))


    # TO DO: display Top 10 start hours and Bottom 10 start hours
    # Top 10 start hours
    top_start_hours = df['start_hour'].value_counts().head(10)

    # Bottom 10 trip start stations
    bottom_start_hours = df['start_hour'].value_counts().tail(10)

    print("\nTop 10 start hours:")
    print(top_start_hours)

    print("\nBottom 10 start hours:")
    print(bottom_start_hours)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mode_start_station = df['Start Station'].mode()[0]
    print('\nThe most commonly used Start Station is {}'.format(mode_start_station))


    # TO DO: display most commonly used end station
    mode_end_station = df['End Station'].mode()[0]
    print('\nThe most commonly used End Station is {}'.format(mode_end_station))


    # TO DO: display Top 10 trip start stations and Bottom 10 trip start stations
    # Top 10 trip start stations
    top_start_stations = df['Start Station'].value_counts().head(10)

    # Bottom 10 trip start stations
    bottom_start_stations = df['Start Station'].value_counts().tail(10)

    print("\nTop 10 Trip Start Stations:")
    print(top_start_stations)

    print("\nBottom 10 Trip Start Stations:")
    print(bottom_start_stations)


    # TO DO: display most frequent combination of start station and end station trip
    # Initialize a dictionary to store combination counts
    combination_counts = {}

    # Iterate through rows and count combinations
    for index, row in df.iterrows():
        start_station = row['Start Station']
        end_station = row['End Station']
        combination = f"{start_station} to {end_station}"
    
        if combination in combination_counts:
            combination_counts[combination] += 1
        else:
            combination_counts[combination] = 1

    # Find the most frequent combination
    most_frequent_combination = max(combination_counts, key=combination_counts.get)

    print('\nThe most frequent combination of Start Station and End Station trip is: {}'.format(most_frequent_combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # display total travel time in hours : minutes : seconds format
    total_trip_duration_sec = df['Trip Duration'].sum()
    total_trip_duration_sec
    total_trip_duration_hour = total_trip_duration_sec // 3600
    remaining_min = (total_trip_duration_sec % 3600) // 60
    remaining_sec = total_trip_duration_sec % 60
    print('\nThe total travel time is {}hours, {}minutes, {}seconds'.format(total_trip_duration_hour, remaining_min, remaining_sec))


    # TO DO: display mean travel time
    # Display mean travel time in seconds
    mean_trip_duration_sec = df['Trip Duration'].mean()
    print('\nThe mean travel time is {}seconds'.format(mean_trip_duration_sec))


    # TO DO: display longest travel time with knownn user type
    # Remove rows with NaN in the 'User Type' column
    df.dropna(subset=['User Type'], inplace=True)
    # display longest travel time in hours : minutes : seconds format
    max_trip_duration_sec = df['Trip Duration'].max()
    max_trip_duration_hour = max_trip_duration_sec // 3600
    remaining_min = (max_trip_duration_sec % 3600) // 60
    remaining_sec = max_trip_duration_sec % 60
    print('\nThe longest travel time is {}hours: {}minutes: {}seconds'.format(max_trip_duration_hour, remaining_min, remaining_sec))


    # TO DO: display shortest travel time with knownn user type
    # display shortest travel time in hours : minutes : seconds format
    min_trip_duration_sec = df['Trip Duration'].min()
    min_trip_duration_hour = min_trip_duration_sec // 3600
    remaining_min = (min_trip_duration_sec % 3600) // 60
    remaining_sec = min_trip_duration_sec % 60
    print('\nThe shortest travel time is {}hours: {}minutes: {}seconds'.format(min_trip_duration_hour, remaining_min, remaining_sec))


    # TO DO: user type associated with the longest travel time and user type associated with the shortest travel time
    
    # Locate the user type associated with the longest travel time
    user_type_longest = df[df['Trip Duration'] == max_trip_duration_sec]['User Type'].values[0]

    # Locate the user type associated with the shortest travel time
    user_type_shortest = df[df['Trip Duration'] == min_trip_duration_sec]['User Type'].values[0]

    print(f"\nThe longest travel time was made by a {user_type_longest}.\n")
    print(f"\nThe shortest travel time was made by a {user_type_shortest}.\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare User Types."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('\nThe categories of Bikeshare users with their respective numbers are:')
    for category, count in user_type_count.items():
        print(f"{category:<12} {count}")


    # TO DO: Display the minimum, maximum, and average trip duration by user type in seconds
    # Remove rows with NaN in the 'User Type' column
    df.dropna(subset=['User Type'], inplace=True)
    # Group the data by 'User Type' and aggregate the statistics
    user_type_stats = df.groupby('User Type')['Trip Duration'].agg(['min', 'max', 'mean'])

    # Rename the columns for clarity
    user_type_stats = user_type_stats.rename(columns={'min': 'Min Trip Duration', 'max': 'Max Trip Duration', 'mean': 'Average Trip Duration'})

    # Display the results
    print('\nThe minimum, maximum, and average trip duration in seconds by user type are:\n', user_type_stats)


    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('\nThe number of Bikeshare users by gender are:')
        for category, count in gender_count.items():
            print(f"{category:<12} {count}")
    except:
        print('\nWashington data does not have Gender information!\n')


    # TO DO: Display earliest, most recent, and most common year of birth
    # Check if 'Birth Year' is a column in the DataFrame
    if 'Birth Year' in df.columns:
        # Remove NaN values from Birth Year
        df.dropna(subset=['Birth Year'], inplace=True)
        # Convert 'Birth Year' to integer
        df['Birth Year'] = df['Birth Year'].astype(int)
        # Display earliest year of birth
        min_birth_year = df['Birth Year'].min()
        print('The earliest year of birth is: {}'.format(min_birth_year))
        # Display most recent year of birth
        max_birth_year = df['Birth Year'].max()
        print('The most recent year of birth is: {}'.format(max_birth_year))
        # Display most common year of birth
        mode_birth_year = df['Birth Year'].mode()[0]
        print('The most common year of birth is: {}'.format(mode_birth_year))
    else:
        print('\nWashington data does not have Birth Year information!\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_dataframe_rows(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
