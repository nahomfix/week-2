import imp

import dvc.api
import mlflow
import pandas as pd
from joblib import load

from scripts.config import Config

path = "data/AdSmartABdata.csv"
repo = "remote"
version = "v1.0"


data_url = dvc.api.get_url(path=path, repo=repo, rev=version)


mlflow.set_experiment("raw-data")


if __name__ == "__main__":
    data = pd.read_csv(data_url, sep=",")

    mlflow.log_param("data_url", data_url)
    mlflow.log_param("data_version", version)

    model = load((Config.MODELS_PATH / "random_forest.pkl").resolve())
