# UDG-ausbildung-code-challenge

## Projektbeschreibung

Dieses Projekt wurde im Rahmen einer Probeaufgabe erstellt. Ziel ist es, eine CSV-Datei zu importieren, die Daten tabellarisch darzustellen, Datensätze zu bearbeiten, zu löschen oder neue hinzuzufügen, eine grafische Auswertung (Tortendiagramm) zu erstellen und die bearbeiteten Daten wieder als CSV zu exportieren. Die gesamte Anwendung läuft über die Kommandozeile.

## Verwendete Technologien

- **Python 3.12**
- **pandas** – zur CSV-Verarbeitung (lesen, schreiben, filtern)
- **colorama** – für farbige und übersichtliche Konsolenausgaben
- **matplotlib** – zur Visualisierung der Daten als Tortendiagramm
- **os** – für Dateipfad- und Verzeichnisoperationen (Standardbibliothek)

## Projektstruktur

```plaintext
├ app.py                # Hauptanwendung (Kommandozeile)
├ requirements.txt      # Abhängigkeiten für Python
├ Ausgaben.csv          # Beispiel-CSV für Tests
├ README.md             # Projektbeschreibung und Anleitung
└ Aufgabenergebnis.pdf  # Offizielles Aufgaben-Dokument
```

##  Installation & Ausführung

### Voraussetzungen:
- Python 3.12 muss lokal installiert sein

### Schritte zur Ausführung:

```bash
$ git clone https://github.com/BenjaminNicoRitter/UDG-ausbildung-code-challenge
$ cd UDG-ausbildung-code-challenge
$ pip install -r requirements.txt
$ python app.py
```

### Hinweis:
- Alle Aktionen finden direkt in der Kommandozeile statt (Menüführung).
- Eine Beispieldatei (`Ausgaben.csv`) ist bereits enthalten.

## Features

- CSV-Datei importieren
- Datensätze anzeigen (tabellarisch)
- Datensätze bearbeiten, löschen oder neue hinzufügen
- CSV-Daten als Tortendiagramm visualisieren
- CSV-Dateien Speichern / Exportieren
