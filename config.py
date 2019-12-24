import os


def getDriverDir():
    return os.path.dirname(os.path.abspath(__file__)) + "/bin/chromedriver"
