import time
from artManager import artManager

am = artManager("belgian")
am.checkFilterMenuOn()
time.sleep(3)
am.getFilterTypes()
am.toggleFilter("Images_online")
time.sleep(5)
am.getFilterTypes()
am.toggleFilter("Belgian")
time.sleep(5)
am.getArtSizingOn()