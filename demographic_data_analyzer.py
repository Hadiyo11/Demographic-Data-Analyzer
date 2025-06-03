import pandas as pd

def calculate_demographic_data():
    df = pd.read_csv("adult.data.csv")

    # 1. Number of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage with Bachelors degree
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. Advanced education vs salary >50K
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    higher_education_rich = round(
        (df[higher_education]['salary'] == '>50K').mean() * 100, 1
    )
    lower_education_rich = round(
        (df[lower_education]['salary'] == '>50K').mean() * 100, 1
    )

    # 5. Minimum number of hours per week
    min_work_hours = df['hours-per-week'].min()

    # 6. Percentage of rich among those who work min hours
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage_min_hours = round(
        (num_min_workers['salary'] == '>50K').mean() * 100, 1
    )

    # 7. Country with highest percentage of rich
    rich_country = df[df['salary'] == '>50K']['native-country'].value_counts()
    total_country = df['native-country'].value_counts()
    rich_percentage_country = (rich_country / total_country * 100).dropna()

    highest_earning_country = rich_percentage_country.idxmax()
    highest_earning_country_percentage = round(rich_percentage_country.max(), 1)

    # 8. Top occupation in India among rich
    top_IN_occupation = df[
        (df['native-country'] == 'India') & (df['salary'] == '>50K')
    ]['occupation'].value_counts().idxmax()

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage_min_hours': rich_percentage_min_hours,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
