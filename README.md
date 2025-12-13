# Grepolis

# AutoKlik - Automatische muisklikker voor Grepolis

AutoKlik is een programma waarmee je automatisch muisklikken kunt uitvoeren in de browsergame Grepolis. Dit programma helpt bij het automatiseren van repetitieve taken door een reeks muisklikken op vooraf gedefinieerde posities uit te voeren. Het biedt een eenvoudige interface en toetsencombinaties om de werking van het programma te starten, stoppen en configureren.

## Functies

- **Sneltoetsen**: Configureer en gebruik sneltoetsen voor verschillende muisklikposities.
# Grepolis — AutoKlik (GUI)

AutoKlik is een hulpmiddel om repetitieve muisklikken in Grepolis te automatiseren. De moderne GUI vervangt de oude console-interface: je stelt muisposities, sneltoetsen en acties in via tabs, start/stop acties met één druk op de knop of via sneltoetsen, en voert updates uit vanuit de GUI.

### Voor Windows:
1. Download de `autoklik.exe` van de [release-pagina](https://github.com/Rog294super/Grepolis-autoklik-feest/releases/latest).
2. Zet het bestand in een map op je computer.
3. Dubbelklik op `autoklik.exe` om het programma te starten.

### Stappen:
1. Kijk bij Sneltoetsen naar de mogelijke sneltoetsen en indien benodigd pas aan, Hou rekening met sneltoetsen van de browser.
2. In de browser op het tablad van grepolis stel de posities in.
- Positie 1 voor Stadsfeest.
- Positie 2 voor Zegetocht.
- Positie 3 voor volgende stad knop.
- Positie 4 is voor boerendorp verzamelen. Zorg dat deze op de juiste knop in overeenkomenst met wachttijd staat.
- Positie 5 is voor volgende boerendorp knop.
3. Selecteer bij de Acties knop een actie bijvoorbeeld: Stadsfeest.
4. Gebruik de sneltoets voor starten.
5. Gebruik wanneer klaar de sneltoets voor stoppen.

Hotkeys
- Stel hotkeys in via `Sneltoetsen` tab. Als een hotkey niet is ingesteld in `config.json`, gebruikt de GUI een standaardwaarde.

Belangrijkste features
- GUI met tabs: Posities, Acties, Sneltoetsen, Instellingen, Log.
- Hotkeys: configureerbaar in de `Sneltoetsen` tab (standaardcombinaties zijn vooraf ingesteld maar volledig aanpasbaar).
- Acties: Stadsfeest, Zegetocht, Stadsfeest+Zegetocht, Boerendorp (automatisch cyclen).
- Update-systeem: `Instellingen` > `Updates` heeft een knop `Update Nu` en een update-check; de GUI zorgt dat `updater.exe` wordt uitgepakt en gestart.
- Debug: `--debug-gui` CLI-flag of via Settings → "Schrijf debug-log naar bestand". Maak een debug-archive met de knop "Maak debug bestand".

Update & updater.exe
- De GUI pakt bij opstart automatisch `updater.exe` uit de ingebedde resources.
- Wanneer je `Update Nu` of de automatische check gebruikt, zoekt de GUI naar een `.exe` asset in de nieuwste GitHub Release, logt de `browser_download_url` en start `updater.exe` met die URL en het doelpad.
- Let op: geef de updater altijd een directe `.exe` download-URL (de GUI haalt deze uit de GitHub API asset `browser_download_url`). Als je handmatig `updater.exe` gebruikt, geef ook die een directe asset-URL.

Debug & troubleshooting
- Debug logfile: `autoklik_debug.log` in de programmamap (wordt aangemaakt zodra debug is ingeschakeld).

Licentie
- Dit project gebruikt de MIT-licentie — zie het `LICENSE` bestand.

Contact
- Voor vragen: rog294super@gmail.com