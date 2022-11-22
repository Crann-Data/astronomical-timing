from datetime import timedelta, date, datetime
from astral import LocationInfo
from astral.sun import sun
import pandas as pd
import matplotlib.pyplot as plt

time_format = "%H:%M:%S"

city = LocationInfo("Berlin", "Germany", "Europe/Berlin")

def format_time(date_time):
    return pd.to_datetime(date_time.strftime('%H:%M:%S'))

if __name__ == "__main__":
    cycles = {}
    for day in range(50, 0, -1):
        s_alt = {}
        s = sun(city.observer, date=date.today() - timedelta(days=day))
        dict = {k: format_time(v) for k, v in s.items()}
        cycles[date.today() - timedelta(days=day)] = dict
    cycles = pd.DataFrame(cycles)
    cycles = cycles.T
    cycles.index = pd.to_datetime(cycles.index)
    cycles.index.name='timestamp'
    print(cycles.info())
    cycles.plot()
    plt.show()
    cycles.to_csv("data/sun.csv")
