# Wine Color Classification

## Opis projektu

Celem niniejszej pracy było porównanie skuteczności trzech popularnych klasyfikatorów uczenia maszynowego w zadaniu rozróżniania koloru wina (białe lub czerwone) na podstawie jego cech fizykochemicznych.

Analizie poddano następujące algorytmy:

- k-Nearest Neighbors (kNN)
- Random Forest
- Support Vector Machine (SVM)

## Dane

W badaniach wykorzystano dane pochodzące ze zbioru **Wine Quality Dataset** dostępnego w repozytorium:

UCI Machine Learning Repository

Zbiór danych zawiera informacje o właściwościach fizykochemicznych win, takich jak m.in.:

- volatile acidity
- total sulfur dioxide
- chlorides
- sulphates

## Przygotowanie danych

Proces przygotowania danych obejmował:

- standaryzację cech
- zrównoważenie zbioru danych metodą **SMOTE**
- podział danych na zestaw treningowy i testowy

## Trenowanie modeli

Każdy z modeli został zoptymalizowany przy użyciu metody **GridSearchCV** w celu doboru najlepszych hiperparametrów.

Porównano skuteczność następujących klasyfikatorów:

- kNN
- Random Forest
- SVM

## Wyniki

Uzyskane wyniki wskazują, że klasyfikatory **Random Forest** oraz **kNN** osiągnęły najwyższą skuteczność predykcji:

Accuracy ≈ **99%**

## Aplikacja webowa

W ramach pracy opracowano również aplikację webową umożliwiającą interaktywną predykcję koloru wina na podstawie wartości cech wprowadzonych przez użytkownika.

Aplikacja została zrealizowana z wykorzystaniem:

- Python
- Flask
- wytrenowanych modeli ML

Użytkownik może wprowadzić wartości cech fizykochemicznych wina poprzez odpowiednie ustawienie paska z wartościami, a aplikacja zwraca przewidywany kolor wina.
Dostępne są również wykresy z wizualizacją wyników. Na interfejsie znajdują się dwa wykresy rozrzutu wprowadzonych danych na tle całego zbioru. 
W podstronach znajdują się wizualizuje macierzy pomyłek (oddzielne podstrony dla każdego z modeli).

## Wnioski

Przeprowadzone badania potwierdzają, że metody uczenia maszynowego mogą z wysoką skutecznością wspomagać proces klasyfikacji danych enologicznych.

Implementacja aplikacji webowej stanowi przykład praktycznego zastosowania algorytmów klasyfikacji w analizie chemicznej.
