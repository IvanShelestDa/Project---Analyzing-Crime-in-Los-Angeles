# Re-run this cell
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
crimes = pd.read_csv("crimes.csv", parse_dates=["Date Rptd", "DATE OCC"], dtype={"TIME OCC": str})

# 1 task
crimes['hour'] = crimes['TIME OCC'].str[:2].astype(int)
peak_crime_hour = crimes.groupby('hour')['DR_NO'].size().idxmax()
print("Hour with the largest volume of crimes:", peak_crime_hour)

# 2 task
night_time = crimes[(crimes['hour'] >= 22) | (crimes['hour'] <= 3)]
peak_night_crime_location = night_time.groupby('AREA NAME')['DR_NO'].size().idxmax()
print("\nArea with the highest frequency of night crimes:", peak_night_crime_location)

# 3 task
age_labels = ["0-17", "18-25", "26-34", "35-44", "45-54", "55-64", "65+"]
age_bins = [0, 17, 25, 34, 44, 54, 64, 100]
crimes['Age Group'] = pd.cut(crimes['Vict Age'], bins=age_bins, labels=age_labels, right=True)
victim_ages = crimes.groupby('Age Group', observed=False)['DR_NO'].count()
print("\nCrimes committed against victims of different age groups:", victim_ages)

#plot 1
plt.figure(figsize=(8,5))
sns.histplot(data=crimes, x='hour', bins=24, kde=False, color='skyblue')
plt.title("Distribution of crimes by hour")
plt.xlabel("Hour of day")
plt.ylabel("Number of crimes")
plt.show()

#plot 2
plt.figure(figsize=(10,6))
sns.countplot(data=night_time, y='AREA NAME', order=night_time['AREA NAME'].value_counts().index, palette='viridis')
plt.title("Night crimes by area")
plt.xlabel("Number of crimes")
plt.ylabel("Area")
plt.show()

#plot 3
plt.figure(figsize=(8,5))
sns.barplot(x=victim_ages.index, y=victim_ages.values, palette='magma')
plt.title("Crimes committed against victims of different age groups")
plt.xlabel("Age group")
plt.ylabel("Number of crimes")
plt.show()