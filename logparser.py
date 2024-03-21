import re
import pandas as pd

def parse_message(message,*args):

    parsed = {}

    parsed['raw_log'] = message
    for pattern in args:
        m = pattern.search(message)
        if m:
            parsed.update(m.groupdict())
        else:
            continue

    return parsed

def parse_messages(messages,*args):
    return pd.DataFrame([parse_message(message,*args) for message in messages])


