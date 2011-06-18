# -*- coding: utf-8 -*-
__author__ = "maxim"

import sys


def run(main):
  if len(sys.argv) == 1:
    print "ICFP 2011 solution. Mandatory argument 0 or 1"
    return
  state = sys.argv[1]
  if state == "1":
    read_oppenent()
  try:
    main(state)
  except IOError:
    pass


counter = 0


def print_step(name, who, arg1, arg2, arg3):
  global counter
  sys.stderr.write("[%s] %s %d: (%s %s %s)\n" % (name.upper(), who.upper(), counter, str(arg1), str(arg2), str(arg3)))
  sys.stderr.flush()


def do_step(arg1, arg2, arg3, name=None, state=None, log=False):
  global counter
  counter += 1
  sys.stdout.write("%s\n%s\n%s\n" % (str(arg1), str(arg2), str(arg3)))
  if name is not None and log:
    print_step(name, state, arg1, arg2, arg3)
  sys.stdout.flush()


def read_oppenent():
  sys.stdin.readline()
  sys.stdin.readline()
  sys.stdin.readline()



def iterate_and_return(steps, name=None, state=None, log=False):
  global counter
  for step in steps:
    do_step(step[0], step[1], step[2], name=name, state=state, log=log)
    read_oppenent()


def iterate_in_loop(steps, name=None, state=None, log=False):
  global counter
  while True:
    if counter >= 100000:
      return
    step = steps[counter % len(steps)]
    do_step(step[0], step[1], step[2], name=name, state=state, log=log)
    read_oppenent()
