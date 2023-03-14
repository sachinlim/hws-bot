# HardwareSwapUK Discord Bot 

This bot is a smaller version of the main [Discord Bot](https://github.com/sachinlim/discord-bot) project. It incorporates the `!search` command and has renamed it to `!ebay` because there are other website specific commands available from other bots in the server. 

### Additional features

* Shortens links from eBay UK and Amazon UK
* Pings users with a certain role if a deal posted within a certain channel has enough votes 

### Community Requested features

These are the features being requested by the community, as of 14th March 2023:
- [ ] [CeX](https://uk.webuy.com/) information retrieval (similar to the `!eBay` command - there was a bot for this before)
- [ ] Option to have eBay [ephemeral](https://support.discord.com/hc/en-us/articles/1500000580222-Ephemeral-Messages-FAQ) commands (when running the eBay command, make it so that only the user can see the message)


## HardwareSwapUK

HardwareSwapUK is a [community on Reddit](https://www.reddit.com/r/HardwareSwapUK/) where people can buy, sell or trade hardware in the UK. It also exists on Discord but the origin of the community is on Reddit. This bot is implemented on the Discord server and only permitted to be used within certain channels.

### Screenshots

<p align="left">
  <img src="https://user-images.githubusercontent.com/80691974/218193178-47d36538-933b-4066-946d-1ca149937d2e.JPG" width="500">
</p>

<p align="left">
  <img src="https://user-images.githubusercontent.com/80691974/212488986-e4bcdba9-e1e8-4835-8299-a6e3d9405da6.png" width="500">
</p>

<p align="left">
  <img src="https://user-images.githubusercontent.com/80691974/218193621-5cc7f57e-061c-4cbb-a9f6-f1e90d5ffce1.JPG" width="500">
</p>


## Mean, median, mode and range

These values are important for traders to understand what is happening with sold items on eBay. Of the 4 values, the mean (average sold price) and the range are perhaps the most beneficial, as it tells a seller what ballpark they are in. 15% of the lowest and highest values are still being trimmed (removed) to remove outliers. 

For example, for an item with an average price of £400 and a range of £350-£425, the seller could choose to sell at a price between £350 and £390 to sell the item quicker. The opposite is true if the seller is willing to wait - they can sell their item between £410 and £425, as these are the prices that the item has previously sold for. 
