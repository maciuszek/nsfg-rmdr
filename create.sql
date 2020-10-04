SET FOREIGN_KEY_CHECKS=0;

USE YOUR_DATABASE;

CREATE TABLE YOUR_DATABASE.guilds (
    id INT UNSIGNED UNIQUE NOT NULL AUTO_INCREMENT,
    guild BIGINT UNSIGNED UNIQUE NOT NULL,

    name VARCHAR(100),

    prefix VARCHAR(5) DEFAULT '$' NOT NULL,
    timezone VARCHAR(32) DEFAULT 'UTC' NOT NULL,

    default_channel_id INT UNSIGNED,
    default_username VARCHAR(32) DEFAULT 'Reminder' NOT NULL,
    default_avatar VARCHAR(512) DEFAULT 'https://raw.githubusercontent.com/maciuszek/nsfg-rmdr/master/Remind_Me_Bot_Logo_PPic.jpg' NOT NULL,

    PRIMARY KEY (id),
    FOREIGN KEY (default_channel_id) REFERENCES YOUR_DATABASE.channels(id) ON DELETE SET NULL
);

CREATE TABLE YOUR_DATABASE.channels (
    id INT UNSIGNED UNIQUE NOT NULL AUTO_INCREMENT,
    channel BIGINT UNSIGNED UNIQUE NOT NULL,

    name VARCHAR(100),

    nudge SMALLINT NOT NULL DEFAULT 0,
    blacklisted BOOL NOT NULL DEFAULT FALSE,

    webhook_id BIGINT UNSIGNED UNIQUE,
    webhook_token TEXT,

    paused BOOL NOT NULL DEFAULT 0,
    paused_until TIMESTAMP,

    guild_id INT UNSIGNED,

    PRIMARY KEY (id),
    FOREIGN KEY (guild_id) REFERENCES YOUR_DATABASE.guilds(id) ON DELETE CASCADE
);

CREATE TABLE YOUR_DATABASE.users (
    id INT UNSIGNED AUTO_INCREMENT UNIQUE NOT NULL,
    user BIGINT UNSIGNED UNIQUE NOT NULL,

    name VARCHAR(37) NOT NULL,

    dm_channel INT UNSIGNED UNIQUE NOT NULL,

    language VARCHAR(2) DEFAULT 'EN' NOT NULL,
    timezone VARCHAR(32), # nullable s.t it can default to server timezone
    allowed_dm BOOLEAN DEFAULT 1 NOT NULL,

    patreon BOOL NOT NULL DEFAULT 0,

    PRIMARY KEY (id),
    FOREIGN KEY (dm_channel) REFERENCES YOUR_DATABASE.channels(id) ON DELETE RESTRICT
);

CREATE TABLE YOUR_DATABASE.roles (
    id INT UNSIGNED UNIQUE NOT NULL AUTO_INCREMENT,
    role BIGINT UNSIGNED UNIQUE NOT NULL,

    name VARCHAR(100),

    guild_id INT UNSIGNED NOT NULL,

    PRIMARY KEY (id),
    FOREIGN KEY (guild_id) REFERENCES YOUR_DATABASE.guilds(id) ON DELETE CASCADE
);

CREATE TABLE YOUR_DATABASE.embeds (
    id INT UNSIGNED AUTO_INCREMENT UNIQUE NOT NULL,

    title VARCHAR(256) NOT NULL DEFAULT '',
    description VARCHAR(2048) NOT NULL DEFAULT '',

    image_url VARCHAR(512),
    thumbnail_url VARCHAR(512),

    footer VARCHAR(2048) NOT NULL DEFAULT '',
    footer_icon VARCHAR(512),

    color MEDIUMINT UNSIGNED NOT NULL DEFAULT 0x0,

    PRIMARY KEY (id)
);

CREATE TABLE YOUR_DATABASE.messages (
    id INT UNSIGNED AUTO_INCREMENT UNIQUE NOT NULL,

    content VARCHAR(2048) NOT NULL DEFAULT '',
    tts BOOL NOT NULL DEFAULT 0,
    embed_id INT UNSIGNED,

    attachment MEDIUMBLOB,
    attachment_name VARCHAR(260),

    PRIMARY KEY (id),
    FOREIGN KEY (embed_id) REFERENCES YOUR_DATABASE.embeds(id) ON DELETE SET NULL
);

CREATE TABLE YOUR_DATABASE.reminders (
    id INT UNSIGNED AUTO_INCREMENT UNIQUE NOT NULL,
    uid VARCHAR(64) UNIQUE NOT NULL,

    name VARCHAR(24) NOT NULL DEFAULT 'Reminder',

    message_id INT UNSIGNED NOT NULL,
    channel_id INT UNSIGNED NOT NULL,

    `time` INT UNSIGNED DEFAULT 0 NOT NULL,
    `interval` INT UNSIGNED DEFAULT NULL,

    enabled BOOLEAN DEFAULT 1 NOT NULL,

    avatar VARCHAR(512) DEFAULT 'https://raw.githubusercontent.com/maciuszek/nsfg-rmdr/master/Remind_Me_Bot_Logo_PPic.jpg' NOT NULL,
    username VARCHAR(32) DEFAULT 'Reminder' NOT NULL,

    method ENUM('remind', 'natural', 'dashboard', 'todo'),
    set_at TIMESTAMP DEFAULT now(),
    set_by INT UNSIGNED,

    PRIMARY KEY (id),
    FOREIGN KEY (message_id) REFERENCES YOUR_DATABASE.messages(id) ON DELETE RESTRICT,
    FOREIGN KEY (channel_id) REFERENCES YOUR_DATABASE.channels(id) ON DELETE CASCADE,
    FOREIGN KEY (set_by) REFERENCES YOUR_DATABASE.users(id) ON DELETE SET NULL
);

-- CREATE TRIGGER message_cleanup AFTER DELETE ON YOUR_DATABASE.reminders
-- FOR EACH ROW
--     DELETE FROM YOUR_DATABASE.messages WHERE id = OLD.message_id;

-- CREATE TRIGGER embed_cleanup AFTER DELETE ON YOUR_DATABASE.messages
-- FOR EACH ROW
--     DELETE FROM YOUR_DATABASE.embeds WHERE id = OLD.embed_id;

CREATE TABLE YOUR_DATABASE.todos (
    id INT UNSIGNED AUTO_INCREMENT UNIQUE NOT NULL,
    user_id INT UNSIGNED,
    guild_id INT UNSIGNED,
    channel_id INT UNSIGNED,
    value VARCHAR(2000) NOT NULL,

    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES YOUR_DATABASE.users(id) ON DELETE SET NULL,
    FOREIGN KEY (guild_id) REFERENCES YOUR_DATABASE.guilds(id) ON DELETE CASCADE,
    FOREIGN KEY (channel_id) REFERENCES YOUR_DATABASE.channels(id) ON DELETE SET NULL
);

CREATE TABLE YOUR_DATABASE.command_restrictions (
    id INT UNSIGNED AUTO_INCREMENT UNIQUE NOT NULL,
    
    guild_id INT UNSIGNED NOT NULL,
    role_id INT UNSIGNED NOT NULL,
    command ENUM('todos', 'natural', 'remind', 'interval', 'timer', 'del', 'look', 'alias') NOT NULL,

    PRIMARY KEY (id),
    FOREIGN KEY (guild_id) REFERENCES YOUR_DATABASE.guilds(id) ON DELETE CASCADE,
    FOREIGN KEY (role_id) REFERENCES YOUR_DATABASE.roles(id) ON DELETE CASCADE,
    UNIQUE KEY (`role_id`, `command`)
);

CREATE TABLE YOUR_DATABASE.timers (
    id INT UNSIGNED AUTO_INCREMENT UNIQUE NOT NULL,
    start_time TIMESTAMP NOT NULL DEFAULT now(),
    name VARCHAR(32) NOT NULL,
    owner BIGINT UNSIGNED NOT NULL,

    PRIMARY KEY (id)
);

CREATE TABLE YOUR_DATABASE.events (
    id INT UNSIGNED AUTO_INCREMENT UNIQUE NOT NULL,
    `time` TIMESTAMP NOT NULL DEFAULT now(),

    event_name ENUM('edit', 'enable', 'disable', 'delete') NOT NULL,
    bulk_count INT UNSIGNED,

    guild_id INT UNSIGNED NOT NULL,
    user_id INT UNSIGNED,
    reminder_id INT UNSIGNED,

    PRIMARY KEY (id),
    FOREIGN KEY (guild_id) REFERENCES YOUR_DATABASE.guilds(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES YOUR_DATABASE.users(id) ON DELETE SET NULL,
    FOREIGN KEY (reminder_id) REFERENCES YOUR_DATABASE.reminders(id) ON DELETE SET NULL
);

CREATE TABLE YOUR_DATABASE.command_aliases (
    id INT UNSIGNED AUTO_INCREMENT UNIQUE NOT NULL,

    guild_id INT UNSIGNED NOT NULL,
    name VARCHAR(12) NOT NULL,

    command VARCHAR(2048) NOT NULL,

    PRIMARY KEY (id),
    FOREIGN KEY (guild_id) REFERENCES YOUR_DATABASE.guilds(id) ON DELETE CASCADE,
    UNIQUE KEY (`guild_id`, `name`)
);

CREATE TABLE YOUR_DATABASE.guild_users (
    guild INT UNSIGNED NOT NULL,
    user INT UNSIGNED NOT NULL,

    can_access BOOL NOT NULL DEFAULT 0,

    FOREIGN KEY (guild) REFERENCES YOUR_DATABASE.guilds(id) ON DELETE CASCADE,
    FOREIGN KEY (user) REFERENCES YOUR_DATABASE.users(id) ON DELETE CASCADE,
    UNIQUE KEY (guild, user)
);

CREATE EVENT YOUR_DATABASE.event_cleanup
ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 1 DAY
ON COMPLETION PRESERVE
DO DELETE FROM YOUR_DATABASE.events WHERE `time` < DATE_SUB(NOW(), INTERVAL 5 DAY);

CREATE TABLE YOUR_DATABASE.languages (
    id SMALLINT UNSIGNED AUTO_INCREMENT UNIQUE NOT NULL,
    name VARCHAR(20) NOT NULL,
    code VARCHAR(2) NOT NULL,

    PRIMARY KEY (id)
);
-- MUST RUN to_database.py TO FORM STRING STORES
