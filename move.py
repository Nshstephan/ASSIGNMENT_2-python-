#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import shutil
from progress import progress_bar
from functools import wraps


def _time(func):
   

    @wraps(func)
    def time_func(*args, **kwargs):
        start_time = time.perf_counter()

        res = func(*args, **kwargs)

        sys.stdout.write(
            "\nDuration of the process: \033[1m{duration}\033[0m\n\n".format(
                duration=time.perf_counter() - start_time
            )
        )

        return res

    return time_func


class Mover:
  

    primary_directory = 'files'
    secondary_directory = 'files_new'

    def __init__(self) -> None:
      
        self._check_folder()

    @_time
    def move(self) -> None:
       
        sys.stdout.write(
            "\033[1mMoving the files from `{primary_folder}` to "
            "`{secondary_folder}`\033[0m\n".format(
                primary_folder=self.primary_directory,
                secondary_folder=self.secondary_directory
            )
        )

        files = os.listdir(self.primary_directory)
        for i, f in enumerate(files):
            self._move(f)
            progress_bar(i, len(files), prefix="Moving Files:")
        sys.stdout.write("\n")

    def _move(self, file_name: str) -> None:
        
        shutil.move(os.path.join(self.primary_directory, file_name),
                    os.path.join(self.secondary_directory, file_name))

    def _check_folder(self) -> None:
       
        if os.listdir(self.secondary_directory):
            assert os.listdir(self.primary_directory) == []
            self.primary_directory, self.secondary_directory = \
                self.secondary_directory, self.primary_directory
        else:
            if not os.listdir(self.primary_directory):
                raise MoverException("No files to move")
            else:
                assert os.listdir(self.secondary_directory) == []


class MoverException(Exception):
   
    pass
