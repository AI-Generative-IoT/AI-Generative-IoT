# **Diamanten Preis Vorhersage Modell**

## **1. Überblick**
Das Modell wurde entwickelt, um den Preis von Diamanten basierend auf verschiedenen Merkmalen wie **carat**, **cut**, **color**, **clarity** und weiteren Attributen vorherzusagen. Der Datensatz stammt aus dem **Seaborn Diamonds Dataset**.

## **2. Datensatz**
- **Zielvariable**: Preis des Diamanten (`price`)
- **Features**:
  - **carat**: Gewicht des Diamanten (in Karat)
  - **cut**: Qualität des Schliffs (nominal)
  - **color**: Farbqualität des Diamanten (nominal)
  - **clarity**: Reinheit des Diamanten (nominal)
  - **depth**: Tiefenmaß des Diamanten
  - **table**: Tischgröße des Diamanten
  - **x, y, z**: Abmessungen des Diamanten (Länge, Breite, Höhe)

## **3. Vorverarbeitung**
- **Kategorische Variablen** (`cut`, `color`, `clarity`) wurden mit **LabelEncoding** in numerische Werte umgewandelt, um sie als Eingabedaten für die Modelle zu verwenden.

## **4. Modellierung**
- **Modelle verwendet**:
  - **Decision Tree Regressor**
  - **Random Forest Regressor**
  
- **Ziel**: Vorhersage des Diamantenpreises basierend auf den Eingabemerkmalen.

## **5. Evaluierung**
### **Performance Metriken**:
#### Decision Tree Regressor:
- **R² Score**: `0.98`
- **MSE**: `126,000`

#### Random Forest Regressor:
- **R² Score**: `0.99`
- **MSE**: `78,000`

- Der **Random Forest Regressor** zeigt eine bessere Leistung, da er eine genauere Schätzung für den Preis des Diamanten bietet.

## **6. Feature-Wichtigkeit (Random Forest)**

- **Wichtigste Merkmale**:
  - **carat**: Sehr wichtig für die Preisvorhersage.
  - **depth** und **x**: Mittlere Bedeutung.
  - **cut**, **color** und **clarity**: Weniger wichtig, aber dennoch signifikant.

### **Feature Importance Diagramm**
Das folgende Diagramm zeigt die Bedeutung der einzelnen Merkmale:

![Feature Importance](feature_importance_plot.png)

## **7. Vorhersagefunktion**

Die Funktion `predict_diamond_price` erlaubt es, für neue Diamanten Vorhersagen zu treffen, basierend auf deren Eigenschaften. Die Eingabewerte müssen wie folgt sein:

- **carat**: Gewicht des Diamanten (z. B. `0.75`)
- **cut**: Qualität des Schliffs (z. B. `Ideal`)
- **color**: Farbqualität des Diamanten (z. B. `G`)
- **clarity**: Reinheit des Diamanten (z. B. `VS2`)
- **depth**: Tiefe des Diamanten (z. B. `61.5`)
- **table**: Tischgröße (z. B. `57.0`)
- **x, y, z**: Abmessungen (Länge, Breite, Höhe)

### Beispiel:
```python
predicted_price = predict_diamond_price(
    carat=0.75, 
    cut='Ideal', 
    color='G', 
    clarity='VS2', 
    depth=61.5, 
    table=57.0, 
    x=5.8, 
    y=5.9, 
    z=3.6
)
print(f"Predicted Price: ${predicted_price}")

