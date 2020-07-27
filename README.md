## Installation

```sh
python3 -m pip install git+https://github.com/LocalToasty/TelegramLogger@master
```


## Setup

1. [Create a new bot](https://core.telegram.org/bots) and save its token in
   `~/.telegramtoken`.
2. Add your bot on Telegram and write a message to it.
3. Run `telegram-logger -u`.  A list of all recent messages the bot has
   received should appear.  Write down the chat id of the message you just
   sent.


## Usage

TelegramLogger implements a logging handler which sends log messages to your
Telegram account.  The basic usage is as follows:

```python3
import logging
from telegramlogger import TelegramHandler

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

# create a Telegram handler relaying less detailed information (no debug info)
th = TelegramHandler(chat_id=123456789)  # TODO: replace with chat ID from above
th.setLevel(logging.INFO)
logger.addHandler(th)


# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
```

The above code should print out all five messages in the console, while only
sending the info, warning, error and critical messages to the recipients
Telegram.

For more information on logging please refer to the [Python
documentation](https://docs.python.org/3/library/logging.html).
