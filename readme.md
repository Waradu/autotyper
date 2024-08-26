### Autotype
Schreibt dein code ab damit es nicht mit dieser Moodle IDE gemacht werden muss.

## Benutzten

[autotyper.exe hier herunterladen](https://github.com/Waradu/autotyper/releases/tag/v1.0.0)

1. Indent von dem code entfernen (ctrl+a und dann shift+tab bis sich nichts mehr ändert)
2. Programm starten
3. Datei auswählen
4. Start drücken
5. Schnell zu moodle IDE wechseln (started nach 5sek nachdem start gedrückt wurde)

Video tutorial:

https://github.com/user-attachments/assets/31ab31fa-86d7-49bf-80e0-b27e73a78b5c

## Build 4 yourself

1. Code klonen oder herunterladen
2. Installiere python
3. pip install pyinstaller pynput
4. pyinstaller --onefile --noconsole --icon=bztf.ico .\autotyper.py
5. exe ist in /dist
