#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from pyke import knowledge_engine
from pyke import krb_traceback
from pyke import goal

engine = knowledge_engine.engine('.')

engine.assert_('facts', 'p', ('a', 'b'))
engine.assert_('facts', 'p', ('b', 'c'))
engine.assert_('facts', 'p', ('b', 'd'))

engine.activate('rules')

with engine.prove_goal('facts.q($x, $y)') as gen:
    for vs, plan in gen:
        print(vs)

engine.print_stats()
