#!/usr/bin/env python3

import argparse
import os
import random

import captcha.image
import cv2
import numpy


def main():
    wid = 128
    ht = 64
    count = 320000  # int(input())
    output_dir = 'Build'
    symbols = 'symbols.txt'
    length = 6

    captcha_generator = captcha.image.ImageCaptcha(width=wid, height=ht)

    symbols_file = open(symbols, 'r')
    captcha_symbols = symbols_file.readline().strip()
    symbols_file.close()

    print("Generating captchas with symbol set {" + captcha_symbols + "}")

    if not os.path.exists(output_dir):
        print("Creating output directory " + output_dir)
        os.makedirs(output_dir)

    for i in range(count):
        path_str = ""
        random_str = ''.join([random.choice(captcha_symbols)
                             for j in range(length)])
        path_str = random_str.replace(' ', '&')
        image_path = os.path.join(output_dir, path_str + '.png')
        if os.path.exists(image_path):
            version = 1
            print(version)
            while os.path.exists(os.path.join(output_dir, path_str + '_' + str(version) + '.png')):
                version += 1
            image_path = os.path.join(
                output_dir, path_str + '_' + str(version) + '.png')
        # print(random_str)
        image = numpy.array(captcha_generator.generate_image(random_str))
        cv2.imwrite(image_path, image)
        print(i, random_str)

    print("Completed captcha generation")


if __name__ == '__main__':
    main()
