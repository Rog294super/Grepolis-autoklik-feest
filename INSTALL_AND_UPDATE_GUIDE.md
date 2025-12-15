# 🎮 Autoklik v1.25.1 - Installatie & Update Gids

## 🚀 Voor Gebruikers

### Optie 1: Online Installer (Aanbevolen - Klein bestand)

1. Download `Autoklik_Installer.exe` (3-5 MB)
2. Dubbelklik om te starten
3. Kies installatielocatie
4. Klik "Installeren"
5. De installer downloadt automatisch de laatste versie
6. Klaar!

### Optie 2: Volledige Download

1. Download `Autoklik.exe` van GitHub Releases
2. Maak een map aan (bijv. `C:\Autoklik`)
3. Plaats `Autoklik.exe` in de map
4. Dubbelklik om te starten
5. Config wordt automatisch aangemaakt

## 🔄 Updates

### Automatisch (in programma)
1. Open Autoklik
2. Ga naar "⚙️ Instellingen" tab
3. Klik "🔄 Controleer op Updates"
4. Bij nieuwe versie: klik "✅ Update Nu"
5. Programma sluit af en updater neemt over
6. Nieuwe versie start automatisch

### Handmatig
1. Download nieuwste `Autoklik.exe`
2. Sluit oude versie
3. Vervang bestand
4. Start nieuwe versie

## ❌ UPDATE ERROR OPLOSSING

Als je de error krijgt: **"Failed to load Python DLL"**

### Oplossing 1: Wacht Langer
De updater heeft meer tijd nodig. Dit is nu opgelost in v1.25.1 met:
- 3 seconden initial wait
- 45 seconden max wait voor proces
- 3 seconden extra voor DLL unload
- 5 pogingen voor bestand vervangen

### Oplossing 2: Handmatig Updaten
1. Sluit Autoklik **VOLLEDIG** (check Task Manager)
2. Wacht 10 seconden
3. Download nieuwe versie handmatig
4. Vervang bestand
5. Start

### Oplossing 3: Schone Installatie
1. Backup je `config.json`
2. Verwijder oude Autoklik map
3. Download installer opnieuw
4. Installeer opnieuw
5. Plaats `config.json` terug

## 💡 Aanbeveling

**Voor Gebruikers:** Gebruik Online Installer  

## 📞 Support

**GitHub:** https://github.com/Rog294super/Grepolis-autoklik-feest  
**Issues:** Open een issue op GitHub  

---

**Auteur:** Rog294super  
**Versie:** 1.25.1  
**Datum:** 2025-12-15
