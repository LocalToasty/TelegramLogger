import logging
import telegram
from pathlib import Path
from typing import Union

default_token_path = Path.home()/'.telegramtoken'

class TelegramHandler(logging.StreamHandler):
    def __init__(self,
                 *args,
                 chat_id: int,
                 token_path: Union[Path, str] = default_token_path,
                 **kwargs) -> None:

        super().__init__(*args, **kwargs)
        
        with open(token_path, 'r') as f:
            token = f.read().strip()
            self.bot = telegram.Bot(token=token)
            
        self.chat_id = chat_id
        
    def emit(self, record) -> None:
        msg = self.format(record)
        try:
            self.bot.send_message(chat_id=self.chat_id, text=msg)
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)
