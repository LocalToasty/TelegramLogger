import logging
import telegram
from pathlib import Path
from typing import Union

class TelegramHandler(logging.StreamHandler):
    def __init__(self,
                 *args,
                 chat_id: int,
                 tokenpath: Union[Path, str] = Path.home()/'.telegramtoken',
                 **kwargs) -> None:

        super().__init__(*args, **kwargs)
        
        with open(tokenpath, 'r') as f:
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
