import pandas as pd
import numpy as np
import datetime

def merge_time_series(df_1, df_2):
    df = df_1.merge(df_2, how='left', left_index=True, right_index=True)
    return df

def filter_by_date(dataframe, years=0):
    
    last_date = dataframe.tail(1).index
    year_nr = last_date.year.values[0]
    month_nr = last_date.month.values[0]
    day_nr = last_date.day.values[0]
    
    if month_nr == 2 and day_nr == 29:
        new_date = str(year_nr - years) + '-' + str(month_nr) + '-' + str(day_nr-1)        
    else:
        new_date = str(year_nr - years) + '-' + str(month_nr) + '-' + str(day_nr)
    
    df = dataframe.loc[new_date:]
    
    if (df.index[0] - df.index[-1]) < datetime.timedelta(days=365):
        dataframe = pd.concat([dataframe.loc[:new_date].tail(1), dataframe.loc[new_date:]])
        return dataframe
    else:
        dataframe = dataframe.loc[new_date:]
        return dataframe

def compute_rolling_cagr(dataframe, years):
    rolling_result = []
    number = len(dataframe)

    for i in np.arange(1, number + 1):
        df = dataframe.iloc[:i]
        df = filter_by_date(df, years=years)
        result = (((df.iloc[-1] / df.iloc[0]) ** (1/years) - 1))
        rolling_result.append(result[0])

    final_df = pd.DataFrame(data = rolling_result, index = dataframe.index[0:number], columns = ['Ret'])
    final_df = final_df.loc[dataframe.index[0] + pd.DateOffset(years=years):]
    return final_df    