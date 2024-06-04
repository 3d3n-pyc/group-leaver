from discord.ext import commands
from datetime import datetime

import discord
import asyncio
import time
import log

import yaml; config = yaml.safe_load(open('config.yml', encoding='utf-8'))


class colors:
    reset = "\033[0m"
    bright_blue = "\033[94m"
    bright_red = "\033[91m"


bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    log.write('discord.utils', f'Script par @3d3n.pyc', log.levels.info)

    # Format: dd/mm/yyyy
    since = datetime.strptime(config['deleteIfInactiveSince'], r'%d/%m/%Y').timestamp()

    channels = bot.private_channels
    for channel in channels:
        if not isinstance(channel, discord.GroupChannel):
            continue

        if channel.id in config['whitelistedGroups']:
            continue

        timestamp = time.mktime(time.strptime(str(channel.last_viewed_timestamp), r"%Y-%m-%d"))

        if since < timestamp:
            continue

        log.write('discord.client', f'{colors.reset}En train de quitter {colors.bright_blue}{channel}{colors.reset} dû à son inactivité depuis le {colors.bright_red}{channel.last_viewed_timestamp.strftime(r'%d/%m/%Y')}', log.levels.warning)
        await channel.send(config['message'])
        await channel.leave(silent=config['silentLeave'])
        await asyncio.sleep(2)

    log.write('discord.utils', f'Fermeture dans 10 secondes', log.levels.info)
    await asyncio.sleep(10)
    await bot.close()


try:
    bot.run(config['token'])
except (
    discord.LoginFailure,
    discord.ConnectionClosed,
    discord.HTTPException,
    discord.GatewayNotFound
):
    log.write('discord.utils', f'Impossible de se connecter au bot, vérifiez le token.', log.levels.error)
    time.sleep(10)
except KeyboardInterrupt:
    log.write('discord.utils', f'Fermeture du bot', log.levels.info)
    time.sleep(10)
