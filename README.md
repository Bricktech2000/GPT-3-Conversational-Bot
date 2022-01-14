# General-Purpose Annoying Bot

Annoying

## Getting started

Clone the repo and navigate to it, and then install these dependencies if you don't already have them:

```bash
pip install discord openai
```

The bots token and prefix are stored in a file called `config.json` located in main folder. Make it, and fill it with this:

```json
{
  "token": "YOUR_TOKEN_HERE",
  "openai_api_key": "YOUR_OPENAI_API_KEY_HERE",
  "prefix": "YOUR_PREFIX_HERE"
}
```

And then fill in the values for your bot's prefix and the [bots token](https://discord.com/developers/applications)

Run the bot with this command (in the bots directiory):

```bash
python main.py training_data/Grace.txt
```

## TODO

- [ ] Modify the Training data to either have long conversations or make short, snappy things
- [x] Make the responses sound like Grace
- [ ] Work with temperature to make it lively
- [ ] Menu in discord to manage options?
- [ ] Support for separate simultaneous conversations
