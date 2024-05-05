import time
from artManager import artManager

am = artManager("church")
am.checkFilterMenuOn()
time.sleep(3)
am.getFilterTypes()
am.toggleFilter("Images_online")
time.sleep(5)
am.getArtSizingOn()