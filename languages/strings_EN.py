#: english

# noinspection PyStatementEffect
{
    '__full__': 'english',

    '__maintainer__': '@JellyWX',

    'blacklisted': ''':x: This channel is blacklisted :x:''',

    'help': '''Please visit https://reminder-bot.com/help?lang=EN''',

    'no_perms_webhook': '''**WARNING**: To set reminders I need the `Manage Webhooks` permission.''',

    'no_perms_embed_links': '''**WARNING**: To operate, I need the `Embed Links` permission.''',

    'no_perms_general': '''Action forbidden. Please ensure I have the correct permissions.''',

    'no_perms_managed': '''You must have `Manage Messages` or have a role capable of sending reminders to that channel. Please talk to your server admin, and ask them to use the `{prefix}restrict` command to specify allowed roles.''',

    'no_perms_restricted': '''You must have permission level `Manage Server` or greater to use this command.''',

    'help_raw': [
        ['''Reminder Commands''', {
            '$natural': 'Easier method to set reminders. Please run this command for more information.',

            '$del': 'Delete reminders and intervals on your server. If the reminders are set up for DMs, direct message this command to the bot.',

            '$look [n] [channel] [enabled] [time]': 'View the reminders in a channel. If provided, <code>n</code> will limit to displaying the next n reminders. If <code>enabled</code> is written, only enabled reminders will be shown. If <code>time</code> is written, the exact time will be shown rather than the offset',

            '$remind [user/channel] <time-to-reminder> <message>': 'Command deprecated. Use <code>$natural</code> instead of this command. Set up a reminder. Takes times in the format of [num][s/m/h/d], for example 10s for 10 seconds or 2s10m for 2 seconds 10 minutes. An exact time can be provided as <code>day/month/year-hour:minute:second</code>.',

            '$interval [user/channel] <time-to-reminder> <interval> <message>': '<strong><a href="https://patreon.com/jellywx/">Patron Only.</a></strong> Command deprecated. Use <code>$natural</code> instead of this command. Set a recurring reminder starting in the given <code>time-to-reminder</code>. Takes times in the normal formats, ex. <code>$interval 0s 20m Hello World!</code> will send \'Hello World!\' to your channel every 20 minutes.',

            '$offset': 'Offset an entire server\'s reminders by a set time (helps account for daylight saving time)',
        }],

        ['''Management Commands''', {
            '$timezone': 'Set your server\'s timezone, for easier date-based reminders.',

            '$lang <name>': 'Change the language.',

            '$nudge <time>': 'Enable nudging on the current channel. This allows you to sync all future reminders by the second to things like in game clocks',

            '$pause [time]': 'Silence reminders on the current channel. A timeout for this can be provided optionally, otherwise reminders are silenced indefinitely. Can be disabled with the same command',

            '$restrict [role mention] [commands]': 'Change which commands can be used by which roles',

            '$blacklist [channel-name]': 'Block or unblock a channel from sending commands.',
        }],

        ['''Other Commands''', {
            '$donate': 'View information about donations.',

            '$prefix <string>': 'Change the prefix from $.',

            '$info': 'Get info on the bot.',

            '$clock': 'Get current time in guild\'s timezone',

            '$todo user': 'TODO list related commands. Use <code>$todo help</code> for more information.',

            '$todo channel': 'Identical to <code>$todo server</code> but for channel-based task management.',

            '$todo server': 'Identical to <code>$todo channel</code> but for server-based task management.',

            '$alias': 'Save a command to a shorter reusable name. Use <code>$alias name command</code> to setup, e.g <code>$alias rem natural in 10 minutes send hello</code>, then use <code>$alias name</code> to recall',

            '$timer': 'Set a timer that marks the current time. Do `$timer` for more information.',

        }]
    ],

    'info': '''
Default prefix: `$`
Reset prefix: `@{user} prefix $`
Help: `{prefix}help`

**Welcome to Reminder Bot!**
Developer: <@203532103185465344>
Icon: <@253202252821430272>
Find me on https://discord.jellywx.com and on https://github.com/JellyWX :)

Invite the bot: https://invite.reminder-bot.com/
Use our dashboard: https://reminder-bot.com/

*If you have enquiries about new features, please send to the discord server*
''',

    'donate': '''
Thinking of adding a monthly contribution? Click below for my patreon and official bot server :D

https://www.patreon.com/jellywx

https://discord.jellywx.com

Here's some more information:

When you donate, Patreon will automatically rank you up on our Discord server, supposing you have properly linked your Patreon and Discord accounts!
With your new rank, you'll be able to:
: set repeating reminders with `interval`, `natural` or the dashboard
: use unlimited uploads on SoundFX

Anyone who is a Patreon supporter, thank you :D You make this bot sustainable

Please note, you must be connected to the Discord server to receive Patreon rewards.
''',

    'prefix': {

        'no_argument': '''
Please use this command as `@reminder-bot prefix <prefix>`
''',
        'success': '''
Prefix changed to {prefix}
''',

        'too_long': '''Please select a prefix under 5 characters'''
    },

    'timezone': {

        'no_argument': '''
Usage:
    ```{prefix}timezone <Name>```
Example:
    ```{prefix}timezone Europe/London```
All timezones: https://gist.github.com/JellyWX/913dfc8b63d45192ad6cb54c829324ee
Current timezone: {timezone}''',

        'no_timezone': '''Timezone not recognized. A list is available at https://gist.github.com/JellyWX/913dfc8b63d45192ad6cb54c829324ee''',

        'set': '''Server timezone has been set to {timezone}. Your current time should be {time}''',

        'set_p': '''Personal timezone has been set to {timezone}. Your current time should be {time}''',
    },

    'alias': {

        'help': '''Usage: 
`{prefix}alias <name> <command>`: attach an alias to a command
`{prefix}alias <name>`: recall a command attached to an alias
`{prefix}alias list`: list aliases
`{prefix}alias remove <name>`: remove an existing alias''',

        'invalid_command': '''Please use a command in the alias text. This command cannot be the alias command''',

        'not_found': '''No alias found with name `{name}`''',

        'created': '''New alias `{name}` created''',

        'removed': '''{count} alias deleted.'''
    },

    'restrict': {

        'disabled': '''Disabled restrictable command permissions for roles.''',

        'enabled': '''Enabled command permissions for roles.''',

        'allowed': '''Rules: {}''',

        'failure': '''Failed to assign permissions for command `{command}`. This command either doesn't exist, or only works on preset restrictions''',

        'help': '''Usage:
**Reset Role Restrictions**
`$restrict @RoleName`

**Permit Command (e.g `natural` and it's alias `n`)**
`$restrict @RoleName natural`

**View Restrictions**
`$restrict`
'''
    },

    'remind': {

        'no_argument': '''
Usage:
    ```{prefix}remind [channel mention or user mention] <time to or time at> <message>```
Example:
    ```{prefix}remind #general 10s Hello world```
    ```{prefix}remind 10:30 It\'s now 10:30```''',

        'invalid_tag': '''Couldn't find a location by your tag present.''',

        'invalid_time': '''Make sure the time you have provided is in the format of [num][s/m/h/d][num][s/m/h/d] etc. or `day/month/year-hour:minute:second`.''',

        'long_time': '''Make sure the time provided is less than {max_time} days in the future.''',

        'past_time': '''Please ensure the time provided is in the future. If the time *is* in the future, please be more specific with the definition.''',

        'success': '''New reminder registered for {location} in {offset}.''',

        'no_webhook': '''This channel has too many webhooks. Please delete one and try again''',
    },

    'interval': {

        'no_argument': '''
Usage:
    ```{prefix}interval [channel mention or user mention] <time to or time at> <interval> <message>```
Example:
    ```{prefix}interval #general 9:30 1d Good morning!```
    ```{prefix}interval 0s 10s This will be really irritating```''',

        'invalid_interval': '''Make sure the interval you have provided is in the format of [num][s/m/h/d][num][s/m/h/d] etc. with no spaces, eg. 10s for 10 seconds or 10s12m15h1d for 10 seconds, 12 minutes, 15 hours and 1 day.''',

        'short_interval': '''Please ensure the interval provided is longer than {min_interval} seconds''',

        'long_interval': '''Please ensure the interval provided is less than {max_time} days''',

        'donor': '''You need to be a Patron (donating 2$ or more) to access this command! Type `{prefix}donate` to find out more.''',

    },

    'natural': {

        'no_argument': '''
Natural language processing
Examples:
    ```{prefix}natural in 10 minutes send Hello World! to #general```
    ```{prefix}natural at 18:00 send The big event has started!```
    ```{prefix}natural on the 16th of july at 14:00 send Subs reset today! to #subs @Sub1 @Sub2```
    ```{prefix}natural now send 10 minutes has passed! every 10 minutes to #timer```
Keywords:
    `send` : define the message
    `every` : define an interval (Patreon Only)
    `to` : define the location to send to (can define multiple locations, like `@JellyWX #general @SomeUser` to send to all three)
Usage:
    ```{prefix}natural <time statement> send <message> [every interval statement] [to #channel/@user]```
    ''',

        'invalid_time': '''Your time failed to process. Please make it as clear as possible, for example `16th of july` or `in 20 minutes`''',

        'long_time': '''Please ensure your reminder is younger than 50 years, or use a more specific time statement.''',

        'send': ''' send ''',

        'to': ''' to ''',

        'every': ''' every ''',

        'bulk_set': ''' {} reminders set successfully''',

    },

    'del': {

        'listing': '''Listing reminders on this server... (there may be a small delay, please wait for the "List (1,2,3...)" message).''',

        'listed': '''List (1,2,3...) the reminders you wish to delete, or type anything else to cancel.''',

        'count': '''Deleted {} reminders!''',
    },

    'look': {

        'listing': '''Listing reminders on specified channel...''',

        'listing_limited': '''Listing the next {} reminders on specified channel...''',

        'inter': '''occurs next at''',

        'no_reminders': '''No reminders on specified channel.''',
    },

    'todo': {

        'add': '''*Do `{prefix}{command} add <message>` to add an item to your TODO, or type `{prefix}{command} help` for more commands!*''',

        'added': '''Added \'{name}\' to todo!''',

        'removed': '''Removed \'{}\' from todo!''',

        'error_value': '''Removal item must be a number. View the numbered TODOs using `{prefix}{command}`''',

        'error_index': '''Couldn\'t find item by that number. Are you in the correct todo list?''',

        'help': '''To use the TODO commands, do `{prefix}{command} add <message>`, `{prefix}{command} remove <number>`, `{prefix}{command} clear` and `{prefix}{command}` to add to, remove from, clear or view your todo list.''',

        'cleared': '''Cleared todo list!''',

        'confirm': '''You are about to delete **{} items** from your **{}** todo list. Are you sure? (type `yes` to confirm)''',

        'canceled': '''Clear canceled''',
    },

    'blacklist': {
        'removed_from': '''Removed blacklists from specified channels.''',

        'added_from': '''Added specified channels to blacklist.''',

        'removed': '''Removed current channel from blacklist.''',

        'added': '''Added current channel to blacklist.''',

    },

    'lang': {

        'invalid': '''Languages:
{}''',

        'set': '''Server language set to English.''',

        'set_p': '''Personal language set to English.''',
    },

    'clock': {

        'time': '''Current time is {}.''',

    },

    'offset': {

        'help': '''Usage: `{prefix}offset <time/s>`''',

        'invalid_time': '''Please ensure the time you have provided is in the format of [num][s/m/h/d][num][s/m/h/d]''',

        'success': '''All reminders have been offset by {} seconds''',

    },

    'nudge': {

        'invalid_time': '''Please ensure the time you have provided is in the format of [num][s/m/h/d][num][s/m/h/d], and is less than 30'000 seconds''',

        'success': '''Future reminders will be nudged by {} seconds''',

    },

    'timer': {

        'limit': '''You already have 25 timers. Please delete some timers before creating a new one''',

        'name_length': '''Please name your timer something shorted (max. 32 characters, you used {})''',

        'unique': '''Please give your timer a unique name''',

        'success': '''Created a new timer''',

        'not_found': '''Could not find a timer by that name''',

        'deleted': '''Deleted a timer''',

        'help': '''**Timer Help**
`timer list` - View all current timers in your server/user

`timer start [name]` - Start a new timer (counts indefinitely)

`timer delete <name>` - Delete a timer by name
        ''',

    },

    'pause': {

        'invalid_time': '''Please ensure the time you have provided is in the format of [num][s/m/h/d][num][s/m/h/d] etc...''',

        'paused_until': '''Reminders in this channel have been silenced until **{}**''',

        'paused_indefinite': '''Reminders in this channel have been silenced indefinitely''',

        'unpaused': '''Reminders in this channel have been unsilenced''',
    },
}
