# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsdialog.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
    QAbstractButton,
    QAbstractItemView,
    QAbstractScrollArea,
    QApplication,
    QCheckBox,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSpacerItem,
    QSpinBox,
    QSplitter,
    QTabWidget,
    QTableWidget,
    QTableWidgetItem,
    QToolButton,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)
import ui.qt.resources_rc


class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(820, 592)
        self.verticalLayout = QVBoxLayout(SettingsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QTabWidget(SettingsDialog)
        self.tabWidget.setObjectName("tabWidget")
        self.generalTab = QWidget()
        self.generalTab.setObjectName("generalTab")
        self.gridLayout = QGridLayout(self.generalTab)
        self.gridLayout.setObjectName("gridLayout")
        self.generalScrollArea = QScrollArea(self.generalTab)
        self.generalScrollArea.setObjectName("generalScrollArea")
        self.generalScrollArea.setStyleSheet(
            "#generalScrollArea { background-color: transparent; }\n"
            "#generalScrollAreaWidgetContents { background-color: transparent; }"
        )
        self.generalScrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.generalScrollArea.setFrameShadow(QFrame.Shadow.Plain)
        self.generalScrollArea.setWidgetResizable(True)
        self.generalScrollAreaWidgetContents = QWidget()
        self.generalScrollAreaWidgetContents.setObjectName(
            "generalScrollAreaWidgetContents"
        )
        self.generalScrollAreaWidgetContents.setGeometry(QRect(0, 0, 371, 636))
        self.generalScrollAreaWidgetContents.setAutoFillBackground(False)
        self.verticalLayout_8 = QVBoxLayout(self.generalScrollAreaWidgetContents)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.groupBox_61 = QGroupBox(self.generalScrollAreaWidgetContents)
        self.groupBox_61.setObjectName("groupBox_61")
        self.gridLayout_3 = QGridLayout(self.groupBox_61)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_3.setContentsMargins(9, 9, 9, 9)
        self.horizontalSpacer_4 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.label_33 = QLabel(self.groupBox_61)
        self.label_33.setObjectName("label_33")
        # if QT_CONFIG(tooltip)
        self.label_33.setToolTip("https://discord.gg/ewUVAqyrQX")
        # endif // QT_CONFIG(tooltip)
        self.label_33.setOpenExternalLinks(True)

        self.gridLayout_3.addWidget(self.label_33, 0, 1, 1, 1)

        self.languageBox = QComboBox(self.groupBox_61)
        self.languageBox.setObjectName("languageBox")

        self.gridLayout_3.addWidget(self.languageBox, 0, 0, 1, 1)

        self.verticalLayout_8.addWidget(self.groupBox_61)

        self.groupBox_5 = QGroupBox(self.generalScrollAreaWidgetContents)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.showMetaBox = QCheckBox(self.groupBox_5)
        self.showMetaBox.setObjectName("showMetaBox")

        self.verticalLayout_2.addWidget(self.showMetaBox)

        self.compactBox = QCheckBox(self.groupBox_5)
        self.compactBox.setObjectName("compactBox")

        self.verticalLayout_2.addWidget(self.compactBox)

        self.hideDownloadInstallBox = QCheckBox(self.groupBox_5)
        self.hideDownloadInstallBox.setObjectName("hideDownloadInstallBox")

        self.verticalLayout_2.addWidget(self.hideDownloadInstallBox)

        self.verticalLayout_8.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.generalScrollAreaWidgetContents)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkForUpdates = QCheckBox(self.groupBox_6)
        self.checkForUpdates.setObjectName("checkForUpdates")

        self.verticalLayout_3.addWidget(self.checkForUpdates)

        self.usePrereleaseBox = QCheckBox(self.groupBox_6)
        self.usePrereleaseBox.setObjectName("usePrereleaseBox")

        self.verticalLayout_3.addWidget(self.usePrereleaseBox)

        self.verticalLayout_8.addWidget(self.groupBox_6)

        self.groupBox_8 = QGroupBox(self.generalScrollAreaWidgetContents)
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.localINIs = QCheckBox(self.groupBox_8)
        self.localINIs.setObjectName("localINIs")

        self.verticalLayout_11.addWidget(self.localINIs)

        self.localSaves = QCheckBox(self.groupBox_8)
        self.localSaves.setObjectName("localSaves")

        self.verticalLayout_11.addWidget(self.localSaves)

        self.automaticArchiveInvalidation = QCheckBox(self.groupBox_8)
        self.automaticArchiveInvalidation.setObjectName("automaticArchiveInvalidation")

        self.verticalLayout_11.addWidget(self.automaticArchiveInvalidation)

        self.verticalLayout_8.addWidget(self.groupBox_8)

        self.groupBox_9 = QGroupBox(self.generalScrollAreaWidgetContents)
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_9)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(9, 9, 9, 9)
        self.centerDialogs = QCheckBox(self.groupBox_9)
        self.centerDialogs.setObjectName("centerDialogs")

        self.verticalLayout_14.addWidget(self.centerDialogs)

        self.changeGameConfirmation = QCheckBox(self.groupBox_9)
        self.changeGameConfirmation.setObjectName("changeGameConfirmation")

        self.verticalLayout_14.addWidget(self.changeGameConfirmation)

        self.showMenubarOnAlt = QCheckBox(self.groupBox_9)
        self.showMenubarOnAlt.setObjectName("showMenubarOnAlt")

        self.verticalLayout_14.addWidget(self.showMenubarOnAlt)

        self.doubleClickPreviews = QCheckBox(self.groupBox_9)
        self.doubleClickPreviews.setObjectName("doubleClickPreviews")

        self.verticalLayout_14.addWidget(self.doubleClickPreviews)

        self.verticalLayout_8.addWidget(self.groupBox_9)

        self.widget_10 = QWidget(self.generalScrollAreaWidgetContents)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.resetDialogsButton = QPushButton(self.widget_10)
        self.resetDialogsButton.setObjectName("resetDialogsButton")
        self.resetDialogsButton.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_12.addWidget(self.resetDialogsButton)

        self.categoriesBtn = QPushButton(self.widget_10)
        self.categoriesBtn.setObjectName("categoriesBtn")

        self.horizontalLayout_12.addWidget(self.categoriesBtn)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)

        self.verticalLayout_8.addWidget(self.widget_10)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.generalScrollArea.setWidget(self.generalScrollAreaWidgetContents)

        self.gridLayout.addWidget(self.generalScrollArea, 0, 0, 1, 1)

        self.tabWidget.addTab(self.generalTab, "")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_20 = QVBoxLayout(self.tab)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.groupBox_11 = QGroupBox(self.tab)
        self.groupBox_11.setObjectName("groupBox_11")
        self.groupBox_11.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )
        self.horizontalLayout_13 = QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.styleBox = QComboBox(self.groupBox_11)
        self.styleBox.setObjectName("styleBox")

        self.horizontalLayout_13.addWidget(self.styleBox)

        self.exploreStyles = QPushButton(self.groupBox_11)
        self.exploreStyles.setObjectName("exploreStyles")

        self.horizontalLayout_13.addWidget(self.exploreStyles)

        self.horizontalSpacer_5 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_13.addItem(self.horizontalSpacer_5)

        self.verticalLayout_20.addWidget(self.groupBox_11)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.ModlistGroupBox = QGroupBox(self.tab)
        self.ModlistGroupBox.setObjectName("ModlistGroupBox")
        self.verticalLayout_13 = QVBoxLayout(self.ModlistGroupBox)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.tableWidget = QTableWidget(self.ModlistGroupBox)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )
        self.tableWidget.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )
        self.tableWidget.setVerticalScrollMode(
            QAbstractItemView.ScrollMode.ScrollPerPixel
        )
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_13.addWidget(self.tableWidget)

        self.widget_5 = QWidget(self.ModlistGroupBox)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.resetColorsBtn = QPushButton(self.widget_5)
        self.resetColorsBtn.setObjectName("resetColorsBtn")

        self.horizontalLayout_3.addWidget(self.resetColorsBtn)

        self.verticalLayout_13.addWidget(self.widget_5)

        self.verticalLayout_18.addWidget(self.ModlistGroupBox)

        self.verticalLayout_20.addLayout(self.verticalLayout_18)

        self.tabWidget.addTab(self.tab, "")
        self.uiTab = QWidget()
        self.uiTab.setObjectName("uiTab")
        self.verticalLayout_19 = QVBoxLayout(self.uiTab)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.widget_11 = QWidget(self.uiTab)
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout_21 = QVBoxLayout(self.widget_11)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.colorSeparatorsBox = QCheckBox(self.widget_11)
        self.colorSeparatorsBox.setObjectName("colorSeparatorsBox")
        self.colorSeparatorsBox.setChecked(True)

        self.verticalLayout_21.addWidget(self.colorSeparatorsBox)

        self.displayForeignBox = QCheckBox(self.widget_11)
        self.displayForeignBox.setObjectName("displayForeignBox")
        self.displayForeignBox.setChecked(True)

        self.verticalLayout_21.addWidget(self.displayForeignBox)

        self.saveFiltersBox = QCheckBox(self.widget_11)
        self.saveFiltersBox.setObjectName("saveFiltersBox")

        self.verticalLayout_21.addWidget(self.saveFiltersBox)

        self.checkUpdateInstallBox = QCheckBox(self.widget_11)
        self.checkUpdateInstallBox.setObjectName("checkUpdateInstallBox")
        self.checkUpdateInstallBox.setChecked(True)

        self.verticalLayout_21.addWidget(self.checkUpdateInstallBox)

        self.autoCollapseDelayBox = QCheckBox(self.widget_11)
        self.autoCollapseDelayBox.setObjectName("autoCollapseDelayBox")

        self.verticalLayout_21.addWidget(self.autoCollapseDelayBox)

        self.verticalLayout_19.addWidget(self.widget_11)

        self.verticalSpacer_5 = QSpacerItem(
            20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed
        )

        self.verticalLayout_19.addItem(self.verticalSpacer_5)

        self.collapsibleSeparatorsWidget = QGroupBox(self.uiTab)
        self.collapsibleSeparatorsWidget.setObjectName("collapsibleSeparatorsWidget")
        self.collapsibleSeparatorsWidget.setFlat(False)
        self.collapsibleSeparatorsWidget.setCheckable(False)
        self.collapsibleSeparatorsWidget.setChecked(False)
        self.verticalLayout_17 = QVBoxLayout(self.collapsibleSeparatorsWidget)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_9.setVerticalSpacing(9)
        self.collapsibleSeparatorsHighlightToBox = QCheckBox(
            self.collapsibleSeparatorsWidget
        )
        self.collapsibleSeparatorsHighlightToBox.setObjectName(
            "collapsibleSeparatorsHighlightToBox"
        )
        self.collapsibleSeparatorsHighlightToBox.setChecked(True)

        self.gridLayout_9.addWidget(
            self.collapsibleSeparatorsHighlightToBox, 5, 1, 1, 1
        )

        self.collapsibleSeparatorsLabel = QLabel(self.collapsibleSeparatorsWidget)
        self.collapsibleSeparatorsLabel.setObjectName("collapsibleSeparatorsLabel")

        self.gridLayout_9.addWidget(self.collapsibleSeparatorsLabel, 1, 0, 1, 1)

        self.label_34 = QLabel(self.collapsibleSeparatorsWidget)
        self.label_34.setObjectName("label_34")

        self.gridLayout_9.addWidget(self.label_34, 5, 0, 1, 1)

        self.collapsibleSeparatorsHighlightFromBox = QCheckBox(
            self.collapsibleSeparatorsWidget
        )
        self.collapsibleSeparatorsHighlightFromBox.setObjectName(
            "collapsibleSeparatorsHighlightFromBox"
        )
        self.collapsibleSeparatorsHighlightFromBox.setChecked(True)

        self.gridLayout_9.addWidget(
            self.collapsibleSeparatorsHighlightFromBox, 5, 2, 1, 1
        )

        self.collapsibleSeparatorsAscBox = QCheckBox(self.collapsibleSeparatorsWidget)
        self.collapsibleSeparatorsAscBox.setObjectName("collapsibleSeparatorsAscBox")
        self.collapsibleSeparatorsAscBox.setChecked(True)

        self.gridLayout_9.addWidget(self.collapsibleSeparatorsAscBox, 1, 1, 1, 1)

        self.collapsibleSeparatorsDscBox = QCheckBox(self.collapsibleSeparatorsWidget)
        self.collapsibleSeparatorsDscBox.setObjectName("collapsibleSeparatorsDscBox")

        self.gridLayout_9.addWidget(self.collapsibleSeparatorsDscBox, 1, 2, 1, 1)

        self.label_35 = QLabel(self.collapsibleSeparatorsWidget)
        self.label_35.setObjectName("label_35")

        self.gridLayout_9.addWidget(self.label_35, 8, 0, 1, 1)

        self.widget_4 = QWidget(self.collapsibleSeparatorsWidget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.collapsibleSeparatorsIconsConflictsBox = QCheckBox(self.widget_4)
        self.collapsibleSeparatorsIconsConflictsBox.setObjectName(
            "collapsibleSeparatorsIconsConflictsBox"
        )
        self.collapsibleSeparatorsIconsConflictsBox.setChecked(True)

        self.horizontalLayout_7.addWidget(self.collapsibleSeparatorsIconsConflictsBox)

        self.collapsibleSeparatorsIconsFlagsBox = QCheckBox(self.widget_4)
        self.collapsibleSeparatorsIconsFlagsBox.setObjectName(
            "collapsibleSeparatorsIconsFlagsBox"
        )
        self.collapsibleSeparatorsIconsFlagsBox.setChecked(True)

        self.horizontalLayout_7.addWidget(self.collapsibleSeparatorsIconsFlagsBox)

        self.collapsibleSeparatorsIconsContentsBox = QCheckBox(self.widget_4)
        self.collapsibleSeparatorsIconsContentsBox.setObjectName(
            "collapsibleSeparatorsIconsContentsBox"
        )
        self.collapsibleSeparatorsIconsContentsBox.setChecked(True)

        self.horizontalLayout_7.addWidget(self.collapsibleSeparatorsIconsContentsBox)

        self.collapsibleSeparatorsIconsVersionBox = QCheckBox(self.widget_4)
        self.collapsibleSeparatorsIconsVersionBox.setObjectName(
            "collapsibleSeparatorsIconsVersionBox"
        )
        self.collapsibleSeparatorsIconsVersionBox.setChecked(True)

        self.horizontalLayout_7.addWidget(self.collapsibleSeparatorsIconsVersionBox)

        self.horizontalSpacer_3 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.gridLayout_9.addWidget(self.widget_4, 8, 1, 1, 2)

        self.verticalLayout_17.addLayout(self.gridLayout_9)

        self.collapsibleSeparatorsPerProfileBox = QCheckBox(
            self.collapsibleSeparatorsWidget
        )
        self.collapsibleSeparatorsPerProfileBox.setObjectName(
            "collapsibleSeparatorsPerProfileBox"
        )

        self.verticalLayout_17.addWidget(self.collapsibleSeparatorsPerProfileBox)

        self.verticalLayout_19.addWidget(self.collapsibleSeparatorsWidget)

        self.verticalSpacer_13 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_19.addItem(self.verticalSpacer_13)

        self.tabWidget.addTab(self.uiTab, "")
        self.pathsTab = QWidget()
        self.pathsTab.setObjectName("pathsTab")
        self.verticalLayout_10 = QVBoxLayout(self.pathsTab)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.browseOverwriteDirBtn = QPushButton(self.pathsTab)
        self.browseOverwriteDirBtn.setObjectName("browseOverwriteDirBtn")

        self.gridLayout_2.addWidget(self.browseOverwriteDirBtn, 6, 2, 1, 1)

        self.browseModDirBtn = QPushButton(self.pathsTab)
        self.browseModDirBtn.setObjectName("browseModDirBtn")
        self.browseModDirBtn.setText("...")

        self.gridLayout_2.addWidget(self.browseModDirBtn, 3, 2, 1, 1)

        self.overwriteDirEdit = QLineEdit(self.pathsTab)
        self.overwriteDirEdit.setObjectName("overwriteDirEdit")

        self.gridLayout_2.addWidget(self.overwriteDirEdit, 6, 1, 1, 1)

        self.browseBaseDirBtn = QPushButton(self.pathsTab)
        self.browseBaseDirBtn.setObjectName("browseBaseDirBtn")

        self.gridLayout_2.addWidget(self.browseBaseDirBtn, 0, 2, 1, 1)

        self.baseDirEdit = QLineEdit(self.pathsTab)
        self.baseDirEdit.setObjectName("baseDirEdit")

        self.gridLayout_2.addWidget(self.baseDirEdit, 0, 1, 1, 1)

        self.label_9 = QLabel(self.pathsTab)
        self.label_9.setObjectName("label_9")

        self.gridLayout_2.addWidget(self.label_9, 4, 0, 1, 1)

        self.label_24 = QLabel(self.pathsTab)
        self.label_24.setObjectName("label_24")

        self.gridLayout_2.addWidget(self.label_24, 6, 0, 1, 1)

        self.downloadDirEdit = QLineEdit(self.pathsTab)
        self.downloadDirEdit.setObjectName("downloadDirEdit")

        self.gridLayout_2.addWidget(self.downloadDirEdit, 2, 1, 1, 1)

        self.cacheDirEdit = QLineEdit(self.pathsTab)
        self.cacheDirEdit.setObjectName("cacheDirEdit")

        self.gridLayout_2.addWidget(self.cacheDirEdit, 4, 1, 1, 1)

        self.browseCacheDirBtn = QPushButton(self.pathsTab)
        self.browseCacheDirBtn.setObjectName("browseCacheDirBtn")
        self.browseCacheDirBtn.setText("...")

        self.gridLayout_2.addWidget(self.browseCacheDirBtn, 4, 2, 1, 1)

        self.label_7 = QLabel(self.pathsTab)
        self.label_7.setObjectName("label_7")

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.gridLayout_2.addItem(self.verticalSpacer_8, 1, 1, 1, 1)

        self.label_22 = QLabel(self.pathsTab)
        self.label_22.setObjectName("label_22")

        self.gridLayout_2.addWidget(self.label_22, 5, 0, 1, 1)

        self.browseDownloadDirBtn = QPushButton(self.pathsTab)
        self.browseDownloadDirBtn.setObjectName("browseDownloadDirBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.browseDownloadDirBtn.sizePolicy().hasHeightForWidth()
        )
        self.browseDownloadDirBtn.setSizePolicy(sizePolicy)
        self.browseDownloadDirBtn.setText("...")

        self.gridLayout_2.addWidget(self.browseDownloadDirBtn, 2, 2, 1, 1)

        self.profilesDirEdit = QLineEdit(self.pathsTab)
        self.profilesDirEdit.setObjectName("profilesDirEdit")

        self.gridLayout_2.addWidget(self.profilesDirEdit, 5, 1, 1, 1)

        self.modDirEdit = QLineEdit(self.pathsTab)
        self.modDirEdit.setObjectName("modDirEdit")

        self.gridLayout_2.addWidget(self.modDirEdit, 3, 1, 1, 1)

        self.browseProfilesDirBtn = QPushButton(self.pathsTab)
        self.browseProfilesDirBtn.setObjectName("browseProfilesDirBtn")

        self.gridLayout_2.addWidget(self.browseProfilesDirBtn, 5, 2, 1, 1)

        self.managedGameDirEdit = QLineEdit(self.pathsTab)
        self.managedGameDirEdit.setObjectName("managedGameDirEdit")
        self.managedGameDirEdit.setAcceptDrops(False)
        self.managedGameDirEdit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.managedGameDirEdit, 11, 1, 1, 1)

        self.label_8 = QLabel(self.pathsTab)
        self.label_8.setObjectName("label_8")

        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.gridLayout_2.addItem(self.verticalSpacer_7, 10, 1, 1, 1)

        self.label_29 = QLabel(self.pathsTab)
        self.label_29.setObjectName("label_29")

        self.gridLayout_2.addWidget(self.label_29, 11, 0, 1, 1)

        self.label_25 = QLabel(self.pathsTab)
        self.label_25.setObjectName("label_25")

        self.gridLayout_2.addWidget(self.label_25, 0, 0, 1, 1)

        self.label_26 = QLabel(self.pathsTab)
        self.label_26.setObjectName("label_26")

        self.gridLayout_2.addWidget(self.label_26, 9, 0, 1, 3)

        self.browseGameDirBtn = QPushButton(self.pathsTab)
        self.browseGameDirBtn.setObjectName("browseGameDirBtn")

        self.gridLayout_2.addWidget(self.browseGameDirBtn, 11, 2, 1, 1)

        self.verticalLayout_10.addLayout(self.gridLayout_2)

        self.verticalSpacer_6 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_10.addItem(self.verticalSpacer_6)

        self.label_23 = QLabel(self.pathsTab)
        self.label_23.setObjectName("label_23")

        self.verticalLayout_10.addWidget(self.label_23)

        self.tabWidget.addTab(self.pathsTab, "")
        self.nexusTab = QWidget()
        self.nexusTab.setObjectName("nexusTab")
        self.verticalLayout_4 = QVBoxLayout(self.nexusTab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.nexusScrollArea = QScrollArea(self.nexusTab)
        self.nexusScrollArea.setObjectName("nexusScrollArea")
        self.nexusScrollArea.setStyleSheet(
            "#nexusScrollArea { background-color: transparent; }\n"
            "#nexusScrollAreaWidgetContents { background-color: transparent; }"
        )
        self.nexusScrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.nexusScrollArea.setFrameShadow(QFrame.Shadow.Plain)
        self.nexusScrollArea.setWidgetResizable(True)
        self.nexusScrollAreaWidgetContents = QWidget()
        self.nexusScrollAreaWidgetContents.setObjectName(
            "nexusScrollAreaWidgetContents"
        )
        self.nexusScrollAreaWidgetContents.setGeometry(QRect(0, 0, 538, 611))
        self.nexusScrollAreaWidgetContents.setAutoFillBackground(False)
        self.verticalLayout_34 = QVBoxLayout(self.nexusScrollAreaWidgetContents)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.groupBox_2 = QGroupBox(self.nexusScrollAreaWidgetContents)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout = QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName("formLayout")
        self.formLayout.setHorizontalSpacing(10)
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.label_2.setTextInteractionFlags(
            Qt.TextInteractionFlag.LinksAccessibleByMouse
            | Qt.TextInteractionFlag.TextSelectableByKeyboard
            | Qt.TextInteractionFlag.TextSelectableByMouse
        )

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.nexusUserID = QLabel(self.groupBox_2)
        self.nexusUserID.setObjectName("nexusUserID")
        self.nexusUserID.setText("id")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nexusUserID)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.nexusName = QLabel(self.groupBox_2)
        self.nexusName.setObjectName("nexusName")
        self.nexusName.setText("name")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.nexusName)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_11)

        self.nexusAccount = QLabel(self.groupBox_2)
        self.nexusAccount.setObjectName("nexusAccount")
        self.nexusAccount.setText("account")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.nexusAccount)

        self.horizontalLayout_17.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.nexusScrollAreaWidgetContents)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout_3 = QFormLayout(self.groupBox_3)
        self.formLayout_3.setObjectName("formLayout_3")
        self.formLayout_3.setHorizontalSpacing(10)
        self.label_30 = QLabel(self.groupBox_3)
        self.label_30.setObjectName("label_30")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_30)

        self.nexusDailyRequests = QLabel(self.groupBox_3)
        self.nexusDailyRequests.setObjectName("nexusDailyRequests")
        self.nexusDailyRequests.setText("daily requests")

        self.formLayout_3.setWidget(
            0, QFormLayout.ItemRole.FieldRole, self.nexusDailyRequests
        )

        self.label_31 = QLabel(self.groupBox_3)
        self.label_31.setObjectName("label_31")

        self.formLayout_3.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_31)

        self.nexusHourlyRequests = QLabel(self.groupBox_3)
        self.nexusHourlyRequests.setObjectName("nexusHourlyRequests")
        self.nexusHourlyRequests.setText("hourly requests")

        self.formLayout_3.setWidget(
            1, QFormLayout.ItemRole.FieldRole, self.nexusHourlyRequests
        )

        self.horizontalLayout_17.addWidget(self.groupBox_3)

        self.verticalLayout_34.addLayout(self.horizontalLayout_17)

        self.nexusBox = QGroupBox(self.nexusScrollAreaWidgetContents)
        self.nexusBox.setObjectName("nexusBox")
        self.horizontalLayout_15 = QHBoxLayout(self.nexusBox)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.widget_9 = QWidget(self.nexusBox)
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_28 = QVBoxLayout(self.widget_9)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.nexusConnect = QPushButton(self.widget_9)
        self.nexusConnect.setObjectName("nexusConnect")

        self.verticalLayout_28.addWidget(self.nexusConnect)

        self.nexusManualKey = QPushButton(self.widget_9)
        self.nexusManualKey.setObjectName("nexusManualKey")

        self.verticalLayout_28.addWidget(self.nexusManualKey)

        self.nexusDisconnect = QPushButton(self.widget_9)
        self.nexusDisconnect.setObjectName("nexusDisconnect")
        icon = QIcon()
        icon.addFile(":/MO/gui/edit_clear", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.nexusDisconnect.setIcon(icon)

        self.verticalLayout_28.addWidget(self.nexusDisconnect)

        self.verticalSpacer_4 = QSpacerItem(
            0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_28.addItem(self.verticalSpacer_4)

        self.horizontalLayout_15.addWidget(self.widget_9)

        self.widget_15 = QWidget(self.nexusBox)
        self.widget_15.setObjectName("widget_15")
        self.verticalLayout_29 = QVBoxLayout(self.widget_15)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.nexusLog = QListWidget(self.widget_15)
        self.nexusLog.setObjectName("nexusLog")
        self.nexusLog.setSizeAdjustPolicy(
            QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents
        )

        self.verticalLayout_29.addWidget(self.nexusLog)

        self.horizontalLayout_15.addWidget(self.widget_15)

        self.verticalLayout_34.addWidget(self.nexusBox)

        self.widget_6 = QWidget(self.nexusScrollAreaWidgetContents)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_34.addWidget(self.widget_6)

        self.settingsBox = QGroupBox(self.nexusScrollAreaWidgetContents)
        self.settingsBox.setObjectName("settingsBox")
        self.horizontalLayout_10 = QHBoxLayout(self.settingsBox)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.widget_16 = QWidget(self.settingsBox)
        self.widget_16.setObjectName("widget_16")
        self.verticalLayout_30 = QVBoxLayout(self.widget_16)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.endorsementBox = QCheckBox(self.widget_16)
        self.endorsementBox.setObjectName("endorsementBox")
        self.endorsementBox.setChecked(True)

        self.verticalLayout_30.addWidget(self.endorsementBox)

        self.trackedBox = QCheckBox(self.widget_16)
        self.trackedBox.setObjectName("trackedBox")
        self.trackedBox.setChecked(True)

        self.verticalLayout_30.addWidget(self.trackedBox)

        self.categoryMappingsBox = QCheckBox(self.widget_16)
        self.categoryMappingsBox.setObjectName("categoryMappingsBox")
        self.categoryMappingsBox.setChecked(True)

        self.verticalLayout_30.addWidget(self.categoryMappingsBox)

        self.hideAPICounterBox = QCheckBox(self.widget_16)
        self.hideAPICounterBox.setObjectName("hideAPICounterBox")

        self.verticalLayout_30.addWidget(self.hideAPICounterBox)

        self.horizontalLayout_10.addWidget(self.widget_16)

        self.widget_17 = QWidget(self.settingsBox)
        self.widget_17.setObjectName("widget_17")
        self.verticalLayout_31 = QVBoxLayout(self.widget_17)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.associateButton = QPushButton(self.widget_17)
        self.associateButton.setObjectName("associateButton")

        self.verticalLayout_31.addWidget(self.associateButton)

        self.clearCacheButton = QPushButton(self.widget_17)
        self.clearCacheButton.setObjectName("clearCacheButton")

        self.verticalLayout_31.addWidget(self.clearCacheButton)

        self.horizontalLayout_10.addWidget(self.widget_17)

        self.verticalLayout_34.addWidget(self.settingsBox)

        self.serversBox = QGroupBox(self.nexusScrollAreaWidgetContents)
        self.serversBox.setObjectName("serversBox")
        self.horizontalLayout_11 = QHBoxLayout(self.serversBox)
        self.horizontalLayout_11.setSpacing(4)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.label_18 = QLabel(self.serversBox)
        self.label_18.setObjectName("label_18")

        self.verticalLayout_32.addWidget(self.label_18)

        self.knownServersList = QListWidget(self.serversBox)
        self.knownServersList.setObjectName("knownServersList")
        self.knownServersList.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.knownServersList.setDefaultDropAction(Qt.DropAction.MoveAction)

        self.verticalLayout_32.addWidget(self.knownServersList)

        self.horizontalLayout_11.addLayout(self.verticalLayout_32)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.label_21 = QLabel(self.serversBox)
        self.label_21.setObjectName("label_21")

        self.verticalLayout_33.addWidget(self.label_21)

        self.preferredServersList = QListWidget(self.serversBox)
        self.preferredServersList.setObjectName("preferredServersList")
        self.preferredServersList.setDragDropMode(
            QAbstractItemView.DragDropMode.DragDrop
        )
        self.preferredServersList.setDefaultDropAction(Qt.DropAction.MoveAction)

        self.verticalLayout_33.addWidget(self.preferredServersList)

        self.horizontalLayout_11.addLayout(self.verticalLayout_33)

        self.verticalLayout_34.addWidget(self.serversBox)

        self.nexusScrollArea.setWidget(self.nexusScrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.nexusScrollArea)

        self.tabWidget.addTab(self.nexusTab, "")
        self.pluginsTab = QWidget()
        self.pluginsTab.setObjectName("pluginsTab")
        self.verticalLayout_9 = QVBoxLayout(self.pluginsTab)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.splitter = QSplitter(self.pluginsTab)
        self.splitter.setObjectName("splitter")
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName("widget")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(4)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.horizontalLayout_6 = QHBoxLayout(self.widget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.splitter_2 = QSplitter(self.widget)
        self.splitter_2.setObjectName("splitter_2")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy2)
        self.splitter_2.setOrientation(Qt.Orientation.Horizontal)
        self.widget1 = QWidget(self.splitter_2)
        self.widget1.setObjectName("widget1")
        self.verticalLayout_15 = QVBoxLayout(self.widget1)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.pluginsList = QTreeWidget(self.widget1)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, "1")
        self.pluginsList.setHeaderItem(__qtreewidgetitem)
        self.pluginsList.setObjectName("pluginsList")

        self.verticalLayout_15.addWidget(self.pluginsList)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pluginFilterEdit = QLineEdit(self.widget1)
        self.pluginFilterEdit.setObjectName("pluginFilterEdit")

        self.horizontalLayout_4.addWidget(self.pluginFilterEdit)

        self.verticalLayout_15.addLayout(self.horizontalLayout_4)

        self.splitter_2.addWidget(self.widget1)
        self.pluginWidget = QWidget(self.splitter_2)
        self.pluginWidget.setObjectName("pluginWidget")
        self.verticalLayout_7 = QVBoxLayout(self.pluginWidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pluginDescription = QWidget(self.pluginWidget)
        self.pluginDescription.setObjectName("pluginDescription")
        self.pluginDescriptionLayout = QFormLayout(self.pluginDescription)
        self.pluginDescriptionLayout.setObjectName("pluginDescriptionLayout")
        self.pluginDescriptionLayout.setLabelAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )
        self.pluginDescriptionLayout.setContentsMargins(6, -1, -1, -1)
        self.label_13 = QLabel(self.pluginDescription)
        self.label_13.setObjectName("label_13")
        self.label_13.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )

        self.pluginDescriptionLayout.setWidget(
            0, QFormLayout.ItemRole.LabelRole, self.label_13
        )

        self.authorLabel = QLabel(self.pluginDescription)
        self.authorLabel.setObjectName("authorLabel")
        self.authorLabel.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )

        self.pluginDescriptionLayout.setWidget(
            0, QFormLayout.ItemRole.FieldRole, self.authorLabel
        )

        self.label_15 = QLabel(self.pluginDescription)
        self.label_15.setObjectName("label_15")
        self.label_15.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )

        self.pluginDescriptionLayout.setWidget(
            1, QFormLayout.ItemRole.LabelRole, self.label_15
        )

        self.versionLabel = QLabel(self.pluginDescription)
        self.versionLabel.setObjectName("versionLabel")
        self.versionLabel.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )

        self.pluginDescriptionLayout.setWidget(
            1, QFormLayout.ItemRole.FieldRole, self.versionLabel
        )

        self.label_14 = QLabel(self.pluginDescription)
        self.label_14.setObjectName("label_14")
        self.label_14.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )

        self.pluginDescriptionLayout.setWidget(
            2, QFormLayout.ItemRole.LabelRole, self.label_14
        )

        self.descriptionLabel = QLabel(self.pluginDescription)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.descriptionLabel.setAlignment(
            Qt.AlignmentFlag.AlignLeading
            | Qt.AlignmentFlag.AlignLeft
            | Qt.AlignmentFlag.AlignTop
        )
        self.descriptionLabel.setWordWrap(True)

        self.pluginDescriptionLayout.setWidget(
            2, QFormLayout.ItemRole.FieldRole, self.descriptionLabel
        )

        self.enabledCheckbox = QCheckBox(self.pluginDescription)
        self.enabledCheckbox.setObjectName("enabledCheckbox")

        self.pluginDescriptionLayout.setWidget(
            3, QFormLayout.ItemRole.LabelRole, self.enabledCheckbox
        )

        self.verticalLayout_7.addWidget(self.pluginDescription)

        self.pluginSettingsList = QTreeWidget(self.pluginWidget)
        self.pluginSettingsList.setObjectName("pluginSettingsList")
        self.pluginSettingsList.setIndentation(0)
        self.pluginSettingsList.setRootIsDecorated(False)
        self.pluginSettingsList.setItemsExpandable(False)
        self.pluginSettingsList.setExpandsOnDoubleClick(False)
        self.pluginSettingsList.header().setVisible(False)
        self.pluginSettingsList.header().setDefaultSectionSize(170)

        self.verticalLayout_7.addWidget(self.pluginSettingsList)

        self.noPluginLabel = QLabel(self.pluginWidget)
        self.noPluginLabel.setObjectName("noPluginLabel")
        self.noPluginLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.noPluginLabel)

        self.verticalLayout_7.setStretch(1, 1)
        self.splitter_2.addWidget(self.pluginWidget)

        self.horizontalLayout_6.addWidget(self.splitter_2)

        self.splitter.addWidget(self.widget)
        self.verticalGroupBox = QGroupBox(self.splitter)
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        sizePolicy3 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(
            self.verticalGroupBox.sizePolicy().hasHeightForWidth()
        )
        self.verticalGroupBox.setSizePolicy(sizePolicy3)
        self.verticalLayout_16 = QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.pluginBlacklist = QListWidget(self.verticalGroupBox)
        self.pluginBlacklist.setObjectName("pluginBlacklist")

        self.verticalLayout_16.addWidget(self.pluginBlacklist)

        self.splitter.addWidget(self.verticalGroupBox)

        self.verticalLayout_9.addWidget(self.splitter)

        self.tabWidget.addTab(self.pluginsTab, "")
        self.workaroundTab = QWidget()
        self.workaroundTab.setObjectName("workaroundTab")
        self.verticalLayout_5 = QVBoxLayout(self.workaroundTab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.workaroundScrollArea = QScrollArea(self.workaroundTab)
        self.workaroundScrollArea.setObjectName("workaroundScrollArea")
        self.workaroundScrollArea.setStyleSheet(
            "#workaroundScrollArea { background-color: transparent; }\n"
            "#workaroundScrollAreaWidgetContents { background-color: transparent; }"
        )
        self.workaroundScrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.workaroundScrollArea.setFrameShadow(QFrame.Shadow.Plain)
        self.workaroundScrollArea.setWidgetResizable(True)
        self.workaroundScrollAreaWidgetContents = QWidget()
        self.workaroundScrollAreaWidgetContents.setObjectName(
            "workaroundScrollAreaWidgetContents"
        )
        self.workaroundScrollAreaWidgetContents.setGeometry(QRect(0, 0, 790, 451))
        self.workaroundScrollAreaWidgetContents.setAutoFillBackground(False)
        self.verticalLayout_6 = QVBoxLayout(self.workaroundScrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.workaroundsOptionsBox = QGroupBox(self.workaroundScrollAreaWidgetContents)
        self.workaroundsOptionsBox.setObjectName("workaroundsOptionsBox")
        self.verticalLayout_23 = QVBoxLayout(self.workaroundsOptionsBox)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(9, 9, 9, 9)
        self.forceEnableBox = QCheckBox(self.workaroundsOptionsBox)
        self.forceEnableBox.setObjectName("forceEnableBox")
        self.forceEnableBox.setChecked(True)

        self.verticalLayout_23.addWidget(self.forceEnableBox)

        self.enableArchiveParsingBox = QCheckBox(self.workaroundsOptionsBox)
        self.enableArchiveParsingBox.setObjectName("enableArchiveParsingBox")
        self.enableArchiveParsingBox.setChecked(True)

        self.verticalLayout_23.addWidget(self.enableArchiveParsingBox)

        self.lockGUIBox = QCheckBox(self.workaroundsOptionsBox)
        self.lockGUIBox.setObjectName("lockGUIBox")
        self.lockGUIBox.setChecked(True)

        self.verticalLayout_23.addWidget(self.lockGUIBox)

        self.verticalLayout_6.addWidget(self.workaroundsOptionsBox)

        self.groupBox_12 = QGroupBox(self.workaroundScrollAreaWidgetContents)
        self.groupBox_12.setObjectName("groupBox_12")
        self.gridLayout_7 = QGridLayout(self.groupBox_12)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.steamUserEdit = QLineEdit(self.groupBox_12)
        self.steamUserEdit.setObjectName("steamUserEdit")

        self.gridLayout_7.addWidget(self.steamUserEdit, 1, 1, 1, 1)

        self.label_20 = QLabel(self.groupBox_12)
        self.label_20.setObjectName("label_20")

        self.gridLayout_7.addWidget(self.label_20, 1, 2, 1, 1)

        self.steamPassEdit = QLineEdit(self.groupBox_12)
        self.steamPassEdit.setObjectName("steamPassEdit")
        self.steamPassEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout_7.addWidget(self.steamPassEdit, 1, 3, 1, 1)

        self.label_19 = QLabel(self.groupBox_12)
        self.label_19.setObjectName("label_19")

        self.gridLayout_7.addWidget(self.label_19, 1, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_12)
        self.label_4.setObjectName("label_4")

        self.gridLayout_7.addWidget(self.label_4, 0, 0, 1, 1)

        self.appIDEdit = QLineEdit(self.groupBox_12)
        self.appIDEdit.setObjectName("appIDEdit")

        self.gridLayout_7.addWidget(self.appIDEdit, 0, 1, 1, 1)

        self.verticalLayout_6.addWidget(self.groupBox_12)

        self.groupBox = QGroupBox(self.workaroundScrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setMinimumSize(QSize(0, 100))
        self.verticalLayout_22 = QVBoxLayout(self.groupBox)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.offlineBox = QCheckBox(self.groupBox)
        self.offlineBox.setObjectName("offlineBox")

        self.verticalLayout_22.addWidget(self.offlineBox)

        self.proxyBox = QCheckBox(self.groupBox)
        self.proxyBox.setObjectName("proxyBox")

        self.verticalLayout_22.addWidget(self.proxyBox)

        self.widget_7 = QWidget(self.groupBox)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.useCustomBrowser = QCheckBox(self.widget_7)
        self.useCustomBrowser.setObjectName("useCustomBrowser")

        self.horizontalLayout_9.addWidget(self.useCustomBrowser)

        self.browserCommand = QLineEdit(self.widget_7)
        self.browserCommand.setObjectName("browserCommand")

        self.horizontalLayout_9.addWidget(self.browserCommand)

        self.browseCustomBrowser = QToolButton(self.widget_7)
        self.browseCustomBrowser.setObjectName("browseCustomBrowser")

        self.horizontalLayout_9.addWidget(self.browseCustomBrowser)

        self.verticalLayout_22.addWidget(self.widget_7)

        self.verticalLayout_6.addWidget(self.groupBox)

        self.widget_12 = QWidget(self.workaroundScrollAreaWidgetContents)
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout = QHBoxLayout(self.widget_12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.resetGeometryBtn = QPushButton(self.widget_12)
        self.resetGeometryBtn.setObjectName("resetGeometryBtn")

        self.horizontalLayout.addWidget(self.resetGeometryBtn)

        self.execBlacklistBtn = QPushButton(self.widget_12)
        self.execBlacklistBtn.setObjectName("execBlacklistBtn")
        self.execBlacklistBtn.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.execBlacklistBtn)

        self.bsaDateBtn = QPushButton(self.widget_12)
        self.bsaDateBtn.setObjectName("bsaDateBtn")
        icon1 = QIcon()
        icon1.addFile(
            ":/MO/gui/resources/emblem-readonly.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.bsaDateBtn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.bsaDateBtn)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_6.addWidget(self.widget_12)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.workaroundScrollArea.setWidget(self.workaroundScrollAreaWidgetContents)

        self.verticalLayout_5.addWidget(self.workaroundScrollArea)

        self.label_6 = QLabel(self.workaroundTab)
        self.label_6.setObjectName("label_6")
        self.label_6.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_6)

        self.tabWidget.addTab(self.workaroundTab, "")
        self.diagnosticsTab = QWidget()
        self.diagnosticsTab.setObjectName("diagnosticsTab")
        self.verticalLayout_24 = QVBoxLayout(self.diagnosticsTab)
        self.verticalLayout_24.setSpacing(12)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.groupBox_4 = QGroupBox(self.diagnosticsTab)
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayout_4 = QFormLayout(self.groupBox_4)
        self.formLayout_4.setObjectName("formLayout_4")
        self.formLayout_4.setFieldGrowthPolicy(
            QFormLayout.FieldGrowthPolicy.FieldsStayAtSizeHint
        )
        self.label_12 = QLabel(self.groupBox_4)
        self.label_12.setObjectName("label_12")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_12)

        self.logLevelBox = QComboBox(self.groupBox_4)
        self.logLevelBox.setObjectName("logLevelBox")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.logLevelBox)

        self.label_27 = QLabel(self.groupBox_4)
        self.label_27.setObjectName("label_27")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_27)

        self.dumpsTypeBox = QComboBox(self.groupBox_4)
        self.dumpsTypeBox.setObjectName("dumpsTypeBox")

        self.formLayout_4.setWidget(
            1, QFormLayout.ItemRole.FieldRole, self.dumpsTypeBox
        )

        self.label_28 = QLabel(self.groupBox_4)
        self.label_28.setObjectName("label_28")

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_28)

        self.dumpsMaxEdit = QSpinBox(self.groupBox_4)
        self.dumpsMaxEdit.setObjectName("dumpsMaxEdit")

        self.formLayout_4.setWidget(
            2, QFormLayout.ItemRole.FieldRole, self.dumpsMaxEdit
        )

        self.verticalLayout_24.addWidget(self.groupBox_4)

        self.groupBox_7 = QGroupBox(self.diagnosticsTab)
        self.groupBox_7.setObjectName("groupBox_7")
        self.formLayout_2 = QFormLayout(self.groupBox_7)
        self.formLayout_2.setObjectName("formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(
            QFormLayout.FieldGrowthPolicy.FieldsStayAtSizeHint
        )
        self.label_32 = QLabel(self.groupBox_7)
        self.label_32.setObjectName("label_32")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_32)

        self.lootLogLevel = QComboBox(self.groupBox_7)
        self.lootLogLevel.setObjectName("lootLogLevel")

        self.formLayout_2.setWidget(
            0, QFormLayout.ItemRole.FieldRole, self.lootLogLevel
        )

        self.verticalLayout_24.addWidget(self.groupBox_7)

        self.diagnosticsExplainedLabel = QLabel(self.diagnosticsTab)
        self.diagnosticsExplainedLabel.setObjectName("diagnosticsExplainedLabel")
        self.diagnosticsExplainedLabel.setWordWrap(True)
        self.diagnosticsExplainedLabel.setOpenExternalLinks(True)

        self.verticalLayout_24.addWidget(self.diagnosticsExplainedLabel)

        self.verticalSpacer_10 = QSpacerItem(
            20, 232, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_24.addItem(self.verticalSpacer_10)

        self.tabWidget.addTab(self.diagnosticsTab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.buttonBox = QDialogButtonBox(SettingsDialog)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok
        )

        self.verticalLayout.addWidget(self.buttonBox)

        QWidget.setTabOrder(self.languageBox, self.usePrereleaseBox)
        QWidget.setTabOrder(self.usePrereleaseBox, self.baseDirEdit)
        QWidget.setTabOrder(self.baseDirEdit, self.browseBaseDirBtn)
        QWidget.setTabOrder(self.browseBaseDirBtn, self.downloadDirEdit)
        QWidget.setTabOrder(self.downloadDirEdit, self.browseDownloadDirBtn)
        QWidget.setTabOrder(self.browseDownloadDirBtn, self.modDirEdit)
        QWidget.setTabOrder(self.modDirEdit, self.browseModDirBtn)
        QWidget.setTabOrder(self.browseModDirBtn, self.cacheDirEdit)
        QWidget.setTabOrder(self.cacheDirEdit, self.browseCacheDirBtn)
        QWidget.setTabOrder(self.browseCacheDirBtn, self.profilesDirEdit)
        QWidget.setTabOrder(self.profilesDirEdit, self.browseProfilesDirBtn)
        QWidget.setTabOrder(self.browseProfilesDirBtn, self.overwriteDirEdit)
        QWidget.setTabOrder(self.overwriteDirEdit, self.browseOverwriteDirBtn)
        QWidget.setTabOrder(self.browseOverwriteDirBtn, self.managedGameDirEdit)
        QWidget.setTabOrder(self.managedGameDirEdit, self.browseGameDirBtn)
        QWidget.setTabOrder(self.browseGameDirBtn, self.pluginSettingsList)
        QWidget.setTabOrder(self.pluginSettingsList, self.lockGUIBox)

        self.retranslateUi(SettingsDialog)
        # self.buttonBox.accepted.connect(SettingsDialog.accept)
        # self.buttonBox.rejected.connect(SettingsDialog.reject)

        self.tabWidget.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(SettingsDialog)

    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(
            QCoreApplication.translate("SettingsDialog", "Settings", None)
        )
        self.groupBox_61.setTitle(
            QCoreApplication.translate("SettingsDialog", "Language", None)
        )
        self.label_33.setText(
            QCoreApplication.translate(
                "SettingsDialog",
                '<a href="https://discord.gg/ewUVAqyrQX">Help translate Mod Organizer on Discord</a>',
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.languageBox.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog", "The language of the user interface.", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.languageBox.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog", "The language of the user interface.", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.groupBox_5.setTitle(
            QCoreApplication.translate("SettingsDialog", "Download List", None)
        )
        # if QT_CONFIG(tooltip)
        self.showMetaBox.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog",
                "Show meta information instead of file names in the download list.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.showMetaBox.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog",
                "Show meta information instead of file names in the download list.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.showMetaBox.setText(
            QCoreApplication.translate("SettingsDialog", "Show meta information", None)
        )
        # if QT_CONFIG(tooltip)
        self.compactBox.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog", "Make the download list more compact.", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.compactBox.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog", "Make the download list more compact.", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.compactBox.setText(
            QCoreApplication.translate("SettingsDialog", "Compact list", None)
        )
        # if QT_CONFIG(tooltip)
        self.hideDownloadInstallBox.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog",
                "Automatically hide downloads after successful installation.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.hideDownloadInstallBox.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog",
                "Automatically hide downloads after successful installation.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.hideDownloadInstallBox.setText(
            QCoreApplication.translate(
                "SettingsDialog", "Hide downloads after installation", None
            )
        )
        self.groupBox_6.setTitle(
            QCoreApplication.translate("SettingsDialog", "Updates", None)
        )
        # if QT_CONFIG(tooltip)
        self.checkForUpdates.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog",
                "Check for Mod Organizer updates on Github on startup.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.checkForUpdates.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog",
                "Check for Mod Organizer updates on Github on startup.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.checkForUpdates.setText(
            QCoreApplication.translate("SettingsDialog", "Check for updates", None)
        )
        # if QT_CONFIG(tooltip)
        self.usePrereleaseBox.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog", "Update to non-stable releases.", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.usePrereleaseBox.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog", "Update to non-stable releases.", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.usePrereleaseBox.setText(
            QCoreApplication.translate(
                "SettingsDialog", "Update to beta versions", None
            )
        )
        self.groupBox_8.setTitle(
            QCoreApplication.translate("SettingsDialog", "Profile Defaults", None)
        )
        self.localINIs.setText(
            QCoreApplication.translate("SettingsDialog", "Local INIs", None)
        )
        self.localSaves.setText(
            QCoreApplication.translate("SettingsDialog", "Local Saves", None)
        )
        self.automaticArchiveInvalidation.setText(
            QCoreApplication.translate(
                "SettingsDialog", "Automatic Archive Invalidation", None
            )
        )
        self.groupBox_9.setTitle(
            QCoreApplication.translate("SettingsDialog", "Miscellaneous", None)
        )
        # if QT_CONFIG(tooltip)
        self.centerDialogs.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog",
                "Dialogs will always be centered on the main window, but will remember their size.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.centerDialogs.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog",
                "Dialogs will always be centered on the main window, but will remember their size.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.centerDialogs.setText(
            QCoreApplication.translate("SettingsDialog", "Always center dialogs", None)
        )
        self.changeGameConfirmation.setText(
            QCoreApplication.translate(
                "SettingsDialog", "Show confirmation when changing instance", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.showMenubarOnAlt.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog", "Show the menubar when the Alt key is pressed", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.showMenubarOnAlt.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog", "Show the menubar when the Alt key is pressed", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.showMenubarOnAlt.setText(
            QCoreApplication.translate(
                "SettingsDialog", "Show menubar when pressing Alt", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.doubleClickPreviews.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog",
                "Whether double-clicking on a file opens the preview window or launches the program associated with it. This applies to the Data tab as well as the Conflicts and Filetree tabs in the mod info window.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.doubleClickPreviews.setText(
            QCoreApplication.translate(
                "SettingsDialog", "Open previews on double-click", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.resetDialogsButton.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog", "Reset all choices made in dialogs.", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.resetDialogsButton.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog", "Reset all choices made in dialogs.", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.resetDialogsButton.setText(
            QCoreApplication.translate("SettingsDialog", "Reset Dialog Choices", None)
        )
        # if QT_CONFIG(tooltip)
        self.categoriesBtn.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog",
                "Modify the categories available to arrange your mods.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.categoriesBtn.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog",
                "Modify the categories available to arrange your mods.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.categoriesBtn.setText(
            QCoreApplication.translate(
                "SettingsDialog", "Configure Mod Categories", None
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.generalTab),
            QCoreApplication.translate("SettingsDialog", "General", None),
        )
        self.groupBox_11.setTitle(
            QCoreApplication.translate("SettingsDialog", "Style", None)
        )
        # if QT_CONFIG(tooltip)
        self.styleBox.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog", "Visual theme of the user interface.", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.styleBox.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog", "Visual theme of the user interface.", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.exploreStyles.setText(
            QCoreApplication.translate("SettingsDialog", "Explore...", None)
        )
        self.ModlistGroupBox.setTitle(
            QCoreApplication.translate("SettingsDialog", "Colors", None)
        )
        # if QT_CONFIG(tooltip)
        self.resetColorsBtn.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog", "Reset all colors to their default value.", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.resetColorsBtn.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog", "Reset all colors to their default value.", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.resetColorsBtn.setText(
            QCoreApplication.translate("SettingsDialog", "Reset Colors", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            QCoreApplication.translate("SettingsDialog", "Theme", None),
        )
        # if QT_CONFIG(accessibility)
        self.uiTab.setAccessibleName("")
        # endif // QT_CONFIG(accessibility)
        # if QT_CONFIG(tooltip)
        self.colorSeparatorsBox.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog",
                "Colors set on separators will also be shown in the mod list scrollbar at the location of the separator. This can be useful for quickly navigating to a specific separator.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.colorSeparatorsBox.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog",
                "Colors set on separators will also be shown in the mod list scrollbar at the location of the separator. This can be useful for quickly navigating to a specific separator.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.colorSeparatorsBox.setText(
            QCoreApplication.translate(
                "SettingsDialog",
                "Show mod list separator colors on the scrollbar",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.displayForeignBox.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog",
                "Disable this to no longer display mods installed outside MO in the mod list (left pane). Assets from those mods will then be treated as having lowest mod priority together with the original game content.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.displayForeignBox.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog",
                "By default Mod Organizer will display esp+bsa bundles installed with foreign tools as mods (left pane). This allows you to control their priority in relation to other mods. This is particularly useful if you also use Steam Workshop to install mods.\n"
                "However, if you installed loose file mods outside MO which conflict with BSAs also installed outside MO those conflicts can't be resolved correctly.\n"
                "\n"
                "If you disable this feature, MO will only display official DLCs this way. Please note that plugins (esps, esms, and esls) displayed in the right pane are completely unaffected by this feature.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.displayForeignBox.setText(
            QCoreApplication.translate(
                "SettingsDialog", "Display mods installed outside MO", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.saveFiltersBox.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog",
                "Save the current filters when closing MO2 and restore them on startup.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.saveFiltersBox.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog",
                "Save the current filters when closing MO2 and restore them on startup.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.saveFiltersBox.setText(
            QCoreApplication.translate(
                "SettingsDialog", "Remember selected filters after restarting MO", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.checkUpdateInstallBox.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog",
                "Check if updates are available for mods after installing them.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.checkUpdateInstallBox.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog",
                "Check if updates are available for mods after installing them.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.checkUpdateInstallBox.setText(
            QCoreApplication.translate(
                "SettingsDialog", "Check for updates when installing mods", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.autoCollapseDelayBox.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog",
                "Automatically collapse separators, categories or nexus ids after a delay when hovering them during drag.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.autoCollapseDelayBox.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog",
                "Automatically collapse separators, categories or nexus ids after a delay when hovering them during drag.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.autoCollapseDelayBox.setText(
            QCoreApplication.translate(
                "SettingsDialog",
                "Automatically collapse items during drag on hover",
                None,
            )
        )
        self.collapsibleSeparatorsWidget.setTitle(
            QCoreApplication.translate("SettingsDialog", "Collapsible Separators", None)
        )
        # if QT_CONFIG(tooltip)
        self.collapsibleSeparatorsHighlightToBox.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog",
                "Highlight collapsed separators based on conflicts and plugins from mods inside them.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.collapsibleSeparatorsHighlightToBox.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog",
                "Highlight collapsed separators based on conflicts and plugins from mods inside them.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.collapsibleSeparatorsHighlightToBox.setText(
            QCoreApplication.translate("SettingsDialog", "on separators", None)
        )
        self.collapsibleSeparatorsLabel.setText(
            QCoreApplication.translate("SettingsDialog", "Enable when sorting by", None)
        )
        self.label_34.setText(
            QCoreApplication.translate(
                "SettingsDialog", "Show conflicts and plugins ", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.collapsibleSeparatorsHighlightFromBox.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog",
                "When selecting a collapsed separator, highlight conflicting mods and plugins from mods inside the separator.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.collapsibleSeparatorsHighlightFromBox.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog",
                "When selecting a collapsed separator, highlight conflicting mods and plugins from mods inside the separator.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.collapsibleSeparatorsHighlightFromBox.setText(
            QCoreApplication.translate("SettingsDialog", "from separators", None)
        )
        self.collapsibleSeparatorsAscBox.setText(
            QCoreApplication.translate("SettingsDialog", "ascending priority", None)
        )
        self.collapsibleSeparatorsDscBox.setText(
            QCoreApplication.translate("SettingsDialog", "descending  priority", None)
        )
        self.label_35.setText(
            QCoreApplication.translate(
                "SettingsDialog", "Show icons on separators", None
            )
        )
        self.collapsibleSeparatorsIconsConflictsBox.setText(
            QCoreApplication.translate("SettingsDialog", "conflicts", None)
        )
        self.collapsibleSeparatorsIconsFlagsBox.setText(
            QCoreApplication.translate("SettingsDialog", "flags", None)
        )
        self.collapsibleSeparatorsIconsContentsBox.setText(
            QCoreApplication.translate("SettingsDialog", "content", None)
        )
        self.collapsibleSeparatorsIconsVersionBox.setText(
            QCoreApplication.translate("SettingsDialog", "version", None)
        )
        # if QT_CONFIG(tooltip)
        self.collapsibleSeparatorsPerProfileBox.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog",
                "Do not share the collapse/expanded state of separators between profiles.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.collapsibleSeparatorsPerProfileBox.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog",
                "Do not share the collapse/expanded state of separators between profiles.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.collapsibleSeparatorsPerProfileBox.setText(
            QCoreApplication.translate(
                "SettingsDialog",
                "Profile-specific collapse states for separators",
                None,
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.uiTab),
            QCoreApplication.translate("SettingsDialog", "Mod List", None),
        )
        self.browseOverwriteDirBtn.setText(
            QCoreApplication.translate("SettingsDialog", "...", None)
        )
        self.browseBaseDirBtn.setText(
            QCoreApplication.translate("SettingsDialog", "...", None)
        )
        self.label_9.setText(
            QCoreApplication.translate("SettingsDialog", "Caches", None)
        )
        self.label_24.setText(
            QCoreApplication.translate("SettingsDialog", "Overwrite", None)
        )
        # if QT_CONFIG(tooltip)
        self.downloadDirEdit.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog", "Directory where downloads are stored.", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.downloadDirEdit.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog", "Directory where downloads are stored.", None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.label_7.setText(
            QCoreApplication.translate("SettingsDialog", "Downloads", None)
        )
        self.label_22.setText(
            QCoreApplication.translate("SettingsDialog", "Profiles", None)
        )
        # if QT_CONFIG(tooltip)
        self.modDirEdit.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog", "Directory where mods are stored.", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.modDirEdit.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog",
                "Directory where mods are stored. Please note that changing this will break all associations of profiles with mods that don't exist in the new location (with the same name).",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.browseProfilesDirBtn.setText(
            QCoreApplication.translate("SettingsDialog", "...", None)
        )
        self.label_8.setText(QCoreApplication.translate("SettingsDialog", "Mods", None))
        self.label_29.setText(
            QCoreApplication.translate("SettingsDialog", "Managed Game", None)
        )
        self.label_25.setText(
            QCoreApplication.translate("SettingsDialog", "Base Directory", None)
        )
        self.label_26.setText(
            QCoreApplication.translate(
                "SettingsDialog", "Use %BASE_DIR% to refer to the Base Directory.", None
            )
        )
        self.browseGameDirBtn.setText(
            QCoreApplication.translate("SettingsDialog", "...", None)
        )
        self.label_23.setText(
            QCoreApplication.translate(
                "SettingsDialog", " All directories must be writable.", None
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.pathsTab),
            QCoreApplication.translate("SettingsDialog", "Paths", None),
        )
        self.groupBox_2.setTitle(
            QCoreApplication.translate("SettingsDialog", "Nexus Account", None)
        )
        self.label_2.setText(
            QCoreApplication.translate("SettingsDialog", "User ID:", None)
        )
        self.label_3.setText(
            QCoreApplication.translate("SettingsDialog", "Name:", None)
        )
        self.label_11.setText(
            QCoreApplication.translate("SettingsDialog", "Account:", None)
        )
        self.groupBox_3.setTitle(
            QCoreApplication.translate("SettingsDialog", "Statistics", None)
        )
        self.label_30.setText(
            QCoreApplication.translate("SettingsDialog", "Daily requests:", None)
        )
        self.label_31.setText(
            QCoreApplication.translate("SettingsDialog", "Hourly requests:", None)
        )
        self.nexusBox.setTitle(
            QCoreApplication.translate("SettingsDialog", "Nexus Connection", None)
        )
        self.nexusConnect.setText(
            QCoreApplication.translate("SettingsDialog", "Connect to Nexus", None)
        )
        # if QT_CONFIG(tooltip)
        self.nexusManualKey.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog", "Manually enter the API key and try to login", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.nexusManualKey.setText(
            QCoreApplication.translate("SettingsDialog", "Enter API Key Manually", None)
        )
        # if QT_CONFIG(tooltip)
        self.nexusDisconnect.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog",
                "Clear the stored Nexus API key and force reauthorization.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.nexusDisconnect.setText(
            QCoreApplication.translate("SettingsDialog", "Disconnect from Nexus", None)
        )
        self.settingsBox.setTitle(
            QCoreApplication.translate("SettingsDialog", "Options", None)
        )
        self.endorsementBox.setText(
            QCoreApplication.translate(
                "SettingsDialog", "Endorsement Integration", None
            )
        )
        self.trackedBox.setText(
            QCoreApplication.translate("SettingsDialog", "Tracked Integration", None)
        )
        self.categoryMappingsBox.setText(
            QCoreApplication.translate(
                "SettingsDialog", "Use Nexus category mappings", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.hideAPICounterBox.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog",
                "<html><head/><body><p>By default, a counter is displayed in the bottom right corner.  This informs the user of their remaining API requests.  The Nexus API becomes unusable once these API requests run out.  Checking this option will hide that counter.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.hideAPICounterBox.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog",
                "<html><head/><body><p>By default, a counter is displayed in the bottom right corner.  This informs the user of their remaining API requests.  The Nexus API becomes unusable once these API requests run out.  Checking this option will hide that counter.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.hideAPICounterBox.setText(
            QCoreApplication.translate(
                "SettingsDialog", "Hide API Request Counter", None
            )
        )
        self.associateButton.setText(
            QCoreApplication.translate(
                "SettingsDialog", 'Associate with "Download with manager" links', None
            )
        )
        # if QT_CONFIG(tooltip)
        self.clearCacheButton.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog", "Remove cache and cookies.", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.clearCacheButton.setText(
            QCoreApplication.translate("SettingsDialog", "Clear Cache", None)
        )
        self.serversBox.setTitle(
            QCoreApplication.translate("SettingsDialog", "Servers", None)
        )
        self.label_18.setText(
            QCoreApplication.translate(
                "SettingsDialog", "Known Servers (updated on download)", None
            )
        )
        self.label_21.setText(
            QCoreApplication.translate(
                "SettingsDialog", "Preferred Servers (Drag & Drop)", None
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.nexusTab),
            QCoreApplication.translate("SettingsDialog", "Nexus", None),
        )
        self.pluginFilterEdit.setPlaceholderText("")
        self.label_13.setText(
            QCoreApplication.translate("SettingsDialog", "Author:", None)
        )
        self.authorLabel.setText("")
        self.label_15.setText(
            QCoreApplication.translate("SettingsDialog", "Version:", None)
        )
        self.versionLabel.setText("")
        self.label_14.setText(
            QCoreApplication.translate("SettingsDialog", "Description:", None)
        )
        self.descriptionLabel.setText("")
        self.enabledCheckbox.setText(
            QCoreApplication.translate("SettingsDialog", "Enabled", None)
        )
        ___qtreewidgetitem = self.pluginSettingsList.headerItem()
        ___qtreewidgetitem.setText(
            1, QCoreApplication.translate("SettingsDialog", "Value", None)
        )
        ___qtreewidgetitem.setText(
            0, QCoreApplication.translate("SettingsDialog", "Key", None)
        )
        self.noPluginLabel.setText(
            QCoreApplication.translate("SettingsDialog", "No plugin found.", None)
        )
        self.verticalGroupBox.setTitle(
            QCoreApplication.translate(
                "SettingsDialog", "Blacklisted Plugins (use <del> to remove):", None
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.pluginsTab),
            QCoreApplication.translate("SettingsDialog", "Plugins", None),
        )
        self.workaroundsOptionsBox.setTitle(
            QCoreApplication.translate("SettingsDialog", "Options", None)
        )
        # if QT_CONFIG(tooltip)
        self.forceEnableBox.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog",
                "If checked, files (i.e. esps, esms and bsas) belonging to the core game can not be disabled in the UI. (default: on)",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.forceEnableBox.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog",
                "If checked, files (i.e. esps, esms and bsas) belonging to the core game can not be disabled in the UI. (default: on)\n"
                "Uncheck this if you want to use Mod Organizer with total conversions (like Nehrim) but be aware that the game will crash if required files are not enabled.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.forceEnableBox.setText(
            QCoreApplication.translate(
                "SettingsDialog", "Force-enable game files", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.enableArchiveParsingBox.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog",
                "Enable parsing of Archives. This is an Experimental Feature. Has negative effects on performance and known incorrectness.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.enableArchiveParsingBox.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog",
                "<html><head/><body><p>By default, MO will parse archive files (BSA, BA2) to calculate conflicts between the contents of the archive files and other loose files. This process has a noticeable cost in performance.</p><p>This feature should not be confused with the archive management feature offered by MO1. MO2 will only show conflicts with archives and will NOT load them into the game or program.</p><p>If you disable this feature, MO will only display conflicts between loose files.</p></body></html>",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.enableArchiveParsingBox.setText(
            QCoreApplication.translate(
                "SettingsDialog", "Enable archives parsing (experimental)", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.lockGUIBox.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog",
                "Disable this to prevent the GUI from being locked when running an executable.  This may result in abnormal behavior.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.lockGUIBox.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog",
                "Disable this to prevent the GUI from being locked when running an executable.  This may result in abnormal behavior.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.lockGUIBox.setText(
            QCoreApplication.translate(
                "SettingsDialog", "Lock GUI when running executable", None
            )
        )
        self.groupBox_12.setTitle(
            QCoreApplication.translate("SettingsDialog", "Steam", None)
        )
        self.label_20.setText(
            QCoreApplication.translate("SettingsDialog", "Password", None)
        )
        self.label_19.setText(
            QCoreApplication.translate("SettingsDialog", "Username", None)
        )
        self.label_4.setText(
            QCoreApplication.translate("SettingsDialog", "Steam App ID", None)
        )
        # if QT_CONFIG(tooltip)
        self.appIDEdit.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog", "The Steam AppID for your game", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.appIDEdit.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">The Steam App ID is required to directly start some games. For Skyrim, if this is not set or wrong, the &quot;Mod Organizer&quot; load mechanism may not work properly.</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">The preset for this is the App ID of the &quot;regular&quot; version so in most cases, you should be set.</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-'
                'right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">If you think you have a different version (GotY or something), follow these steps to get to the id:</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">1. Navigate to the game library in steam</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">2. right-click on the game you need the id for and choose </span><span style=" font-size:8pt; font-weight:600;">Create desktop shortcut</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">3. right-click on the newly created shortcut on your desktop and select </span><span style=" font-size:8pt; font-weight:600;">Properties</span></p>\n'
                "<p sty"
                'le=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">4. in the URL-field you should see something like this: </span><span style=" font-size:8pt; font-style:italic;">steam://rungameid/22380</span></p>\n'
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:8pt;">22380 is the id you\'re looking for.</span></p></body></html>',
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.groupBox.setTitle(
            QCoreApplication.translate("SettingsDialog", "Network", None)
        )
        # if QT_CONFIG(statustip)
        self.offlineBox.setStatusTip(
            QCoreApplication.translate(
                "SettingsDialog", "Disable automatic internet features", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.offlineBox.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog",
                "Disable automatic internet features. This does not affect features that are explicitly invoked by the user (like checking mods for updates, endorsing, opening the web browser)",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.offlineBox.setText(
            QCoreApplication.translate("SettingsDialog", "Offline Mode", None)
        )
        # if QT_CONFIG(statustip)
        self.proxyBox.setStatusTip(
            QCoreApplication.translate(
                "SettingsDialog", "Use a proxy for network connections.", None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.proxyBox.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog",
                "Use a proxy for network connections. This uses the system-wide settings which can be configured in Internet Explorer. Please note that MO will start up a few seconds slower on some systems when using a proxy.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.proxyBox.setText(
            QCoreApplication.translate("SettingsDialog", "Use System HTTP Proxy", None)
        )
        # if QT_CONFIG(tooltip)
        self.useCustomBrowser.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog", 'Use "%1" as a placeholder for the URL.', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.useCustomBrowser.setStatusTip(
            QCoreApplication.translate(
                "SettingsDialog", 'Use "%1" as a placeholder for the URL.', None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.useCustomBrowser.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog", 'Use "%1" as a placeholder for the URL.', None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.useCustomBrowser.setText(
            QCoreApplication.translate("SettingsDialog", "Custom browser", None)
        )
        # if QT_CONFIG(tooltip)
        self.browserCommand.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog", 'Use "%1" as a placeholder for the URL.', None
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(statustip)
        self.browserCommand.setStatusTip(
            QCoreApplication.translate(
                "SettingsDialog", 'Use "%1" as a placeholder for the URL.', None
            )
        )
        # endif // QT_CONFIG(statustip)
        # if QT_CONFIG(whatsthis)
        self.browserCommand.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog", 'Use "%1" as a placeholder for the URL.', None
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.browseCustomBrowser.setText(
            QCoreApplication.translate("SettingsDialog", "...", None)
        )
        # if QT_CONFIG(tooltip)
        self.resetGeometryBtn.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog",
                "Resets the window geometries for all windows.  This can be useful if a window becomes too small or too large, if a column becomes too thin or too wide, and in similar situations.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.resetGeometryBtn.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog",
                "Resets the window geometries for all windows.  This can be useful if a window becomes too small or too large, if a column becomes too thin or too wide, and in similar situations.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.resetGeometryBtn.setText(
            QCoreApplication.translate(
                "SettingsDialog", "Reset Window Geometries", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.execBlacklistBtn.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog",
                "Add executables to the blacklist to prevent them from\n"
                "accessing the virtual file system. This is useful to prevent\n"
                "unintended programs from being hooked. Hooking unintended\n"
                "programs may affect the execution of these programs or the\n"
                "programs you are intentionally running.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.execBlacklistBtn.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog",
                "Add executables to the blacklist to prevent them from accessing the virtual file system.  This is useful to prevent unintended programs from being hooked.  Hooking unintended programs may affect the execution of these programs or the programs you are intentionally running.",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.execBlacklistBtn.setText(
            QCoreApplication.translate("SettingsDialog", "Executables Blacklist", None)
        )
        # if QT_CONFIG(tooltip)
        self.bsaDateBtn.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog",
                "For Skyrim, this can be used instead of Archive Invalidation. It should make AI redundant for all Profiles.\n"
                "For the other games this is not a sufficient replacement for AI!",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.bsaDateBtn.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog",
                "For Skyrim, this can be used instead of Archive Invalidation. It should make AI redundant for all Profiles.\n"
                "For the other games this is not a sufficient replacement for AI!",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.bsaDateBtn.setText(
            QCoreApplication.translate("SettingsDialog", "Back-date BSAs", None)
        )
        self.label_6.setText(
            QCoreApplication.translate(
                "SettingsDialog",
                "These are workarounds for problems with Mod Organizer. Please make sure you read the help text before changing anything here.",
                None,
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.workaroundTab),
            QCoreApplication.translate("SettingsDialog", "Workarounds", None),
        )
        self.groupBox_4.setTitle(
            QCoreApplication.translate("SettingsDialog", "Logs and Crashes", None)
        )
        self.label_12.setText(
            QCoreApplication.translate("SettingsDialog", "Log Level", None)
        )
        # if QT_CONFIG(tooltip)
        self.logLevelBox.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog",
                'Decides the amount of data printed to "ModOrganizer.log"',
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.logLevelBox.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog",
                "\n"
                '                                    Decides the amount of data printed to "ModOrganizer.log".\n'
                '                                    "Debug" produces very useful information for finding problems. There is usually no noteworthy performance impact but the file may become rather large. If this is a problem you may prefer the "Info" level for regular use. On the "Error" level the log file usually remains empty.\n'
                "                                ",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.label_27.setText(
            QCoreApplication.translate("SettingsDialog", "Crash Dumps", None)
        )
        # if QT_CONFIG(tooltip)
        self.dumpsTypeBox.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog",
                "Decides which type of crash dumps are collected when injected processes crash.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.dumpsTypeBox.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog",
                "\n"
                "                                    Decides which type of crash dumps are collected when injected processes crash.\n"
                '                                    "None" Disables the generation of crash dumps by MO.\n'
                '                                    "Mini" Default level which generates small dumps (only stack traces).\n'
                '                                    "Data" Much larger dumps with additional information which may be need (also data segments).\n'
                '                                    "Full" Even larger dumps with a full memory dump of the process.\n'
                "                                ",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.label_28.setText(
            QCoreApplication.translate("SettingsDialog", "Max Dumps To Keep", None)
        )
        # if QT_CONFIG(tooltip)
        self.dumpsMaxEdit.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog",
                "Maximum number of crash dumps to keep on disk. Use 0 for unlimited.",
                None,
            )
        )
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.dumpsMaxEdit.setWhatsThis(
            QCoreApplication.translate(
                "SettingsDialog",
                "\n"
                "                                    Maximum number of crash dumps to keep on disk. Use 0 for unlimited.\n"
                '                                    Set "Crash Dumps" above to None to disable crash dump collection.\n'
                "                                ",
                None,
            )
        )
        # endif // QT_CONFIG(whatsthis)
        self.groupBox_7.setTitle(
            QCoreApplication.translate("SettingsDialog", "Integrated LOOT", None)
        )
        self.label_32.setText(
            QCoreApplication.translate("SettingsDialog", "LOOT Log Level", None)
        )
        # if QT_CONFIG(tooltip)
        self.diagnosticsExplainedLabel.setToolTip(
            QCoreApplication.translate(
                "SettingsDialog", "Click a link to open the location", None
            )
        )
        # endif // QT_CONFIG(tooltip)
        self.diagnosticsExplainedLabel.setText(
            QCoreApplication.translate(
                "SettingsDialog",
                "\n"
                '                            Logs and crash dumps are stored under your current instance in the <a href="LOGS_FULL_PATH">LOGS_DIR</a>\n'
                '                            and <a href="DUMPS_FULL_PATH">DUMPS_DIR</a> folders.\n'
                "                            Sending logs and/or crash dumps to the developers can help investigate issues.\n"
                "                            It is recommended to compress large log and dmp files before sending.\n"
                "                        ",
                None,
            )
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.diagnosticsTab),
            QCoreApplication.translate("SettingsDialog", "Diagnostics", None),
        )

    # retranslateUi
