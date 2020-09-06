#: deutsch

# noinspection PyStatementEffect
{
    '__full__': 'deutsch',

    '__maintainer__': '@TebosBrime',

    'blacklisted': ''':x: Dieser Channel ist geblockt :x:''',

    'help': '''Bitte besuche https://reminder-bot.com/help?lang=DE''',

    'no_perms_webhook': '''**WARNUNG**: Um Erinnerungen zu setzte, benötige ich die `Webhooks verwalten` Permission.''',

    'no_perms_embed_links': '''**WARNUNG**: Zum arbeiten, benötige ich die `Links einbetten` Permission.''',

    'no_perms_general': '''Aktion verboten! Stelle bitte sicher, dass ich die korrekten Permissions habe.''',

    'no_perms_managed': '''Du benötigst die `Nachrichten verwalten` Permssions oder Rollen-Rechte um Erinnerungen zu diesem Channel hinzuzufügen. Bitte spreche mit deinem Administrator, und frage ihn, den `{prefix}restrict` Befehl zu nutzen und deine Rolle hinzuzufügen.''',

    'no_perms_restricted': '''Du benötigst mindestens das Permissions-Level `Server verwalten` um diesen Befehl zu verwenden.''',

    'help_raw': [
        ['''Reminder Commands''', {
            '$natural': 'Einfache Methode um Erinnerungen hinzuzufügen. Führe diesen Befehl aus um weitere Hilfe zu erhalten.',

            '$del': 'Lösche Erinnerungen und Intervalle von deinem Server. Wenn Erinnerungen für PNs gesetzt sind, schreibe dies dem Bot direkt.',

            '$look [n] [Kanal] [aktiviert]': 'Zeige alle Erinnerungen in einem Kanal an. Wenn <code>n</code> angegeben ist, werden nur die nächsten n Erinnerungen angezeigt. Wenn <code>enabled</code> angegeben ist, werden nur aktivierte Erinnerungen angezeigt.',

            '$remind [User/Kanal] <Zeit-bis-zur-Errinnerung> <Nachricht>': 'Verwende lieber <code>$natural</code> als diesen Befehl. Dieser Befehl benötigt eine Zeitangabe im folgendem Format: [num][s/m/h/d]. (Beispiel: 10s für 10 Sekunden oder 2s10m für 2 Sekunden und 10 Minuten. Eine exakte Zeit kann durch <code>day/month/year-hour:minute:second</code> angegeben werden.',

            '$interval [User/Kanal] <Zeit-bis-zur-Errinnerung> <Interval> <Nachricht>': '<strong><a href="https://patreon.com/jellywx/">Nur für Patron.</a></strong> Verwende lieber <code>$natural</code> als diesen Befehl. Setzt eine, sich wiederholende, Erinnerung welche in <code>Zeit-bis-zur-Errinnerung</code>. Verwendet das oben angegebende Intervall, z.B. <code>$interval 0s 20m Hallo Welt!</code> wird jede 20 Minuten \'Hallo Welt!\' in deinen Kanal senden.',

            '$offset': 'Verschiebt alle Erinnerungen eines Server\'s um eine bestimmte Zeit. (Hilft u.a. bei der Zeitumstellung)'}],

        ['''Management Commands''', {
            '$timezone': 'Setzt die Server Zeitzone, für einfache zeitbasierte Erinnerungen.',

            '$lang <name>': 'Ändert die Sprache.',

            '$nudge <time>': 'Aktiviert anstoßen für den derzeitigen Kanal. So können zukünftige Erinnerungen sekundengenau synchronisiert werden.',

            '$restrict [Rolle] [Befehl]': 'Ändert, welche Rollen, welche Befehle verwenden dürfen.',

            '$blacklist [Kanal]': 'Blockiert oder hebt die Blockierung eines Kanals auf. Wenn ein Kanal blockiert ist, können dort keine Befehle mehr verwendet werden.',

        }],

        ['''Other Commands''', {
            '$donate': 'Zeige Informationen über die Spendemöglichkeiten.',

            '$prefix <string>': 'Ändere den Bot-Befehle Prefix (Standard: $).',

            '$info': 'Zeige alle Informationen.',

            '$clock': 'Zeigt die derzeitige Zeit an.',

            '$todo': 'Befehle zur TODO-Liste. Nutze <code>$todo help</code> für weitere Hilfe.',

            '$todos': 'Ähnlich wie <code>$todo</code> allerings für serverweite Aufgaben.',

            '$timer': 'Startet einen Timer. Nutze `$timer` für weitere Hilfe.',

        }
         ]
    ],

    'info': '''
Standard prefix: `$`
Prefix zurücksetzten: `@{user} prefix $`
Hilfe: `{prefix}help`

**Willkommen zum Reminder Bot!**
Developer: <@203532103185465344>
Icon: <@253202252821430272>
Du findest mich unter https://discord.jellywx.com und auf https://github.com/JellyWX :)

Lade den Bot zu deinem Server ein: https://invite.reminder-bot.com/
Nutze unser Web-Dashboard: https://reminder-bot.com/

*Wenn du Vorschläge hast, melde dich gerne auf dem oben genannten Discord*
''',

    'donate': '''
Möchtest du mich unterstützen? Unten findest du mein patreon und den offiziellen bot discord server.

https://www.patreon.com/jellywx

https://discord.jellywx.com

Hier sind einige Informationen:

Wenn du spendest, wird Patreon deine Rolle auf meinem Discord-Server automatisch ändern. (Dies setzt vorraus, dass du deinen Patreon-Account mit deinem Discord-Account verbunden hast)
Mit deinem Rang wirst du folgendes können:
: Den Befehl `interval` nutzen
: Patreon-only Features von SoundFX nutzen
: Farbige Erinnerungen setzen (Nur über das Web-Dashboard möglich)
: Nutze benutzerdefinierte Avatare  (Nur über das Web-Dashboard und ab $5 Patreon möglich)
: Nutze Patreon-only Features vom Bot o'clock (Nur über das Web-Dashboard und ab $5 Patreon möglich)

An jedem, der Patreon ist: Ein herzliches Danke! Du machst den Bot möglich!

Bitte bedenke, du musst mit Discord verbunden sein um deine Patreon-Belohnungen  zu erhalten.
''',

    'prefix': {

        'no_argument': '''
Bitte nutze diesen Command als `@reminder-bot prefix <prefix>`
''',
        'success': '''
Prefix erfolgreich zu {prefix} geändert
''',

        'too_long': '''Die Prefix-Länge darf maximal 5 Zeichen sein'''
    },

    'timezone': {

        'no_argument': '''
Benutze:
    ```{prefix}timezone <Name>```
Beispiel:
    ```{prefix}timezone Europe/Berlin```
Alle Zeitzonen: https://gist.github.com/JellyWX/913dfc8b63d45192ad6cb54c829324ee
Derzeitige Zeitzone: {timezone}''',

        'no_timezone': '''Unbekannte Zeitzone. Eine Liste findest du hier https://gist.github.com/JellyWX/913dfc8b63d45192ad6cb54c829324ee''',

        'set': '''Zeitzone zu {timezone} geändert. Die derzeitige Zeit sollte {time} sein''',

        'set_p': '''Deine persönliche Zeitzone wurde zu {timezone} geändert. Die derzeitige Zeit sollte {time} sein''',
    },

    'restrict': {

        'disabled': '''Deaktivierte Befehlsberechtigungen für bestimmte Rollen''',

        'enabled': '''Aktivierte Befehlsberechtigungen für bestimmte Rollen''',

        'allowed': '''Regeln: {}''',

        'failure': '''Zuweisung von Berechtigungen für den Befehl `{command}` fehlgeschlagen. Dieser Befehl existiert entweder nicht oder funktioniert nur mit voreingestellten Einschränkungen''',

        'help': '''Benutze:
**Rolle zurücksetzten**
`$restrict @RoleName`

**Erlaube Befehl für eine Rolle (z.B. `natural` oder als Alias `n`)**
`$restrict @RoleName natural n`

**Zeige Befehlsberechtigungen an**
`$restrict`
'''
    },

    'remind': {

        'no_argument': '''
Benutze:
    ```{prefix}remind [Kanal / User] <Zeit-bis-zur-Errinnerung> <Nachricht>```
Beispiel:
    ```{prefix}remind #general 10s Hallo Welt!```
    ```{prefix}remind 10:30 Es ist 10:30 Uhr```''',

        'invalid_tag': '''Finde keinen Kanal mit dem angegebenen Tag.''',

        'invalid_time': '''Bitte stelle sicher, dass die Zeit durch [num][s/m/h/d][num][s/m/h/d] etc. oder `day/month/year-hour:minute:second` angeben wird.''',

        'long_time': '''Bitte stelle sicher, dass die Zeit nicht mehr als {max_time} Tage in der Zukunft liegt.''',

        'past_time': '''Bitte stelle sicher, dass die Zeit in der Zukunft liegt. Wenn die angegebene Zeit *in* der Zukunft liegt, sei bitte spezifischer in der Zeitangabe.''',

        'success': '''Neue Erinnerung in {location} wird in {offset} gesendet.''',
    },

    'interval': {

        'no_argument': '''
Benutze:
    ```{prefix}interval [Kanal / User] <Zeit-bis-zur-Errinnerung> <Interval> <Nachricht>```
Beispiel:
    ```{prefix}interval #general 9:30 1d Guten Morgen!```
    ```{prefix}interval 0s 10s Dies wird wirklich irritierend sein```''',

        'invalid_interval': '''Bitte stelle sicher, dass die Zeit durch [num][s/m/h/d][num][s/m/h/d] angeben wird. Es sind keine Leerzeichen erlaubt. (z.B. 10s für 10 Sekunden oder 10s12m15h1d für 10 Sekunden, 12 Minuten, 15 Stunden und 1 Tag.''',

        'short_interval': '''Bitte stelle sicher, dass die Zeit länger als {min_interval} Sekunden ist. Ein kürzeres Intervall ist nicht erlaubt.''',

        'long_interval': '''Bitte stelle sicher, dass die Zeit kürzer als {max_time} Tage ist. Ein längeres Intervall ist nicht erlaubt.''',

        'donor': '''Du benötigst Patreon (gebe 2$ oder mehr) um diesen Command zu verwenden! Gebe `{prefix}donate` für mehr Informationen ein.''',

    },

    'natural': {

        'no_argument': '''
Verarbeitung natürlicher Sprache
Beispiele:
    ```{prefix}natural in 10 minutes sende Hallo Welt! an #general```
    ```{prefix}natural at 18:00 sende Das große Event ist gestartet!```
    ```{prefix}natural on the 16th of july at 14:00 sende Abonenten werden heute zurückgesetzt! an #Abonenten @Abo1 @Abo2```
    ```{prefix}natural Es sind 10 Minuten vergangen! jede 10 minutes an #timer```
Keywords:
    `sende` : Definiert eine Nachricht
    `jede` : Definiert ein Interval (Nur für Patreon)
    `an` : Definiert einen Kanal oder Nutzer an welchem die Nachricht gesendet wird (Es können auch mehrere Kanäle/User angegeben werden. z.B. `an @JellyWX #general @SomeUser`)
Benutze:
    ```{prefix}natural <Zeit-zum-Start> sende <Nachricht> [jede interval statement] [an #channel/@user]```
    ''',

        'invalid_time': '''Zeitverarbeitung fehlgeschlagen. Bitte mache deine Zeit so klar wie möglich, zum Beispiel `16th of july` oder `in 20 minutes`''',

        'long_time': '''Bitte stelle sicher, dass die Zeit nicht später als 50 Jahre ist.''',

        'send': ''' sende ''',

        'to': ''' an ''',

        'every': ''' jede ''',

        'bulk_set': ''' {} Erinnerungen wurden erfolgreich gesetzt''',

    },

    'del': {

        'listing': '''Alle Erinnerungen... (Es könnte etwas dauern, warte bitte auf die "Verwende (1,2,3...) .." Nachricht).''',

        'listed': '''Verwende (1,2,3...) um eine Erinnerung zu löschen. Eine andere Angabe führt zum Abbruch.''',

        'count': '''Entferne {}. Erinnerung!''',
    },

    'look': {

        'listing': '''Zeige alle Erinnerungen in diesem Kanal...''',

        'listing_limited': '''Zeige die nächsten {} Erinnerungen in disem Kanal an...''',

        'inter': '''erinnert wieder auf in''',

        'no_reminders': '''Keine Erinnerungen wurden in diesem Kanal gesetzt.''',
    },

    'todo': {

        'add': '''*Verwende `{prefix}{command} add <Nachricht>` um Elemente zur der TODO-Liste hinzuzufügen, oder `{prefix}{command} help` für Hilfe!*''',

        'added': '''Erfolgreich \'{name}\' zur TODO-Liste hinzugefügt!''',

        'removed': '''Erfolgreich \'{}\' von der TODO-Liste entfernt!''',

        'error_value': '''Zu entfernendes Element muss eine Nummer sein. Zeige alle TODOs mit `{prefix}{command}` an''',

        'error_index': '''Kann kein Element mit dieser Nummer finden. Bist du in der richtigen Liste?''',

        'help': '''Nutze `{prefix}{command} add <Nachricht>`, `{prefix}{command} remove <Nummer>`, `{prefix}{command} clear` oder `{prefix}{command}` um TODOs hinzuzufügen, entfernen oder die Liste zu leeren.''',

        'cleared': '''TODO-Liste gelöscht!''',
    },

    'blacklist': {
        'removed_from': '''Kanal von der Blocklist entfernt.''',

        'added_from': '''Kanal zu der Blocklist hinzugefügt.''',

        'removed': '''Derzeitiger Kanal von der Blocklist entfernt.''',

        'added': '''Derzeitiger Kanal zu der Blocklist hinzugefügt.''',

    },

    'lang': {

        'invalid': '''Sprachen:
{}''',

        'set': '''Serversprache wurde zu Deutsch gesetzt.''',

        'set_p': '''Persönliche Sprache zu Deutsch gesetzt.''',
    },

    'clock': {

        'time': '''Derzeit ist es {} Uhr.''',

    },

    'offset': {

        'help': '''Benutze: `{prefix}offset <Zeit>`''',

        'invalid_time': '''Bitte stelle sicher, dass die Zeit im folgendem Format angegeben ist: [num][s/m/h/d][num][s/m/h/d]''',

        'success': '''Alle Erinnerungen haben nun einen Offset von {} Sekunden''',

    },

    'nudge': {

        'invalid_time': '''Bitte stelle sicher, dass die Zeit im folgendem Format angegeben ist [num][s/m/h/d][num][s/m/h/d]. Außerdem muss sie kleiner als 30'000 Sekunden sein.''',

        'success': '''Zukünftige Erinnerungen werden in {} Sekunden angestoßen''',

    },

    'timer': {

        'limit': '''Du hast bereits 25 Timer. Bitte lösche eine um eine eine neue zu erstellen.''',

        'name_length': '''Der Name des Timers ist zu lang (Maximal sind 32 Zeichen erlaubt, du verwendest aber {})''',

        'unique': '''Bitte geben deinen Timer einen eindeutigen Namen''',

        'success': '''Neuer Timer erstellt''',

        'not_found': '''Es wurde kein Timer mit diesem Namen gefunden''',

        'deleted': '''Timer gelöscht''',

        'help': '''**Timer Hilfe**
`timer list` - Zeige alle Timer vom Server / User

`timer start [Name]` - Starte einen neuen Timer (Zählt unendlich hoch)

`timer delete <Name>` - Löscht einen Timer
        ''',

    },
}
