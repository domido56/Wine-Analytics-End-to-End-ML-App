# Wine Color Classification

## Opis projektu

Projekt polega na klasyfikacji koloru wina (**białe / czerwone**) na podstawie jego cech fizykochemicznych z wykorzystaniem metod uczenia maszynowego.

Celem było porównanie skuteczności trzech popularnych algorytmów:
- k-Nearest Neighbors (kNN)
- Random Forest
- Support Vector Machine (SVM)

Projekt obejmuje zarówno część analityczną (trenowanie i porównanie modeli), jak i aplikację webową umożliwiającą interaktywną predykcję.

## Dane

Wykorzystano zbiór danych **Wine Quality Dataset** z repozytorium UCI Machine Learning Repository.

Zbiór zawiera parametry fizykochemiczne wina, m.in.:
- volatile acidity
- chlorides
- total sulfur dioxide
- sulphates
- alcohol

## Przygotowanie danych

W ramach preprocessingu wykonano:
- standaryzację cech (`StandardScaler`)
- zrównoważenie klas metodą **SMOTE**
- podział na zbiór treningowy i testowy

## Trenowanie modeli

Modele zostały zoptymalizowane przy użyciu:
- `GridSearchCV` (dobór hiperparametrów)

Porównywane modele:
- kNN
- Random Forest
- SVM

## Wyniki

Uzyskane wyniki wskazują, że klasyfikatory **Random Forest** oraz **kNN** osiągnęły najwyższą skuteczność predykcji:

Accuracy ≈ **99%**

Dodatkowo analizowano:
- macierze pomyłek
- precision, recall, f1-score

## Aplikacja webowa

Projekt zawiera aplikację webową umożliwiającą predykcję koloru wina na podstawie danych wejściowych użytkownika.

### Technologie
- Python
- Flask
- scikit-learn
- HTML / CSS

### Funkcjonalności
- wprowadzanie danych przez suwaki
- predykcja koloru wina dla 3 modeli
- wizualizacja danych na wykresach (scatter plot)
- macierze pomyłek dla każdego modelu
- szczegółowe statystyki modeli (classification report)

## Przykładowe zdjęcia z aplikacji
<img width="1759" height="743" alt="strona_start_wykresy" src="https://github.com/user-attachments/assets/1bb8631d-2732-423b-b5af-ea0c9abed129" />

<img width="1709" height="714" alt="raport_svm" src="https://github.com/user-attachments/assets/3215099f-ae2f-4fc5-9782-d4db3be29181" />

## Instalacja 
### 1. Klonowanie repozytorium
Pobierz projekt na swój komputer:
```bash
git clone [https://github.com/domido56/Wine_prediction.git](https://github.com/domido56/Wine_prediction.git)
cd Wine_prediction
```
### 2. Środowisko wirtualne
Stwórz i aktywuj środowisko:
(Windows)
```bash
python -m venv venv
venv\Scripts\activate
```
### 3. Instalacja bibliotek
```bash
pip install -r requirements.txt
```
### 4. Uruchomienie aplikacji
```bash
python main.py
```
Aplikacja będzie dostępna pod adresem: http://127.0.0.1:5000/



