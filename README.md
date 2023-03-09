# Task1
Приложение по отслеживанию времени человека на работе
Цель работы: создания своего приложения для учета времени работника.
Суть работы приложения:
Происходит регистрация с помощью функции face_photo(вы фотографируетесь) и человека заносят в базу фотографий, которую распознаёт программа.
Человек заходит в программу, если он есть в базе, то вебкамера его распознаёт. Работник нажимает на кнопку “Начало работы” и идёт отсчёт времени(пока человек находится у вебкамеры). Время начала и окончания работы записывается в csv файл.
Используемые инструменты:
•	Графический интерфейс разработан в qt design
•	Cреда разработки: PyCharm
•	Используемые библиотеки
•	from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot, QTimer, QDate, Qt
from PyQt5.QtWidgets import QDialog,QMessageBox
import cv2
import face_recognition
import numpy as np
import datetime
import os
import csv

