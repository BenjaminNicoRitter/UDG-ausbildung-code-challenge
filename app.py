"""imports"""
import pandas as pd
import os
from colorama import Fore
import matplotlib.pyplot as plt


def plot_data(df):
    """Zeigt ein Diagramm mit den prozentualen Werten der Kategorien."""
    # Überprüft ob das dataframe leer ist, gibt einen Fehler zurück falls es leer ist
    if df.empty:    
        print("Die CSV-Datei ist leer. Es kann kein Diagramm angezeigt werden.")
        return
    # Berechnung der Prozentwerte
    total_value = df['Wert'].sum()  # Berechnet den Gesamtwert aller Kategorien
    df['Prozent'] = (df['Wert'] / total_value) * 100    # Berechnet die prozentualen Anteile jeder Kategorie 
    # Erstellt ein Tortendiagramm
    plt.figure(figsize=(8, 6))  # Legt die größe vom Diagramm fest
    plt.pie(df['Prozent'], labels=df['Kategorie'], autopct='%1.1f%%', startangle=90)    # Erste das Tortendiagramm
    plt.title("Prozentuale Verteilung der Kategorien")  # Gibt dem Diagramm einen Namen / Titel
    plt.axis('equal')  # Sorgt dafür, dass das Diagramm rund ist
    plt.show()  # Zeigt das Diagramm an


def clear_screen():
    """Lässt den screen cleaner aussehen, indem er einmal quasi gecleared wird. Funktioniert am besten, wenn man das terminal normal skaliert und gezoomt hat."""
    print(50*"\n")  # Schreibt 50 Leere Zeilen


def load_csv(CSV_FILE):
    """Lädt die CSV-Datei oder erstellt eine neue, falls sie nicht existiert."""
    if os.path.exists(CSV_FILE):    # Überprüft, ob die Datei existiert
        try:
            return pd.read_csv(CSV_FILE)    # Gibt den Inhalt der Datei zurück
        except Exception as e:  # Falls es einen Fehler beim Laden gibt, wird dies dem User hier mitgeteilt
            print(Fore.RED + f"Fehler beim Laden der Datei: {e}" + Fore.RESET)
            return pd.DataFrame(columns=["Kategorie", "Wert"])
    else:
        return pd.DataFrame(columns=["Kategorie", "Wert"])


def list_csv_files():
    """Listet alle CSV-Dateien im aktuellen Verzeichnis auf."""
    files = []
    # Sammelt alle CSV-Dateien und fügt die an die Liste files an
    for i in os.listdir():
        if i.endswith('.csv'):
            files.append(i)
    # Überprüft, ob es CSV-Dateien im Verzeichnis gibt
    if not files:
        # Gibt Fehler an den User zurück
        print("Keine CSV-Dateien im aktuellen Verzeichnis gefunden.")
        return []
    else:
        # Gibt alle verfügbaren CSV-Dateien aus
        print("\nVerfügbare CSV-Dateien:")
        for i, file in enumerate(files, 1):
            print(f"{i}. {file}")


def create_csv():
    """User kann eine CSV-Datei erstellen."""
    temp_name = input(Fore.GREEN + "\nGib einen Namen für die neue CSV-Datei ein: " + Fore.RESET) + ".csv"  # Setzt temp_name zu der Eingabe des Users plus '.csv' als Dateiendung
    new_csv = {"Kategorie": [], "Wert": []} # Erstellt das Gerüst für die neue CSV-Datei
    df = pd.DataFrame(new_csv)  # Erstellt neues Dataframe nach dem vorherigen Gerüst / Schema
    df.to_csv(temp_name, index=False)   # Erstellt CSV-Datei mit dem vom User angegebenen Namen
    print("Neue CSV-Datei wurde erfolgreich erstellt.")
    input(Fore.YELLOW + "Drücke enter zum fortsetzen\n" + Fore.RESET)
    clear_screen()
    

def select_file():
    """User kann eine CSV-Datei auswählen."""
    files = []
    # Sammelt alle CSV-Dateien und fügt die an die Liste files an
    for i in os.listdir():
        if i.endswith('.csv'):
            files.append(i)
    # Überprüft, ob es CSV-Dateien im Verzeichnis gibt
    if not files:
        print("Keine CSV-Dateien im aktuellen Verzeichnis gefunden.")
        return create_csv() # Sendet den User zum CSV erstellungsmenü
    # Gibt alle verfügbaren CSV-Dateien aus 
    print("Verfügbare CSV-Dateien:")
    for idx, file in enumerate(files, 1):
        print(f"{idx}. {file}")
    # User kann eine vorhandene CSV-Datei auswählen, bei falscher Eingabe wird er erneur aufgefordert eine Datei auszuwählen
    while True:
        try:
            choice = int(input(Fore.GREEN + "Wähle eine Datei (Zahl eingeben): " + Fore.RESET))
            try:
                sel_file = files[choice - 1]    # setzt sel_file zu der vom user gewählen Datei
                print("CSV-Datei wurde erfolgreich ausgewählt.\n")
                input(Fore.YELLOW + "Drücke enter zum fortsetzen\n" + Fore.RESET)
                clear_screen()
                return sel_file
            except:
                print(Fore.RED + "\nDas ist keine gültige Eingabe!" + Fore.RESET)
        except:
            print(Fore.RED + "\nDas ist keine gültige Eingabe!" + Fore.RESET)


def show_data(df):
    """Zeigt dem User den aktuellen Inhalt der CSV-Datei"""
    # Gibt dem User feedback, falls das dataframe leer ist
    if df.empty:
        print("Die CSV ist aktuell leer.")
    else:
        # Zeigt dem User den Inhalt der gewählten CSV-Datei
        print("\nAktueller Inhalt der CSV:\n")
        print(df.to_string(index=False))


def add_data(df, file_name):
    """User kann Daten in die CSV-Datei hinzufügen."""
    # Fragt den User wie die Kategorie heißen soll
    kategorie = input(Fore.GREEN + "Kategorie hinzufügen (z.B. 'Lebensmittel'): " + Fore.RESET)
    # Fragt den User wie der Wert sein soll
    while True:
        wert = input(Fore.GREEN + "Wert (numerisch): " + Fore.RESET)
        try:
            wert = float(wert)  # Setzt den Wert von einem string zu einem float
            break
        except ValueError:
            # Gibt Feedback an den User falls die Eingabe ungültig ist
            print(Fore.RED + "Der Wert muss eine Zahl sein!")
            input(Fore.YELLOW + "Drücke enter zum fortsetzen\n" + Fore.RESET)
            clear_screen()
    # Neuer Eintrag wird übertragen
    neuer_eintrag = pd.DataFrame([{"Kategorie": kategorie, "Wert": wert}])  # Ordnet die Angaben vom User ins richtige Schema
    df = pd.concat([df, neuer_eintrag], ignore_index=True)  # Erstellt den neuen Eintrag in der CSV-Datei bzw. erst einmal im dataframe
    df.to_csv(file_name, index=False)   # Speichert die Änderungen vom dataframe in die CSV-Datei
    print(Fore.LIGHTGREEN_EX + "Datensatz hinzugefügt!" + Fore.RESET)
    return df


def del_data(df, file_name):
    """User kann Daten aus der CSV-Datei entfernen."""
    # Zeigt dem User noch einmal den Inhalt der CSV-Datei
    show_data(df)
    # Setzt die Variable 'kategorie' zur Eingabe des Users
    kategorie = input(Fore.GREEN + "\nKategorie entfernen: " + Fore.RESET)
    if not df[df['Kategorie'] == kategorie].empty:  # Überprüft, ob die Kategorie in der Datei vorhanden ist
        # Fragt den User, ob der Eintrag wirklich gelöscht werden soll
        choice = input(Fore.GREEN + "Wollen sie diesen Eintrag wirklich löchen? [j|n]\n" + Fore.RESET)
        if choice == "j" or choice == "J":
            df = df[df['Kategorie'] != kategorie]   # erstellt ein neues dataframe, das dem alten deckungsgleich ist, nur dass die von User angegebene Kategorie entfernt wird 
            df.to_csv(file_name, index=False)   # Speichert das dataframe in die CSV-Datei
            print(Fore.LIGHTGREEN_EX + "Eintrag erfolgreich entfernt!")
        else:
            print(Fore.LIGHTGREEN_EX + "Eintrag wird nicht entfernt.")
    else:
        print(Fore.RED + "Kategorie nicht gefunden!")
    return df


def edit_data(df, file_name):
    """User kann Daten in der CSV-Datei bearbeiten."""
    # Zeigt dem User noch einmal den Inhalt der CSV-Datei
    show_data(df)
    # Setzt die Variable 'kategorie' zur Eingabe des Users
    kategorie = input(Fore.GREEN + "\nWert aus Kategorie bearbeiten: " + Fore.RESET)
    if not df[df['Kategorie'] == kategorie].empty:  # Überprüft, ob die Kategorie in der Datei vorhanden ist
        while True:
            # Fragt User so lange nach neuen Wert, bis der User einen gültigen Wert eingibt
            neuer_wert = input(Fore.GREEN + "\nNeuen Wert (numerisch) eingeben: " + Fore.RESET)
            try:
                neuer_wert = float(neuer_wert)  # Convertiert die Eingabe des Users von einem string zu einem float
                break
            except ValueError:
                print(Fore.RED + "Der Wert muss eine Zahl sein!")
        df.loc[df['Kategorie'] == kategorie, 'Wert'] = neuer_wert   # Lokalisiert im dataframe / in der CSV-Datei die angegebene Kategorie
        df.to_csv(file_name, index=False)   # Speichert das dataframe in der CSV-Datei
        print(Fore.LIGHTGREEN_EX + "Wert erfolgreich bearbeitet!")
    else:
        print(Fore.RED + "Kategorie nicht gefunden!")
    return df


def file_menu(file_name):
    """Submenu, wird aufgerufen wenn User eine Datei ausgewählt hat."""
    df = load_csv(file_name)    # Lädt die CSV-Datei
    # Ruft das Menü zur Bearbeitung der Datei auf
    # Gibt alle Auswahlmöglichkeiten aus, und öffnet dann je nach dem was der User angibt, die dazugehörige Funktion
    while True:
        print(f"\nAktuelle Datei: {file_name}")
        print("1. CSV-Daten anzeigen")
        print("2. Neuen Datensatz hinzufügen")
        print("3. Bestehenden Datensatz entfernen")
        print("4. Bestehenden Datensatz bearbeiten")
        print("5. Daten als Diagramm anzeigen")
        print("6. Zurück zum Hauptmenü")
        choice = input(Fore.GREEN + "Wähle eine Option: " + Fore.RESET)
        if choice == "1":
            show_data(df)
            input(Fore.YELLOW + "Drücke enter zum fortsetzen\n" + Fore.RESET)
            clear_screen()
        elif choice == "2":
            df = add_data(df, file_name)
            input(Fore.YELLOW + "Drücke enter zum fortsetzen\n" + Fore.RESET)
            clear_screen()
        elif choice == "3":
            df = del_data(df, file_name)
            input(Fore.YELLOW + "Drücke enter zum fortsetzen\n" + Fore.RESET)
            clear_screen()
        elif choice == "4":
            df = edit_data(df, file_name)
            input(Fore.YELLOW + "Drücke enter zum fortsetzen\n" + Fore.RESET)
            clear_screen()
        elif choice == "5":
            df = plot_data(df)
            input(Fore.YELLOW + "Drücke enter zum fortsetzen\n" + Fore.RESET)
            clear_screen()
        elif choice == "6":
            clear_screen()
            main()
            break
        else:
            print(Fore.RED + "\nDas ist keine gültige Eingabe!")
            input(Fore.YELLOW + "Drücke enter zum fortsetzen\n" + Fore.RESET)
            clear_screen()


def main():
    """Hauptmenü der Anwendung."""
    # Listet alle CSV-Dateien auf
    list_csv_files()
    # Benutzer kann eine Datei auswählen, eine neue erstellen oder das Programm beenden
    print(f"{32*"-"}\n1. Wähle eine bestehende CSV-Datei\n2. Erstelle eine neue CSV-Datei\n3. Programm beenden")
    choice = input(Fore.GREEN + "Wähle eine Option (1, 2 oder 3): " + Fore.RESET)
    if choice == "1":
        clear_screen()
        selected_file = select_file()
        file_menu(selected_file)
    elif choice == "2":
        create_csv()
        main()
    elif choice == "3":
        clear_screen()
        exit()
    else:
        print(Fore.RED + "\nDas ist keine gültige Eingabe!")
        input(Fore.GREEN + Fore.YELLOW + "Drücke enter zum fortsetzen\n" + Fore.RESET)
        clear_screen()
        main()


"""Startet das Programm"""
clear_screen()
main()
