# -*- coding: utf-8 -*-
import cv2
import numpy as np
import struct
import wave
from tqdm import tqdm

def main():
    img = cv2.imread('../data/src/lena.png')

    # 読み込んだ画像の高さと幅を取得
    height = img.shape[0]
    width = img.shape[1]
    pixel = height*width
    x = 0
    y = 0
    data = []
    datas = b''
    print (pixel)
    
    for n in tqdm(range(pixel)):
        if x == width:
            x = 0
            y += 1

        data = [int((img[y ,x , 0] - 128) * 0.001 * 32767.0)]
        bindata = struct.pack("h" * len(data), *data)
        #print (bindata)
        datas += bindata
        x +=1
    
    #.wavとして書き出し
    #print (datas)
    w = wave.Wave_write("output.wav")
    p = (1, 2, 8000, len(datas), 'NONE', 'not compressed')
    w.setparams(p)
    w.writeframes(datas)
    w.close()
    

if __name__ == '__main__':
    main()
