#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import shutil


def progress_bar(iteration: int, total: int, prefix: str = '',
                 suffix: str = '') -> None:
   
    columns, _ = shutil.get_terminal_size(fallback=(80, 24))
    bar_len = columns - (len(suffix) + 2) - (len(prefix) + 2) - 7
    percent = iteration / total
    fill_len = int(bar_len * percent) + 1
    bar = '=' * fill_len + '-' * (bar_len - fill_len)
    sys.stdout.write(
        '{prefix} [{bar}] {percent}% {suffix}\r'.format(
            prefix=prefix,
            bar=bar,
            percent=round(percent * 100, 1),
            suffix=suffix
        )
    )
    sys.stdout.flush()
