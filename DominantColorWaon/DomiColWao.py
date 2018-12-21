# -*- coding: utf-8 -*-

# USAGE
# python color_kmeans.py --image images/lena.png --clusters 3




import wave
import numpy as np
import struct
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import argparse
import utils
import cv2

def createCombinedWave (A, freqList, fs, length):
    """freqListの正弦波を合成した波を返す"""
    data = []
    amp = float(A) / len(freqList)
    # [-1.0, 1.0]の小数値が入った波を作成
    for n in np.arange(length * fs):  # nはサンプルインデックス
        s = 0.0
        for f in freqList:
            s += amp * np.sin(2 * np.pi * f * n / fs)
        # 振幅が大きい時はクリッピング
        if s > 1.0:  s = 1.0
        if s < -1.0: s = -1.0
        data.append(s)
    return data

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
ap.add_argument("-c", "--clusters", required = True, type = int, help = "# of clusters")
args = vars(ap.parse_args())

# load the image and convert it from BGR to RGB so that
# we can dispaly it with matplotlib
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# show our image
plt.figure()
plt.axis("off")
plt.imshow(image)

# reshape the image to be a list of pixels
image = image.reshape((image.shape[0] * image.shape[1], 3))

# cluster the pixel intensities
clt = KMeans(n_clusters = args["clusters"])
clt.fit(image)

# build a histogram of clusters and then create a figure
# representing the number of pixels labeled to each color
hist = utils.centroid_histogram(clt)
bar = utils.plot_colors(sorted(hist), clt.cluster_centers_)
#hist = sorted(hist)
print(hist)#クラスタの割合

#print(clt.cluster_centers_)
#print(type(clt.cluster_centers_))
cltCenters = clt.cluster_centers_
cltCenters_list = cltCenters.tolist()
print(len(cltCenters_list))#画素値 [(R,G,B), (...)]

allcombData = []

for chordfreqList, histList in zip(cltCenters_list, hist):
    data = createCombinedWave(1.0, chordfreqList, 8000.0, histList*10)
    allcombData += data
allcombData = [int(x * 32767.0) for x in allcombData]
combbinData = struct.pack("h" * len(allcombData), *allcombData)

#save wave
w = wave.Wave_write("lowDomiCol.wav")
p = (1, 2, 8000, len(combbinData), 'NONE', 'not compressed')
w.setparams(p)
w.writeframes(combbinData)
w.close()

# show our color bart
plt.figure()
plt.axis("off")
plt.imshow(bar)
plt.show()