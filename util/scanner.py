import cv2
import os


class Scanner:

    @staticmethod
    def scanner(path: str):
        return cv2.imread(os.getcwd() + path)
