# Languages

## All translations for Reminder Bot

### Contributing

If you wish to contribute, please open a PR with your new translation file

To produce a translation file, please refer to the `strings_EN.py` file (consider it __always__ up to date)

Translations should be named `strings_CC.py`, where CC is the 2-character country code. Translations should also include some meta tags including `__full__` for the full name of the language, and `__maintainer__` for some link to who maintains the language (although this isnt necessary). 

Some things aren't translated since they are necessary for the bot to work. See the following example:

__strings_EN.py__

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
        
__strings_ZH.py__

        'info': '''
    默认前缀：`$`
    重设前缀：`@{user} prefix $`
    帮助：`{prefix}help`
    
    **欢迎来到Reminder Bot！**
    开发者：<@203532103185465344>
    图标：<@253202252821430272>
    
    可以在 https://discord.jellywx.com 或 https://github.com/JellyWX 找到我 :)
    邀请此bot： https://invite.reminder-bot.com/
    使用控制台： https://reminder-bot.com/
    
    *如果你需要询问有关新功能的问题，请发往Discord服务器*
    ''',
    
Some stuff doesn't change, e.g `'info'`, `{user}`, links and the name of the bot itself. Most of these are fairly common sense.
