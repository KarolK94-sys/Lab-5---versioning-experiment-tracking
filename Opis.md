Lab 5 – Data Versioning & Experiment Tracking
Celem laboratorium było zapoznanie się z narzędziami do wersjonowania danych oraz śledzenia eksperymentów uczenia maszynowego. W ramach zadania wykorzystano DVC do kontroli wersji danych oraz MLflow do rejestrowania eksperymentów i wyników modeli.
Laboratorium zostało podzielone na dwie części:

wersjonowanie danych przy użyciu DVC,
śledzenie eksperymentów z wykorzystaniem MLflow.


Część 1 – Data Versioning (DVC)
Dane wykorzystane w laboratorium (Ames Housing Dataset) zostały dodane do DVC. W repozytorium przechowywane są jedynie pliki metadanych (.dvc), natomiast same dane znajdują się w lokalnym repozytorium zdalnym.
W ramach tej części:

skonfigurowano DVC i zdalne repozytorium danych,
dodano pliki danych do kontroli wersji,
zapewniono możliwość odtworzenia dokładnej wersji danych użytej w eksperymentach.


Część 2 – Experiment Tracking (MLflow)
Druga część laboratorium dotyczyła śledzenia eksperymentów przy użyciu MLflow. Eksperymenty były uruchamiane lokalnie z wykorzystaniem serwera MLflow.
Eksperyment 1 – Scikit-learn (autologging)
W pierwszym ćwiczeniu wykorzystano mechanizm autologging dostępny w MLflow dla modeli Scikit-learn. Przetestowano pięć modeli:

Ridge Regression
Decision Tree
K-Nearest Neighbors
Random Forest
Gradient Boosting

Wszystkie parametry i metryki były logowane automatycznie. Najlepsze wyniki uzyskał model Gradient Boosting (R² ≈ 0.90), który wykazał najlepszą zdolność generalizacji.
Wnioski:

metody zespołowe (ensemble) osiągają lepsze wyniki niż pojedyncze drzewa,
model liniowy (Ridge) radzi sobie lepiej niż proste modele nieliniowe,
autologging znacząco upraszcza proces rejestrowania eksperymentów.


Eksperyment 2 – PyTorch (manual logging)
W drugim ćwiczeniu zaimplementowano prostą sieć neuronową w PyTorch. W tym przypadku zastosowano manualne logowanie metryk i parametrów do MLflow.
Model:

dwie warstwy ukryte (128 neuronów),
dropout = 0.1,
walidacja krzyżowa 5‑krotna.

Logowane były m.in.:

RMSE,
MAE,
R²,
wyniki dla poszczególnych foldów walidacji.

Zastosowanie walidacji krzyżowej pozwoliło zauważyć różnice pomiędzy foldami (jeden z nich osiągnął znacznie gorszy wynik), co pokazuje znaczenie takiego podejścia przy ocenie stabilności modelu.
Dodatkowo do MLflow zapisano metadane DVC, co pozwala jednoznacznie powiązać wyniki eksperymentu z konkretną wersją danych.

Porównanie autologging vs manual logging

Autologging – szybki i wygodny, idealny dla standardowych eksperymentów w Scikit-learn.
Manual logging – większa kontrola nad tym, co jest zapisywane, konieczny przy niestandardowych pętlach treningowych (np. PyTorch).

Oba podejścia zostały wykorzystane i porównane w ramach laboratorium.

Reprodukowalność
Projekt jest w pełni odtwarzalny:

kod znajduje się w repozytorium Git,
dane są wersjonowane przy użyciu DVC,
eksperymenty i wyniki są zapisane w MLflow.

Dzięki temu możliwe jest ponowne uruchomienie eksperymentów z tą samą wersją danych i tymi samymi parametrami.

Podsumowanie
W ramach laboratorium:

poprawnie skonfigurowano DVC i MLflow,
przeprowadzono eksperymenty z autologgingiem i manualnym logowaniem,
przeanalizowano wyniki różnych modeli,
zapewniono pełną reprodukowalność eksperymentów.
