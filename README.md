>**Note**: Please **fork** the current Udacity repository so that you will have a **remote** repository in **your** Github account. Clone the remote repository to your local machine. Later, as a part of the project "Post your Work on Github", you will push your proposed changes to the remote repository in your Github account.
# BikeShare Project

## Date created
22nd October 2023

## Project Title
US Bikeshare Data Analysis

## Description
This Python script Project, bikeshare.py, analyzes bikeshare data for three major cities in US: Chicago, New York City, and Washington. It allows users to interactively explore and analyze various aspects of bikeshare data, such as the most common times of travel, popular stations, trip durations, and user statistics.

## Files used
- bikeshare.py
- chicago.csv
- new_york_city.csv
- washington.csv

## Credits
- Udacity's Data Science Nanodegree program for providing the project structure and guidance.

## Installation
To run the project, make sure you have Python 3 installed. You can download it from the official Python website: [Python](https://www.python.org/downloads/).

**Prerequisites:**
1. Python 3.x
2. Pandas
3. Numpy

**How to Run the Script:**
1. Open your terminal or command prompt.
2. Clone this repository to your local machine:
   ```shell
   git clone https://github.com/YourUsername/pdsnd_github.git
```
3. Navigate to the project directory:
   ```shell
   cd pdsnd_github
```
4. Run the project by executing the following command:
   ```shell
   python bikeshare.py
```

**Using the Script:**

- The script will ask you to select a city from Chicago, New York City, or Washington. You should type 'C' for Chicago, 'NY' for New York, or 'W' for Washington.

- You can choose to filter the data by month, day, both, or none. The script provides options for filtering the data by month and/or day.

- The script displays various statistics on bikeshare data, such as the most common times of travel, popular stations, trip durations, and user statistics.

- You can view the first five rows of the data and decide if you want to see the next five rows.

- The script allows you to restart and explore data for another city or with different filters.

**Script Structure:**

The script consists of the following main functions:

1. `get_filters()`: Asks the user to specify a city, month, and day for analysis.

2. `load_data(city, month, day)`: Loads data for the specified city and applies filters for month and day.

3. `display_dataframe_rows(df)`: Allows the user to view the first five rows of the DataFrame interactively.

4. `time_stats(df)`: Displays statistics on the most frequent times of travel.

5. `station_stats(df)`: Displays statistics on the most popular stations and trips.

6. `trip_duration_stats(df)`: Displays statistics on trip duration, including the longest and shortest travel times.

7. `user_stats(df)`: Displays statistics on user types, gender, and birth year.

8. `main()`: Controls the flow of the script and allows the user to interactively explore data and restart if needed.

## License
- Licensing information will be provided in subsequent revisions

## Acknowledgments
- Special thanks to Udacity for providing the project structure and guidance.

## Known Bugs
- There are currently no known bugs in this project.

## Updates and Revisions
- **[22nd October 2023]**: In this update, we have improved the user interface to make it more user-friendly and intuitive. We have also optimized data processing for faster results. Additionally, we fixed a minor issue related to date formatting for better accuracy.
