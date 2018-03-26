#!/usr/bin/python
# -*- coding: utf-8 -*-

import itertools
import os
import sys
import time
import zipfile

from closure_linter.gjslint import _CheckPaths, _PrintErrorRecords
from jsbeautifier import Beautifier, BeautifierOptions
from jsbeautifier import beautify_file, mkdir_p, isFileDifferent


from detector.config import APP_EXTENSION_NAME
from detector.constants import DetectorMode
from detector.error import H5DetectorException
from detector.logger import H5DetectorLogger

logger = H5DetectorLogger()


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        times = end_time - start_time
        logger.info('【function name：' + func.__name__ + '】:' +
                    ' executed time is:{}'.format(times))
        return result
    return wrapper


class DecompressApk:
    def __init__(self):
        pass

    @timer
    def decompress(self, input_file, output_base_path):
        """
        This function is to decompress apk
        :param input_file: inout file is an apk file
        :param output_base_path: out path is a path for app file to decompress
        :return: out path
        """

        if not os.path.exists(input_file):
            raise H5DetectorException('file not found!')

        file_path, extension_name = input_file.split('.')
        if extension_name != APP_EXTENSION_NAME:
            raise H5DetectorException('this file is not android app file')
        file_name = file_path[file_path.rfind('/')+1:]
        output_path = output_base_path + '/' + file_name

        r = zipfile.is_zipfile(input_file)
        if r:
            fz = zipfile.ZipFile(input_file, 'r')
            if not os.path.exists(output_path):
                os.makedirs(output_path)

            for f in fz.namelist():
                # write files to output path
                fz.extract(f, output_path)
        else:
            raise H5DetectorException('file is not an zip file')

        return output_path

    @timer
    def checker(self, path, mode=DetectorMode.default):
        """
        create_feature current path has js and html files
            :return: boolean: True or False
        """
        paths = []
        # TODO:
        for root, dirs, files in os.walk(path):
            current_root = root
            for f in files:
                if mode == DetectorMode.default:
                    if f.endswith('.html') or f.endswith('.js'):
                        paths.append(os.path.join(current_root, f))
                elif mode == DetectorMode.js:
                    if f.endswith('.js'):
                        js_path = os.path.join(current_root, f)
                        self.decompress_mini_js(js_path)
                        paths.append(js_path)
                else:
                    if f.endswith('.html'):
                        paths.append(os.path.join(current_root, f))

        return paths

    @timer
    def decompress_mini_js(self, js_file):
        """
        解压被压缩的JS文件
        :param js_file:
        :return:
        """
        js_options = BeautifierOptions()
        replace = True
        outfile = js_file
        try:
            if replace:
                outfile = js_file

            pretty = beautify_file(js_file, js_options)

            if outfile == 'stdout':
                sys.stdout.write(pretty)
            else:
                if isFileDifferent(outfile, pretty):
                    mkdir_p(os.path.dirname(outfile))
                    with open(outfile, 'w') as f:
                        f.write(pretty)

        except Exception as ex:
            raise H5DetectorException('There is an exception when'
                                      ' decompressing js file: {}'.format(js_file))



class H5Detector:
    def __init__(self):
        pass

    def _detectoring(self, paths):
        """
        Check JS code style
        :param paths:
        :return:
        """
        records_iter = _CheckPaths(paths)
        records_iter, records_iter_copy = itertools.tee(records_iter, 2)
        _PrintErrorRecords(records_iter_copy)

    def detectoring(self, paths):
        self._detectoring(paths)


if __name__ == '__main__':
    de = DecompressApk()
    detector = H5Detector()
    out_path = de.decompress("/media/wtq/0008943A0007A7BC/android-ad-apk/test_apk/0b7b0d6cd50bca1cbc2f9a818e802d3a.apk", "/home/output")
    # out_path = de.decompress('/home/kevin/Temps/t.apk', '/home/kevin/Temps/android1')
    detector.detectoring(de.checker(out_path, mode=DetectorMode.js))
