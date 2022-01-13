# The General-Purpose Annoying Bot

Annoying

## Getting started

Clone the repo and navigate to it, and then install these dependencies if you don't already have them:

```bash
pip install discord.py
```

The bots token and prefix are stored in a file called `config.json` located in main folder. Make it, and fill it with this:

```json
{
  "token": "YOUR_TOKEN_HERE",
  "prefix": "YOUR_PREFIX_HERE"
}
```

And then fill in the values for your bot's prefix and the [bots token](https://discord.com/developers/applications)

Run the bot with this command (in the bots directiory):

```bash
python main.py
```

## TODO

- Detect speech and respond accordingly
- Make the responses sound like Grace
- Menu in discord to manage options?
