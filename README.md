# Discord Bot

A Discord bot built with Python using the [discord.py](https://discordpy.readthedocs.io/en/stable/) library. It responds to commands, 
sends random memes, and welcomes new members to the server.

---

## ✨ Features (for now)

- Responds to `$hello` with "Hello World!"
- Sends a random meme from the internet when you type `$meme`
- Greets new members with a welcome message in the `#general` channel

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/memebot.git
cd memebot
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

## 💡 Future Ideas
Add meme categories or subreddits

Use embeds for nicer formatting

Add commands like $joke, $quote, etc.

Log joins and message activity

## 📜 More Resources