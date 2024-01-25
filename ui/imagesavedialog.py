# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imagesavedialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ImageSaveDialog(object):
    def setupUi(self, ImageSaveDialog):
        ImageSaveDialog.setObjectName("ImageSaveDialog")
        ImageSaveDialog.resize(390, 106)
        self.gridLayout = QtWidgets.QGridLayout(ImageSaveDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_Copy = QtWidgets.QPushButton(ImageSaveDialog)
        self.pushButton_Copy.setObjectName("pushButton_Copy")
        self.gridLayout.addWidget(self.pushButton_Copy, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(ImageSaveDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(ImageSaveDialog)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)
        self.spinBox_Width = QtWidgets.QSpinBox(ImageSaveDialog)
        self.spinBox_Width.setMinimum(1)
        self.spinBox_Width.setMaximum(99999)
        self.spinBox_Width.setProperty("value", 1)
        self.spinBox_Width.setObjectName("spinBox_Width")
        self.gridLayout.addWidget(self.spinBox_Width, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(ImageSaveDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.spinBox_Height = QtWidgets.QSpinBox(ImageSaveDialog)
        self.spinBox_Height.setMinimum(1)
        self.spinBox_Height.setMaximum(99999)
        self.spinBox_Height.setProperty("value", 1)
        self.spinBox_Height.setObjectName("spinBox_Height")
        self.gridLayout.addWidget(self.spinBox_Height, 1, 1, 1, 1)

        self.retranslateUi(ImageSaveDialog)
        self.buttonBox.accepted.connect(ImageSaveDialog.accept)
        self.buttonBox.rejected.connect(ImageSaveDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ImageSaveDialog)

    def retranslateUi(self, ImageSaveDialog):
        _translate = QtCore.QCoreApplication.translate
        ImageSaveDialog.setWindowTitle(_translate("ImageSaveDialog", "Save Current View as Image"))
        self.pushButton_Copy.setText(_translate("ImageSaveDialog", "Copy to Clipboard"))
        self.label_2.setText(_translate("ImageSaveDialog", "Image height"))
        self.spinBox_Width.setSuffix(_translate("ImageSaveDialog", " px"))
        self.label.setText(_translate("ImageSaveDialog", "Image width"))
        self.spinBox_Height.setSuffix(_translate("ImageSaveDialog", " px"))
