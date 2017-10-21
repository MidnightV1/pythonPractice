import re, argparse
import sys
from matplotlib import pyplot
import plistlib
import numpy as np

def findCommonTracks(fileNames):
    """Find common tracks in given playlist files, and save them to common.txt"""
    # a list of sets of track names



