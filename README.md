# yj_hixpy
Eine Pythonfunktion, um Texte mittels Hohenheimer Verständlichkeitsindex (HIX) zu prüfen.
Der Hohenheimer Verständlichkeitsindex (HIX) wird benutzt, um die Verständlichkeit von deutschsprachigen Textenobjetiv bewerten und vergleichen zu können.
Mehr dazu und zur Arbeit von [Frank Breitschneider und Claudia Thoms](https://klartext.uni-hohenheim.de/hix) an der Universität Hohenheim gibt es beispielsweise auch in
Brettschneider, Frank (2019). Verständliche PR-Sprache – Klartext statt Kauderwelsch. In: Ternès, A., Englert, M. (eds) Digitale Unternehmensführung. Springer Gabler, Wiesbaden. [https://doi.org/10.1007/978-3-658-23053-1_10](https://doi.org/10.1007/978-3-658-23053-1_10).
Der Fremdwortanteil wird derzeit nicht berücksichtigt von dieser Funktion.

- Because HIX is something quite uniquely applicable to German texts, this readme is solely in German.

# Vorausseztungen
- Python 3

# Benutzung
```
import yj_hixpy
yjCalcHIX(strText)
```
Danach kann die Funktion ganz normal benutzt werden und gibt den HIX (von 0 bis 20) zurück:
```
strText = """
Das ist ein Beispieltext.
Er enthält mehrere Sätze, die unterschiedlich lang sind. 
Einige Wörter sind auch unterschiedlich lang. Die durchschnittliche Wortlänge variiert somit.
"""
hix_value = yjCalcHIX(strText)
print("Der Hohenheimer Verständlichkeitsindex (HIX) für den gegebenen Text beträgt:", hix_value)
```

# todos
- Fremdwörter berücksichtigen
- hardening
