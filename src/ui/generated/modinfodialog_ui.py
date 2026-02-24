# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modinfodialog.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDialog, QFrame, QHBoxLayout, QHeaderView,
    QLCDNumber, QLabel, QLineEdit, QListView,
    QPlainTextEdit, QPushButton, QRadioButton, QScrollBar,
    QSizePolicy, QSpacerItem, QSplitter, QTabWidget,
    QTextEdit, QToolButton, QTreeView, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

from texteditor import TextEditor
import resources_rc

class Ui_ModInfoDialog(object):
    def setupUi(self, ModInfoDialog):
        if not ModInfoDialog.objectName():
            ModInfoDialog.setObjectName(u"ModInfoDialog")
        ModInfoDialog.resize(735, 534)
        self.verticalLayout = QVBoxLayout(ModInfoDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(ModInfoDialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setMovable(True)
        self.tabText = QWidget()
        self.tabText.setObjectName(u"tabText")
        self.verticalLayout_15 = QVBoxLayout(self.tabText)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.tabTextSplitter = QSplitter(self.tabText)
        self.tabTextSplitter.setObjectName(u"tabTextSplitter")
        self.tabTextSplitter.setOrientation(Qt.Horizontal)
        self.tabTextSplitter.setChildrenCollapsible(False)
        self.widget_6 = QWidget(self.tabTextSplitter)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_16 = QVBoxLayout(self.widget_6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget_6)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_16.addWidget(self.label_5)

        self.textFileList = QListView(self.widget_6)
        self.textFileList.setObjectName(u"textFileList")
        self.textFileList.setAlternatingRowColors(True)
        self.textFileList.setUniformItemSizes(True)

        self.verticalLayout_16.addWidget(self.textFileList)

        self.textFileFilter = QLineEdit(self.widget_6)
        self.textFileFilter.setObjectName(u"textFileFilter")

        self.verticalLayout_16.addWidget(self.textFileFilter)

        self.tabTextSplitter.addWidget(self.widget_6)
        self.widget_7 = QWidget(self.tabTextSplitter)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_17 = QVBoxLayout(self.widget_7)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.textFileEditor = QPlainTextEdit(self.widget_7)
        self.textFileEditor.setObjectName(u"textFileEditor")

        self.verticalLayout_17.addWidget(self.textFileEditor)

        self.tabTextSplitter.addWidget(self.widget_7)

        self.verticalLayout_15.addWidget(self.tabTextSplitter)

        self.tabWidget.addTab(self.tabText, "")
        self.tabIni = QWidget()
        self.tabIni.setObjectName(u"tabIni")
        self.verticalLayout_9 = QVBoxLayout(self.tabIni)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tabIniSplitter = QSplitter(self.tabIni)
        self.tabIniSplitter.setObjectName(u"tabIniSplitter")
        self.tabIniSplitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.tabIniSplitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_5.addWidget(self.label_6)

        self.iniFileList = QListView(self.layoutWidget)
        self.iniFileList.setObjectName(u"iniFileList")
        self.iniFileList.setAlternatingRowColors(True)
        self.iniFileList.setUniformItemSizes(True)

        self.verticalLayout_5.addWidget(self.iniFileList)

        self.iniFileFilter = QLineEdit(self.layoutWidget)
        self.iniFileFilter.setObjectName(u"iniFileFilter")

        self.verticalLayout_5.addWidget(self.iniFileFilter)

        self.tabIniSplitter.addWidget(self.layoutWidget)
        self.layoutWidget1 = QWidget(self.tabIniSplitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.iniFileEditor = TextEditor(self.layoutWidget1)
        self.iniFileEditor.setObjectName(u"iniFileEditor")

        self.verticalLayout_4.addWidget(self.iniFileEditor)

        self.tabIniSplitter.addWidget(self.layoutWidget1)

        self.verticalLayout_9.addWidget(self.tabIniSplitter)

        self.tabWidget.addTab(self.tabIni, "")
        self.tabImages = QWidget()
        self.tabImages.setObjectName(u"tabImages")
        self.verticalLayout_19 = QVBoxLayout(self.tabImages)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.tabImagesSplitter = QSplitter(self.tabImages)
        self.tabImagesSplitter.setObjectName(u"tabImagesSplitter")
        self.tabImagesSplitter.setOrientation(Qt.Horizontal)
        self.tabImagesSplitter.setChildrenCollapsible(False)
        self.widget_8 = QWidget(self.tabImagesSplitter)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_2 = QVBoxLayout(self.widget_8)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.imagesScroller = QWidget(self.widget_8)
        self.imagesScroller.setObjectName(u"imagesScroller")
        self.horizontalLayout_4 = QHBoxLayout(self.imagesScroller)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.imagesThumbnails = QWidget(self.imagesScroller)
        self.imagesThumbnails.setObjectName(u"imagesThumbnails")
        self.imagesThumbnails.setFocusPolicy(Qt.StrongFocus)

        self.horizontalLayout_4.addWidget(self.imagesThumbnails)

        self.imagesScrollerVBar = QScrollBar(self.imagesScroller)
        self.imagesScrollerVBar.setObjectName(u"imagesScrollerVBar")
        self.imagesScrollerVBar.setOrientation(Qt.Vertical)

        self.horizontalLayout_4.addWidget(self.imagesScrollerVBar)


        self.verticalLayout_2.addWidget(self.imagesScroller)

        self.imagesShowDDS = QCheckBox(self.widget_8)
        self.imagesShowDDS.setObjectName(u"imagesShowDDS")

        self.verticalLayout_2.addWidget(self.imagesShowDDS)

        self.imagesFilter = QLineEdit(self.widget_8)
        self.imagesFilter.setObjectName(u"imagesFilter")

        self.verticalLayout_2.addWidget(self.imagesFilter)

        self.verticalLayout_2.setStretch(0, 1)
        self.tabImagesSplitter.addWidget(self.widget_8)
        self.imagesContainer = QWidget(self.tabImagesSplitter)
        self.imagesContainer.setObjectName(u"imagesContainer")
        self.verticalLayout_18 = QVBoxLayout(self.imagesContainer)
        self.verticalLayout_18.setSpacing(3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.widget_12 = QWidget(self.imagesContainer)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.previewPluginButton = QToolButton(self.widget_12)
        self.previewPluginButton.setObjectName(u"previewPluginButton")

        self.horizontalLayout_3.addWidget(self.previewPluginButton)

        self.imagesExplore = QToolButton(self.widget_12)
        self.imagesExplore.setObjectName(u"imagesExplore")

        self.horizontalLayout_3.addWidget(self.imagesExplore)

        self.imagesPath = QLineEdit(self.widget_12)
        self.imagesPath.setObjectName(u"imagesPath")
        self.imagesPath.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.imagesPath)

        self.imagesSize = QLabel(self.widget_12)
        self.imagesSize.setObjectName(u"imagesSize")

        self.horizontalLayout_3.addWidget(self.imagesSize)


        self.verticalLayout_18.addWidget(self.widget_12)

        self.imagesImage = QWidget(self.imagesContainer)
        self.imagesImage.setObjectName(u"imagesImage")

        self.verticalLayout_18.addWidget(self.imagesImage)

        self.verticalLayout_18.setStretch(1, 1)
        self.tabImagesSplitter.addWidget(self.imagesContainer)

        self.verticalLayout_19.addWidget(self.tabImagesSplitter)

        self.tabWidget.addTab(self.tabImages, "")
        self.tabESPs = QWidget()
        self.tabESPs.setObjectName(u"tabESPs")
        self.verticalLayout_23 = QVBoxLayout(self.tabESPs)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.ESPsSplitter = QSplitter(self.tabESPs)
        self.ESPsSplitter.setObjectName(u"ESPsSplitter")
        self.ESPsSplitter.setOrientation(Qt.Horizontal)
        self.widget_9 = QWidget(self.ESPsSplitter)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_20 = QVBoxLayout(self.widget_9)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_9)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_20.addWidget(self.label_2)

        self.inactiveESPList = QListView(self.widget_9)
        self.inactiveESPList.setObjectName(u"inactiveESPList")
        self.inactiveESPList.setAlternatingRowColors(True)
        self.inactiveESPList.setUniformItemSizes(True)

        self.verticalLayout_20.addWidget(self.inactiveESPList)

        self.ESPsSplitter.addWidget(self.widget_9)
        self.widget_11 = QWidget(self.ESPsSplitter)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_2)

        self.activateESP = QToolButton(self.widget_11)
        self.activateESP.setObjectName(u"activateESP")
        icon = QIcon()
        icon.addFile(u":/MO/gui/next", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.activateESP.setIcon(icon)
        self.activateESP.setIconSize(QSize(22, 22))

        self.verticalLayout_22.addWidget(self.activateESP)

        self.deactivateESP = QToolButton(self.widget_11)
        self.deactivateESP.setObjectName(u"deactivateESP")
        icon1 = QIcon()
        icon1.addFile(u":/MO/gui/previous", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.deactivateESP.setIcon(icon1)
        self.deactivateESP.setIconSize(QSize(22, 22))

        self.verticalLayout_22.addWidget(self.deactivateESP)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_22)

        self.widget_10 = QWidget(self.widget_11)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_21 = QVBoxLayout(self.widget_10)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_10)
        self.label.setObjectName(u"label")

        self.verticalLayout_21.addWidget(self.label)

        self.activeESPList = QListView(self.widget_10)
        self.activeESPList.setObjectName(u"activeESPList")
        self.activeESPList.setAlternatingRowColors(True)
        self.activeESPList.setUniformItemSizes(True)

        self.verticalLayout_21.addWidget(self.activeESPList)


        self.horizontalLayout_2.addWidget(self.widget_10)

        self.ESPsSplitter.addWidget(self.widget_11)

        self.verticalLayout_23.addWidget(self.ESPsSplitter)

        self.tabWidget.addTab(self.tabESPs, "")
        self.tabConflicts = QWidget()
        self.tabConflicts.setObjectName(u"tabConflicts")
        self.verticalLayout_8 = QVBoxLayout(self.tabConflicts)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tabConflictsTabs = QTabWidget(self.tabConflicts)
        self.tabConflictsTabs.setObjectName(u"tabConflictsTabs")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_12 = QVBoxLayout(self.tab)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 100))
        self.verticalLayout_11 = QVBoxLayout(self.widget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.overwriteRoot = QVBoxLayout()
        self.overwriteRoot.setObjectName(u"overwriteRoot")
        self.overwriteHeader = QHBoxLayout()
        self.overwriteHeader.setObjectName(u"overwriteHeader")
        self.overwriteExpander = QToolButton(self.widget)
        self.overwriteExpander.setObjectName(u"overwriteExpander")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.overwriteExpander.sizePolicy().hasHeightForWidth())
        self.overwriteExpander.setSizePolicy(sizePolicy)
        self.overwriteExpander.setStyleSheet(u"border: none;\n"
"text-align: left;")

        self.overwriteHeader.addWidget(self.overwriteExpander)

        self.overwriteLineEdit = QLineEdit(self.widget)
        self.overwriteLineEdit.setObjectName(u"overwriteLineEdit")

        self.overwriteHeader.addWidget(self.overwriteLineEdit)

        self.overwriteCount = QLCDNumber(self.widget)
        self.overwriteCount.setObjectName(u"overwriteCount")
        self.overwriteCount.setFrameShadow(QFrame.Sunken)
        self.overwriteCount.setLineWidth(1)
        self.overwriteCount.setSegmentStyle(QLCDNumber.Flat)

        self.overwriteHeader.addWidget(self.overwriteCount)

        self.overwriteHeader.setStretch(0, 1)

        self.overwriteRoot.addLayout(self.overwriteHeader)


        self.verticalLayout_11.addLayout(self.overwriteRoot)

        self.overwriteTree = QTreeView(self.widget)
        self.overwriteTree.setObjectName(u"overwriteTree")
        self.overwriteTree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.overwriteTree.setAlternatingRowColors(True)
        self.overwriteTree.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.overwriteTree.setTextElideMode(Qt.ElideLeft)
        self.overwriteTree.setUniformRowHeights(True)
        self.overwriteTree.setSortingEnabled(True)

        self.verticalLayout_11.addWidget(self.overwriteTree)

        self.overwrittenRoot = QVBoxLayout()
        self.overwrittenRoot.setObjectName(u"overwrittenRoot")
        self.overwrittenHeader = QHBoxLayout()
        self.overwrittenHeader.setObjectName(u"overwrittenHeader")
        self.overwrittenExpander = QToolButton(self.widget)
        self.overwrittenExpander.setObjectName(u"overwrittenExpander")
        sizePolicy.setHeightForWidth(self.overwrittenExpander.sizePolicy().hasHeightForWidth())
        self.overwrittenExpander.setSizePolicy(sizePolicy)
        self.overwrittenExpander.setStyleSheet(u"border: none;\n"
"text-align: left;")

        self.overwrittenHeader.addWidget(self.overwrittenExpander)

        self.overwrittenLineEdit = QLineEdit(self.widget)
        self.overwrittenLineEdit.setObjectName(u"overwrittenLineEdit")

        self.overwrittenHeader.addWidget(self.overwrittenLineEdit)

        self.overwrittenCount = QLCDNumber(self.widget)
        self.overwrittenCount.setObjectName(u"overwrittenCount")
        self.overwrittenCount.setFrameShadow(QFrame.Sunken)
        self.overwrittenCount.setSegmentStyle(QLCDNumber.Flat)

        self.overwrittenHeader.addWidget(self.overwrittenCount)

        self.overwrittenHeader.setStretch(0, 1)

        self.overwrittenRoot.addLayout(self.overwrittenHeader)


        self.verticalLayout_11.addLayout(self.overwrittenRoot)

        self.overwrittenTree = QTreeView(self.widget)
        self.overwrittenTree.setObjectName(u"overwrittenTree")
        self.overwrittenTree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.overwrittenTree.setAlternatingRowColors(True)
        self.overwrittenTree.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.overwrittenTree.setTextElideMode(Qt.ElideLeft)
        self.overwrittenTree.setUniformRowHeights(True)
        self.overwrittenTree.setSortingEnabled(True)

        self.verticalLayout_11.addWidget(self.overwrittenTree)

        self.noConflictRoot = QVBoxLayout()
        self.noConflictRoot.setObjectName(u"noConflictRoot")
        self.noConflictHeader = QHBoxLayout()
        self.noConflictHeader.setObjectName(u"noConflictHeader")
        self.noConflictExpander = QToolButton(self.widget)
        self.noConflictExpander.setObjectName(u"noConflictExpander")
        sizePolicy.setHeightForWidth(self.noConflictExpander.sizePolicy().hasHeightForWidth())
        self.noConflictExpander.setSizePolicy(sizePolicy)
        self.noConflictExpander.setStyleSheet(u"border: none;\n"
"text-align: left;")

        self.noConflictHeader.addWidget(self.noConflictExpander)

        self.noConflictLineEdit = QLineEdit(self.widget)
        self.noConflictLineEdit.setObjectName(u"noConflictLineEdit")

        self.noConflictHeader.addWidget(self.noConflictLineEdit)

        self.noConflictCount = QLCDNumber(self.widget)
        self.noConflictCount.setObjectName(u"noConflictCount")
        self.noConflictCount.setFrameShadow(QFrame.Sunken)
        self.noConflictCount.setSegmentStyle(QLCDNumber.Flat)

        self.noConflictHeader.addWidget(self.noConflictCount)

        self.noConflictHeader.setStretch(0, 1)

        self.noConflictRoot.addLayout(self.noConflictHeader)


        self.verticalLayout_11.addLayout(self.noConflictRoot)

        self.noConflictTree = QTreeView(self.widget)
        self.noConflictTree.setObjectName(u"noConflictTree")
        self.noConflictTree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.noConflictTree.setAlternatingRowColors(True)
        self.noConflictTree.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.noConflictTree.setTextElideMode(Qt.ElideLeft)
        self.noConflictTree.setUniformRowHeights(True)
        self.noConflictTree.setSortingEnabled(True)

        self.verticalLayout_11.addWidget(self.noConflictTree)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer)

        self.verticalLayout_11.setStretch(1, 1)
        self.verticalLayout_11.setStretch(3, 1)
        self.verticalLayout_11.setStretch(5, 1)

        self.verticalLayout_12.addWidget(self.widget)

        self.tabConflictsTabs.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_13 = QVBoxLayout(self.tab_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.widget_2 = QWidget(self.tab_2)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_14 = QVBoxLayout(self.widget_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.conflictsAdvancedList = QTreeView(self.widget_3)
        self.conflictsAdvancedList.setObjectName(u"conflictsAdvancedList")
        self.conflictsAdvancedList.setContextMenuPolicy(Qt.CustomContextMenu)
        self.conflictsAdvancedList.setAlternatingRowColors(True)
        self.conflictsAdvancedList.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.conflictsAdvancedList.setUniformRowHeights(True)
        self.conflictsAdvancedList.setSortingEnabled(True)

        self.horizontalLayout_10.addWidget(self.conflictsAdvancedList)


        self.verticalLayout_14.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.conflictsAdvancedShowNoConflict = QCheckBox(self.widget_4)
        self.conflictsAdvancedShowNoConflict.setObjectName(u"conflictsAdvancedShowNoConflict")
        self.conflictsAdvancedShowNoConflict.setChecked(True)

        self.horizontalLayout_9.addWidget(self.conflictsAdvancedShowNoConflict)

        self.conflictsAdvancedShowAll = QRadioButton(self.widget_4)
        self.conflictsAdvancedShowAll.setObjectName(u"conflictsAdvancedShowAll")
        self.conflictsAdvancedShowAll.setChecked(True)

        self.horizontalLayout_9.addWidget(self.conflictsAdvancedShowAll)

        self.conflictsAdvancedShowNearest = QRadioButton(self.widget_4)
        self.conflictsAdvancedShowNearest.setObjectName(u"conflictsAdvancedShowNearest")

        self.horizontalLayout_9.addWidget(self.conflictsAdvancedShowNearest)

        self.widget_5 = QWidget(self.widget_4)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(20, 0, 0, 0)
        self.conflictsAdvancedFilter = QLineEdit(self.widget_5)
        self.conflictsAdvancedFilter.setObjectName(u"conflictsAdvancedFilter")

        self.horizontalLayout_8.addWidget(self.conflictsAdvancedFilter)


        self.horizontalLayout_9.addWidget(self.widget_5)


        self.verticalLayout_14.addWidget(self.widget_4)


        self.verticalLayout_13.addWidget(self.widget_2)

        self.tabConflictsTabs.addTab(self.tab_2, "")

        self.verticalLayout_8.addWidget(self.tabConflictsTabs)

        self.tabWidget.addTab(self.tabConflicts, "")
        self.tabCategories = QWidget()
        self.tabCategories.setObjectName(u"tabCategories")
        self.verticalLayout_7 = QVBoxLayout(self.tabCategories)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.categories = QTreeWidget(self.tabCategories)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.categories.setHeaderItem(__qtreewidgetitem)
        self.categories.setObjectName(u"categories")
        self.categories.setAlternatingRowColors(True)
        self.categories.setUniformRowHeights(True)
        self.categories.header().setVisible(False)

        self.verticalLayout_7.addWidget(self.categories)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_12 = QLabel(self.tabCategories)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_12.addWidget(self.label_12)

        self.primaryCategories = QComboBox(self.tabCategories)
        self.primaryCategories.setObjectName(u"primaryCategories")

        self.horizontalLayout_12.addWidget(self.primaryCategories)


        self.verticalLayout_7.addLayout(self.horizontalLayout_12)

        self.tabWidget.addTab(self.tabCategories, "")
        self.tabNexus = QWidget()
        self.tabNexus.setObjectName(u"tabNexus")
        self.verticalLayout_6 = QVBoxLayout(self.tabNexus)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_14 = QWidget(self.tabNexus)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_25 = QVBoxLayout(self.widget_14)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.widget_14)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.modID = QLineEdit(self.widget_14)
        self.modID.setObjectName(u"modID")

        self.horizontalLayout_6.addWidget(self.modID)

        self.label_10 = QLabel(self.widget_14)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_6.addWidget(self.label_10)

        self.sourceGame = QComboBox(self.widget_14)
        self.sourceGame.setObjectName(u"sourceGame")

        self.horizontalLayout_6.addWidget(self.sourceGame)

        self.versionLabel = QLabel(self.widget_14)
        self.versionLabel.setObjectName(u"versionLabel")

        self.horizontalLayout_6.addWidget(self.versionLabel)

        self.version = QLineEdit(self.widget_14)
        self.version.setObjectName(u"version")
        self.version.setMaxLength(32)

        self.horizontalLayout_6.addWidget(self.version)

        self.categoryLabel = QLabel(self.widget_14)
        self.categoryLabel.setObjectName(u"categoryLabel")

        self.horizontalLayout_6.addWidget(self.categoryLabel)

        self.category = QLineEdit(self.widget_14)
        self.category.setObjectName(u"category")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.category.sizePolicy().hasHeightForWidth())
        self.category.setSizePolicy(sizePolicy1)
        self.category.setBaseSize(QSize(0, 0))

        self.horizontalLayout_6.addWidget(self.category)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_6.setStretch(8, 1)

        self.verticalLayout_25.addLayout(self.horizontalLayout_6)

        self.widget_15 = QWidget(self.widget_14)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.refresh = QPushButton(self.widget_15)
        self.refresh.setObjectName(u"refresh")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.refresh.sizePolicy().hasHeightForWidth())
        self.refresh.setSizePolicy(sizePolicy2)
        icon2 = QIcon()
        icon2.addFile(u":/MO/gui/refresh", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.refresh.setIcon(icon2)

        self.horizontalLayout_7.addWidget(self.refresh)

        self.visitNexus = QPushButton(self.widget_15)
        self.visitNexus.setObjectName(u"visitNexus")
        icon3 = QIcon()
        icon3.addFile(u":/MO/gui/resources/internet-web-browser.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.visitNexus.setIcon(icon3)

        self.horizontalLayout_7.addWidget(self.visitNexus)

        self.endorse = QPushButton(self.widget_15)
        self.endorse.setObjectName(u"endorse")
        icon4 = QIcon()
        icon4.addFile(u":/MO/gui/icon_favorite", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.endorse.setIcon(icon4)

        self.horizontalLayout_7.addWidget(self.endorse)

        self.track = QPushButton(self.widget_15)
        self.track.setObjectName(u"track")
        icon5 = QIcon()
        icon5.addFile(u":/MO/gui/tracked", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.track.setIcon(icon5)
        self.track.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.track)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)


        self.verticalLayout_25.addWidget(self.widget_15)


        self.verticalLayout_6.addWidget(self.widget_14)

        self.frame = QFrame(self.tabNexus)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_24 = QVBoxLayout(self.frame)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.browser = QWebEngineView(self.frame)
        self.browser.setObjectName(u"browser")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.browser.sizePolicy().hasHeightForWidth())
        self.browser.setSizePolicy(sizePolicy3)
        self.browser.setMinimumSize(QSize(0, 200))
        self.browser.setProperty(u"url", QUrl(u"about:blank"))

        self.verticalLayout_24.addWidget(self.browser)


        self.verticalLayout_6.addWidget(self.frame)

        self.widget_13 = QWidget(self.tabNexus)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.hasCustomURL = QCheckBox(self.widget_13)
        self.hasCustomURL.setObjectName(u"hasCustomURL")

        self.horizontalLayout_5.addWidget(self.hasCustomURL)

        self.customURL = QLineEdit(self.widget_13)
        self.customURL.setObjectName(u"customURL")

        self.horizontalLayout_5.addWidget(self.customURL)

        self.visitCustomURL = QPushButton(self.widget_13)
        self.visitCustomURL.setObjectName(u"visitCustomURL")

        self.horizontalLayout_5.addWidget(self.visitCustomURL)


        self.verticalLayout_6.addWidget(self.widget_13)

        self.tabWidget.addTab(self.tabNexus, icon3, "")
        self.tabNotes = QWidget()
        self.tabNotes.setObjectName(u"tabNotes")
        self.verticalLayout_10 = QVBoxLayout(self.tabNotes)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.comments = QLineEdit(self.tabNotes)
        self.comments.setObjectName(u"comments")

        self.horizontalLayout_11.addWidget(self.comments)

        self.setColorButton = QPushButton(self.tabNotes)
        self.setColorButton.setObjectName(u"setColorButton")

        self.horizontalLayout_11.addWidget(self.setColorButton)

        self.resetColorButton = QPushButton(self.tabNotes)
        self.resetColorButton.setObjectName(u"resetColorButton")

        self.horizontalLayout_11.addWidget(self.resetColorButton)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        self.notes = QTextEdit(self.tabNotes)
        self.notes.setObjectName(u"notes")
        self.notes.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse|Qt.TextBrowserInteraction|Qt.TextEditable|Qt.TextEditorInteraction|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout_10.addWidget(self.notes)

        self.tabWidget.addTab(self.tabNotes, "")
        self.tabFiles = QWidget()
        self.tabFiles.setObjectName(u"tabFiles")
        self.verticalLayout_3 = QVBoxLayout(self.tabFiles)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.openInExplorer = QToolButton(self.tabFiles)
        self.openInExplorer.setObjectName(u"openInExplorer")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.openInExplorer.sizePolicy().hasHeightForWidth())
        self.openInExplorer.setSizePolicy(sizePolicy4)

        self.horizontalLayout_13.addWidget(self.openInExplorer)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)

        self.filetree = QTreeView(self.tabFiles)
        self.filetree.setObjectName(u"filetree")
        self.filetree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.filetree.setDragDropMode(QAbstractItemView.InternalMove)
        self.filetree.setDefaultDropAction(Qt.MoveAction)
        self.filetree.setAlternatingRowColors(True)
        self.filetree.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.filetree.setUniformRowHeights(True)
        self.filetree.setSortingEnabled(True)

        self.verticalLayout_3.addWidget(self.filetree)

        self.tabWidget.addTab(self.tabFiles, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.previousMod = QPushButton(ModInfoDialog)
        self.previousMod.setObjectName(u"previousMod")
        self.previousMod.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.previousMod)

        self.nextMod = QPushButton(ModInfoDialog)
        self.nextMod.setObjectName(u"nextMod")
        self.nextMod.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.nextMod)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.close = QPushButton(ModInfoDialog)
        self.close.setObjectName(u"close")
        self.close.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.close)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ModInfoDialog)

        self.tabWidget.setCurrentIndex(0)
        self.tabConflictsTabs.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ModInfoDialog)
    # setupUi

    def retranslateUi(self, ModInfoDialog):
        ModInfoDialog.setWindowTitle(QCoreApplication.translate("ModInfoDialog", u"Mod Info", None))
        self.label_5.setText(QCoreApplication.translate("ModInfoDialog", u"Text Files", None))
#if QT_CONFIG(tooltip)
        self.textFileList.setToolTip(QCoreApplication.translate("ModInfoDialog", u"A list of text-files in the mod directory.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.textFileList.setWhatsThis(QCoreApplication.translate("ModInfoDialog", u"A list of text-files in the mod directory like readmes. ", None))
#endif // QT_CONFIG(whatsthis)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabText), QCoreApplication.translate("ModInfoDialog", u"Text Files", None))
        self.label_6.setText(QCoreApplication.translate("ModInfoDialog", u"Ini Files", None))
#if QT_CONFIG(tooltip)
        self.iniFileList.setToolTip(QCoreApplication.translate("ModInfoDialog", u"This is a list of .ini files in the mod.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.iniFileList.setWhatsThis(QCoreApplication.translate("ModInfoDialog", u"This is a list of .ini files in the mod. These are usually used to configure the behaviour of mods if there are configurable parameters.", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.iniFileEditor.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.iniFileEditor.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabIni), QCoreApplication.translate("ModInfoDialog", u"INI Files", None))
        self.imagesShowDDS.setText(QCoreApplication.translate("ModInfoDialog", u"Show .dds files", None))
        self.previewPluginButton.setText(QCoreApplication.translate("ModInfoDialog", u"Open with Preview Plugin", None))
        self.imagesExplore.setText(QCoreApplication.translate("ModInfoDialog", u"Open in Explorer", None))
        self.imagesSize.setText(QCoreApplication.translate("ModInfoDialog", u"0x0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabImages), QCoreApplication.translate("ModInfoDialog", u"Images", None))
        self.label_2.setText(QCoreApplication.translate("ModInfoDialog", u"Optional ESPs", None))
#if QT_CONFIG(tooltip)
        self.inactiveESPList.setToolTip(QCoreApplication.translate("ModInfoDialog", u"List of esps, esms, and esls that can not be loaded by the game.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.inactiveESPList.setWhatsThis(QCoreApplication.translate("ModInfoDialog", u"List of esps, esms, and esls contained in this plugin that currently can not be loaded by the game. They will not even appear in the esp-list in the main MO-window.\n"
"They usually contain optional functionality, see the readme.\n"
"\n"
"Most mods do not have optional esps, so chances are good you are looking at an empty list.", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.activateESP.setToolTip(QCoreApplication.translate("ModInfoDialog", u"Move a file to the data directory.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.activateESP.setWhatsThis(QCoreApplication.translate("ModInfoDialog", u"This moves a esp to the esp directory so it can be enabled in the main window. Please note that the ESP merely becomes \"available\", it will not necessarily be loaded! That is configured in the main window of MO.", None))
#endif // QT_CONFIG(whatsthis)
        self.activateESP.setText("")
#if QT_CONFIG(tooltip)
        self.deactivateESP.setToolTip(QCoreApplication.translate("ModInfoDialog", u"Make the selected mod in the right list unavailable.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.deactivateESP.setWhatsThis(QCoreApplication.translate("ModInfoDialog", u"The selected esp (in the right list) will be pushed into a subdirectory of the mod and will thus become \"invisible\" to the game. It can then no longer be activated.", None))
#endif // QT_CONFIG(whatsthis)
        self.deactivateESP.setText("")
        self.label.setText(QCoreApplication.translate("ModInfoDialog", u"Available ESPs", None))
#if QT_CONFIG(tooltip)
        self.activeESPList.setToolTip(QCoreApplication.translate("ModInfoDialog", u"ESPs in the data directory and thus visible to the game.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.activeESPList.setWhatsThis(QCoreApplication.translate("ModInfoDialog", u"<html><head/><body><p>These are the mod files that are in the (virtual) data directory of your game and will thus be selectable in the esp list in the main window.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabESPs), QCoreApplication.translate("ModInfoDialog", u"Optional ESPs", None))
#if QT_CONFIG(tooltip)
        self.overwriteExpander.setToolTip(QCoreApplication.translate("ModInfoDialog", u"Files that exist in other mods but are overwritten by this mod", None))
#endif // QT_CONFIG(tooltip)
        self.overwriteExpander.setText(QCoreApplication.translate("ModInfoDialog", u"Winning file conflicts:", None))
#if QT_CONFIG(tooltip)
        self.overwriteTree.setToolTip(QCoreApplication.translate("ModInfoDialog", u"Files that exist in other mods but are overwritten by this mod", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.overwrittenExpander.setToolTip(QCoreApplication.translate("ModInfoDialog", u"Files that are unused because they are overwritten by other mods", None))
#endif // QT_CONFIG(tooltip)
        self.overwrittenExpander.setText(QCoreApplication.translate("ModInfoDialog", u"Losing file conflicts:", None))
#if QT_CONFIG(tooltip)
        self.overwrittenTree.setToolTip(QCoreApplication.translate("ModInfoDialog", u"Files that are unused because they are overwritten by other mods", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.noConflictExpander.setToolTip(QCoreApplication.translate("ModInfoDialog", u"Files that have no conflicts", None))
#endif // QT_CONFIG(tooltip)
        self.noConflictExpander.setText(QCoreApplication.translate("ModInfoDialog", u"The following files have no conflicts", None))
#if QT_CONFIG(tooltip)
        self.noConflictTree.setToolTip(QCoreApplication.translate("ModInfoDialog", u"Files that have no conflicts", None))
#endif // QT_CONFIG(tooltip)
        self.tabConflictsTabs.setTabText(self.tabConflictsTabs.indexOf(self.tab), QCoreApplication.translate("ModInfoDialog", u"General", None))
#if QT_CONFIG(tooltip)
        self.conflictsAdvancedShowNoConflict.setToolTip(QCoreApplication.translate("ModInfoDialog", u"Whether files that have no conflicts should be visible in the list", None))
#endif // QT_CONFIG(tooltip)
        self.conflictsAdvancedShowNoConflict.setText(QCoreApplication.translate("ModInfoDialog", u"Show files that have no conflicts", None))
#if QT_CONFIG(tooltip)
        self.conflictsAdvancedShowAll.setToolTip(QCoreApplication.translate("ModInfoDialog", u"Shows all mods overwriting or being overwritten by this mod", None))
#endif // QT_CONFIG(tooltip)
        self.conflictsAdvancedShowAll.setText(QCoreApplication.translate("ModInfoDialog", u"Show all conflicting mods", None))
#if QT_CONFIG(tooltip)
        self.conflictsAdvancedShowNearest.setToolTip(QCoreApplication.translate("ModInfoDialog", u"Shows only the nearest conflicting mods, in order of priority", None))
#endif // QT_CONFIG(tooltip)
        self.conflictsAdvancedShowNearest.setText(QCoreApplication.translate("ModInfoDialog", u"Show nearest conflicting mod", None))
        self.conflictsAdvancedFilter.setPlaceholderText(QCoreApplication.translate("ModInfoDialog", u"Filter", None))
        self.tabConflictsTabs.setTabText(self.tabConflictsTabs.indexOf(self.tab_2), QCoreApplication.translate("ModInfoDialog", u"Advanced", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabConflicts), QCoreApplication.translate("ModInfoDialog", u"Conflicts", None))
        self.label_12.setText(QCoreApplication.translate("ModInfoDialog", u"Primary Category", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCategories), QCoreApplication.translate("ModInfoDialog", u"Categories", None))
        self.label_3.setText(QCoreApplication.translate("ModInfoDialog", u"Mod ID", None))
#if QT_CONFIG(tooltip)
        self.modID.setToolTip(QCoreApplication.translate("ModInfoDialog", u"Mod ID for this mod on Nexus.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.modID.setWhatsThis(QCoreApplication.translate("ModInfoDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Mod ID for this mod on Nexus. This is filled in automatically if you downloaded and installed the mod from inside MO. Otherwise you can enter it manually. To find the correct id, find the mod on nexus. The URL will look like this: <a href=\" https://www.nexusmods.com/skyrimspecialedition/mods/6194\"><span style=\" text-decoration: underline; color:#0000ff;\">https://www.nexusmods.com/skyrimspecialedition/mods/6194</span></a>. In this example, 6194 is the id you're looking for. Besides: The above is the link to Mod Organizer 2 on Nexus. Why not go there now "
                        "and endorse us?</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_10.setText(QCoreApplication.translate("ModInfoDialog", u"Source Game", None))
#if QT_CONFIG(tooltip)
        self.sourceGame.setToolTip(QCoreApplication.translate("ModInfoDialog", u"Source game for this mod.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.sourceGame.setWhatsThis(QCoreApplication.translate("ModInfoDialog", u"<html><head/><body><p>Source game for this mod. This determines where the mod was downloaded from and decides where to fetch info, version updates, and send endorsements. Changing this will likely require you to enter a new Mod ID.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(whatsthis)
        self.versionLabel.setWhatsThis(QCoreApplication.translate("ModInfoDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Installed Version of the Mod. The tooltip will contain the current version available on nexus. The installed version is only set if you installed the mod through MO.</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.versionLabel.setText(QCoreApplication.translate("ModInfoDialog", u"Version", None))
        self.categoryLabel.setText(QCoreApplication.translate("ModInfoDialog", u"Category", None))
#if QT_CONFIG(tooltip)
        self.refresh.setToolTip(QCoreApplication.translate("ModInfoDialog", u"Refresh", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.refresh.setWhatsThis(QCoreApplication.translate("ModInfoDialog", u"Refresh all information from Nexus.", None))
#endif // QT_CONFIG(whatsthis)
        self.refresh.setText(QCoreApplication.translate("ModInfoDialog", u"Refresh", None))
        self.visitNexus.setText(QCoreApplication.translate("ModInfoDialog", u"Open in Browser", None))
        self.endorse.setText(QCoreApplication.translate("ModInfoDialog", u"Endorse", None))
        self.track.setText(QCoreApplication.translate("ModInfoDialog", u"Track", None))
        self.hasCustomURL.setText(QCoreApplication.translate("ModInfoDialog", u"Use Custom URL", None))
        self.visitCustomURL.setText(QCoreApplication.translate("ModInfoDialog", u"Open in Browser", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabNexus), QCoreApplication.translate("ModInfoDialog", u"Nexus Info", None))
#if QT_CONFIG(tooltip)
        self.comments.setToolTip(QCoreApplication.translate("ModInfoDialog", u"Enter comments about the mod here.  These are displayed in the notes column of the mod list.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.comments.setWhatsThis(QCoreApplication.translate("ModInfoDialog", u"Enter comments about the mod here.  These are displayed in the notes column of the mod list.", None))
#endif // QT_CONFIG(whatsthis)
        self.comments.setPlaceholderText(QCoreApplication.translate("ModInfoDialog", u"Enter comments about the mod here.  These are displayed in the notes column of the mod list.", None))
        self.setColorButton.setText(QCoreApplication.translate("ModInfoDialog", u"Set Color", None))
        self.resetColorButton.setText(QCoreApplication.translate("ModInfoDialog", u"Reset Color", None))
#if QT_CONFIG(tooltip)
        self.notes.setToolTip(QCoreApplication.translate("ModInfoDialog", u"Enter notes about the mod here.  These can be viewed in the mod list by hovering over the notes column or the flags column.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.notes.setWhatsThis(QCoreApplication.translate("ModInfoDialog", u"Enter notes about the mod here.  These can be viewed in the mod list by hovering over the notes column or the flags column.", None))
#endif // QT_CONFIG(whatsthis)
        self.notes.setPlaceholderText(QCoreApplication.translate("ModInfoDialog", u"Enter notes about the mod here.  These can be viewed in the mod list by hovering over the notes column or the flags column.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabNotes), QCoreApplication.translate("ModInfoDialog", u"Notes", None))
        self.openInExplorer.setText(QCoreApplication.translate("ModInfoDialog", u"Open Mod in Explorer", None))
#if QT_CONFIG(tooltip)
        self.filetree.setToolTip(QCoreApplication.translate("ModInfoDialog", u"A directory view of this mod", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.filetree.setWhatsThis(QCoreApplication.translate("ModInfoDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">This is a modifiable directory view of the mod directory. You can move around files using drag &amp; drop and rename them (double click).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Changes happen immediately on disc, so do</span><span style=\" font-size:8pt; font-weight:600;\"> be careful</span><span style=\" font-size:8pt;\">.</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFiles), QCoreApplication.translate("ModInfoDialog", u"Filetree", None))
        self.previousMod.setText(QCoreApplication.translate("ModInfoDialog", u"Previous", None))
        self.nextMod.setText(QCoreApplication.translate("ModInfoDialog", u"Next", None))
        self.close.setText(QCoreApplication.translate("ModInfoDialog", u"Close", None))
    # retranslateUi

