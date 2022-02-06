# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_Window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(690, 600)
        Form.setMinimumSize(QSize(690, 600))
        Form.setMaximumSize(QSize(690, 600))
        font = QFont()
        font.setFamily(u"Noto Sans TC")
        font.setPointSize(10)
        font.setStyleStrategy(QFont.PreferAntialias)
        Form.setFont(font)
        self.SettingGroup = QGroupBox(Form)
        self.SettingGroup.setObjectName(u"SettingGroup")
        self.SettingGroup.setGeometry(QRect(10, 130, 671, 151))
        self.FPS_Text = QLabel(self.SettingGroup)
        self.FPS_Text.setObjectName(u"FPS_Text")
        self.FPS_Text.setGeometry(QRect(10, 40, 41, 21))
        self.FPS = QSpinBox(self.SettingGroup)
        self.FPS.setObjectName(u"FPS")
        self.FPS.setGeometry(QRect(50, 40, 42, 22))
        self.FPS.setMinimum(1)
        self.FPS.setMaximum(999)
        self.line = QFrame(self.SettingGroup)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(100, 10, 20, 81))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.Framerate_Text = QLabel(self.SettingGroup)
        self.Framerate_Text.setObjectName(u"Framerate_Text")
        self.Framerate_Text.setGeometry(QRect(120, 40, 111, 21))
        self.Framerate = QSpinBox(self.SettingGroup)
        self.Framerate.setObjectName(u"Framerate")
        self.Framerate.setGeometry(QRect(230, 40, 51, 22))
        self.Framerate.setMinimum(1)
        self.line_2 = QFrame(self.SettingGroup)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(290, 10, 20, 81))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.SettingGroup)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(520, 10, 20, 151))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(self.SettingGroup)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(0, 80, 531, 16))
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.Resolution_Text = QLabel(self.SettingGroup)
        self.Resolution_Text.setObjectName(u"Resolution_Text")
        self.Resolution_Text.setGeometry(QRect(10, 110, 51, 21))
        self.Resolution_W = QLineEdit(self.SettingGroup)
        self.Resolution_W.setObjectName(u"Resolution_W")
        self.Resolution_W.setGeometry(QRect(70, 110, 71, 21))
        self.StartButton = QPushButton(self.SettingGroup)
        self.StartButton.setObjectName(u"StartButton")
        self.StartButton.setGeometry(QRect(544, 20, 111, 121))
        font1 = QFont()
        font1.setFamily(u"Noto Sans TC")
        font1.setPointSize(16)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.StartButton.setFont(font1)
        self.Resolution_H = QLineEdit(self.SettingGroup)
        self.Resolution_H.setObjectName(u"Resolution_H")
        self.Resolution_H.setGeometry(QRect(180, 110, 71, 21))
        self.Resolution_X = QLabel(self.SettingGroup)
        self.Resolution_X.setObjectName(u"Resolution_X")
        self.Resolution_X.setGeometry(QRect(150, 110, 16, 21))
        self.Resolution_X.setAlignment(Qt.AlignCenter)
        self.FileFormat_Text = QLabel(self.SettingGroup)
        self.FileFormat_Text.setObjectName(u"FileFormat_Text")
        self.FileFormat_Text.setGeometry(QRect(310, 40, 71, 21))
        self.FileFormat = QLineEdit(self.SettingGroup)
        self.FileFormat.setObjectName(u"FileFormat")
        self.FileFormat.setGeometry(QRect(380, 40, 113, 20))
        self.label_2 = QLabel(self.SettingGroup)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 110, 231, 21))
        self.line.raise_()
        self.FPS_Text.raise_()
        self.FPS.raise_()
        self.Framerate_Text.raise_()
        self.Framerate.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.Resolution_Text.raise_()
        self.Resolution_W.raise_()
        self.StartButton.raise_()
        self.Resolution_H.raise_()
        self.Resolution_X.raise_()
        self.FileFormat_Text.raise_()
        self.FileFormat.raise_()
        self.label_2.raise_()
        self.FileGroup = QGroupBox(Form)
        self.FileGroup.setObjectName(u"FileGroup")
        self.FileGroup.setGeometry(QRect(10, 0, 671, 131))
        self.InputButton = QPushButton(self.FileGroup)
        self.InputButton.setObjectName(u"InputButton")
        self.InputButton.setGeometry(QRect(560, 30, 101, 31))
        font2 = QFont()
        font2.setFamily(u"Noto Sans TC")
        font2.setPointSize(11)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.InputButton.setFont(font2)
        self.OutputButton = QPushButton(self.FileGroup)
        self.OutputButton.setObjectName(u"OutputButton")
        self.OutputButton.setGeometry(QRect(560, 80, 101, 31))
        self.OutputButton.setFont(font2)
        self.InputDir = QLineEdit(self.FileGroup)
        self.InputDir.setObjectName(u"InputDir")
        self.InputDir.setGeometry(QRect(10, 30, 541, 31))
        self.OutputDir = QLineEdit(self.FileGroup)
        self.OutputDir.setObjectName(u"OutputDir")
        self.OutputDir.setGeometry(QRect(10, 80, 541, 31))
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 280, 671, 281))
        self.ErrorLog = QTextBrowser(self.groupBox)
        self.ErrorLog.setObjectName(u"ErrorLog")
        self.ErrorLog.setGeometry(QRect(10, 20, 651, 251))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 570, 671, 21))
        self.label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"影片合成器", None))
        self.SettingGroup.setTitle(
            QCoreApplication.translate("Form", u"\u8a2d\u5b9a", None)
        )
        self.FPS_Text.setText(QCoreApplication.translate("Form", u"FPS:", None))
        self.Framerate_Text.setText(
            QCoreApplication.translate(
                "Form", u"\u6bcf\u5f35\u7167\u7247\u6642\u9593(\u79d2):", None
            )
        )
        self.Resolution_Text.setText(
            QCoreApplication.translate("Form", u"\u89e3\u6790\u5ea6:", None)
        )
        self.StartButton.setText(
            QCoreApplication.translate("Form", u"\u958b\u59cb", None)
        )
        self.Resolution_X.setText(QCoreApplication.translate("Form", u"X", None))
        self.FileFormat_Text.setText(
            QCoreApplication.translate("Form", u"\u6a94\u6848\u683c\u5f0f:", None)
        )
        self.FileFormat.setInputMask("")
        self.FileFormat.setText("")
        self.label_2.setText(
            QCoreApplication.translate(
                "Form",
                u"\u70ba\u907f\u514d\u932f\u8aa4\uff0c\u76ee\u524d\u66ab\u4e0d\u652f\u63f4\u6b64\u529f\u80fd",
                None,
            )
        )
        self.FileGroup.setTitle(
            QCoreApplication.translate("Form", u"\u6a94\u6848", None)
        )
        self.InputButton.setText(
            QCoreApplication.translate("Form", u"\u9078\u64c7\u6a94\u6848...", None)
        )
        self.OutputButton.setText(
            QCoreApplication.translate("Form", u"\u8f38\u51fa\u6a94\u6848...", None)
        )
        self.groupBox.setTitle(
            QCoreApplication.translate("Form", u"\u8f38\u51fa\u7d00\u9304", None)
        )
        self.label.setText(
            QCoreApplication.translate(
                "Form",
                u'<html><head/><body><p>\u672c\u8edf\u9ad4\u7531<a href="http://github.com/cytsai1008"><span\n'
                '                 style=" text-decoration: underline; color:#0000ff;">CYTsai</span></a>\u88fd\u4f5c\uff0c\u672a\u7d93\u8a31\u53ef\u4e0d\u5f97\u64c5\u81ea\u5206\u4eab\u4ed8\u8cbb\u7248\uff0c\u672c\u4eba\u4e0d\u5c0d\u81ea\u884c\u7de8\u8b6f\u7248\u8ca0\u8cac</p></body></html>\n'
                "             ",
                None,
            )
        )

    # retranslateUi
