# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NodeWindowBasic.ui'
#
# Created: Mon Apr 01 22:57:51 2013
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(859, 846)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/brasero.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mainSplitter = QtGui.QSplitter(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.mainSplitter.sizePolicy().hasHeightForWidth())
        self.mainSplitter.setSizePolicy(sizePolicy)
        self.mainSplitter.setMinimumSize(QtCore.QSize(700, 700))
        self.mainSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.mainSplitter.setChildrenCollapsible(False)
        self.mainSplitter.setObjectName(_fromUtf8("mainSplitter"))
        self.nodeWindow_nodes_Splitter = QtGui.QSplitter(self.mainSplitter)
        self.nodeWindow_nodes_Splitter.setOrientation(QtCore.Qt.Vertical)
        self.nodeWindow_nodes_Splitter.setOpaqueResize(True)
        self.nodeWindow_nodes_Splitter.setChildrenCollapsible(False)
        self.nodeWindow_nodes_Splitter.setObjectName(_fromUtf8("nodeWindow_nodes_Splitter"))
        self.nodeDropGraphicsView = QtGui.QGraphicsView(self.nodeWindow_nodes_Splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.nodeDropGraphicsView.sizePolicy().hasHeightForWidth())
        self.nodeDropGraphicsView.setSizePolicy(sizePolicy)
        self.nodeDropGraphicsView.setMinimumSize(QtCore.QSize(0, 0))
        self.nodeDropGraphicsView.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.TextAntialiasing)
        self.nodeDropGraphicsView.setDragMode(QtGui.QGraphicsView.RubberBandDrag)
        self.nodeDropGraphicsView.setResizeAnchor(QtGui.QGraphicsView.NoAnchor)
        self.nodeDropGraphicsView.setObjectName(_fromUtf8("nodeDropGraphicsView"))
        self.nodesWindow = QtGui.QTabWidget(self.nodeWindow_nodes_Splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodesWindow.sizePolicy().hasHeightForWidth())
        self.nodesWindow.setSizePolicy(sizePolicy)
        self.nodesWindow.setMinimumSize(QtCore.QSize(450, 209))
        self.nodesWindow.setMovable(True)
        self.nodesWindow.setObjectName(_fromUtf8("nodesWindow"))
        self.tempTab = QtGui.QWidget()
        self.tempTab.setObjectName(_fromUtf8("tempTab"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.tempTab)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.rigNodesList = QtGui.QListWidget(self.tempTab)
        self.rigNodesList.setDragEnabled(True)
        self.rigNodesList.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.rigNodesList.setProperty(_fromUtf8("isWrapping"), True)
        self.rigNodesList.setLayoutMode(QtGui.QListView.SinglePass)
        self.rigNodesList.setGridSize(QtCore.QSize(100, 20))
        self.rigNodesList.setObjectName(_fromUtf8("rigNodesList"))
        self.horizontalLayout_4.addWidget(self.rigNodesList)
        self.nodesWindow.addTab(self.tempTab, _fromUtf8(""))
        self.nodeOption_description_Splitter = QtGui.QSplitter(self.mainSplitter)
        self.nodeOption_description_Splitter.setOrientation(QtCore.Qt.Vertical)
        self.nodeOption_description_Splitter.setChildrenCollapsible(False)
        self.nodeOption_description_Splitter.setObjectName(_fromUtf8("nodeOption_description_Splitter"))
        self.nodeOptionsWindow = QtGui.QGroupBox(self.nodeOption_description_Splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.nodeOptionsWindow.sizePolicy().hasHeightForWidth())
        self.nodeOptionsWindow.setSizePolicy(sizePolicy)
        self.nodeOptionsWindow.setMinimumSize(QtCore.QSize(225, 200))
        self.nodeOptionsWindow.setObjectName(_fromUtf8("nodeOptionsWindow"))
        self.gridLayout_2 = QtGui.QGridLayout(self.nodeOptionsWindow)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.nodeMenuArea = QtGui.QScrollArea(self.nodeOptionsWindow)
        self.nodeMenuArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.nodeMenuArea.setWidgetResizable(True)
        self.nodeMenuArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.nodeMenuArea.setObjectName(_fromUtf8("nodeMenuArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 205, 514))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_4 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.nodeMenuArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.nodeMenuArea, 0, 0, 1, 1)
        self.descriptionWindow = QtGui.QGroupBox(self.nodeOption_description_Splitter)
        self.descriptionWindow.setMinimumSize(QtCore.QSize(225, 235))
        self.descriptionWindow.setObjectName(_fromUtf8("descriptionWindow"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.descriptionWindow)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.descriptionLabel = QtGui.QLabel(self.descriptionWindow)
        self.descriptionLabel.setText(_fromUtf8(""))
        self.descriptionLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.descriptionLabel.setWordWrap(True)
        self.descriptionLabel.setObjectName(_fromUtf8("descriptionLabel"))
        self.horizontalLayout_2.addWidget(self.descriptionLabel)
        self.gridLayout.addWidget(self.mainSplitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 859, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.nodesWindow.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Rig Node Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.nodesWindow.setTabText(self.nodesWindow.indexOf(self.tempTab), QtGui.QApplication.translate("MainWindow", "temp", None, QtGui.QApplication.UnicodeUTF8))
        self.nodeOptionsWindow.setTitle(QtGui.QApplication.translate("MainWindow", "Node Name", None, QtGui.QApplication.UnicodeUTF8))
        self.descriptionWindow.setTitle(QtGui.QApplication.translate("MainWindow", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
