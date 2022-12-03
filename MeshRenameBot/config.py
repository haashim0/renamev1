from typing import Union

try:
    from .tconfig import Config
except ImportError:
    class Config:
        DATABASE_URL = [str, "mongodb+srv://Haashim:Haashim@mfile0.t9hxg.mongodb.net/?retryWrites=true&w=majority"]
        API_HASH = [str, "620f0a2aa2cd1474a4953619b3e3643d"]
        API_ID = [int, 14505719]
        BOT_TOKEN = [str, "5945219564:AAHMjrNCDXTgfBT-HuBmxjDN_0RHOORYqbA"]
        COMPLETED_STR = [str, "▰"]
        REMAINING_STR = [str, "▱"]
        MAX_QUEUE_SIZE = [int, 10]
        SLEEP_SECS = [int, 0]
        IS_MONGO = [bool, true]

        # Access Restriction
        IS_PRIVATE = [bool, true]
        AUTH_USERS = [list,[123456789]]
        OWNER_ID = [int, 5291606032]

        # Public username url or invite link of private chat
        FORCEJOIN = [str,"@tamildub_linkzz"]
        FORCEJOIN_ID = [int,-1001786200411]

        TRACE_CHANNEL = [int, 0]

try:
    from .tconfig import Commands
except ImportError:
    class Commands:
        START = "/start"
        RENAME = "/rename"
        FILTERS = "/filters"
        SET_THUMB = "/setthumb"
        GET_THUMB = "/getthumb"
        CLR_THUMB = "/clrthumb"
        QUEUE = "/queue"
        MODE = "/mode"
        HELP = "/help"
