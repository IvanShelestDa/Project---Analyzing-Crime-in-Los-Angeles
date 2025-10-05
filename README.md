
# Project: Analyzing Crime in Los Angeles

**Author:** *Completed independently by Ivan Shelest*

**Based on DataCamp project:** [Analyzing Crime in Los Angeles](https://app.datacamp.com/learn/projects/1876)

---

## Description

Los Angeles, California — a vibrant and diverse city that attracts people from all over the world, offering endless opportunities... not all of them good ones.

In this project, you will act as a **data detective** helping the **Los Angeles Police Department (LAPD)** analyze real crime data. The goal is to provide insights that can help the department allocate resources more effectively and make the city a safer place.

---

## Objectives

Tasks in this project include:

1. **Identify the hour with the highest frequency of crimes.**

   * Store the result as an integer variable called `peak_crime_hour`.

2. **Determine which area has the highest frequency of night crimes.**

   * Night crimes are defined as incidents occurring between **10:00 PM and 3:59 AM**.
   * Save the result as a string variable called `peak_night_crime_location`.

3. **Analyze victim age groups.**

   * Categorize victims into predefined age groups and count the number of crimes for each group.
   * Save this data as a pandas Series called `victim_ages`, where the index corresponds to age group labels and the values represent the number of crimes.

---

## Dataset Information

The dataset contains detailed information about reported crimes in Los Angeles. Below are the key columns used in this project:

| Column Name        | Description                                                                                               |
| ------------------ | --------------------------------------------------------------------------------------------------------- |
| **`DR_NO`**        | Division of Records Number — an official file number consisting of a 2-digit year, area ID, and 5 digits. |
| **`Date Rptd`**    | Date the crime was reported (`MM/DD/YYYY`).                                                               |
| **`DATE OCC`**     | Date the crime occurred (`MM/DD/YYYY`).                                                                   |
| **`TIME OCC`**     | Time of occurrence in **24-hour format**.                                                                 |
| **`AREA NAME`**    | Name of the LAPD geographic area (e.g., *Central*, *77th Street*, *Hollywood*).                           |
| **`Crm Cd Desc`**  | Description of the crime committed.                                                                       |
| **`Vict Age`**     | Victim's age (in years).                                                                                  |
| **`Vict Sex`**     | Victim's gender (`F`: Female, `M`: Male, `X`: Unknown).                                                   |
| **`Vict Descent`** | Victim's ethnic background. See list below.                                                               |
| **`Weapon Desc`**  | Description of the weapon used (if applicable).                                                           |
| **`Status Desc`**  | Status of the case (e.g., *Investigation Ongoing*, *Arrest Made*).                                        |
| **`LOCATION`**     | Address or intersection where the crime occurred.                                                         |

---

### Victim Descent Codes

| Code | Description                      | Code | Description      |
| ---- | -------------------------------- | ---- | ---------------- |
| A    | Other Asian                      | J    | Japanese         |
| B    | Black                            | K    | Korean           |
| C    | Chinese                          | L    | Laotian          |
| D    | Cambodian                        | O    | Other            |
| F    | Filipino                         | P    | Pacific Islander |
| G    | Guamanian                        | S    | Samoan           |
| H    | Hispanic / Latin / Mexican       | U    | Hawaiian         |
| I    | American Indian / Alaskan Native | V    | Vietnamese       |
| W    | White                            | X    | Unknown          |
| Z    | Asian Indian                     | –    | –                |

---

## Analytical Tasks in Python

Each step of the analysis was implemented using **pandas**, **numpy**, and **matplotlib/seaborn**.

**Tasks implemented:**

```python
# 1. Peak crime hour
peak_crime_hour = crimes.groupby('hour')['DR_NO'].size().idxmax()

# 2. Area with most night crimes (22:00–03:59)
night_time = crimes[(crimes['hour'] >= 22) | (crimes['hour'] <= 3)]
peak_night_crime_location = night_time.groupby('AREA NAME')['DR_NO'].size().idxmax()

# 3. Crimes by victim age group
age_labels = ["0-17", "18-25", "26-34", "35-44", "45-54", "55-64", "65+"]
age_bins = [0, 17, 25, 34, 44, 54, 64, 100]
crimes['Age Group'] = pd.cut(crimes['Vict Age'], bins=age_bins, labels=age_labels, right=True)
victim_ages = crimes.groupby('Age Group')['DR_NO'].count()
```

---

## Example Output

```
Hour with the largest volume of crimes: 12
Area with the highest frequency of night crimes: Central

Crimes committed against victims of different age groups:
0-17      4528
18-25    28291
26-34    47470
35-44    42157
45-54    28353
55-64    20169
65+      14747
Name: DR_NO, dtype: int64
```

---

## Technologies Used

* **Python 3.12**
* **pandas** — data manipulation
* **numpy** — numerical operations
* **matplotlib / seaborn** — data visualization
* **VS Code** — development environment

---

## Key Insights

* Most crimes occur around **12:00 PM**, during peak daytime activity.
* The **Central** area records the highest frequency of night-time crimes.
* The **26–34 age group** represents the most frequent victims of reported crimes.

---

## Repository Structure

```
Analyzing-Crime-in-Los-Angeles/
│
├── main.py          # Main Python analysis script
├── crimes.csv       # Dataset
├── README.md        # Project documentation
└── requirements.txt # (optional) List of dependencies
```

---

## Source

Dataset and problem description provided by **DataCamp** as part of the project:
🔗 [Analyzing Crime in Los Angeles](https://app.datacamp.com/learn/projects/1876)

---