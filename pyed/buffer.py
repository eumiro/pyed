#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Buffer:
    def __init__(self, lines=None):
        if lines is None:
            self.lines = []
        else:
            self.lines = [str(line) for line in lines]

    def __len__(self):
        return len(('\n'.join(self.lines)).encode('utf8'))
