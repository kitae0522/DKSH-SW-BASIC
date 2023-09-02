#!/usr/bin/python3

import re
import sys

type_list = [
    "FEAT",
    "FIX",
    "REFACTOR",
    "STYLE",
    "DOCS",
    "TEST",
    "CHORE",
    "CI",
    "PERF",
]
type_regex = (
    r"^(FEAT|FIX|REFACTOR|STYLE|DOCS|TEST|CHORE|CI|PERF)(\(.+\))?\:\s(.{3,})"
)


class bcolors:
    FAIL = "\033[91m"
    ENDC = "\033[0m"


def verify_commit_message():
    with open(sys.argv[1]) as commit:
        lines = commit.readlines()

        # Remove comments
        lines = [line for line in lines if not line.startswith("#")]

        # If the last line is whitespace, remove it
        while lines[-1] == "\n":
            lines = lines[:-1]
            if len(lines) == 0:
                break

        # Empty commit message
        if len(lines) == 0:
            sys.stderr.write(
                f"\n{bcolors.FAIL} Commit failed: {bcolors.ENDC}Empty commit message.\n"
            )
            sys.exit(1)
        # Subject line should be less than 50 characters.
        if len(lines[0]) > 50:
            sys.stderr.write(
                f"\n{bcolors.FAIL} Commit failed: {bcolors.ENDC}Subject line should be less than 50 characters.\n"
            )
            sys.exit(1)
        # Subject line should follow the rule.
        if re.match(f"({type_regex})", lines[0]) is None:
            sys.stderr.write(
                f"\n{bcolors.FAIL} Commit failed: {bcolors.ENDC}The commit message subject line does not follow the rule."
            )
            sys.stderr.write("\n<type>: <subject> is required.\n")
            sys.exit(1)
        # The subject should be a title-case.
        #if not lines[0].split(":")[1].strip()[0].istitle():
        #    sys.stderr.write(
        #        f"\n{bcolors.FAIL} Commit failed: {bcolors.ENDC}The subject should be title-cased.\n"
        #    )
        #    sys.exit(1)
        # If commit message has single line, description might be missing.
        if len(lines) == 1:
            sys.stderr.write(
                f"\n{bcolors.FAIL} Commit failed: {bcolors.ENDC}Descriptions are missing.\n"
            )
            sys.exit(1)
        # After subject line, line space is required.
        if lines[1] != "\n":
            sys.stderr.write(
                "\nThe line space after the subject line is required.\n"
            )
            sys.exit(1)
        for line in lines[2:]:
            # Every single description should be less than 72 characters.
            if len(line) > 72:
                sys.stderr.write(
                    "\nEvery single description should be less than 72 characters.\n"
                )
                sys.exit(1)
            # Description starts with "-".
            #if not line.startswith("-"):
            #    sys.stderr.write(line)
            #    sys.stderr.write(
            #        f"\n{bcolors.FAIL} Commit failed: {bcolors.ENDC}Description should start with a dash '-'.\n"
            #    )
            #    sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    verify_commit_message()