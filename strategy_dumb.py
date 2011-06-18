#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "maxim"

from lib import run, iterate_in_loop


def main(state):
  iterate_in_loop(steps=[(1, "I", 0)], name="DUMB", state=state, log=False)


if __name__ == "__main__":
  run(main)
