#!/usr/bin/env python3
# Pylint is a tool to lint (style) python code.
# Github uses this file for Continuous Integration.

import os
import subprocess
import sys

path = sys.argv[-1]
current_path = os.path.dirname(os.path.abspath(__file__))

if path.startswith(current_path + "/project/"):
    path = path.replace(current_path + "/project/", "/src/")
    subprocess.run(
        [
            "docker-compose",
            "exec",
            "-T",
            "web",
            "sh",
            "-c",
            "PYTHONPATH=/src/extrasrc pylint {} {}".format(
                " ".join(sys.argv[1:-1]), path
            ),
        ],
        stdout=sys.stdout,
    )
else:
    subprocess.run([os.environ["HOME"] + "/.local/bin/pylint"] + sys.argv[1:])
