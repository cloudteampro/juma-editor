# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'color_picker.ui'
#
# Created: Thu Apr  7 15:14:47 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ColorPicker(object):
    def setupUi(self, ColorPicker):
        ColorPicker.setObjectName("ColorPicker")
        ColorPicker.resize(460, 250)
        ColorPicker.setMinimumSize(QtCore.QSize(460, 250))
        ColorPicker.setMaximumSize(QtCore.QSize(460, 250))
        self.containerPreview = QtGui.QFrame(ColorPicker)
        self.containerPreview.setGeometry(QtCore.QRect(250, 10, 81, 61))
        self.containerPreview.setFrameShape(QtGui.QFrame.StyledPanel)
        self.containerPreview.setFrameShadow(QtGui.QFrame.Raised)
        self.containerPreview.setObjectName("containerPreview")
        self.widget = QtGui.QWidget(ColorPicker)
        self.widget.setGeometry(QtCore.QRect(250, 100, 81, 121))
        self.widget.setObjectName("widget")
        self.formLayout = QtGui.QFormLayout(self.widget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(2)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.numR = QtGui.QDoubleSpinBox(self.widget)
        self.numR.setMaximum(1.0)
        self.numR.setSingleStep(0.01)
        self.numR.setObjectName("numR")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.numR)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.numG = QtGui.QDoubleSpinBox(self.widget)
        self.numG.setMaximum(1.0)
        self.numG.setSingleStep(0.01)
        self.numG.setObjectName("numG")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.numG)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.numB = QtGui.QDoubleSpinBox(self.widget)
        self.numB.setMaximum(1.0)
        self.numB.setSingleStep(0.01)
        self.numB.setObjectName("numB")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.numB)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.numA = QtGui.QDoubleSpinBox(self.widget)
        self.numA.setMaximum(1.0)
        self.numA.setSingleStep(0.01)
        self.numA.setObjectName("numA")
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.numA)
        self.widget_2 = QtGui.QWidget(ColorPicker)
        self.widget_2.setGeometry(QtCore.QRect(330, 100, 101, 71))
        self.widget_2.setObjectName("widget_2")
        self.formLayout_2 = QtGui.QFormLayout(self.widget_2)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setSpacing(2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_5 = QtGui.QLabel(self.widget_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_5)
        self.numH = QtGui.QDoubleSpinBox(self.widget_2)
        self.numH.setDecimals(0)
        self.numH.setMaximum(360.0)
        self.numH.setObjectName("numH")
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.numH)
        self.label_6 = QtGui.QLabel(self.widget_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_6)
        self.numS = QtGui.QDoubleSpinBox(self.widget_2)
        self.numS.setMaximum(1.0)
        self.numS.setSingleStep(0.01)
        self.numS.setObjectName("numS")
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.numS)
        self.numV = QtGui.QDoubleSpinBox(self.widget_2)
        self.numV.setMaximum(1.0)
        self.numV.setSingleStep(0.01)
        self.numV.setObjectName("numV")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.numV)
        self.label_7 = QtGui.QLabel(self.widget_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_7)
        self.containerPalette = QtGui.QFrame(ColorPicker)
        self.containerPalette.setGeometry(QtCore.QRect(10, 250, 441, 201))
        self.containerPalette.setFrameShape(QtGui.QFrame.StyledPanel)
        self.containerPalette.setFrameShadow(QtGui.QFrame.Raised)
        self.containerPalette.setObjectName("containerPalette")
        self.layoutWidget = QtGui.QWidget(ColorPicker)
        self.layoutWidget.setGeometry(QtCore.QRect(350, 10, 91, 66))
        self.layoutWidget.setObjectName("layoutWidget")
        self.groupConfirmButtons = QtGui.QVBoxLayout(self.layoutWidget)
        self.groupConfirmButtons.setContentsMargins(0, 0, 0, 0)
        self.groupConfirmButtons.setObjectName("groupConfirmButtons")
        self.buttonOK = QtGui.QPushButton(self.layoutWidget)
        self.buttonOK.setAutoDefault(True)
        self.buttonOK.setDefault(True)
        self.buttonOK.setObjectName("buttonOK")
        self.groupConfirmButtons.addWidget(self.buttonOK)
        self.buttonCancel = QtGui.QPushButton(self.layoutWidget)
        self.buttonCancel.setObjectName("buttonCancel")
        self.groupConfirmButtons.addWidget(self.buttonCancel)
        self.layoutWidget1 = QtGui.QWidget(ColorPicker)
        self.layoutWidget1.setGeometry(QtCore.QRect(310, 220, 136, 23))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.groupCopyButtons = QtGui.QHBoxLayout(self.layoutWidget1)
        self.groupCopyButtons.setContentsMargins(0, 0, 0, 0)
        self.groupCopyButtons.setObjectName("groupCopyButtons")
        self.buttonCopyRGB = QtGui.QToolButton(self.layoutWidget1)
        self.buttonCopyRGB.setObjectName("buttonCopyRGB")
        self.groupCopyButtons.addWidget(self.buttonCopyRGB)
        self.buttonCopyHSV = QtGui.QToolButton(self.layoutWidget1)
        self.buttonCopyHSV.setObjectName("buttonCopyHSV")
        self.groupCopyButtons.addWidget(self.buttonCopyHSV)
        self.buttonCopyHEX = QtGui.QToolButton(self.layoutWidget1)
        self.buttonCopyHEX.setObjectName("buttonCopyHEX")
        self.groupCopyButtons.addWidget(self.buttonCopyHEX)
        self.containerMain = QtGui.QWidget(ColorPicker)
        self.containerMain.setGeometry(QtCore.QRect(0, 0, 251, 251))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.containerMain.sizePolicy().hasHeightForWidth())
        self.containerMain.setSizePolicy(sizePolicy)
        self.containerMain.setObjectName("containerMain")
        self.containerColorPlane = QtGui.QFrame(self.containerMain)
        self.containerColorPlane.setGeometry(QtCore.QRect(10, 10, 200, 200))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.containerColorPlane.sizePolicy().hasHeightForWidth())
        self.containerColorPlane.setSizePolicy(sizePolicy)
        self.containerColorPlane.setMinimumSize(QtCore.QSize(200, 200))
        self.containerColorPlane.setMaximumSize(QtCore.QSize(200, 200))
        self.containerColorPlane.setFrameShape(QtGui.QFrame.StyledPanel)
        self.containerColorPlane.setFrameShadow(QtGui.QFrame.Raised)
        self.containerColorPlane.setObjectName("containerColorPlane")
        self.containerHueSlider = QtGui.QFrame(self.containerMain)
        self.containerHueSlider.setGeometry(QtCore.QRect(220, 10, 20, 200))
        self.containerHueSlider.setMinimumSize(QtCore.QSize(20, 200))
        self.containerHueSlider.setMaximumSize(QtCore.QSize(20, 200))
        self.containerHueSlider.setFrameShape(QtGui.QFrame.StyledPanel)
        self.containerHueSlider.setFrameShadow(QtGui.QFrame.Raised)
        self.containerHueSlider.setObjectName("containerHueSlider")
        self.containerAlphaSlider = QtGui.QFrame(self.containerMain)
        self.containerAlphaSlider.setGeometry(QtCore.QRect(10, 220, 200, 20))
        self.containerAlphaSlider.setMinimumSize(QtCore.QSize(200, 20))
        self.containerAlphaSlider.setMaximumSize(QtCore.QSize(200, 20))
        self.containerAlphaSlider.setFrameShape(QtGui.QFrame.StyledPanel)
        self.containerAlphaSlider.setFrameShadow(QtGui.QFrame.Raised)
        self.containerAlphaSlider.setObjectName("containerAlphaSlider")
        self.buttonScreenPick = QtGui.QToolButton(self.containerMain)
        self.buttonScreenPick.setGeometry(QtCore.QRect(220, 220, 21, 21))
        self.buttonScreenPick.setObjectName("buttonScreenPick")
        self.layoutWidget2 = QtGui.QWidget(ColorPicker)
        self.layoutWidget2.setGeometry(QtCore.QRect(340, 180, 101, 23))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.formLayout_3 = QtGui.QFormLayout(self.layoutWidget2)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.textHex = QtGui.QLineEdit(self.layoutWidget2)
        self.textHex.setObjectName("textHex")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.textHex)
        self.label_8 = QtGui.QLabel(self.layoutWidget2)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_8)

        self.retranslateUi(ColorPicker)
        QtCore.QMetaObject.connectSlotsByName(ColorPicker)
        ColorPicker.setTabOrder(self.buttonOK, self.buttonCancel)
        ColorPicker.setTabOrder(self.buttonCancel, self.numR)
        ColorPicker.setTabOrder(self.numR, self.numG)
        ColorPicker.setTabOrder(self.numG, self.numB)
        ColorPicker.setTabOrder(self.numB, self.numA)
        ColorPicker.setTabOrder(self.numA, self.numH)
        ColorPicker.setTabOrder(self.numH, self.numS)
        ColorPicker.setTabOrder(self.numS, self.numV)
        ColorPicker.setTabOrder(self.numV, self.textHex)
        ColorPicker.setTabOrder(self.textHex, self.buttonCopyRGB)
        ColorPicker.setTabOrder(self.buttonCopyRGB, self.buttonCopyHSV)
        ColorPicker.setTabOrder(self.buttonCopyHSV, self.buttonCopyHEX)
        ColorPicker.setTabOrder(self.buttonCopyHEX, self.buttonScreenPick)

    def retranslateUi(self, ColorPicker):
        ColorPicker.setWindowTitle(QtGui.QApplication.translate("ColorPicker", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ColorPicker", "R", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ColorPicker", "G", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ColorPicker", "B", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ColorPicker", "A", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ColorPicker", "H", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ColorPicker", "S", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ColorPicker", "V", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonOK.setText(QtGui.QApplication.translate("ColorPicker", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonCancel.setText(QtGui.QApplication.translate("ColorPicker", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonCopyRGB.setText(QtGui.QApplication.translate("ColorPicker", "RGB", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonCopyHSV.setText(QtGui.QApplication.translate("ColorPicker", "HSV", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonCopyHEX.setText(QtGui.QApplication.translate("ColorPicker", "HEX", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonScreenPick.setText(QtGui.QApplication.translate("ColorPicker", "P", None, QtGui.QApplication.UnicodeUTF8))
        self.textHex.setText(QtGui.QApplication.translate("ColorPicker", "#FFFFFF", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ColorPicker", "Hex", None, QtGui.QApplication.UnicodeUTF8))

