#!/usr/bin/python
# -*- coding: utf-8 -*-

from vigenere import *
from test import *

cle = "PASSION"

with open('message.txt') as f:
    message_a_decoder = f.read()
    message_clair = decoderMessage(cle, message_a_decoder)

print message_clair
