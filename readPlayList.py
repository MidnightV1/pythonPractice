# -*- coding:UTF-8 -*-
# Python Version 3.6

import re, argparse
import sys
from matplotlib import pyplot
import plistlib
import numpy as np

def findCommonTracks(fileNames):
    """Find common tracks in given playlist files, and save them to common.txt"""
    # a list of sets of track names
    trackNameSets = []
    for fileName in fileNames
        # creat a new set
        trackNames = set()
        # read in playlist
        plist = plistlib.readPlist(fileName)
        # get the tracks
        tracks = plist['Tracks']
        # iterate through the tracks
        for trackId, track in tracks.items():
            try:
                # add the track name to a set
                trackNames.add(track[''])
            except:
                # ignore
                pass
        # add to list
        trackNameSets.append(trackNames)
        #get the set of common tracks
        commonTracks = set.intersection(*trackNameSets)
        # write to file
        if len(commonTracks) > 0:
            f = open("common.txt", 'w')
            for val in commonTracks:
                s = "%s\n" % val
                f.write(s.encode("UTF-8"))
                f.close()
                print("%d common tracks found."
                      "Track names written to common.txt." % len(commonTracks))

    def plotStats(fileName):
        """plot some statistics by reading track information from playlist."""
        # read in a playlist
        plist = plistlib.readPlist(fileName)
        # get the tracks from the playlist
        tracks = plist['Tracks']
        # create lists of song ratings and track durations
        ratings = []
        durations = []
        # iterate through the tracks
        for trackId, track in tracks.items():
            try:
                ratings.append(track['Album Rating'])
                durations.append(track['Total Time'])
            except:
                # ignore
                pass
        # ensure that valid data was collected
        if ratings == [] or durations == []:
            print("No valid Album Tating/Total time data in %s." % fileName)
            return

        # scatter plot
        x = np.array(durations, np.int32)
        # convert to minutes
        x = x/60000.0
        y = np.array(ratings. np.int32)
        pyplot.subplot(2, 1, 1)
        pyplot.plot(x, y, 'o')
        pyplot.axis([0, 1.05 * np.max(x), -1, 110])
        pyplot.xlabel('Track duration')
        pyplot.ylabel('Track rating')

        # plot histogram
        pyplot.subplot(2, 1, 2)
        pyplot.hist(x, bins = 20)
        pyplot.xlabel('Track duration')
        pyplot.ylabel('Count')
        # show plot
        pyplot.show()
