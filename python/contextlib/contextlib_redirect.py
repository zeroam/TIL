"""
Poorly designed library code may write directly to sys.stdout or sys.stderr, 
without providing arguments to configure different output destinations.

The `redirect_stdout()` and `redirect_stderr()` context mangers can be
used to capture output from functions like this, for which the source
cannot be changed to accept a new output argument.
"""
from contextlib import redirect_stdout, redirect_stderr
import io
import sys


def misbehaving_function(a):
    sys.stdout.write('(stdout) A: {!r}\n'.format(a))
    sys.stderr.write('(stderr) A: {!r}\n'.format(a))


capture = io.StringIO()
with redirect_stdout(capture), redirect_stderr(capture):
    misbehaving_function(5)

print(capture.getvalue())
