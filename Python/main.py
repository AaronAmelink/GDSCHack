import time
from artManager import artManager

am = artManager()
am.checkFilterMenuOn()
time.sleep(3)
am.getFilterTypes()
am.toggleFilter("Images_online")
time.sleep(10)
am.getArtSizingOn()
time.sleep(5)