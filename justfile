#!/bin/bash

# justfile

# This is a Justfile for the BookBot project

run:
    python3 main.py

run-with-param path="dracula.txt":
    python3 main.py books/{{path}}

run-for-frankenstein:
    just run-with-param frankenstein.txt

run-for-pride-and-prejudice:
    just run-with-param prideandprejudice.txt

run-for-moby-dick:
    just run-with-param mobydick.txt

run-for-dracula:
    just run-with-param dracula.txt