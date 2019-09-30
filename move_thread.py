#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from progress import progress_bar
from Move.move import Mover, _time
from concurrent.futures import ThreadPoolExecutor


class MoverThread(Mover):
    

    @_time
    def move(self):
        
        sys.stdout.write(
            "\033[1mMoving the files from `{primary_folder}` to "
            "`{secondary_folder}` using threading\033[0m\n".format(
                primary_folder=self.primary_directory,
                secondary_folder=self.secondary_directory
            )
        )

        files = os.listdir(self.primary_directory)

        with ThreadPoolExecutor(max_workers=4) as executor:
            for i, f in enumerate(files):
                progress_bar(i, len(files), prefix="Moving Files:")
                executor.submit(self._move, f)
        sys.stdout.write("\n")
