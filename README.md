# NYC_Subway_Schedules
Extracted CSVs of NYC subway timetables (12/01/2024)

## Extraction
`timetables_weekend.py` extracts all timetables from `weekend.html` and puts them in folders by weekend date ex. `Sunday_December_1_2024`. \\
`timetables_weekday.py` extracts all timetables from `weekday.html` and has no special organization.

## Cleaning
`cleaner.py` removes any numerical headings, duplicate headers, and organizes the headers to a standard of `STATION_NAME (DEPARTURE/ARRIVAL)` as opposed to the preset `STATION_NAME Departure` and `Arrival at STATION_NAME`.

## Current Extracted Period
`weekend.html` and `weekday.html` were extracted from their official timetable sites (https://www.panynj.gov/path/en/schedules-maps/weekday-schedules.html) and (https://www.panynj.gov/path/en/schedules-maps/weekend-schedules.html) respectfully on December 1, 2024.
