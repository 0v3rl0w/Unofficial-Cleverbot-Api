#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
from selenium import webdriver

"""
    This lib is an unoffcicial API of Cleverbot

    Usage:
        >>> bot = Cleverbot()
        >>> bot.send('Hello')
        >>> print(bot.get())

        "Hi !"
"""

__version__ = "1.0"
__all__ = ["Cleverbot"]

class Cleverbot(object):
    def __init__(self):
        os.environ['MOZ_HEADLESS'] = '1'
        self.driver = webdriver.Firefox()

        self.driver.get("http://www.cleverbot.com/")

    def get(self):
        return self.driver.execute_script("return cleverbot.reply")
    def send(self, reply):
        return self.driver.execute_script("cleverbot.sendAI('%s')" % (reply.replace('\'', ' ').replace("à", "a").replace("ï", "i").replace("\"", " ").replace("@", "").replace("ô", "o").replace("ê", "e").replace("é", "e").replace("è", "e").replace("?", "").replace("!", "").lower()))
