# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QAbstractItemView,
    QAbstractScrollArea,
    QApplication,
    QCheckBox,
    QComboBox,
    QDockWidget,
    QFrame,
    QGroupBox,
    QHBoxLayout,
    QHeaderView,
    QLCDNumber,
    QLabel,
    QLineEdit,
    QListView,
    QMainWindow,
    QMenu,
    QMenuBar,
    QPushButton,
    QRadioButton,
    QSizePolicy,
    QSpacerItem,
    QSplitter,
    QStatusBar,
    QTabWidget,
    QToolBar,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)

import ui.qt.resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1009, 710)
        MainWindow.setAcceptDrops(True)
        MainWindow.setWindowTitle("Mod Organizer")
        icon = QIcon()
        icon.addFile(
            "../../../modorganizer/src/mo_icon.ico", QSize(), QIcon.Normal, QIcon.Off
        )
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        self.actionInstallMod = QAction(MainWindow)
        self.actionInstallMod.setObjectName("actionInstallMod")
        icon1 = QIcon()
        icon1.addFile(
            ":/MO/gui/resources/system-installer.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.actionInstallMod.setIcon(icon1)
        self.actionAdd_Profile = QAction(MainWindow)
        self.actionAdd_Profile.setObjectName("actionAdd_Profile")
        icon2 = QIcon()
        icon2.addFile(":/MO/gui/profiles", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAdd_Profile.setIcon(icon2)
        self.actionModify_Executables = QAction(MainWindow)
        self.actionModify_Executables.setObjectName("actionModify_Executables")
        icon3 = QIcon()
        icon3.addFile(":/MO/gui/icon_executable", QSize(), QIcon.Normal, QIcon.Off)
        self.actionModify_Executables.setIcon(icon3)
        self.actionTool = QAction(MainWindow)
        self.actionTool.setObjectName("actionTool")
        icon4 = QIcon()
        icon4.addFile(":/MO/gui/plugins", QSize(), QIcon.Normal, QIcon.Off)
        self.actionTool.setIcon(icon4)
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        icon5 = QIcon()
        icon5.addFile(":/MO/gui/settings", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSettings.setIcon(icon5)
        self.actionNexus = QAction(MainWindow)
        self.actionNexus.setObjectName("actionNexus")
        icon6 = QIcon()
        icon6.addFile(
            ":/MO/gui/resources/internet-web-browser.png",
            QSize(),
            QIcon.Normal,
            QIcon.Off,
        )
        self.actionNexus.setIcon(icon6)
        self.actionModPage = QAction(MainWindow)
        self.actionModPage.setObjectName("actionModPage")
        self.actionModPage.setIcon(icon6)
        self.actionModPage.setVisible(False)
        self.actionUpdate = QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionUpdate.setEnabled(False)
        icon7 = QIcon()
        icon7.addFile(":/MO/gui/update", QSize(), QIcon.Normal, QIcon.Off)
        self.actionUpdate.setIcon(icon7)
        self.actionNotifications = QAction(MainWindow)
        self.actionNotifications.setObjectName("actionNotifications")
        icon8 = QIcon()
        icon8.addFile(":/MO/gui/warning", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNotifications.setIcon(icon8)
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        icon9 = QIcon()
        icon9.addFile(":/MO/gui/help", QSize(), QIcon.Normal, QIcon.Off)
        self.actionHelp.setIcon(icon9)
        self.actionEndorseMO = QAction(MainWindow)
        self.actionEndorseMO.setObjectName("actionEndorseMO")
        icon10 = QIcon()
        icon10.addFile(":/MO/gui/icon_favorite", QSize(), QIcon.Normal, QIcon.Off)
        self.actionEndorseMO.setIcon(icon10)
        self.actionChange_Game = QAction(MainWindow)
        self.actionChange_Game.setObjectName("actionChange_Game")
        icon11 = QIcon()
        icon11.addFile(":/MO/gui/instance_switch", QSize(), QIcon.Normal, QIcon.Off)
        self.actionChange_Game.setIcon(icon11)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionToolBarMainToggle = QAction(MainWindow)
        self.actionToolBarMainToggle.setObjectName("actionToolBarMainToggle")
        self.actionToolBarMainToggle.setCheckable(True)
        self.actionToolBarSmallIcons = QAction(MainWindow)
        self.actionToolBarSmallIcons.setObjectName("actionToolBarSmallIcons")
        self.actionToolBarSmallIcons.setCheckable(True)
        self.actionToolBarLargeIcons = QAction(MainWindow)
        self.actionToolBarLargeIcons.setObjectName("actionToolBarLargeIcons")
        self.actionToolBarLargeIcons.setCheckable(True)
        self.actionToolBarIconsOnly = QAction(MainWindow)
        self.actionToolBarIconsOnly.setObjectName("actionToolBarIconsOnly")
        self.actionToolBarIconsOnly.setCheckable(True)
        self.actionToolBarTextOnly = QAction(MainWindow)
        self.actionToolBarTextOnly.setObjectName("actionToolBarTextOnly")
        self.actionToolBarTextOnly.setCheckable(True)
        self.actionToolBarIconsAndText = QAction(MainWindow)
        self.actionToolBarIconsAndText.setObjectName("actionToolBarIconsAndText")
        self.actionToolBarIconsAndText.setCheckable(True)
        self.actionMainMenuToggle = QAction(MainWindow)
        self.actionMainMenuToggle.setObjectName("actionMainMenuToggle")
        self.actionMainMenuToggle.setCheckable(True)
        self.actionStatusBarToggle = QAction(MainWindow)
        self.actionStatusBarToggle.setObjectName("actionStatusBarToggle")
        self.actionStatusBarToggle.setCheckable(True)
        self.actionViewLog = QAction(MainWindow)
        self.actionViewLog.setObjectName("actionViewLog")
        self.actionViewLog.setCheckable(True)
        self.action_Refresh = QAction(MainWindow)
        self.action_Refresh.setObjectName("action_Refresh")
        icon12 = QIcon()
        icon12.addFile(
            ":/MO/gui/resources/view-refresh.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.action_Refresh.setIcon(icon12)
        self.actionToolBarMediumIcons = QAction(MainWindow)
        self.actionToolBarMediumIcons.setObjectName("actionToolBarMediumIcons")
        self.actionToolBarMediumIcons.setCheckable(True)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralWidget.sizePolicy().hasHeightForWidth()
        )
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.verticalLayout_8 = QVBoxLayout(self.centralWidget)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.categoriesSplitter = QSplitter(self.centralWidget)
        self.categoriesSplitter.setObjectName("categoriesSplitter")
        self.categoriesSplitter.setOrientation(Qt.Horizontal)
        self.categoriesSplitter.setChildrenCollapsible(False)
        self.categoriesGroup = QGroupBox(self.categoriesSplitter)
        self.categoriesGroup.setObjectName("categoriesGroup")
        self.categoriesGroup.setMaximumSize(QSize(500, 16777215))
        self.verticalLayout_10 = QVBoxLayout(self.categoriesGroup)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(3, 15, 3, 0)
        self.filters = QTreeWidget(self.categoriesGroup)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, "1")
        self.filters.setHeaderItem(__qtreewidgetitem)
        self.filters.setObjectName("filters")
        self.filters.setMinimumSize(QSize(120, 0))
        self.filters.setContextMenuPolicy(Qt.NoContextMenu)
        self.filters.setAlternatingRowColors(True)
        self.filters.setSelectionMode(QAbstractItemView.NoSelection)

        self.verticalLayout_10.addWidget(self.filters)

        self.widget_2 = QWidget(self.categoriesGroup)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 2, 0, 0)
        self.filtersClear = QPushButton(self.widget_2)
        self.filtersClear.setObjectName("filtersClear")

        self.horizontalLayout_8.addWidget(self.filtersClear)

        self.filtersEdit = QPushButton(self.widget_2)
        self.filtersEdit.setObjectName("filtersEdit")

        self.horizontalLayout_8.addWidget(self.filtersEdit)

        self.verticalLayout_10.addWidget(self.widget_2)

        self.widget = QWidget(self.categoriesGroup)
        self.widget.setObjectName("widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.horizontalLayout_11 = QHBoxLayout(self.widget)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(1, 2, 1, 2)
        self.filtersAnd = QRadioButton(self.widget)
        self.filtersAnd.setObjectName("filtersAnd")
        self.filtersAnd.setChecked(True)

        self.horizontalLayout_11.addWidget(self.filtersAnd)

        self.filtersOr = QRadioButton(self.widget)
        self.filtersOr.setObjectName("filtersOr")

        self.horizontalLayout_11.addWidget(self.filtersOr)

        self.filtersSeparators = QComboBox(self.widget)
        self.filtersSeparators.setObjectName("filtersSeparators")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.filtersSeparators.sizePolicy().hasHeightForWidth()
        )
        self.filtersSeparators.setSizePolicy(sizePolicy1)

        self.horizontalLayout_11.addWidget(self.filtersSeparators)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 1)
        self.horizontalLayout_11.setStretch(2, 2)

        self.verticalLayout_10.addWidget(self.widget)

        self.categoriesSplitter.addWidget(self.categoriesGroup)
        self.splitter = QSplitter(self.categoriesSplitter)
        self.splitter.setObjectName("splitter")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy2)
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred
        )
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.profileBox = QComboBox(self.layoutWidget)
        self.profileBox.setObjectName("profileBox")

        self.horizontalLayout_6.addWidget(self.profileBox)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.listOptionsBtn = QPushButton(self.layoutWidget)
        self.listOptionsBtn.setObjectName("listOptionsBtn")
        self.listOptionsBtn.setMaximumSize(QSize(16777215, 16777215))
        self.listOptionsBtn.setIcon(icon5)
        self.listOptionsBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_6.addWidget(self.listOptionsBtn)

        self.openFolderMenu = QPushButton(self.layoutWidget)
        self.openFolderMenu.setObjectName("openFolderMenu")
        icon13 = QIcon()
        icon13.addFile(":/MO/gui/open_folder", QSize(), QIcon.Normal, QIcon.Off)
        self.openFolderMenu.setIcon(icon13)

        self.horizontalLayout_6.addWidget(self.openFolderMenu)

        self.restoreModsButton = QPushButton(self.layoutWidget)
        self.restoreModsButton.setObjectName("restoreModsButton")
        self.restoreModsButton.setText("")
        icon14 = QIcon()
        icon14.addFile(":/MO/gui/restore", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreModsButton.setIcon(icon14)

        self.horizontalLayout_6.addWidget(self.restoreModsButton)

        self.saveModsButton = QPushButton(self.layoutWidget)
        self.saveModsButton.setObjectName("saveModsButton")
        self.saveModsButton.setText("")
        icon15 = QIcon()
        icon15.addFile(":/MO/gui/backup", QSize(), QIcon.Normal, QIcon.Off)
        self.saveModsButton.setIcon(icon15)

        self.horizontalLayout_6.addWidget(self.saveModsButton)

        self.activeModslabel = QLabel(self.layoutWidget)
        self.activeModslabel.setObjectName("activeModslabel")

        self.horizontalLayout_6.addWidget(self.activeModslabel)

        self.activeModsCounter = QLCDNumber(self.layoutWidget)
        self.activeModsCounter.setObjectName("activeModsCounter")
        self.activeModsCounter.setMinimumSize(QSize(0, 26))
        self.activeModsCounter.setFrameShadow(QFrame.Sunken)
        self.activeModsCounter.setDigitCount(5)
        self.activeModsCounter.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout_6.addWidget(self.activeModsCounter)

        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.modList = QTreeWidget(self.layoutWidget)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, "1")
        self.modList.setHeaderItem(__qtreewidgetitem1)
        self.modList.setObjectName("modList")
        self.modList.setMinimumSize(QSize(330, 400))
        self.modList.setContextMenuPolicy(Qt.CustomContextMenu)
        self.modList.setStyleSheet("")
        self.modList.setEditTriggers(
            QAbstractItemView.EditKeyPressed | QAbstractItemView.SelectedClicked
        )
        self.modList.setProperty("showDropIndicator", True)
        self.modList.setDragEnabled(True)
        self.modList.setDragDropMode(QAbstractItemView.DragDrop)
        self.modList.setDefaultDropAction(Qt.MoveAction)
        self.modList.setAlternatingRowColors(True)
        self.modList.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.modList.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout.addWidget(self.modList)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.displayCategoriesBtn = QPushButton(self.layoutWidget)
        self.displayCategoriesBtn.setObjectName("displayCategoriesBtn")
        self.displayCategoriesBtn.setMaximumSize(QSize(20, 16777215))
        self.displayCategoriesBtn.setText("x")
        self.displayCategoriesBtn.setIconSize(QSize(20, 20))
        self.displayCategoriesBtn.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.displayCategoriesBtn)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        sizePolicy4 = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred
        )
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)

        self.horizontalLayout_4.addWidget(self.label_2)

        self.currentCategoryLabel = QLabel(self.layoutWidget)
        self.currentCategoryLabel.setObjectName("currentCategoryLabel")

        self.horizontalLayout_4.addWidget(self.currentCategoryLabel)

        self.horizontalSpacer_5 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.clearFiltersButton = QPushButton(self.layoutWidget)
        self.clearFiltersButton.setObjectName("clearFiltersButton")
        sizePolicy5 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum
        )
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(
            self.clearFiltersButton.sizePolicy().hasHeightForWidth()
        )
        self.clearFiltersButton.setSizePolicy(sizePolicy5)
        self.clearFiltersButton.setMinimumSize(QSize(0, 22))
        self.clearFiltersButton.setBaseSize(QSize(95, 0))
        self.clearFiltersButton.setVisible(False)
        self.clearFiltersButton.setLayoutDirection(Qt.RightToLeft)
        self.clearFiltersButton.setStyleSheet("border:1px solid #ff0000;")
        icon16 = QIcon()
        icon16.addFile(":/MO/gui/edit_clear", QSize(), QIcon.Normal, QIcon.Off)
        self.clearFiltersButton.setIcon(icon16)
        self.clearFiltersButton.setIconSize(QSize(12, 12))

        self.horizontalLayout_4.addWidget(self.clearFiltersButton, 0, Qt.AlignLeft)

        self.groupCombo = QComboBox(self.layoutWidget)
        self.groupCombo.addItem("")
        self.groupCombo.addItem("")
        self.groupCombo.addItem("")
        self.groupCombo.setObjectName("groupCombo")
        self.groupCombo.setBaseSize(QSize(220, 0))
        self.groupCombo.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_4.addWidget(self.groupCombo)

        self.modFilterEdit = QLineEdit(self.layoutWidget)
        self.modFilterEdit.setObjectName("modFilterEdit")
        self.modFilterEdit.setBaseSize(QSize(220, 0))

        self.horizontalLayout_4.addWidget(self.modFilterEdit)

        self.horizontalLayout_4.setStretch(2, 1)
        self.horizontalLayout_4.setStretch(3, 1)
        self.horizontalLayout_4.setStretch(5, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.splitter.addWidget(self.layoutWidget)
        self.layoutWidget_2 = QWidget(self.splitter)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.startGroup = QFrame(self.layoutWidget_2)
        self.startGroup.setObjectName("startGroup")
        self.horizontalLayout_5 = QHBoxLayout(self.startGroup)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 4)
        self.executablesListBox = QComboBox(self.startGroup)
        self.executablesListBox.setObjectName("executablesListBox")
        sizePolicy1.setHeightForWidth(
            self.executablesListBox.sizePolicy().hasHeightForWidth()
        )
        self.executablesListBox.setSizePolicy(sizePolicy1)
        self.executablesListBox.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        self.executablesListBox.setFont(font)
        self.executablesListBox.setIconSize(QSize(32, 32))
        self.executablesListBox.setFrame(False)

        self.horizontalLayout_5.addWidget(self.executablesListBox)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.startButton = QPushButton(self.startGroup)
        self.startButton.setObjectName("startButton")
        sizePolicy6 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy6)
        self.startButton.setMinimumSize(QSize(120, 0))
        self.startButton.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.startButton.setFont(font1)
        self.startButton.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon17 = QIcon()
        icon17.addFile(":/MO/gui/run", QSize(), QIcon.Normal, QIcon.Off)
        self.startButton.setIcon(icon17)
        self.startButton.setIconSize(QSize(36, 36))

        self.verticalLayout_12.addWidget(self.startButton)

        self.linkButton = QPushButton(self.startGroup)
        self.linkButton.setObjectName("linkButton")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.linkButton.sizePolicy().hasHeightForWidth())
        self.linkButton.setSizePolicy(sizePolicy7)
        self.linkButton.setMinimumSize(QSize(140, 0))
        self.linkButton.setMaximumSize(QSize(16777215, 16777215))
        self.linkButton.setBaseSize(QSize(0, 0))
        icon18 = QIcon()
        icon18.addFile(":/MO/gui/link", QSize(), QIcon.Normal, QIcon.Off)
        self.linkButton.setIcon(icon18)

        self.verticalLayout_12.addWidget(self.linkButton)

        self.horizontalLayout_5.addLayout(self.verticalLayout_12)

        self.horizontalLayout_5.setStretch(0, 1)

        self.verticalLayout_2.addWidget(self.startGroup)

        self.tabWidget = QTabWidget(self.layoutWidget_2)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setMinimumSize(QSize(340, 250))
        self.tabWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget.setContextMenuPolicy(Qt.NoContextMenu)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.espTab = QWidget()
        self.espTab.setObjectName("espTab")
        sizePolicy2.setHeightForWidth(self.espTab.sizePolicy().hasHeightForWidth())
        self.espTab.setSizePolicy(sizePolicy2)
        self.espTab.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.espTab)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 6, -1, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.sortButton = QPushButton(self.espTab)
        self.sortButton.setObjectName("sortButton")
        icon19 = QIcon()
        icon19.addFile(":/MO/gui/sort", QSize(), QIcon.Normal, QIcon.Off)
        self.sortButton.setIcon(icon19)

        self.horizontalLayout_7.addWidget(self.sortButton)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.restoreButton = QPushButton(self.espTab)
        self.restoreButton.setObjectName("restoreButton")
        self.restoreButton.setText("")
        self.restoreButton.setIcon(icon14)
        self.restoreButton.setIconSize(QSize(16, 16))

        self.horizontalLayout_7.addWidget(self.restoreButton)

        self.saveButton = QPushButton(self.espTab)
        self.saveButton.setObjectName("saveButton")
        self.saveButton.setText("")
        self.saveButton.setIcon(icon15)

        self.horizontalLayout_7.addWidget(self.saveButton)

        self.activePluginsLabel = QLabel(self.espTab)
        self.activePluginsLabel.setObjectName("activePluginsLabel")

        self.horizontalLayout_7.addWidget(self.activePluginsLabel)

        self.activePluginsCounter = QLCDNumber(self.espTab)
        self.activePluginsCounter.setObjectName("activePluginsCounter")
        self.activePluginsCounter.setMinimumSize(QSize(0, 26))
        self.activePluginsCounter.setFrameShadow(QFrame.Sunken)
        self.activePluginsCounter.setDigitCount(4)
        self.activePluginsCounter.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout_7.addWidget(self.activePluginsCounter)

        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.espList = QTreeWidget(self.espTab)
        __qtreewidgetitem2 = QTreeWidgetItem()
        __qtreewidgetitem2.setText(0, "1")
        self.espList.setHeaderItem(__qtreewidgetitem2)
        self.espList.setObjectName("espList")
        self.espList.setMinimumSize(QSize(250, 250))
        self.espList.setContextMenuPolicy(Qt.CustomContextMenu)
        self.espList.setEditTriggers(
            QAbstractItemView.EditKeyPressed | QAbstractItemView.SelectedClicked
        )
        self.espList.setDragEnabled(True)
        self.espList.setDragDropOverwriteMode(False)
        self.espList.setDragDropMode(QAbstractItemView.InternalMove)
        self.espList.setDefaultDropAction(Qt.MoveAction)
        self.espList.setAlternatingRowColors(True)
        self.espList.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.espList.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_4.addWidget(self.espList)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)

        self.espFilterEdit = QLineEdit(self.espTab)
        self.espFilterEdit.setObjectName("espFilterEdit")

        self.horizontalLayout_10.addWidget(self.espFilterEdit)

        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.tabWidget.addTab(self.espTab, "")
        self.bsaTab = QWidget()
        self.bsaTab.setObjectName("bsaTab")
        self.bsaTab.setVisible(False)
        self.verticalLayout_9 = QVBoxLayout(self.bsaTab)
        self.verticalLayout_9.setSpacing(2)
        self.verticalLayout_9.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 6, -1, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(6)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.managedArchiveLabel = QLabel(self.bsaTab)
        self.managedArchiveLabel.setObjectName("managedArchiveLabel")
        self.managedArchiveLabel.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.managedArchiveLabel)

        self.bsaList = QTreeWidget(self.bsaTab)
        __qtreewidgetitem3 = QTreeWidgetItem()
        __qtreewidgetitem3.setText(0, "1")
        self.bsaList.setHeaderItem(__qtreewidgetitem3)
        self.bsaList.setObjectName("bsaList")

        self.verticalLayout_13.addWidget(self.bsaList)

        self.horizontalLayout_9.addLayout(self.verticalLayout_13)

        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.tabWidget.addTab(self.bsaTab, "")
        self.dataTab = QWidget()
        self.dataTab.setObjectName("dataTab")
        self.verticalLayout_5 = QVBoxLayout(self.dataTab)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 6, -1, 0)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.dataTabRefresh = QPushButton(self.dataTab)
        self.dataTabRefresh.setObjectName("dataTabRefresh")
        self.dataTabRefresh.setIcon(icon12)

        self.horizontalLayout_12.addWidget(self.dataTabRefresh)

        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_12.addItem(self.horizontalSpacer_4)

        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dataTree = QTreeWidget(self.dataTab)
        __qtreewidgetitem4 = QTreeWidgetItem()
        __qtreewidgetitem4.setText(0, "1")
        self.dataTree.setHeaderItem(__qtreewidgetitem4)
        self.dataTree.setObjectName("dataTree")
        self.dataTree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.dataTree.setAlternatingRowColors(True)
        self.dataTree.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.dataTree.setUniformRowHeights(True)
        self.dataTree.setSortingEnabled(True)

        self.horizontalLayout_2.addWidget(self.dataTree)

        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.dataTabShowOnlyConflicts = QCheckBox(self.dataTab)
        self.dataTabShowOnlyConflicts.setObjectName("dataTabShowOnlyConflicts")

        self.horizontalLayout_13.addWidget(self.dataTabShowOnlyConflicts)

        self.dataTabShowFromArchives = QCheckBox(self.dataTab)
        self.dataTabShowFromArchives.setObjectName("dataTabShowFromArchives")

        self.horizontalLayout_13.addWidget(self.dataTabShowFromArchives)

        self.dataTabFilter = QLineEdit(self.dataTab)
        self.dataTabFilter.setObjectName("dataTabFilter")

        self.horizontalLayout_13.addWidget(self.dataTabFilter)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 1)
        self.horizontalLayout_13.setStretch(2, 2)

        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.tabWidget.addTab(self.dataTab, "")
        self.savesTab = QWidget()
        self.savesTab.setObjectName("savesTab")
        self.verticalLayout_3 = QVBoxLayout(self.savesTab)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 6, -1, 0)
        self.savegameList = QTreeWidget(self.savesTab)
        __qtreewidgetitem5 = QTreeWidgetItem()
        __qtreewidgetitem5.setText(0, "1")
        self.savegameList.setHeaderItem(__qtreewidgetitem5)
        self.savegameList.setObjectName("savegameList")
        self.savegameList.setContextMenuPolicy(Qt.CustomContextMenu)
        # if QT_CONFIG(tooltip)
        self.savegameList.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.savegameList.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.savegameList.setAlternatingRowColors(True)
        self.savegameList.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.savegameList.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_3.addWidget(self.savegameList)

        self.tabWidget.addTab(self.savesTab, "")
        self.downloadTab = QWidget()
        self.downloadTab.setObjectName("downloadTab")
        self.verticalLayout_7 = QVBoxLayout(self.downloadTab)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 6, -1, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnRefreshDownloads = QPushButton(self.downloadTab)
        self.btnRefreshDownloads.setObjectName("btnRefreshDownloads")
        self.btnRefreshDownloads.setIcon(icon12)

        self.horizontalLayout.addWidget(self.btnRefreshDownloads)

        self.horizontalSpacer_7 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_7)

        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.downloadLayout = QVBoxLayout()
        self.downloadLayout.setSpacing(6)
        self.downloadLayout.setObjectName("downloadLayout")
        self.downloadView = QTreeWidget(self.downloadTab)
        __qtreewidgetitem6 = QTreeWidgetItem()
        __qtreewidgetitem6.setText(0, "1")
        self.downloadView.setHeaderItem(__qtreewidgetitem6)
        self.downloadView.setObjectName("downloadView")
        self.downloadView.setMinimumSize(QSize(320, 0))
        self.downloadView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.downloadView.setAcceptDrops(True)
        self.downloadView.setDragEnabled(True)
        self.downloadView.setDragDropMode(QAbstractItemView.DragDrop)
        self.downloadView.setDefaultDropAction(Qt.MoveAction)
        self.downloadView.setAlternatingRowColors(True)
        self.downloadView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.downloadLayout.addWidget(self.downloadView)

        self.verticalLayout_7.addLayout(self.downloadLayout)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(6)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.showHiddenBox = QCheckBox(self.downloadTab)
        self.showHiddenBox.setObjectName("showHiddenBox")

        self.horizontalLayout_16.addWidget(self.showHiddenBox)

        self.horizontalSpacer_6 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_16.addItem(self.horizontalSpacer_6)

        self.downloadFilterEdit = QLineEdit(self.downloadTab)
        self.downloadFilterEdit.setObjectName("downloadFilterEdit")

        self.horizontalLayout_16.addWidget(self.downloadFilterEdit)

        self.horizontalLayout_16.setStretch(0, 1)
        self.horizontalLayout_16.setStretch(1, 1)
        self.horizontalLayout_16.setStretch(2, 2)

        self.verticalLayout_7.addLayout(self.horizontalLayout_16)

        self.tabWidget.addTab(self.downloadTab, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.splitter.addWidget(self.layoutWidget_2)
        self.categoriesSplitter.addWidget(self.splitter)

        self.verticalLayout_8.addWidget(self.categoriesSplitter)

        MainWindow.setCentralWidget(self.centralWidget)
        self.logDock = QDockWidget(MainWindow)
        self.logDock.setObjectName("logDock")
        self.logDock.setMinimumSize(QSize(82, 44))
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_6 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.logList = QListView(self.dockWidgetContents)
        self.logList.setObjectName("logList")
        sizePolicy.setHeightForWidth(self.logList.sizePolicy().hasHeightForWidth())
        self.logList.setSizePolicy(sizePolicy)
        self.logList.setMinimumSize(QSize(30, 20))
        self.logList.setContextMenuPolicy(Qt.CustomContextMenu)
        self.logList.setAlternatingRowColors(True)
        self.logList.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_6.addWidget(self.logList)

        self.logDock.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.logDock)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName("menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1009, 19))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QMenu(self.menuBar)
        self.menuTools.setObjectName("menuTools")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuView = QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuToolbars = QMenu(self.menuView)
        self.menuToolbars.setObjectName("menuToolbars")
        self.menuRun = QMenu(self.menuBar)
        self.menuRun.setObjectName("menuRun")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        self.toolBar.setContextMenuPolicy(Qt.CustomContextMenu)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QSize(42, 36))
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        # if QT_CONFIG(shortcut)
        self.label_3.setBuddy(self.profileBox)
        # endif // QT_CONFIG(shortcut)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        self.menuBar.addAction(self.menuRun.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionChange_Game)
        self.menuFile.addAction(self.actionInstallMod)
        self.menuFile.addAction(self.actionNexus)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuTools.addAction(self.actionAdd_Profile)
        self.menuTools.addAction(self.actionModify_Executables)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionTool)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.actionSettings)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionUpdate)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionEndorseMO)
        self.menuView.addAction(self.action_Refresh)
        self.menuView.addAction(self.menuToolbars.menuAction())
        self.menuView.addAction(self.actionViewLog)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionNotifications)
        self.menuToolbars.addAction(self.actionMainMenuToggle)
        self.menuToolbars.addAction(self.actionToolBarMainToggle)
        self.menuToolbars.addAction(self.actionStatusBarToggle)
        self.menuToolbars.addSeparator()
        self.menuToolbars.addAction(self.actionToolBarSmallIcons)
        self.menuToolbars.addAction(self.actionToolBarMediumIcons)
        self.menuToolbars.addAction(self.actionToolBarLargeIcons)
        self.menuToolbars.addSeparator()
        self.menuToolbars.addAction(self.actionToolBarIconsOnly)
        self.menuToolbars.addAction(self.actionToolBarTextOnly)
        self.menuToolbars.addAction(self.actionToolBarIconsAndText)
        self.toolBar.addAction(self.actionChange_Game)
        self.toolBar.addAction(self.actionInstallMod)
        self.toolBar.addAction(self.actionNexus)
        self.toolBar.addAction(self.actionModPage)
        self.toolBar.addAction(self.actionAdd_Profile)
        self.toolBar.addAction(self.action_Refresh)
        self.toolBar.addAction(self.actionModify_Executables)
        self.toolBar.addAction(self.actionTool)
        self.toolBar.addAction(self.actionSettings)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionEndorseMO)
        self.toolBar.addAction(self.actionNotifications)
        self.toolBar.addAction(self.actionUpdate)
        self.toolBar.addAction(self.actionHelp)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        self.actionInstallMod.setText(
            QCoreApplication.translate("MainWindow", "Install &Mod...", None)
        )
        self.actionInstallMod.setIconText(
            QCoreApplication.translate("MainWindow", "Install &Mod", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionInstallMod.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "Install a new mod from an archive", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionInstallMod.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", "Install a new mod from an archive", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionInstallMod.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+M", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionAdd_Profile.setText(
            QCoreApplication.translate("MainWindow", "&Profiles...", None)
        )
        self.actionAdd_Profile.setIconText(
            QCoreApplication.translate("MainWindow", "&Profiles", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionAdd_Profile.setToolTip(
            QCoreApplication.translate("MainWindow", "Configure profiles", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionAdd_Profile.setStatusTip(
            QCoreApplication.translate("MainWindow", "Configure profiles", None)
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionAdd_Profile.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+P", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionModify_Executables.setText(
            QCoreApplication.translate("MainWindow", "&Executables...", None)
        )
        self.actionModify_Executables.setIconText(
            QCoreApplication.translate("MainWindow", "&Executables", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionModify_Executables.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "Configure the executables that can be started through Mod Organizer",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionModify_Executables.setStatusTip(
            QCoreApplication.translate(
                "MainWindow",
                "Configure the executables that can be started through Mod Organizer",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionModify_Executables.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+E", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionTool.setText(
            QCoreApplication.translate("MainWindow", "&Tool Plugins", None)
        )
        self.actionTool.setIconText(
            QCoreApplication.translate("MainWindow", "&Tools", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionTool.setToolTip(
            QCoreApplication.translate("MainWindow", "Tools", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(shortcut)
        self.actionTool.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+I", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionSettings.setText(
            QCoreApplication.translate("MainWindow", "&Settings...", None)
        )
        self.actionSettings.setIconText(
            QCoreApplication.translate("MainWindow", "&Settings", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionSettings.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "Configure settings and workarounds", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionSettings.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", "Configure settings and workarounds", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionSettings.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+S", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionNexus.setText(
            QCoreApplication.translate("MainWindow", "Visit &Nexus", None)
        )
        self.actionNexus.setIconText(
            QCoreApplication.translate("MainWindow", "Visit &Nexus", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionNexus.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "Visit the Nexus website in your browser for more mods",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionNexus.setStatusTip(
            QCoreApplication.translate(
                "MainWindow",
                "Visit the Nexus website in your browser for more mods",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionNexus.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+N", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionModPage.setText(
            QCoreApplication.translate("MainWindow", "Browse Mod Page", None)
        )
        self.actionModPage.setIconText(
            QCoreApplication.translate("MainWindow", "Browse Mod Page", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionModPage.setToolTip(
            QCoreApplication.translate("MainWindow", "Browse Mod Page", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionModPage.setStatusTip(
            QCoreApplication.translate("MainWindow", "Browse Mod Page", None)
        )
        # endif // QT_CONFIG(statustip)
        self.actionUpdate.setText(
            QCoreApplication.translate("MainWindow", "&Update Mod Organizer", None)
        )
        self.actionUpdate.setIconText(
            QCoreApplication.translate("MainWindow", "&Update Mod Organizer", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionUpdate.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "Mod Organizer is up-to-date", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionUpdate.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", "Mod Organizer is up-to-date", None
            )
        )
        # endif // QT_CONFIG(statustip)
        self.actionNotifications.setText(
            QCoreApplication.translate("MainWindow", "&Notifications...", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionNotifications.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "Open the notifications dialog", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionNotifications.setStatusTip(
            QCoreApplication.translate(
                "MainWindow", "Open the notifications dialog", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.actionNotifications.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "This button will be highlighted on the toolbar if MO discovered potential problems in your setup and provide tips on how to fix them.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", "&Help", None))
        self.actionHelp.setIconText(
            QCoreApplication.translate("MainWindow", "&Help", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionHelp.setToolTip(
            QCoreApplication.translate("MainWindow", "Show help options", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionHelp.setStatusTip(
            QCoreApplication.translate("MainWindow", "Show help options", None)
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(shortcut)
        self.actionHelp.setShortcut(
            QCoreApplication.translate("MainWindow", "Ctrl+H", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionEndorseMO.setText(
            QCoreApplication.translate("MainWindow", "&Endorse ModOrganizer", None)
        )
        self.actionEndorseMO.setIconText(
            QCoreApplication.translate("MainWindow", "&Endorse ModOrganizer", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionEndorseMO.setToolTip(
            QCoreApplication.translate("MainWindow", "Endorse Mod Organizer", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionEndorseMO.setStatusTip(
            QCoreApplication.translate("MainWindow", "Endorse Mod Organizer", None)
        )
        # endif // QT_CONFIG(statustip)
        self.actionChange_Game.setText(
            QCoreApplication.translate("MainWindow", "Manage Instan&ces...", None)
        )
        self.actionChange_Game.setIconText(
            QCoreApplication.translate("MainWindow", "Manage Instan&ces...", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionChange_Game.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "Open the instance manager window to manage a different instance",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionChange_Game.setStatusTip(
            QCoreApplication.translate(
                "MainWindow",
                "Open the instance manager window to manage a different instance",
                None,
            )
        )
        # endif // QT_CONFIG(statustip)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", "E&xit", None))
        self.actionExit.setIconText(
            QCoreApplication.translate("MainWindow", "E&xit", None)
        )
        # if QT_CONFIG(tooltip)
        self.actionExit.setToolTip(
            QCoreApplication.translate("MainWindow", "Exits Mod Organizer", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.actionExit.setStatusTip(
            QCoreApplication.translate("MainWindow", "Exits Mod Organizer", None)
        )
        # endif // QT_CONFIG(statustip)
        self.actionToolBarMainToggle.setText(
            QCoreApplication.translate("MainWindow", "M&ain Toolbar", None)
        )
        self.actionToolBarSmallIcons.setText(
            QCoreApplication.translate("MainWindow", "&Small Icons", None)
        )
        self.actionToolBarLargeIcons.setText(
            QCoreApplication.translate("MainWindow", "Lar&ge Icons", None)
        )
        self.actionToolBarIconsOnly.setText(
            QCoreApplication.translate("MainWindow", "&Icons Only", None)
        )
        self.actionToolBarTextOnly.setText(
            QCoreApplication.translate("MainWindow", "&Text Only", None)
        )
        self.actionToolBarIconsAndText.setText(
            QCoreApplication.translate("MainWindow", "I&cons and Text", None)
        )
        self.actionMainMenuToggle.setText(
            QCoreApplication.translate("MainWindow", "&Menu", None)
        )
        self.actionStatusBarToggle.setText(
            QCoreApplication.translate("MainWindow", "Status &bar", None)
        )
        self.actionViewLog.setText(
            QCoreApplication.translate("MainWindow", "Log", None)
        )
        self.action_Refresh.setText(
            QCoreApplication.translate("MainWindow", "&Refresh", None)
        )
        # if QT_CONFIG(shortcut)
        self.action_Refresh.setShortcut(
            QCoreApplication.translate("MainWindow", "F5", None)
        )
        # endif // QT_CONFIG(shortcut)
        self.actionToolBarMediumIcons.setText(
            QCoreApplication.translate("MainWindow", "M&edium Icons", None)
        )
        self.categoriesGroup.setTitle(
            QCoreApplication.translate("MainWindow", "Filters", None)
        )
        self.filtersClear.setText(
            QCoreApplication.translate("MainWindow", "Clear", None)
        )
        self.filtersEdit.setText(
            QCoreApplication.translate("MainWindow", "Edit...", None)
        )
        # if QT_CONFIG(tooltip)
        self.filtersAnd.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "Display mods that match all selected categories.", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.filtersAnd.setText(QCoreApplication.translate("MainWindow", "And", None))
        # if QT_CONFIG(tooltip)
        self.filtersOr.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "Display mods that match at least one of the selected categories",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.filtersOr.setText(QCoreApplication.translate("MainWindow", "Or", None))
        # if QT_CONFIG(tooltip)
        self.filtersSeparators.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "\n"
                "                              Filter: only show the separators that match the current filters\n"
                "                              Show: always show separators\n"
                "                              Hide: never show separators\n"
                "                            ",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", "Profile", None))
        # if QT_CONFIG(tooltip)
        self.profileBox.setToolTip(
            QCoreApplication.translate("MainWindow", "Pick a module collection", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.profileBox.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\n"
                '                              <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '                              <html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "                              p, li { white-space: pre-wrap; }\n"
                "                              </style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '                              <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">Create profiles here. Each profile contains its own list of active mods and esps. This way you can quickly switch between setups for different playthroughs.</span></p>\n'
                '                              <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">Please note that r'
                "ight now your esp load order is not kept separate for different profiles.</span></p></body></html>\n"
                "                            ",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.listOptionsBtn.setToolTip(
            QCoreApplication.translate("MainWindow", "Open list options...", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.listOptionsBtn.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "Refresh list. This is usually not necessary unless you modified data outside the program.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.listOptionsBtn.setText("")
        # if QT_CONFIG(tooltip)
        self.openFolderMenu.setToolTip(
            QCoreApplication.translate("MainWindow", "Show Open Folders menu...", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.openFolderMenu.setText("")
        # if QT_CONFIG(tooltip)
        self.restoreModsButton.setToolTip(
            QCoreApplication.translate("MainWindow", "Restore Backup...", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.saveModsButton.setToolTip(
            QCoreApplication.translate("MainWindow", "Create Backup", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.activeModslabel.setText(
            QCoreApplication.translate("MainWindow", "Active:", None)
        )
        # if QT_CONFIG(whatsthis)
        self.activeModsCounter.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "This provides statistics about the mod list.  The total number of active mod is normally displayed.  Other statistics may be accessed with the tooltip of this counter.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(whatsthis)
        self.modList.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                'This is a list of installed mods. Use the checkboxes to activate/deactivate mods and drag & drop mods to change their "installation" orders.',
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.label_2.setText(QCoreApplication.translate("MainWindow", "Filter", None))
        self.clearFiltersButton.setText(
            QCoreApplication.translate("MainWindow", "Clear all Filters", None)
        )
        self.groupCombo.setItemText(
            0, QCoreApplication.translate("MainWindow", "No groups", None)
        )
        self.groupCombo.setItemText(
            1, QCoreApplication.translate("MainWindow", "Categories", None)
        )
        self.groupCombo.setItemText(
            2, QCoreApplication.translate("MainWindow", "Nexus IDs", None)
        )

        self.modFilterEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Filter", None)
        )
        # if QT_CONFIG(tooltip)
        self.executablesListBox.setToolTip(
            QCoreApplication.translate("MainWindow", "Pick a program to run.", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.executablesListBox.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\n"
                '                                <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '                                <html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "                                p, li { white-space: pre-wrap; }\n"
                "                                </style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '                                <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">Choose the program to run. Once you start using ModOrganizer, you should always run your game and tools from here or through shortcuts created here, otherwise mods installed through MO will not be visible.</span></p>\n'
                '                                <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-ind'
                'ent:0px;"><span style=" font-size:8pt;">You can add new Tools to this list, but I can\'t promise tools I haven\'t tested will work.</span></p></body></html>\n'
                "                              ",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.startButton.setToolTip(
            QCoreApplication.translate("MainWindow", "Run program", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.startButton.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\n"
                '                                    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '                                    <html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "                                    p, li { white-space: pre-wrap; }\n"
                "                                    </style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '                                    <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">Run the selected program with ModOrganizer enabled.</span></p></body></html>\n'
                "                                  ",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.startButton.setText(QCoreApplication.translate("MainWindow", "Run", None))
        # if QT_CONFIG(tooltip)
        self.linkButton.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "Create a shortcut in your start menu or on the desktop to the specified program",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.linkButton.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\n"
                '                                    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '                                    <html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "                                    p, li { white-space: pre-wrap; }\n"
                "                                    </style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '                                    <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">This creates a start menu shortcut that directly starts the selected program with the MO active.</span></p></body></html>\n'
                "                                  ",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.linkButton.setText(
            QCoreApplication.translate("MainWindow", "Shortcut", None)
        )
        # if QT_CONFIG(tooltip)
        self.sortButton.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "Sort the plugins using LOOT.", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.sortButton.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow", "Sort the plugins using LOOT.", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.sortButton.setText(QCoreApplication.translate("MainWindow", "Sort", None))
        # if QT_CONFIG(tooltip)
        self.restoreButton.setToolTip(
            QCoreApplication.translate("MainWindow", "Restore a backup.", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.restoreButton.setWhatsThis(
            QCoreApplication.translate("MainWindow", "Restore a backup.", None)
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.saveButton.setToolTip(
            QCoreApplication.translate("MainWindow", "Create a backup.", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.saveButton.setWhatsThis(
            QCoreApplication.translate("MainWindow", "Create a backup.", None)
        )
        # endif // QT_CONFIG(whatsthis)
        self.activePluginsLabel.setText(
            QCoreApplication.translate("MainWindow", "Active:", None)
        )
        # if QT_CONFIG(whatsthis)
        self.activePluginsCounter.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>This provides statistics about the plugin list. The total number of active plugins is normally displayed.  Other statistics may be accessed with the tooltip of this counter.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.espList.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "List of available esp/esm files.", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.espList.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow", "List of available esp/esm files.", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.espFilterEdit.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "Filter the list of plugins.", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.espFilterEdit.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow", "Filter the list of plugins.", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.espFilterEdit.setText("")
        self.espFilterEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Filter", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.espTab),
            QCoreApplication.translate("MainWindow", "Plugins", None),
        )
        # if QT_CONFIG(tooltip)
        self.managedArchiveLabel.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "<html><head/><body><p>BSAs / BA2s are bundles of game assets (textures, scripts, etc.). By default, the engine loads these bundles in a separate step from loose files. <p>Their load order is specified by the priority of the corresponding plugin (right pane, plugins tab).</p><p>If there is a matching plugin, the game will load them no matter what.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.managedArchiveLabel.setText(
            QCoreApplication.translate(
                "MainWindow",
                '<html><head/><body><p>Currently detected archives. (<a href="#">What is an archive?</a>)</p></body></html>',
                None,
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.bsaTab),
            QCoreApplication.translate("MainWindow", "Archives", None),
        )
        # if QT_CONFIG(tooltip)
        self.dataTabRefresh.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "Refresh the data structure.", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.dataTabRefresh.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow", "Refresh the data structure.", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.dataTabRefresh.setText(
            QCoreApplication.translate("MainWindow", "Refresh", None)
        )
        # if QT_CONFIG(whatsthis)
        self.dataTree.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "This is an overview of your data directory as visible to the game (and tools). ",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.dataTabShowOnlyConflicts.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "Filter the list so that only conflicts are displayed.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.dataTabShowOnlyConflicts.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "Filter the list so that only conflicts are displayed.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.dataTabShowOnlyConflicts.setText(
            QCoreApplication.translate("MainWindow", "Conflicts only", None)
        )
        # if QT_CONFIG(tooltip)
        self.dataTabShowFromArchives.setToolTip(
            QCoreApplication.translate(
                "MainWindow",
                "Filter the list so that files from archives are shown.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.dataTabShowFromArchives.setStatusTip("")
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.dataTabShowFromArchives.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "Filter the list so that files from archives are shown.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.dataTabShowFromArchives.setText(
            QCoreApplication.translate("MainWindow", "Archives", None)
        )
        # if QT_CONFIG(tooltip)
        self.dataTabFilter.setToolTip(
            QCoreApplication.translate("MainWindow", "Filter the Data tree.", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.dataTabFilter.setWhatsThis(
            QCoreApplication.translate("MainWindow", "Filter the Data tree.", None)
        )
        # endif // QT_CONFIG(whatsthis)
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.dataTab),
            QCoreApplication.translate("MainWindow", "Data", None),
        )
        # if QT_CONFIG(whatsthis)
        self.savegameList.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "\n"
                '                                  <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '                                  <html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "                                  p, li { white-space: pre-wrap; }\n"
                "                                  </style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '                                  <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">This is a list of all save games for this game. Hover over a list entry to get detailed information about the save including a list of esps/esms that were used at the time this save was created but aren\'t active now.</span></p>\n'
                '                                  <p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px'
                '; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;"></p>\n'
                '                                  <p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">If you click &quot;Fix Mods...&quot; in the context menu, MO will try to activate all mods and esps to fix those missing esps. It will not disable anything!</span></p></body></html>\n'
                "                                ",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.savesTab),
            QCoreApplication.translate("MainWindow", "Saves", None),
        )
        # if QT_CONFIG(tooltip)
        self.btnRefreshDownloads.setToolTip(
            QCoreApplication.translate("MainWindow", "Refresh the downloads.", None)
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.btnRefreshDownloads.setWhatsThis(
            QCoreApplication.translate("MainWindow", "Refresh the downloads.", None)
        )
        # endif // QT_CONFIG(whatsthis)
        self.btnRefreshDownloads.setText(
            QCoreApplication.translate("MainWindow", "Refresh", None)
        )
        # if QT_CONFIG(tooltip)
        self.downloadView.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.downloadView.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow",
                "This is a list of mods you downloaded from Nexus. Double click one to install it. You can also drag an archive into here.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        # if QT_CONFIG(tooltip)
        self.showHiddenBox.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "Show downloads marked as hidden.", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.showHiddenBox.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow", "Show downloads marked as hidden.", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.showHiddenBox.setText(
            QCoreApplication.translate("MainWindow", "Hidden files", None)
        )
        # if QT_CONFIG(tooltip)
        self.downloadFilterEdit.setToolTip(
            QCoreApplication.translate(
                "MainWindow", "Filter the list of downloads.", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.downloadFilterEdit.setWhatsThis(
            QCoreApplication.translate(
                "MainWindow", "Filter the list of downloads.", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.downloadFilterEdit.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "Filter", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.downloadTab),
            QCoreApplication.translate("MainWindow", "Downloads", None),
        )
        self.logDock.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Log", None)
        )
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", "&File", None))
        self.menuTools.setTitle(
            QCoreApplication.translate("MainWindow", "&Tools", None)
        )
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", "&Help", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", "&View", None))
        self.menuToolbars.setTitle(
            QCoreApplication.translate("MainWindow", "&Toolbars", None)
        )
        self.menuRun.setTitle(QCoreApplication.translate("MainWindow", "&Run", None))
        self.toolBar.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Main ToolBar", None)
        )
        pass

    # retranslateUi
