import pandas as pd


class Split:
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.df = dataframe

    def split_by_browser(self, dataframe: pd.DataFrame) -> None:
        return self.df.drop(columns=["browser"], axis=1)

    def split_by_platform(self, dataframe: pd.DataFrame) -> None:
        return self.df.drop(columns=["platform_os"], axis=1)

    def save_dataset(self, dataframe: pd.DataFrame) -> None:
        # dataframe.to_csv()
        pass
