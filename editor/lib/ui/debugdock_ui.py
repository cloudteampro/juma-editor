# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'debugdock.ui'
#
# Created: Fri Mar 25 09:55:11 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DebugDrawDock(object):
    def setupUi(self, DebugDrawDock):
        DebugDrawDock.setObjectName("DebugDrawDock")
        DebugDrawDock.resize(475, 405)
        self.DrawContent = QtGui.QWidget()
        self.DrawContent.setObjectName("DrawContent")
        self.gridLayout = QtGui.QGridLayout(self.DrawContent)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtGui.QGroupBox(self.DrawContent)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.partitionCells = QtGui.QCheckBox(self.groupBox)
        self.partitionCells.setObjectName("partitionCells")
        self.gridLayout_2.addWidget(self.partitionCells, 0, 0, 1, 1)
        self.partitionPaddedCells = QtGui.QCheckBox(self.groupBox)
        self.partitionPaddedCells.setObjectName("partitionPaddedCells")
        self.gridLayout_2.addWidget(self.partitionPaddedCells, 1, 0, 1, 1)
        self.partitionPaddedCellsWidth = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.partitionPaddedCellsWidth.sizePolicy().hasHeightForWidth())
        self.partitionPaddedCellsWidth.setSizePolicy(sizePolicy)
        self.partitionPaddedCellsWidth.setMaximumSize(QtCore.QSize(40, 16777215))
        self.partitionPaddedCellsWidth.setObjectName("partitionPaddedCellsWidth")
        self.gridLayout_2.addWidget(self.partitionPaddedCellsWidth, 1, 1, 1, 1)
        self.textBox = QtGui.QCheckBox(self.groupBox)
        self.textBox.setObjectName("textBox")
        self.gridLayout_2.addWidget(self.textBox, 5, 0, 1, 1)
        self.partitionCellsWidth = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.partitionCellsWidth.sizePolicy().hasHeightForWidth())
        self.partitionCellsWidth.setSizePolicy(sizePolicy)
        self.partitionCellsWidth.setMaximumSize(QtCore.QSize(40, 16777215))
        self.partitionCellsWidth.setObjectName("partitionCellsWidth")
        self.gridLayout_2.addWidget(self.partitionCellsWidth, 0, 1, 1, 1)
        self.textBoxLayout = QtGui.QCheckBox(self.groupBox)
        self.textBoxLayout.setObjectName("textBoxLayout")
        self.gridLayout_2.addWidget(self.textBoxLayout, 8, 0, 1, 1)
        self.textBoxBaselines = QtGui.QCheckBox(self.groupBox)
        self.textBoxBaselines.setObjectName("textBoxBaselines")
        self.gridLayout_2.addWidget(self.textBoxBaselines, 7, 0, 1, 1)
        self.partitionCellsColor = QtGui.QToolButton(self.groupBox)
        self.partitionCellsColor.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.partitionCellsColor.setText("")
        self.partitionCellsColor.setObjectName("partitionCellsColor")
        self.gridLayout_2.addWidget(self.partitionCellsColor, 0, 2, 1, 1)
        self.partitionPaddedCellsColor = QtGui.QToolButton(self.groupBox)
        self.partitionPaddedCellsColor.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.partitionPaddedCellsColor.setText("")
        self.partitionPaddedCellsColor.setObjectName("partitionPaddedCellsColor")
        self.gridLayout_2.addWidget(self.partitionPaddedCellsColor, 1, 2, 1, 1)
        self.propModelBounds = QtGui.QCheckBox(self.groupBox)
        self.propModelBounds.setObjectName("propModelBounds")
        self.gridLayout_2.addWidget(self.propModelBounds, 2, 0, 1, 1)
        self.propWorldBounds = QtGui.QCheckBox(self.groupBox)
        self.propWorldBounds.setObjectName("propWorldBounds")
        self.gridLayout_2.addWidget(self.propWorldBounds, 4, 0, 1, 1)
        self.propModelBoundsWidth = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.propModelBoundsWidth.sizePolicy().hasHeightForWidth())
        self.propModelBoundsWidth.setSizePolicy(sizePolicy)
        self.propModelBoundsWidth.setMaximumSize(QtCore.QSize(40, 16777215))
        self.propModelBoundsWidth.setObjectName("propModelBoundsWidth")
        self.gridLayout_2.addWidget(self.propModelBoundsWidth, 2, 1, 1, 1)
        self.propModelBoundsColor = QtGui.QToolButton(self.groupBox)
        self.propModelBoundsColor.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.propModelBoundsColor.setText("")
        self.propModelBoundsColor.setObjectName("propModelBoundsColor")
        self.gridLayout_2.addWidget(self.propModelBoundsColor, 2, 2, 1, 1)
        self.propWorldBoundsWidth = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.propWorldBoundsWidth.sizePolicy().hasHeightForWidth())
        self.propWorldBoundsWidth.setSizePolicy(sizePolicy)
        self.propWorldBoundsWidth.setMaximumSize(QtCore.QSize(40, 16777215))
        self.propWorldBoundsWidth.setObjectName("propWorldBoundsWidth")
        self.gridLayout_2.addWidget(self.propWorldBoundsWidth, 4, 1, 1, 1)
        self.propWorldBoundsColor = QtGui.QToolButton(self.groupBox)
        self.propWorldBoundsColor.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.propWorldBoundsColor.setText("")
        self.propWorldBoundsColor.setObjectName("propWorldBoundsColor")
        self.gridLayout_2.addWidget(self.propWorldBoundsColor, 4, 2, 1, 1)
        self.textBoxWidth = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBoxWidth.sizePolicy().hasHeightForWidth())
        self.textBoxWidth.setSizePolicy(sizePolicy)
        self.textBoxWidth.setMaximumSize(QtCore.QSize(40, 16777215))
        self.textBoxWidth.setObjectName("textBoxWidth")
        self.gridLayout_2.addWidget(self.textBoxWidth, 5, 1, 1, 1)
        self.textBoxBaselinesWidth = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBoxBaselinesWidth.sizePolicy().hasHeightForWidth())
        self.textBoxBaselinesWidth.setSizePolicy(sizePolicy)
        self.textBoxBaselinesWidth.setMaximumSize(QtCore.QSize(40, 16777215))
        self.textBoxBaselinesWidth.setObjectName("textBoxBaselinesWidth")
        self.gridLayout_2.addWidget(self.textBoxBaselinesWidth, 7, 1, 1, 1)
        self.textBoxLayoutWidth = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBoxLayoutWidth.sizePolicy().hasHeightForWidth())
        self.textBoxLayoutWidth.setSizePolicy(sizePolicy)
        self.textBoxLayoutWidth.setMaximumSize(QtCore.QSize(40, 16777215))
        self.textBoxLayoutWidth.setObjectName("textBoxLayoutWidth")
        self.gridLayout_2.addWidget(self.textBoxLayoutWidth, 8, 1, 1, 1)
        self.textBoxColor = QtGui.QToolButton(self.groupBox)
        self.textBoxColor.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.textBoxColor.setText("")
        self.textBoxColor.setObjectName("textBoxColor")
        self.gridLayout_2.addWidget(self.textBoxColor, 5, 2, 1, 1)
        self.textBoxBaselinesColor = QtGui.QToolButton(self.groupBox)
        self.textBoxBaselinesColor.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.textBoxBaselinesColor.setText("")
        self.textBoxBaselinesColor.setObjectName("textBoxBaselinesColor")
        self.gridLayout_2.addWidget(self.textBoxBaselinesColor, 7, 2, 1, 1)
        self.textBoxLayoutColor = QtGui.QToolButton(self.groupBox)
        self.textBoxLayoutColor.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.textBoxLayoutColor.setText("")
        self.textBoxLayoutColor.setObjectName("textBoxLayoutColor")
        self.gridLayout_2.addWidget(self.textBoxLayoutColor, 8, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        DebugDrawDock.setWidget(self.DrawContent)

        self.retranslateUi(DebugDrawDock)
        QtCore.QObject.connect(self.partitionCells, QtCore.SIGNAL("toggled(bool)"), DebugDrawDock.togglePartitionCells)
        QtCore.QObject.connect(self.partitionPaddedCells, QtCore.SIGNAL("toggled(bool)"), DebugDrawDock.togglePartitionPaddedCells)
        QtCore.QObject.connect(self.propModelBounds, QtCore.SIGNAL("toggled(bool)"), DebugDrawDock.togglePropModelBounds)
        QtCore.QObject.connect(self.propWorldBounds, QtCore.SIGNAL("toggled(bool)"), DebugDrawDock.togglePropWorldBounds)
        QtCore.QObject.connect(self.textBox, QtCore.SIGNAL("toggled(bool)"), DebugDrawDock.toggleTextBox)
        QtCore.QObject.connect(self.textBoxBaselines, QtCore.SIGNAL("toggled(bool)"), DebugDrawDock.toggleTextBoxBaselines)
        QtCore.QObject.connect(self.textBoxLayout, QtCore.SIGNAL("toggled(bool)"), DebugDrawDock.toggleTextBoxLayout)
        QtCore.QObject.connect(self.partitionCellsWidth, QtCore.SIGNAL("textChanged(QString)"), DebugDrawDock.setWidthPartitionCells)
        QtCore.QObject.connect(self.partitionPaddedCellsWidth, QtCore.SIGNAL("textChanged(QString)"), DebugDrawDock.setWidthPartitionPaddedCells)
        QtCore.QObject.connect(self.propModelBoundsWidth, QtCore.SIGNAL("textChanged(QString)"), DebugDrawDock.setWidthPropModelBounds)
        QtCore.QObject.connect(self.propWorldBoundsWidth, QtCore.SIGNAL("textChanged(QString)"), DebugDrawDock.setWidthPropWorldBounds)
        QtCore.QObject.connect(self.textBoxWidth, QtCore.SIGNAL("textChanged(QString)"), DebugDrawDock.setWidthTextBox)
        QtCore.QObject.connect(self.textBoxBaselinesWidth, QtCore.SIGNAL("textChanged(QString)"), DebugDrawDock.setWidthTextBoxBaselines)
        QtCore.QObject.connect(self.textBoxLayoutWidth, QtCore.SIGNAL("textChanged(QString)"), DebugDrawDock.setWidthTextBoxLayout)
        QtCore.QObject.connect(self.partitionCellsColor, QtCore.SIGNAL("clicked()"), DebugDrawDock.pickColorPartitionCells)
        QtCore.QObject.connect(self.partitionPaddedCellsColor, QtCore.SIGNAL("clicked()"), DebugDrawDock.pickColorPartitionPaddedCells)
        QtCore.QObject.connect(self.propModelBoundsColor, QtCore.SIGNAL("clicked()"), DebugDrawDock.pickColorPropModelBounds)
        QtCore.QObject.connect(self.propWorldBoundsColor, QtCore.SIGNAL("clicked()"), DebugDrawDock.pickColorPropWorldBounds)
        QtCore.QObject.connect(self.textBoxColor, QtCore.SIGNAL("clicked()"), DebugDrawDock.pickColorTextBox)
        QtCore.QObject.connect(self.textBoxBaselinesColor, QtCore.SIGNAL("clicked()"), DebugDrawDock.pickColorTextBoxBaselines)
        QtCore.QObject.connect(self.textBoxLayoutColor, QtCore.SIGNAL("clicked()"), DebugDrawDock.pickColorTextBoxLayout)
        QtCore.QMetaObject.connectSlotsByName(DebugDrawDock)
        DebugDrawDock.setTabOrder(self.partitionCells, self.partitionCellsWidth)
        DebugDrawDock.setTabOrder(self.partitionCellsWidth, self.partitionPaddedCells)
        DebugDrawDock.setTabOrder(self.partitionPaddedCells, self.partitionPaddedCellsWidth)
        DebugDrawDock.setTabOrder(self.partitionPaddedCellsWidth, self.propModelBounds)
        DebugDrawDock.setTabOrder(self.propModelBounds, self.propModelBoundsWidth)
        DebugDrawDock.setTabOrder(self.propModelBoundsWidth, self.propWorldBounds)
        DebugDrawDock.setTabOrder(self.propWorldBounds, self.propWorldBoundsWidth)
        DebugDrawDock.setTabOrder(self.propWorldBoundsWidth, self.textBox)
        DebugDrawDock.setTabOrder(self.textBox, self.textBoxWidth)
        DebugDrawDock.setTabOrder(self.textBoxWidth, self.textBoxBaselines)
        DebugDrawDock.setTabOrder(self.textBoxBaselines, self.textBoxBaselinesWidth)
        DebugDrawDock.setTabOrder(self.textBoxBaselinesWidth, self.textBoxLayout)
        DebugDrawDock.setTabOrder(self.textBoxLayout, self.textBoxLayoutWidth)
        DebugDrawDock.setTabOrder(self.textBoxLayoutWidth, self.propWorldBoundsColor)
        DebugDrawDock.setTabOrder(self.propWorldBoundsColor, self.textBoxColor)
        DebugDrawDock.setTabOrder(self.textBoxColor, self.textBoxBaselinesColor)
        DebugDrawDock.setTabOrder(self.textBoxBaselinesColor, self.textBoxLayoutColor)
        DebugDrawDock.setTabOrder(self.textBoxLayoutColor, self.partitionPaddedCellsColor)
        DebugDrawDock.setTabOrder(self.partitionPaddedCellsColor, self.propModelBoundsColor)
        DebugDrawDock.setTabOrder(self.propModelBoundsColor, self.partitionCellsColor)

    def retranslateUi(self, DebugDrawDock):
        DebugDrawDock.setWindowTitle(QtGui.QApplication.translate("DebugDrawDock", "Debug", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("DebugDrawDock", "Debug Draw", None, QtGui.QApplication.UnicodeUTF8))
        self.partitionCells.setText(QtGui.QApplication.translate("DebugDrawDock", "PARTITION_CELLS", None, QtGui.QApplication.UnicodeUTF8))
        self.partitionPaddedCells.setText(QtGui.QApplication.translate("DebugDrawDock", "PARTITION_PADDED_CELLS", None, QtGui.QApplication.UnicodeUTF8))
        self.textBox.setText(QtGui.QApplication.translate("DebugDrawDock", "TEXT_BOX", None, QtGui.QApplication.UnicodeUTF8))
        self.textBoxLayout.setText(QtGui.QApplication.translate("DebugDrawDock", "TEXT_BOX_LAYOUT", None, QtGui.QApplication.UnicodeUTF8))
        self.textBoxBaselines.setText(QtGui.QApplication.translate("DebugDrawDock", "TEXT_BOX_BASELINES", None, QtGui.QApplication.UnicodeUTF8))
        self.propModelBounds.setText(QtGui.QApplication.translate("DebugDrawDock", "PROP_MODEL_BOUNDS", None, QtGui.QApplication.UnicodeUTF8))
        self.propWorldBounds.setText(QtGui.QApplication.translate("DebugDrawDock", "PROP_WORLD_BOUNDS", None, QtGui.QApplication.UnicodeUTF8))

