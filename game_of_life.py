#!/usr/bin/env python
from curses import wrapper
from time import sleep

def enumerate_lines(matrix):
    on = '*'
    off = ' '
    for i, row in enumerate(matrix):
        yield i, ''.join(on if v else off for v in row)

def paint(stdscr, matrix):
    stdscr.clear()
    for i, line in enumerate_lines(matrix):
        stdscr.addstr(i, 0, line)
    stdscr.refresh()


size = 50
m1 = [
    [i == j or i == size - j for j in xrange(0, size + 1)]
    for i in xrange(0, size + 1)
]
m2 = [
    [i == size / 2 or j == size / 2 for j in xrange(0, size + 1)]
    for i in xrange(0, size + 1)
]

def main(stdscr):
    for i in xrange(0,100):
        matrix = m1 if i % 2 else m2
        paint(stdscr, matrix)
        sleep(0.5)
    stdscr.getkey()

wrapper(main)
