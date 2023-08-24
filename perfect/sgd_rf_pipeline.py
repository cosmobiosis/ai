from prefect import flow, task
from training_data_loader import *
from sklearn.base import ClassifierMixin
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier
from typing import Tuple

import pandas as pd

from typing_extensions import Annotated

@task
def random_forest_trainer_mlflow(
    X_train: pd.DataFrame,
    y_train: pd.Series,
) -> ClassifierMixin:
    """Train a sklearn Random Forest classifier and log to MLflow."""
    model = RandomForestClassifier()
    model.fit(X_train.to_numpy(), y_train.to_numpy())
    train_acc = model.score(X_train.to_numpy(), y_train.to_numpy())
    print(f"Train accuracy: {train_acc}")
    return model

@task
def sgd_trainer_mlflow(
    X_train: pd.DataFrame,
    y_train: pd.Series,
) -> ClassifierMixin:
    """Train a SGD classifier and log to MLflow."""
    model = SGDClassifier()
    model.fit(X_train.to_numpy(), y_train.to_numpy())
    train_acc = model.score(X_train.to_numpy(), y_train.to_numpy())
    print(f"Train accuracy: {train_acc}")
    return model

@task
def best_model_selector(
    X_test: pd.DataFrame,
    y_test: pd.Series,
    model1: ClassifierMixin,
    model2: ClassifierMixin,
) -> Tuple[
    Annotated[ClassifierMixin, "best_model"],
    Annotated[float, "best_model_test_acc"],
]:
    """Calculate the accuracy on the test set and return the best model and its accuracy."""
    test_acc1 = model1.score(X_test.to_numpy(), y_test.to_numpy())
    test_acc2 = model2.score(X_test.to_numpy(), y_test.to_numpy())
    print(f"Test accuracy ({model1.__class__.__name__}): {test_acc1}")
    print(f"Test accuracy ({model2.__class__.__name__}): {test_acc2}")
    if test_acc1 > test_acc2:
        best_model = model1
        best_model_test_acc = test_acc1
    else:
        best_model = model2
        best_model_test_acc = test_acc2
    return best_model, best_model_test_acc

@flow(name="Main")
def main():
    """Train a model."""
    X_train, X_test, y_train, y_test = training_data_loader()
    model1 = random_forest_trainer_mlflow(X_train=X_train, y_train=y_train)
    model2 = sgd_trainer_mlflow(X_train=X_train, y_train=y_train)
    best_model, best_model_test_acc = best_model_selector(
        X_test=X_test, y_test=y_test, model1=model1, model2=model2
    )
    print(best_model_test_acc)

if __name__ == "__main__":
    main()