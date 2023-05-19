# GPT-3 Conversational Bot

_A general-purpose annoying Discord bot based on GPT-3_

## Getting started

Clone the repo and install all necessary dependencies:

```bash
pip install discord openai
```

The Discord bot token and OpenAI API key are stored in the config file `config.json` at the root of the project. It must contain the following key-value pairs:

```json
{
  "token": "YOUR_TOKEN_HERE",
  "openai_api_key": "YOUR_OPENAI_API_KEY_HERE"
}
```

See <https://discord.com/developers/applications> and <https://openai.com/api> for more details.

## Running the Bot

```bash
python main.py training_data/Grace_optimized.txt training_data/Grace_optimized.txt
```

## TODO

- [ ] Modify the training data to either have long conversations or make short, snappy responses
- [x] Make the responses sound like Grace
- [ ] Work with temperature to make the bot lively
- [ ] Menu in discord to manage options?
- [x] Support for separate simultaneous conversations
- [x] Different systems for _whether_ it should answer and _what_ it actually answers (turned out not to work)
- [x] Shorten the length of the usernames in the training data (sha1 hashes ?) (turned out not to work)
