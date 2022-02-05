# StockScreenerBot
A simple discord.py bot application that will query a stock screen from FinViz.com on demand

In order to use this bot, you need to:
- Download the code to your local computer
- Create a Discord Bot Application on the Discord Developer Portal
- Create a file called "token.txt" and place it in the same directory as ``main.py``. 
- Add your bot application to your server through Discord's Dev Portal
- Run ``main.py`` in terminal and the bot will come online and be ready for use.
- (OPTIONAL) You can also use a hosting service, such as Heroku, to keep the bot on 24/7.

## Commands
Stock Screener Bot has 2 base commands: ``!screen lf`` and ``!screen options``. 
- The ``lf`` argument runs a screen based on parameters ideal for low float trading
- The ``options`` argument runs a screen based on paramters ideal for large cap options trading

