import sys
import time
import telepot
import telepot.namedtuple
from StringIO import StringIO
import urllib2
from PIL import Image
import requests
import numpy as np



"""
$ python2.7 emodi.py <token>

Emodi: An Emoji Unicode Decoder - You send me an emoji, I give you the unicode.

Caution: Python's treatment of unicode characters longer than 2 bytes (which
most emojis are) varies across versions and platforms. I have tested this program
on Python2.7.3/Raspbian. If you try it on other versions/platforms, the length-
checking and substring-extraction below may not work as expected.
"""

def handle(msg):

    content_type, chat_type, chat_id = telepot.glance(msg)
    m = telepot.namedtuple.Message(**msg)
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

    if chat_id < 0:
        # group message
        print 'Received a %s from %s, by %s' % (content_type, m.chat, m.from_)
    else:
        # private message
        print 'Received a %s from %s' % (content_type, m.chat)  # m.chat == m.from_

    if content_type == 'text':
        # For long messages, only return the first 10 characters.
        # Length-checking and substring-extraction may work differently
        # depending on Python versions and platforms. See above.
        f = open("images/craft_chest.png",'rb')
        bot.sendPhoto(chat_id, f)


TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print 'Listening ...'

# Keep the program running.
while 1:
    time.sleep(10)
