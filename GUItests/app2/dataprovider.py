import pandas as pd
from config import SOURCE

class dataProvider(object):
    # deals with the data

    COLS = ["hello","there"]

    def __init__(self):
        self.data = data = pd.read_excel(SOURCE)

    def update_filter(self):
        # update masks to filter which data to show
        print("DP: some filter updates... WIP")
        pass