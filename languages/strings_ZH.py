#: simplified chinese

# noinspection PyStatementEffect
{
    '__full__': 'simplified chinese',

    '__maintainer__': '@Gourdyu',

    'blacklisted': ''':x: 此频道已被禁止使用指令 :x:''',

    'help': '''请查看 https://reminder-bot.com/help?lang=ZH''',

    'no_perms_webhook': '''**警告**：我需要`管理Webhooks`权限才能设置提醒事项。''',

    'no_perms_embed_links': '''**警告**:我需要`嵌入链接`权限才能完成操作。''',

    'no_perms_general': '''指令被拒绝执行。请确保已正确设置我的权限。''',

    'no_perms_managed': '''你必须拥有`管理信息`权限或可以向该频道发送提醒的身份组。请联系服务器的管理员，让他们使用`{prefix}restrict`指令来指定允许设置提醒的身份组。''',

    'no_perms_restricted': '''你必须拥有`管理服务器`或更大的权限才能使用此指令。''',

    'help_raw': [
        ['''提醒事项指令''', {
            '$natural': '一种更简单的设置提醒的方式。请运行这个指令来获取更多信息。',

            '$del': '删除服务器上的提醒事项或周期重复提醒。如果是私信提醒，请给bot私信发送这个指令。',

            '$look [n] [频道] [enabled] [time]': '查看频道中的提醒事项。如果给出了<code>n</code>，将只显示接下来的指定n个提醒事项。如果写了<code>enabled</code>，则只显示启用的提醒事项。如果给出了<code>time</code>，将显示每条提醒事项的精确时间而不是剩余时间',

            '$remind [用户/频道] <提醒时间> <内容>': '请优先考虑使用<code>$natural</code>而不是用这个指令。设置一个提醒。将时间设置成 [数字][s/m/h/d] 的格式，比如 10s 即10秒， 2s10m 即10分钟2秒。也可用<code>日/月/年-时:分:秒</code>的格式设置精确时间。',

            '$interval [用户/频道] <提醒时间> <重复周期> <内容>': '<strong><a href="https://patreon.com/jellywx/">仅限Patron。</a></strong> 请优先考虑使用<code>$natural</code>而不是用这个指令。设置一个从<code>提醒时间</code>开始的周期重复提醒。将时间设置成普通的格式，例如<code>$interval 0s 20m Hello World!</code>就会每20分钟向该频道发送一次“Hello World!”。',

            '$offset': '将服务器内的所有提醒事项全部平移指定时长（来应对夏令时）' }],

        ['''管理指令''', {
            '$timezone': '设置服务器的时区，来让设置提醒更加容易。',

            '$lang <语言名称>': '更改语言。',

            '$nudge <时间>': '在当前频道上启动推迟功能。这可以让将来的所有提醒事项都推迟指定秒数，可以用于游戏时钟等情况。',

            '$pause [时间]': '暂停发送当前频道的提醒事项。可以选择设置暂停时间，否则将无限期暂停发送。可以使用相同指令取消暂停。',

            '$restrict [指定身份组] [指令]': '更改哪个身份组可以使用哪个指令',

            '$blacklist [频道名称]': '允许/禁止在指定频道发送指令。',

        }],

        ['''其他指令''', {
            '$donate': '查看有关捐赠的信息。',

            '$prefix <前缀符号>': '更改前缀。',

            '$info': '获取此bot的相关信息。',

            '$clock': '显示集体所在的时区当前的时间。',

            '$todo user': '与待办事项列表有关的指令。使用<code>$todo help</code>来获取更多信息。',

            '$todo channel': '和<code>$todo server</code>一样，用于频道的任务管理。',

            '$todo server': '和<code>$todo channel</code>一样，用于服务器的任务管理。',

            '$alias': '将指令保存为较短的可重复调用的名称。使用<code>$alias 名称 指令</code>来设置，例如<code>$alias rem natural in 10 minutes send hello</code>，然后使用<code>$alias 名称</code>来调用',

            '$timer': '设置一个标记当前时间的计时器。 使用<code>$timer</code>来获取更多信息。',

            }]
    ],

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

    'donate': '''
想要每个月贡献些什么？请点击下方我的Patreon页面和官方bot服务器链接:D

https://www.patreon.com/jellywx

https://discord.jellywx.com

更多信息：

请将你的Patreon和Discord账号连接，这样当你捐赠的时候，Patreon就会自动将你从我们的Discord服务器上标识出来！
然后，你就可以：
: 使用`interval`、`natural`或者使用控制台来设置周期重复提醒
: 在SoundFX上使用无限制的上传。

感谢所有已经成为Patreon支持者的人 :D 是你们让这个bot得以维护。

请注意，务必将你的Patreon和Discord账号连接，这样才能获得Patreon的权限。
''',

    'prefix': {

        'no_argument': '''
请像这样使用这个指令 `@reminder-bot prefix <前缀>`
''',
        'success': '''
前缀已更改为{prefix}
''',

        'too_long': '''请将前缀控制在5字符以下'''
    },

    'timezone': {

        'no_argument': '''
用法：
    ```{prefix}timezone <时区名>```
举例：
    ```{prefix}timezone Europe/London```
时区列表： https://gist.github.com/JellyWX/913dfc8b63d45192ad6cb54c829324ee
当前时区：{timezone}''',

        'no_timezone': '''未知时区。可用的时区列表： https://gist.github.com/JellyWX/913dfc8b63d45192ad6cb54c829324ee''',

        'set': '''服务器时区已被设置为{timezone}。您当前的时间应为{time}''',

        'set_p': '''您个人的时区已被设置为{timezone}。您当前的时间应为{time}''',
    },

    'alias': {

        'help': '''用法：
`{prefix}alias <名称> <指令>`：将指令设置成别名
`{prefix}alias <名称>`：重新调用一个已经设置成别名的指令
`{prefix}alias list`：列出指令别名
`{prefix}alias remove <名称>`：移除一个已经存在的指令别名''',

        'invalid_command': '''请在别名文字中使用指令。此指令不能作为别名指令。''',

        'not_found': '''未找到名为`{name}`的指令别名''',

        'created': '''已创建新指令别名`{name}`''',

        'removed': '''已删除{count}个指令别名。'''
    },

    'restrict': {

        'disabled': '''成功禁止该身份组使用有限制的指令。''',

        'enabled': '''成功允许该身份组使用指令。''',

        'allowed': '''规则：{}''',

        'failure': '''未能成功设置`{command}`指令的使用权限。此指令可能不存在，或可能仅在预设的使用限制中才有效果''',

        'help': '''用法：
**重设身份组限制**
`$restrict @身份组`

**允许使用指令（例如`natural`和它的简写`n`）**
`$restrict @身份组 natural`

**查看使用限制**
`$restrict`
'''
    },

    'remind': {

        'no_argument': '''
用法:
    ```{prefix}remind [发往的频道或用户] <剩余时间或时间点> <内容>```
举例:
    ```{prefix}remind #general 10s Hello world```
    ```{prefix}remind 10:30 现在是10:30```''',

        'invalid_tag': '''无法定位你给出的发送对象。''',

        'invalid_time': '''请以 [数字][s/m/h/d][数字][s/m/h/d]... 的格式，或 `日/月/年-时:分:秒` 的格式给出时间。''',

        'long_time': '''给出的时间不能超过未来{max_time}天。''',

        'past_time': '''请确保给出的时间是未来的时间。如果该时间*确实是*未来的时间，请换一种更具体的说法。''',

        'success': '''发往{location}的提醒将在{offset}后发出。''',
    },

    'interval': {

        'no_argument': '''
用法：
    ```{prefix}interval [指定频道或用户] <剩余时间或时间点> <重复周期> <内容>```
举例：
    ```{prefix}interval #general 9:30 1d 早上好！```
    ```{prefix}interval 0s 10s 这能烦死人```''',

        'invalid_interval': '''请以 [数字][s/m/h/d][数字][s/m/h/d]... 的格式给出重复周期，不要空格，比如 10s 即10秒，或 10s12m15h1d 即1天15小时12分钟10秒。''',

        'short_interval': '''请让重复周期大于{min_interval}秒。''',

        'long_interval': '''给出的时间不能超过未来{max_time}天。''',

        'donor': '''你必须成为Patron（捐赠2美元或更多）才能使用这个指令！输入`{prefix}donate`来了解更多。''',

    },

    'natural': {

        'no_argument': '''
自然语言处理
举例：
    ```{prefix}natural in 10 minutes send Hello World! to #general```
    ```{prefix}natural at 18:00 send 搞一波大操作！```
    ```{prefix}natural on the 16th of july at 14:00 send 该交订阅费了！ to #subs @Sub1 @Sub2```
    ```{prefix}natural now send 10分钟过去了！ every 10 minutes to #timer```
关键词：
    `send`：给出提醒内容
    `every`：给出重复周期（仅限Patreon）
    `to`：给出发往的对象（可以指定多个对象，如`@JellyWX #general @SomeUser`来同时发给这三个对象）
用法：
    ```{prefix}natural <时间短语> send <内容> [every 重复周期短语] [to #频道/@用户]```
    ''',

        'invalid_time': '''未能成功处理给出的时间。请尽可能清楚地表述，比如`16th of july`或是`in 20 minutes`''',

        'long_time': '''提醒事项的时间不能超过未来50年。如果没有，请尝试使用更明确的时间表述。''',

        'send': ''' send ''',

        'to': ''' to ''',

        'every': ''' every ''',

        'bulk_set': ''' {} 提醒事项已成功设置''',

    },

    'del': {

        'listing': '''正在列出此服务器上的提醒事项。（可能会有延迟，请等待“列出 (1,2,3...)”这条信息被发出。）''',

        'listed': '''列出事项的编号(1,2,3...)来删除提醒，或者发送任意其他内容来取消。''',

        'count': '''删除了{}条提醒！''',
    },

    'look': {

        'listing': '''正在列出指定频道上的提醒事项……''',

        'listing_limited': '''正在列出指定频道上的接下来{}个提醒事项……''',

        'inter': '''在''',
        
        'no_reminders': '''指定频道上没有提醒事项。''',
    },

    'todo': {

        'add': '''*用`{prefix}{command} add <内容>`来向你的待办事项列表里添加事项，或输入`{prefix}{command} help`来查看更多指令！*''',

        'added': '''成功将“{name}”加入待办事项列表！''',

        'removed': '''“{name}”已从待办事项列表中移除！''',

        'error_value': '''输入想要移除的事项的编号。用`{prefix}{command}`来查看待办事项列表。''',

        'error_index': '''没有找到该数字对应的事项。你不会是迷路了吧？''',

        'help': '''待办事项列表指令有：用`{prefix}{command} add <内容>`来增加待办事项，用`{prefix}{command} remove <编号>`来移除待办事项，用`{prefix}{command} clear`来清空待办事项列表，用`{prefix}{command}`来查看待办事项列表。''',

        'cleared': '''待办事项列表已被清空！''',

        'confirm': '''你将要把**{}件项目**从你的**{}**待办事项列表删除。你确定吗？（输入`yes`来确定）''',

        'canceled': '''已取消清空''',
    },

    'blacklist': {
        'removed_from': '''成功允许在该频道使用指令。''',

        'added_from': '''成功禁止在该频道使用指令。''',

        'removed': '''成功允许在此频道使用指令。''',

        'added': '''成功禁止在此频道使用指令。''',

    },

    'lang': {

        'invalid': '''语言：
{}''',

        'set': '''服务器语言已设置为中文。''',

        'set_p': '''您个人的语言已设置为中文''',
    },

    'clock': {

        'time': '''当前时间为{}。''',

    },

    'offset': {

        'help': '''用法：`{prefix}offset <时间/秒>`''',

        'invalid_time': '''请以 [num][s/m/h/d][num][s/m/h/d] 的格式给出时间''',

        'success': '''已将所有提醒事项平移{}秒''',

    },

    'nudge': {

        'invalid_time': '''请以 [num][s/m/h/d][num][s/m/h/d] 的格式给出时间，并保证时间不超过3万秒。''',

        'success': '''未来的提醒事项会全部推迟{}秒''',

    },

    'timer': {

        'limit': '''你已经设置了25个计时器。请先删除其中的一些，才能继续添加新计时器''',

        'name_length': '''请使用短一些的名称命名计时器（最大32个字符，你使用了{}个）''',

        'unique': '''请不要与其他计时器重名''',

        'success': '''成功设置新计时器''',

        'not_found': '''没有找到此名称的计时器''',

        'deleted': '''成功删除计时器''',

        'help': '''**计时器帮助**
`timer list` - 查看服务器/用户当前设置了的所有计时器

`timer start [名称]` - 开始一个新计时器（永久计时）

`timer delete <名称>` - 删除指定名称的计时器
        ''',

    },

    'pause': {

        'invalid_time': '''请以 [数字][s/m/h/d][数字][s/m/h/d]... 的格式给出时间。''',

        'paused_until': '''已暂停发送此频道的提醒事项直到 **{}**''',

        'paused_indefinite': '''已无限期暂停发送此频道的提醒事项''',

        'unpaused': '''已取消暂停发送此频道的提醒事项''',
    },
}
