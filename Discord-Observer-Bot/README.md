# Discord Observer

This is a bot that, after a specific amount of days, sends a message, that the user has been on the guild for that specific amount of days.

This can come in handy, if you have a guest role, and after for example two weeks the user can be promoted to a member.

## Running the bot

I recommend using repl.it. It's a free way to host your server. Using the keep_alive.py file included in this repo, the bot will also stay online.as long as you use something like uptimerobot.com/, to automatically ping the webserver.

To do that, all you have to do to run the bot.py file, and then a small window will pop up. In there, there should be an URL bar. Copy that link and go to https://uptimerobot.com.

## config.py - Configuring the bot

For now, this bot will use the exact role name. In the future, you will probably be able to use ID's.

~~NOTE: This bot uses ID's, for accurate results. If you dont know how to get the ID of a role, watch this youtube video: https://www.youtube.com/watch?v=OS2rp7wHVTI (Not by me.)
If you still have problems with getting the ID, open an issue.~~

You can change how long a user needs to be on the guild.

You can do that with the DAYS variable. (Note that this needs to be an INT, e.g. 5, no such numbers like 5.5)
If you still use such a number, the bot will round the number.

You can change for which roles the bot should look out, so for example it should only look for users with the guest role, not for users that are already a member.

You can do that with the ROLES_TO_LOOK_OUT variable.

TODO:
- [ ] Add possibility of choosing days, hours, minutes, seconds.
