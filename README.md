# GPT-3 Conversational Bot

A general-purpose annoying Discord bot based on GPT-3.

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

And then fill in the values for your bot's prefix, the [bot's token](https://discord.com/developers/applications) and an [OpenAI API key](https://openai.com/api).

Run the bot with this command (in the bots directiory):

```bash
python main.py training_data/Grace_optimized.txt
```

## TODO

- [ ] Modify the Training data to either have long conversations or make short, snappy things
- [x] Make the responses sound like Grace
- [ ] Work with temperature to make it lively
- [ ] Menu in discord to manage options?
- [x] Support for separate simultaneous conversations
- [ ] Different systems for _whether_ it should answer and _what_ it actually answers
- [ ] Shorten the length of the usernames in the training data (sha1 hashes ?)
