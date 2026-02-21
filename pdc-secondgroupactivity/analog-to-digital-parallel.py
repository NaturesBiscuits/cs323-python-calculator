from concurrent.futures import ThreadPoolExecutor
import time
import queue

class IceWrapper:
    def __init__(self):
        self.filledWithWater = False
        self.isTied = False
        self.isInFreezer = False
        self.isFrozen = False

    def fillWithWater(self):
        time.sleep(5)
        self.filledWithWater = True

    def tie(self):
        time.sleep(1)
        self.isTied = True

    def putInFreezer(self):
        time.sleep(1)
        self.isInFreezer = True

    def takeFromFreezer(self):
        time.sleep(10)
        self.isFrozen = True
        self.isInFreezer = False

def fillIceWrapper():
    myIceWrapper = IceWrapper()
    myIceWrapper.fillWithWater()
    return myIceWrapper

def tieIceWrapper(myIceWrapper : IceWrapper):
    myIceWrapper.tie()
    return myIceWrapper

def putinFreezer(myIceWrapper : IceWrapper):
    myIceWrapper.putInFreezer()
    return myIceWrapper

def takeFromFreezer(myIceWrapper : IceWrapper):
    myIceWrapper.takeFromFreezer()
    return myIceWrapper
