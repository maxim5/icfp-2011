#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "maxim"

from lib import run, iterate_in_loop


__doc__ = """
2 0 K
2 0 S
1 S 0
2 0 K
// получили B в нулевом слоте, B - композиция функций S (K S) K
2 0 K
2 0 get
1 S 0
2 0 dec
// получили в нулевом слоте F = S (K * get) dec - функция, которая
ждёт x, делает dec(x), возвращает get(x),
1 S 0
2 0 I
// получили в нулевом слоте S F I, она ждёт аргумент, делает dec от
аргумента, и вызывает себя с этим же аргументом покак не вылитит
Native.AppLimitExceeded
2 0 zero
// отняли 111 vitality у нулевого слота противника
"""


def main(state):
  iterate_in_loop(steps=[(2, 0, "K"),
                         (2, 0, "S"),
                         (1, "S", 0),
                         (2, 0, "K"),
                         (2, 0, "K"),
                         (2, 0, "get"),
                         (1, "S", 0),
                         (2, 0, "dec"),
                         (1, "S", 0),
                         (2, 0, "I"),
                         (2, 0, "zero")],
                  name="DUMB", state=state)


if __name__ == "__main__":
  run(main)
