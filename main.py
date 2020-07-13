#!/usr/bin/python
# -*- coding: utf-8 -*-

from vigenere import *
from test import *

cle = "PASSION"
message_a_decoder = "Jn tsqgrg, msaa o gdul hzsasrw, ic'sfi-cw?\n" \
"Mv grgmwfb tnxt v'mv drj pdma dets, mfm dedmwkas."
print decoderMessage(cle, message_a_decoder)
