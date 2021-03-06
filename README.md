Project: ZENOBOT
Author: Nathan Browne
Created: Jan 2022
Last Edited: 17 Mar 2022

Description:
------------
Currently, ZenoBot is a service at t.me/zeno_crypto_bot that watches cryptos and notifies users when CUSUM filter events occur. This is best articulated by an example. Let's say you have 'BTC/USDT tick_100_10' in your watchlist. Zenobot will watch the BTC/USDT transactions in real-time and record a price every 100 ticks. When it records a new price, it finds the percentage difference between it and the previously recorded price, adding the modulus (so a change of -0.45% would INCREASE the sum by 0.45) of this value to a Cumulative Sum count. Once the Cumulative Sum count adds up to your filter level of 10%, it will notify you.

For brevity: A notification is sent when the cumulative percentage change between adjacent 100-tick-aggregated
BTC/USDT prices exceeds 10%.

So what's the point? Prices are not impacted by time. They are impacted by stores of wealth exchanging hands (market events). As a result, you'd rather know when market events are occurring than just checking the charts every x minutes. The CUSUM filter therefore sends many more notifications in periods of high volatility than it does in low ones, so you know when to pay attention. Available aggregations are tick (trade number), dollar (dollars exchanged) and volume (coins exchanged) Enter /future to learn more about future developments.

Execution:
----------
The code has 2 executable scripts that require the same poetry virtual environment.

Firstly, watcher/cusum.py is  executed from the run_watcher.py script at the top level. This is the script that counts and aggregates tick information.

Secondly, listener/listener.py runs and polls the bot's chats for messages from users. This is used as an interface between the user and their watchlist stored in MongoDB. This is fine with few users but eventually I may make this a webhook cloud function to deal with more frequent loads.

Updates Mar 2022:
-----------------
Zenobot now references a set of known support and resistance levels from a separate MongoDB Collection. This means every
notification now comes with an "Active range" giving users some more context for price direction.

Zenobot now includes a /stats command for a quick update on Crypto Market Cap statistics.

Market Cap statistics are now sent as pie charts.

Updates Feb 2022:
----------------
Zenobot now runs with a watchlist schema on MongoDB. This allows users to update or delete elements of their watchlist
directly from the message chat.
