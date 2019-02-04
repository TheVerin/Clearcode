"""Required tasks:
    - import the data,
    - check if the data are able to process,
    - change data into YYYY-MM-DD format,
    - filling 'Unknown' counrty as XXX
    - create column contains country code,
    - add column contains number of clicks,
    - remove country name and CTR column,
    - save as UTF-8 CSV file with Unix ending"""


import pandas as pd
import pycountry
import sys


def importing(data_path: str):
    """Importing data from given path"""
    try:
        return pd.read_csv(data_path, sep='\t', encoding='utf-16')
    except ImportError:
        print('Cannot import the data.')


def checking(data_frame):
    """Checking if there is right format of data and number of missing values"""
    if data_frame['impressions'].dtype != int:
        sys.stderr.write("Wrong type of data")
        return False
    else:
        for i in df.columns.values:
            if round((df[i].isnull().mean() * 100), 2) > 50:
                sys.stderr.write("Too many missing data")
        return True


def preprocessing(data_frame):
    """Function contains data changing tasks"""

    # Changing 'column date' from MM/DD/YYYY to YYYY-MM-DD
    data_frame['date'] = pd.to_datetime(data_frame.date)

    # Dealing with Unknown values
    data_frame = data_frame['state name'].replace('Unknown', 'XXX')

    # Creating 'country_code' column by mapping 'state date' using pycountry.
    data_frame['country_code'] = pycountry.countries.get(name=data_frame['state name']).alpha3

    # Adding 'clicks_num' column. In CTR column I have to remove '%' and convert column into float.
    data_frame['clicks_num'] = round(data_frame['impressions'] * data_frame['CTR'].astype(str).str[:-1].astype(float), 0)

    # Removing columns
    data_frame.drop(['state name', 'CTR'], axis=1, inplace=True)

    return data_frame


def saving(data_frame):
    """Saving data as data_after_preprocessing.csv in UTF-8 and Unix endings"""
    data_frame.to_csv('data_after_preprocessing.csv', sep='\t', encoding='utf-8', line_terminator='\n')


if __name__ == '__main__':
    df = importing('Here should be right path')
    if checking(df):
        df_pre = preprocessing(df)
        saving(df_pre)
