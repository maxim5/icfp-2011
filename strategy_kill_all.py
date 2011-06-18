#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "maxim"

from lib import run, iterate_and_return


__doc__ = """
2 0 dec
1 K 0
1 S 0
2 0 get
// slot[0] = dec * get
1 K 0
1 S 0
2 0 succ
// slot[0] = dec * get * succ (dgs)
1 S 0
2 0 get
1 S 0
2 0 I
// slot[0] = S (S dgc get) I
//copy slot[0] to slot[2]:
2 2 zero
1 get 2
// slot[2] = S (S dgc get) I
// setup opponent slot to attack:
2 1 zero
1 succ 1
// slot[1] = 1
2 2 zero
//-83 vitality (255-get(slot[1])), slot[2] = I
//copy slot[0] to slot[2]:
2 2 zero
1 get 2
//now slot[2] = S (S dgc get) I again

repeat
2 2 zero
2 2 zero
1 get 2
"""


def main(state):
  iterate_and_return(steps=[(2, 0, "dec"),
                            (1, "K", 0),
                            (1, "S", 0),
                            (2, 0, "get"),

                            (1, "K", 0),
                            (1, "S", 0),
                            (2, 0, "succ"),

                            (1, "S", 0),
                            (2, 0, "get"),
                            (1, "S", 0),
                            (2, 0, "I"),

                            (2, 2, "zero"),
                            (1, "get", 2),

                            (2, 1, "zero"),
                           ],
                     name="KILL ALL", state=state, log=False)

  i = 0
  while True:
    for j in range(121):
      iterate_and_return(steps=[(2, 2, "zero"),
                                (2, 2, "zero"),
                                (1, "get", 2),],
                         name="KILL ALL", state=state, log=False)

    if i > 255: 
     #reset slot[1] to 0
      iterate_and_return(steps=[(1, "put", 1),
                                (2, 1, "zero"),],
                         name="KILL ALL", state=state, log=False)
      i = 0
    else:
     #inc slot[1] 
      iterate_and_return(steps=[(1, "succ", 1),],
                         name="KILL ALL", state=state, log=False)
      i = i + 1


if __name__ == "__main__":
  run(main)
