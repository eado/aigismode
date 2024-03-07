# beatmap.py
# Converts .osu files to time series of bitmaps
# Inference step: takes function that converts beatmap img to position
# Exports video of play through

import pygame
from pygame.locals import *

from neurochan.posu.env_utils import *
from neurochan.posu.emulator import *
from neurochan.posu.emulator_utils import *
from neurochan.osuparser.beatmapparser import *
from neurochan.data.data_utils import *
from neurochan.data.dataset import *

class Beatmap:
    def __init__(self, filename) -> None:
        parser = BeatmapParser()
        parser.parseFile(filename)
        beatmap_d = parser.build_beatmap()
        
        hitObjects = FormatParsedBeatmap(beatmap_d)