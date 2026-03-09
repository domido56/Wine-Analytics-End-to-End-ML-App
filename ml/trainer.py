import os
import joblib
import numpy as np
from ml.loader import get_full_dataset, features, target

from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE

RANDOM_STATE = 42

def train_all_models():
    os.makedirs("models", exist_ok=True)

    print("\nPoczekaj na utworzenie plików modeli oraz wybór najlepszych hiperparamatrów." \
    "Nie zajmie to więcej niż 5 min.")

    df = get_full_dataset()
    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, stratify=y, random_state=RANDOM_STATE
    )

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)

    # --- KNN ---
    knn_pipe = Pipeline(steps=[
        ("smote", SMOTE(random_state=RANDOM_STATE)),
        ("scaler", StandardScaler()),
        ("clf", KNeighborsClassifier())
    ])
    knn_grid = {
        "clf__n_neighbors": list(range(3, 25)),
        "clf__weights": ["uniform", "distance"],
        "clf__p": [1, 2]  #1-M, 2-E
    }
    knn_search = GridSearchCV(
        knn_pipe, knn_grid, cv=cv, n_jobs=-1, scoring="accuracy",
        return_train_score=True
    )
    knn_search.fit(X_train, y_train)
    joblib.dump(knn_search.best_estimator_, "models/knn.pkl")

    # --- SVM ---
    svm_pipe = Pipeline(steps=[
        ("smote", SMOTE(random_state=RANDOM_STATE)),
        ("scaler", StandardScaler()),
        ("clf", SVC(class_weight="balanced", probability=False, random_state=RANDOM_STATE))
    ])
    svm_grid = {
        "clf__kernel": ["linear", "rbf"],
        "clf__C": [0.1, 1, 5, 10, 20, 50, 100],
        "clf__gamma": ["scale", 0.01, 0.1, 1]
    }
    svm_search = GridSearchCV(
        svm_pipe, svm_grid, cv=cv, n_jobs=-1, scoring="accuracy",
        return_train_score=True
    )
    svm_search.fit(X_train, y_train)
    joblib.dump(svm_search.best_estimator_, "models/svm.pkl")

    # --- Random Forest ---
    rf_pipe = Pipeline(steps=[
        ("smote", SMOTE(random_state=RANDOM_STATE)),
        ("clf", RandomForestClassifier(class_weight="balanced", random_state=RANDOM_STATE))
    ])
    rf_grid = {
        "clf__n_estimators": [50, 100, 150, 200, 250],
        "clf__max_depth": [None, 5, 10, 20],
        "clf__min_samples_split": [2, 5, 10],
        "clf__min_samples_leaf": [1, 2, 4]
    }
    rf_search = GridSearchCV(
        rf_pipe, rf_grid, cv=cv, n_jobs=-1, scoring="accuracy",
        return_train_score=True
    )
    rf_search.fit(X_train, y_train)
    joblib.dump(rf_search.best_estimator_, "models/rf.pkl")

    # Dodatkowe logi do konsoli:
    print("\n=== Najlepsze parametry ===")
    print("KNN:", knn_search.best_params_, "CV acc:",
          knn_search.best_score_)
    print("SVM:", svm_search.best_params_, "CV acc:",
          svm_search.best_score_)
    print("RF :", rf_search.best_params_, "CV acc:",
          rf_search.best_score_)

    print("\nModele zapisane w folderze 'models' (każdy zawiera SMOTE/Scaler/Model).")

if __name__ == "__main__":
    train_all_models()
