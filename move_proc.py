#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import os
import sys
from progress import progress_bar
from Move.move import Mover, _time
from multiprocessing import Pool, cpu_count


class MoverProcess(Mover):
   

    @_time
    def move(self) -> None:
        
        sys.stdout.write(
            "\033[1mMoving the files from `{primary_folder}` to "
            "`{secondary_folder}` using processing\033[0m\n".format(
                primary_folder=self.primary_directory,
                secondary_folder=self.secondary_directory
            )
        )

        files = os.listdir(self.primary_directory)

        pool = Pool(processes=cpu_count())

        for i, f in enumerate(files):
            pool.apply_async(self._move, (f,))
            progress_bar(i, len(files), prefix="Moving files:")

        pool.close()
        pool.join()

        sys.stdout.write("\n")
