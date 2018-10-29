#!/usr/bin/env python3
import sys

from pylint import lint
from pylint.reporters.text import ParseableTextReporter

if len(sys.argv) > 1:
    output_stream = open(sys.argv[1], 'w')
else:
    output_stream = sys.stdout

reporter = ParseableTextReporter(output_stream)

run = lint.Run(['philips_hue_hooks'], reporter=reporter, do_exit=False)

if run.linter.stats['error'] > 0 or run.linter.stats['fatal'] > 0:
    print('Errors detected.')
    sys.exit(1)

score = run.linter.stats['global_note']

if score < 0:
    print(f'Negative score ({score}), failing.')
    sys.exit(1)
