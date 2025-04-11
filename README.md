# Discord Bot

A Discord bot built with Python using the [discord.py](https://discordpy.readthedocs.io/en/stable/) library. It responds to commands, 
sends random memes, and welcomes new members to the server.

This project is based on one of the guided project on Codedex: https://www.codedex.io/projects/build-a-discord-bot-with-python
The features will be further extended.

---

## ✨ Features (for now)

- Responds to `$hello` with "Hello World!"
- Sends a random meme from the internet when you type `$meme`
- Greets new members with a welcome message in the `#general` channel

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/madelinegtj/Discord-Bot.git
```
### 2. Install Dependencies

```bash
py -m pip install discord.py python-dotenv requests
```
### 3. Create a .env File
Create a .env file in the root folder and add your Discord bot token:

```ini
DISCORD_TOKEN=your_discord_token_here
```

## 🧪 Running the Bot
```bash
py bot.py
```

---

## 💡 More features to come
Add meme categories or subreddits
Use embeds for nicer formatting
Add more commands like $joke, $quote, etc.
Log joins and message activity

---

## 📜 More Resources
Discord Developer Portal: https://discord.com/developers/
Discord API documentation: https://discord.com/developers/docs/intro
Popular Discord Bots out there: https://top.gg/list/top
Start creating new applications (i.e. discord bots) here: https://discord.com/developers/applications
Python 'discord.py' package documentation: https://discordpy.readthedocs.io/en/stable/
Open-source meme API: https://github.com/D3vd/Meme_Api [see how it works: https://meme-api.com/gimme]

Codedex on GitHub: https://github.com/codedex-io/projects/blob/main/projects/build-a-discord-bot-with-python