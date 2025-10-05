# Project: Analyzing-Crime-in-Los-Angeles

This is DataCamp project completed by myself
https://app.datacamp.com/learn/projects/1876

Description: 

Los Angeles, California, attracts people from all over the world, offering lots of opportunities, not always of the good kind!  In this project, you'll serve as a data detective, supporting the Los Angeles Police Department (LAPD) in analyzing crime data to guide how they should allocate resources to protect the people of their city!

Tasks:
- Which hour has the highest frequency of crimes? Store as an integer variable called peak_crime_hour.
- Which area has the largest frequency of night crimes (crimes committed between 10pm and 3:59am)? Save as a string variable called peak_night_crime_location.
- Identify the number of crimes committed against victims of different age groups. Save as a pandas Series called victim_ages, with age group labels "0-17", "18-25", "26-34", "35-44", "45-54", "55-64", and "65+" as the index and the frequency of crimes as the values.

Data descriptions:

1. 'DR_NO'	Division of Records Number: Official file number made up of a 2-digit year, area ID, and 5 digits.
2. 'Date Rptd'	Date reported - MM/DD/YYYY.
3. 'DATE OCC'	Date of occurrence - MM/DD/YYYY.
4. 'TIME OCC'	In 24-hour military time.
5. 'AREA NAME'	The 21 Geographic Areas or Patrol Divisions are also given a name designation that references a landmark or the surrounding community that it is responsible for. For example, the 77th Street Division is located at the intersection of South Broadway and 77th Street, serving neighborhoods in South Los Angeles.
6. 'Crm Cd Desc'	Indicates the crime committed.
7. 'Vict Age'	Victim's age in years.
8. 'Vict Sex'	Victim's sex: F: Female, M: Male, X: Unknown.
9. 'Vict Descent'	Victim's descent:
- A - Other Asian
- B - Black
- C - Chinese
- D - Cambodian
- F - Filipino
- G - Guamanian
- H - Hispanic/Latin/Mexican
- I - American Indian/Alaskan Native
- J - Japanese
- K - Korean
- L - Laotian
- O - Other
- P - Pacific Islander
- S - Samoan
- U - Hawaiian
- V - Vietnamese
- W - White
- X - Unknown
- Z - Asian Indian
10. 'Weapon Desc'	Description of the weapon used (if applicable).
11. 'Status Desc'	Crime status.
12. 'LOCATION'	Street address of the crime.