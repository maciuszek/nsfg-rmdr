#: español

{
    '__full__': 'español',

    '__maintainer__' : '@Giuh',

    'blacklisted' : ''':x: Este canal está en la blacklist :x:''',

    'help' : '''Por favor visita https://reminder-bot.com/help?lang=ES''',

    'no_perms_webhook' : '''**AVISO**: Para colocar recordatorios necesito el permiso de `Gestionar webhooks`.''',
    
    'no_perms_embed_links' : '''**AVISO**: Parar operar necesito el permiso de `Insertar enlaces`.''',

    'no_perms_general' : '''Acción imposible. Asegúrese que tengo los permisos correctos.''',

    'no_perms_managed' : '''Necesitas el permiso `Gestionar mensajes` o tener un rol con el cual puedas colocar recordaorios a ese canal. Contacta al admnistrador de tu servidor y dile que utilice el comando `{prefix}restrict` para especificar roles permitidos.''',
    
    'no_perms_restricted': '''Necesitas el permiso `Gestionar servidor` o uno más alto para utilizar este comando.''',

    'help_raw' : [
        ['''Comandos de recordatorios''', {
            '$natural' : 'Método más fácil para colocar recordatorios. Envía el comando para más información.',

            '$del' : 'Elimina recordatorios e intervalos en tu servidor. Si los recordatorios fueron colocados para un usuario específico, deberá enviar un mensaje directo al bot con el comando.',

            '$look [n] [canal]' : 'Ver los recordatorios de un canal. Si se provee, <code>n</code> lo limitará a mostrar los siguientes n recordatorios',

            '$remind [usuario/canal] <tiempo-para-recordatorio> <mensaje>' : 'Considere utilizar el comando <code>$natural</code> en lugar de este. Coloca un recordatorio. El tiempo debe ponerse como [num][s/m/h/d], por ejemplo 10s para 10 segundos o 2s10m para 2 segundos 10 minutos. Un tiempo exacto puede ser colocado como <code>día/mes/año-hora:minuto:segundo</code>.',

            '$interval [usuario/canal] <tiempo-para-recordatorio> <intervalo> <mensaje>' : '<strong><a href="https://patreon.com/jellywx/">Solo para donadores Patreon.</a></strong> Considere utilizar el comando <code>$natural</code> en lugar de este. Coloca un recordatorio periódico iniciando desde el <code>tiempo-para-recordatorio</code> dado. El tiempo se coloca como dice arriba. Ej. `$interval 0s 20m ¡Hola Mundo!` enviará "¡Hola Mundo!" a tu canal cada 20 minutos.',

            '$offset' : 'Ajustar o compensar la hora de todos los recordatorios del servidor por un determinado tiempo (por horarios de verano, etc.)', }],

        ['''Comandos de administración''', {
            '$timezone' : 'Configura la zona horaria del servidor, para facilitar los recordatorios basados en tiempo.',
            
            '$lang <nombre>' : 'Cambia el idioma.',
            
            '$nudge <tiempo>' : 'Habilita empujes ("nudge") en el canal. Esto permite sincronizar todos los futuros recordatorios del canal a algo como el tiempo dentro de un juego.',
            
            '$pause [tiempo]' : 'Silencia los recordatorios en el canal actual. Un tiempo puede ser proporcionado para esto, de lo contrario los recordatorios serán pausados indefinidamente. Puede deshabilitarse con el mismo comando.',
            
            '$restrict [@rol] [comandos]' : 'Cambia qué comandos puedes ser utilizados por qué rol.',

            '$blacklist [canal]' : 'Bloquea o desbloquea un canal de enviar comandos.',

        }],

        ['''Otros comandos''', {
            '$donate' : 'Muestra información sobre donaciones.',

            '$prefix <prefijo>' : 'Cambia el prefijo "$".',

            '$info' : 'Obtén información sobre el bot.',

            '$clock' : 'Obtén la hora actual acorde a la zona horaria del servidor.',
            
            '$todo' : 'Comandos relacionado a la lista TO-DO (lista de tareas). Utiliza <code>$todo help</code> para más información.',

            '$todo channel' : 'Idéntico a <code>$todo server<code> pero para tareas a nivel de canal.',
            
            '$todo server' : 'Idéntico a <code>$todo channel<code> pero para tareas a nivel de servidor.',
            
            '$alias' : 'Guarda un comando a un nombre reusable más corto. Utilice <code>$alias nombre comando</code> para configurar, ej. <code>$alias reco natural en 10 minutes enviar hola</code>, luego utilice <code>$alias reco</code> para reclamarlo',

            '$a' : 'Alias para <code>$alias</code>',
            
            '$timer' : 'Configura un contador que marca desde el tiempo actual. Envía `$timer` para más información.',

            }
        ]
    ],


    'info' : '''
Prefijo por defecto: `$`
Reajustar prefijo: `@{user} prefix $`
Ayuda: `{prefix}help`

**Bienvenido a RemindMe!**
Desarrollador: <@203532103185465344>
Ícono: <@253202252821430272>
Encuéntrame en https://discord.jellywx.com y en https://github.com/JellyWX :)

Invita este bot: https://invite.reminder-bot.com/
Usa nuestro dashboard: https://reminder-bot.com/

*Si tienes consultas sobre nuevas caracterísicas, por favor envíalas a nuestro servidor de Discord*
''',

    'donate' : '''
¿Pensando en aportar una contribución mensual? Presiona abajo para mi Patreon y el servidor oficial del bot :D

https://www.patreon.com/jellywx

https://discord.jellywx.com

Aquí hay un poco más información:

Cuando donas, Patreon automáticamente te dará el rango en nuestro servidor de Discord, siempre y cuando hayas vinculado tus cuentas de Patreon y Discord!
Con tu nuevo rango, podrás:
: crear recordatorios recurrentes con `interval`, `natural` y desde el dashboard
: usar subidas ilimitadas con SoundFX

Para quienes estén en Patreon, muchas gracias :D Haces que este bot pueda sostenerse.

Ten en cuenta que debes estar conectado a nuestro servidor de Discord para recibir las recompenzas de Patreon.
''',

    'prefix' : {
        
        'no_argument' : '''
Por favor utiliza este comando como `@reminder-bot prefix <prefijo>`
''',
        'success' : '''
Prefijo cambiado a {prefix}
''',

        'too_long' : '''Por favor selecciona un prefijo menor a 5 caracteres.'''
    },

    'timezone' : {

        'no_argument' : '''
Uso:
    ```{prefix}timezone <nombre>```
Ejemplo:
    ```{prefix}timezone Europe/London```
Todas las zonas horarias: https://gist.github.com/JellyWX/913dfc8b63d45192ad6cb54c829324ee
Zona horaria actual: {timezone}''',

        'no_timezone' : '''Zona horaria no reconocida. Una lista está disponible en https://gist.github.com/JellyWX/913dfc8b63d45192ad6cb54c829324ee''',

        'set' : '''La zona horaria del servidor ha sido cambiada a {timezone}. Tu hora actual debería ser {time}''',
        
        'set_p' : '''La zona horaria personal se ha establecido a {timezone}. Tu hora actual debería ser {time}''',
    },

    'alias' : {

        'help' : '''Uso: 
`{prefix}alias <nombre> <comando>`: adjuntar un alias a un comando
`{prefix}alias <nombre>`: reclamar un comando adjuntado a un alias
`{prefix}alias list`: listar aliases,
`{prefix}alias remove <nombre>`: eliminar un alias existente''',

        'invalid_command' : '''Por favor utilice un comando en el texto del alias. Este comando no puede ser el comando del alias''',

        'not_found' : '''No hubo alias encontrados con el nombre `{name}`''',

        'created' : '''Nuevo alias `{name}` creado''',
        
        'removed' : '''{count} alias eliminados.'''

    },

    'restrict' : {
        
        'disabled' : '''Desactivados los permisos de restricción de comandos para roles.''',

        'enabled' : '''Activados los permisos de comandos para roles.''',

        'allowed' : '''Reglas: {}''',

        'failure' : '''Fallo al asignar permisos al comando `{command}`. Este comando no existe, o solo funciona en restricciones predefinidas.''',

        'help' : '''Uso:
**Reiniciar Rol**
`$restrict @NombreRol`
**Permitir Comando (ej. `natural` y su alias `n`)**
`$restrict @NombreRol natural n`
**Ver Restricciones**
`$restrict`
'''
    },

    'remind' : {
        
        'no_argument' : '''
Uso:
    ```{prefix}remind [canal o usuario] <tiempo para/tiempo exacto> <mensaje>```
Ejemplo:
    ```{prefix}remind #general 10s Hola mundo```
    ```{prefix}remind 10:30 Son las 10:30```''',

        'invalid_tag' : '''No es posible encontrar la localización de tu tag.''',

        'invalid_time' : '''Asegúrate que la hora que colocaste es en el formato [num][s/m/h/d][num][s/m/h/d] etc. o `día/mes/año-hora:minuto:segundo`.''',

        'long_time' : '''Asegúrate de que el tiempo colocado es menor a {max_time} días en el futuro.''',
        
        'past_time' : '''Por favor asegúrate que el tiempo proveído es en el futuro. Si el tiempo *está* en el futuro, se más específico con la definición.''',

        'success' : '''Nuevo recordatorio registrado para {location} en {offset}. Ya no puedes editarlo, así que eres libre de eliminarlo.''',
    },

    'interval' : {
        
        'no_argument' : '''
Uso:
    ```{prefix}interval [canal o usuario] <tiempo para/tiempo exacto> <intervalo> <mensaje>```
Ejemplo:
    ```{prefix}interval #general 9:30 1d ¡Buen día!```
    ```{prefix}interval 0s 10s Esto será muy irritante```''',
        
        'invalid_interval' : '''Asegúrate que la hora que colocaste es en el formato [num][s/m/h/d][num][s/m/h/d] etc. sin espacios, ej. 10s para 10 segundos o 10s12m15h1d for 10 segundos, 12 minutos, 15 horas y 1 día.''',

        'short_interval' : '''Por favor asegúrate que tu intervalo es mayor a {min_interval} segundos.''',

        'long_time' : '''Asegúrate de que el tiempo del intervalo colocado es menor a {max_time} días.''',

        'donor' : '''¡Necesitas ser un Patreon (dona 2$ o más) para acceder a este comando! Escribe `{prefix}donate` para más información.''',

    },

    'natural' : {
        
        'no_argument' : '''
Procesamiento en lenguaje natural
Ejemplos:
    ```{prefix}natural en 10 minutos enviar ¡Hola Mundo! para #general```
    ```{prefix}natural a las 18:00 enviar ¡El gran evento ha comenzado!```
    ```{prefix}natural el 16 de julio a las 14:00 enviar ¡Hoy se reinician las subs! para #subs @Sub1 @Sub2```
    ```{prefix}natural ahora enviar ¡Han pasado 10 minutos! cada 10 minutos para #timer```
Palabras clave:
    `enviar` : define el mensaje
    `cada` : define el intervalo (solo donadores Patreon)
    `para` : define el destino del mensaje (puedes definir múltiples destinos, como `@JellyWX #general @AlgunUser`para enviar a los tres)
Uso:
    ```{prefix}natural <tiempo para> enviar <mensaje> [cada intervalo] [para #canal/@usuario]```
    ''',

        'invalid_time' : '''Has fallado en colocar correctamente el tiempo. Por favor, colócalo claro, por ejemplo `16 de julio` o `en 20 minutos`''',

        'long_time' : '''¡Eso es un tiempo muy grande! Por favor, asegúrate que tu recordatorio es menor a 50 años, o utiliza algo más específico.''',

        'send' : ''' enviar''',

        'to' : ''' para ''',

        'every' : ''' cada ''',
        
        'bulk_set' : '''{} recordatorios colocados satisfactoriamente''',

    },

    'del' : {
        
        'listing' : '''Listando recordatorios en este servidor... (puede haber un pequeño retraso, espera que el mensaje "Selecciona (1,2,3...)" aparezca).''',

        'listed' : '''Selecciona (1,2,3...) el recordaorio que quieres eliminar, o escribe cualquier otra cosa para cancelar.''',

        'count' : '''¡Se han eliminado {} recordatorios!'''
    },

    'look' : {
        
        'listing' : '''Listando los recordatorios del canal especificado...''',

        'inter' : '''será enviado el''',

        'no_reminders' : '''No hay recordatorios en el canal especificado.''',
    },

    'todo' : {
        
        'add' : '''*Pon `{prefix}{command} add <mensaje>` para añadir un ítem a tu TODO, o escribe `{prefix}{command} help` para más comandos*''',

        'added' : '''¡Añadido \'{name}\' a la lista de tareas!''',

        'removed' : '''¡Eliminado \'{}\' de la lista de tareas!''',

        'error_value' : '''El ítem a remover ha de ser un número. Mira el número de las tareas usando `{prefix}{command}`''',

        'error_index' : '''No se pudo encontrar un ítem con ese número. ¿Estás en la lista correcta?''',

        'help' : '''Para usar comandos de la lista de tareas (TODO), pon `{prefix}{command} add <mensaje>`, `{prefix}{command} remove <número>`, `{prefix}{command} clear` y `{prefix}{command}` para añadir, remover, limpiar o mirar tu lista de tareas.''',

        'cleared' : '''¡Limpiada la lista de tareas!'''
    },

    'blacklist' : {
        'removed_from' : '''Removidas las blacklists de los canales especificados.''',

        'added_from' : '''Añadido los canales especificados a la blacklist.''',

        'removed' : '''Removido el canal actual de la blacklist.''',

        'added' : '''Añadido el canal actual a la blacklist.'''

    },

    'lang' : {

        'invalid' : '''Idiomas:
{}''',

        'set' : '''Idioma del servidor cambiado a Español.''',
        
        'set_p' : '''Idioma personal cambiado a Español.''',
    },

    'clock' : {
        
        'time' : '''La hora actual es {}.''',
        
    },

    'offset' : {
        
        'help' : '''Uso: `{prefix}offset <tiempo/s>`''',

        'invalid_time' : '''Por favor asegurate que el tiempo que provees es en el formato [num][s/m/h/d][num][s/m/h/d]''',

        'success' : '''Todos los recordatorios han sido ajustados por {} segundos''',

    },

    'nudge' : {

        'invalid_time' : '''Por favor asegurate que el tiempo que provees es en el formato [num][s/m/h/d][num][s/m/h/d]''',

        'success' : '''Todos los recordatorios serán empujados por {} segundos''',

    },

    'timer' : {

        'limit' : '''Ya tienes 25 contadores. Por favor elimina algunos antes de crear nuevos''',

        'name_length' : '''Por favor nombra tu contador algo más corto (máx. 32 caracteres, utilizaste {})''',

        'unique' : '''Por favor dale a tu contador un nombre único''',

        'success' : '''Creado nuevo contador''',

        'not_found' : '''No se pudo encontrar un contador con ese nombre''',

        'deleted' : '''Eliminado un contador''',

        'help' : '''**Ayuda del Contador**
`timer list` - Ver todos los contadores actuales en tu servidor/usuario

`timer start [nombre]` - Iniciar un nuevo contador (cuenta indefinidamente)

`timer delete <nombre>` - Eliminar un contador por el nombre
        ''',

    },

    'pause' : {

        'invalid_time' : '''Por favor asegurate que el tiempo proporcionado es del formato [num][s/m/h/d][num][s/m/h/d] etc...''',

        'paused_until' : '''Los recordatorios en este canal han sido silenciados hasta **{}**''',

        'paused_indefinite' : '''Los recordatorios en este canal han sido silenciados indefinidamente''',

        'unpaused' : '''Los recordatorios en este canal han sido reanudados''',
    },
}
