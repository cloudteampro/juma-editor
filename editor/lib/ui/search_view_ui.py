# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_view.ui'
#
# Created: Fri Mar 25 09:55:11 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SearchView(object):
    def setupUi(self, SearchView):
        SearchView.setObjectName("SearchView")
        SearchView.resize(279, 141)
        self.verticalLayout = QtGui.QVBoxLayout(SearchView)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelInfo = QtGui.QLabel(SearchView)
        self.labelInfo.setText("")
        self.labelInfo.setObjectName("labelInfo")
        self.verticalLayout.addWidget(self.labelInfo)
        self.containerTextTerm = QtGui.QWidget(SearchView)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.containerTextTerm.sizePolicy().hasHeightForWidth())
        self.containerTextTerm.setSizePolicy(sizePolicy)
        self.containerTextTerm.setObjectName("containerTextTerm")
        self.verticalLayout.addWidget(self.containerTextTerm)
        self.containerResultTree = QtGui.QFrame(SearchView)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.containerResultTree.sizePolicy().hasHeightForWidth())
        self.containerResultTree.setSizePolicy(sizePolicy)
        self.containerResultTree.setFrameShape(QtGui.QFrame.StyledPanel)
        self.containerResultTree.setFrameShadow(QtGui.QFrame.Raised)
        self.containerResultTree.setObjectName("containerResultTree")
        self.verticalLayout.addWidget(self.containerResultTree)
        self.containerBottom = QtGui.QWidget(SearchView)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.containerBottom.sizePolicy().hasHeightForWidth())
        self.containerBottom.setSizePolicy(sizePolicy)
        self.containerBottom.setObjectName("containerBottom")
        self.horizontalLayout = QtGui.QHBoxLayout(self.containerBottom)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonAll = QtGui.QToolButton(self.containerBottom)
        self.buttonAll.setObjectName("buttonAll")
        self.horizontalLayout.addWidget(self.buttonAll)
        self.buttonNone = QtGui.QToolButton(self.containerBottom)
        self.buttonNone.setObjectName("buttonNone")
        self.horizontalLayout.addWidget(self.buttonNone)
        self.buttonInverse = QtGui.QToolButton(self.containerBottom)
        self.buttonInverse.setObjectName("buttonInverse")
        self.horizontalLayout.addWidget(self.buttonInverse)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonOK = QtGui.QPushButton(self.containerBottom)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonOK.sizePolicy().hasHeightForWidth())
        self.buttonOK.setSizePolicy(sizePolicy)
        self.buttonOK.setObjectName("buttonOK")
        self.horizontalLayout.addWidget(self.buttonOK)
        self.buttonCancel = QtGui.QPushButton(self.containerBottom)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonCancel.sizePolicy().hasHeightForWidth())
        self.buttonCancel.setSizePolicy(sizePolicy)
        self.buttonCancel.setObjectName("buttonCancel")
        self.horizontalLayout.addWidget(self.buttonCancel)
        self.verticalLayout.addWidget(self.containerBottom)

        self.retranslateUi(SearchView)
        QtCore.QMetaObject.connectSlotsByName(SearchView)

    def retranslateUi(self, SearchView):
        SearchView.setWindowTitle(QtGui.QApplication.translate("SearchView", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonAll.setText(QtGui.QApplication.translate("SearchView", "A", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonNone.setText(QtGui.QApplication.translate("SearchView", "N", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonInverse.setText(QtGui.QApplication.translate("SearchView", "I", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonOK.setText(QtGui.QApplication.translate("SearchView", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonCancel.setText(QtGui.QApplication.translate("SearchView", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
