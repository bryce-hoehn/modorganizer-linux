# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'createinstancedialog.ui'
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
    QApplication,
    QCheckBox,
    QCommandLinkButton,
    QDialog,
    QDialogButtonBox,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QTextEdit,
    QToolButton,
    QVBoxLayout,
    QWidget,
)

from linklabel import LinkLabel
import resources_rc


class Ui_CreateInstanceDialog(object):
    def setupUi(self, CreateInstanceDialog):
        if not CreateInstanceDialog.objectName():
            CreateInstanceDialog.setObjectName("CreateInstanceDialog")
        CreateInstanceDialog.resize(493, 444)
        self.verticalLayout = QVBoxLayout(CreateInstanceDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QWidget(CreateInstanceDialog)
        self.widget.setObjectName("widget")
        self.verticalLayout_15 = QVBoxLayout(self.widget)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.widget)
        self.title.setObjectName("title")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.title.setFont(font)

        self.verticalLayout_15.addWidget(self.title)

        self.verticalSpacer_5 = QSpacerItem(
            20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed
        )

        self.verticalLayout_15.addItem(self.verticalSpacer_5)

        self.verticalLayout.addWidget(self.widget)

        self.pages = QStackedWidget(CreateInstanceDialog)
        self.pages.setObjectName("pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName("page_1")
        self.verticalLayout_21 = QVBoxLayout(self.page_1)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_15 = QLabel(self.page_1)
        self.label_15.setObjectName("label_15")
        self.label_15.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.label_15.setWordWrap(True)

        self.verticalLayout_21.addWidget(self.label_15)

        self.label_19 = LinkLabel(self.page_1)
        self.label_19.setObjectName("label_19")
        self.label_19.setOpenExternalLinks(True)

        self.verticalLayout_21.addWidget(self.label_19)

        self.verticalSpacer_6 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_21.addItem(self.verticalSpacer_6)

        self.hideIntro = QCheckBox(self.page_1)
        self.hideIntro.setObjectName("hideIntro")

        self.verticalLayout_21.addWidget(self.hideIntro)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_3 = QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_7 = QWidget(self.page_2)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_6 = QVBoxLayout(self.widget_7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_7)
        self.label_2.setObjectName("label_2")

        self.verticalLayout_6.addWidget(self.label_2)

        self.verticalLayout_3.addWidget(self.widget_7)

        self.widget_3 = QWidget(self.page_2)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_15 = QWidget(self.widget_3)
        self.widget_15.setObjectName("widget_15")
        self.verticalLayout_16 = QVBoxLayout(self.widget_15)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, 0, 0, 0)
        self.createGlobal = QCommandLinkButton(self.widget_15)
        self.createGlobal.setObjectName("createGlobal")
        self.createGlobal.setCheckable(True)

        self.verticalLayout_16.addWidget(self.createGlobal)

        self.createPortable = QCommandLinkButton(self.widget_15)
        self.createPortable.setObjectName("createPortable")
        self.createPortable.setCheckable(True)

        self.verticalLayout_16.addWidget(self.createPortable)

        self.verticalLayout_2.addWidget(self.widget_15)

        self.portableExistsLabel = QLabel(self.widget_3)
        self.portableExistsLabel.setObjectName("portableExistsLabel")
        self.portableExistsLabel.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter
        )

        self.verticalLayout_2.addWidget(self.portableExistsLabel)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout_3.addWidget(self.widget_3)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_7 = QVBoxLayout(self.page_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_5 = QWidget(self.page_3)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName("label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.verticalLayout_7.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.page_3)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_25 = QVBoxLayout(self.widget_6)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.widget_23 = QWidget(self.widget_6)
        self.widget_23.setObjectName("widget_23")
        self.verticalLayout_5 = QVBoxLayout(self.widget_23)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.widget_23)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.games = QWidget()
        self.games.setObjectName("games")
        self.games.setGeometry(QRect(0, 0, 455, 275))
        self.verticalLayout_26 = QVBoxLayout(self.games)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3.setWidget(self.games)

        self.verticalLayout_5.addWidget(self.scrollArea_3)

        self.verticalLayout_25.addWidget(self.widget_23)

        self.widget_21 = QWidget(self.widget_6)
        self.widget_21.setObjectName("widget_21")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.showAllGames = QCheckBox(self.widget_21)
        self.showAllGames.setObjectName("showAllGames")

        self.horizontalLayout_6.addWidget(self.showAllGames)

        self.horizontalSpacer_5 = QSpacerItem(
            175, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.gamesFilter = QLineEdit(self.widget_21)
        self.gamesFilter.setObjectName("gamesFilter")

        self.horizontalLayout_6.addWidget(self.gamesFilter)

        self.verticalLayout_25.addWidget(self.widget_21)

        self.verticalLayout_7.addWidget(self.widget_6)

        self.pages.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_19 = QVBoxLayout(self.page_4)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.widget_16 = QWidget(self.page_4)
        self.widget_16.setObjectName("widget_16")
        self.verticalLayout_18 = QVBoxLayout(self.widget_16)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_16)
        self.label_4.setObjectName("label_4")

        self.verticalLayout_18.addWidget(self.label_4)

        self.label_14 = QLabel(self.widget_16)
        self.label_14.setObjectName("label_14")
        self.label_14.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.label_14)

        self.verticalLayout_19.addWidget(self.widget_16)

        self.widget_17 = QWidget(self.page_4)
        self.widget_17.setObjectName("widget_17")
        self.verticalLayout_20 = QVBoxLayout(self.widget_17)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.widget_17)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 455, 265))
        self.verticalLayout_17 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.editions = QDialogButtonBox(self.scrollAreaWidgetContents)
        self.editions.setObjectName("editions")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editions.sizePolicy().hasHeightForWidth())
        self.editions.setSizePolicy(sizePolicy)
        self.editions.setOrientation(Qt.Vertical)
        self.editions.setStandardButtons(QDialogButtonBox.NoButton)

        self.verticalLayout_17.addWidget(self.editions)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_20.addWidget(self.scrollArea_2)

        self.verticalLayout_19.addWidget(self.widget_17)

        self.pages.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_9 = QVBoxLayout(self.page_5)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget_8 = QWidget(self.page_5)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.instanceNameLabel = QLabel(self.widget_8)
        self.instanceNameLabel.setObjectName("instanceNameLabel")
        self.instanceNameLabel.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.instanceNameLabel)

        self.verticalLayout_9.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.page_5)
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_8 = QVBoxLayout(self.widget_9)
        self.verticalLayout_8.setSpacing(9)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.instanceName = QLineEdit(self.widget_9)
        self.instanceName.setObjectName("instanceName")

        self.verticalLayout_8.addWidget(self.instanceName)

        self.instanceNameExists = QLabel(self.widget_9)
        self.instanceNameExists.setObjectName("instanceNameExists")

        self.verticalLayout_8.addWidget(self.instanceNameExists)

        self.instanceNameInvalid = QLabel(self.widget_9)
        self.instanceNameInvalid.setObjectName("instanceNameInvalid")

        self.verticalLayout_8.addWidget(self.instanceNameInvalid)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.verticalLayout_9.addWidget(self.widget_9)

        self.pages.addWidget(self.page_5)
        self.page = QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_31 = QVBoxLayout(self.page)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.widget_24 = QWidget(self.page)
        self.widget_24.setObjectName("widget_24")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.profileSettingsLabel = QLabel(self.widget_24)
        self.profileSettingsLabel.setObjectName("profileSettingsLabel")
        self.profileSettingsLabel.setWordWrap(True)

        self.horizontalLayout_8.addWidget(self.profileSettingsLabel)

        self.verticalLayout_31.addWidget(self.widget_24)

        self.widget_25 = QWidget(self.page)
        self.widget_25.setObjectName("widget_25")
        self.verticalLayout_28 = QVBoxLayout(self.widget_25)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.profileInisCheckbox = QCheckBox(self.widget_25)
        self.profileInisCheckbox.setObjectName("profileInisCheckbox")

        self.verticalLayout_28.addWidget(self.profileInisCheckbox)

        self.profileSavesCheckbox = QCheckBox(self.widget_25)
        self.profileSavesCheckbox.setObjectName("profileSavesCheckbox")

        self.verticalLayout_28.addWidget(self.profileSavesCheckbox)

        self.archiveInvalidationCheckbox = QCheckBox(self.widget_25)
        self.archiveInvalidationCheckbox.setObjectName("archiveInvalidationCheckbox")
        self.archiveInvalidationCheckbox.setChecked(True)

        self.verticalLayout_28.addWidget(self.archiveInvalidationCheckbox)

        self.verticalSpacer_7 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_28.addItem(self.verticalSpacer_7)

        self.verticalLayout_31.addWidget(self.widget_25)

        self.pages.addWidget(self.page)
        self.page_6 = QWidget()
        self.page_6.setObjectName("page_6")
        self.verticalLayout_14 = QVBoxLayout(self.page_6)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.widget_10 = QWidget(self.page_6)
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_10 = QVBoxLayout(self.widget_10)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget_10)
        self.label_5.setObjectName("label_5")
        self.label_5.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.label_5)

        self.pathsLabel = QLabel(self.widget_10)
        self.pathsLabel.setObjectName("pathsLabel")
        self.pathsLabel.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.pathsLabel)

        self.verticalLayout_14.addWidget(self.widget_10)

        self.widget_13 = QWidget(self.page_6)
        self.widget_13.setObjectName("widget_13")
        self.verticalLayout_11 = QVBoxLayout(self.widget_13)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.pathPages = QStackedWidget(self.widget_13)
        self.pathPages.setObjectName("pathPages")
        self.page_6_simple = QWidget()
        self.page_6_simple.setObjectName("page_6_simple")
        self.verticalLayout_12 = QVBoxLayout(self.page_6_simple)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.page_6_simple)
        self.widget_11.setObjectName("widget_11")
        self.gridLayout = QGridLayout(self.widget_11)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.browseLocation = QToolButton(self.widget_11)
        self.browseLocation.setObjectName("browseLocation")

        self.gridLayout.addWidget(self.browseLocation, 0, 2, 1, 1)

        self.label_6 = QLabel(self.widget_11)
        self.label_6.setObjectName("label_6")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.gridLayout.addItem(self.verticalSpacer_3, 3, 0, 1, 1)

        self.locationExists = QLabel(self.widget_11)
        self.locationExists.setObjectName("locationExists")

        self.gridLayout.addWidget(self.locationExists, 2, 0, 1, 3)

        self.location = QLineEdit(self.widget_11)
        self.location.setObjectName("location")

        self.gridLayout.addWidget(self.location, 0, 1, 1, 1)

        self.locationInvalid = QLabel(self.widget_11)
        self.locationInvalid.setObjectName("locationInvalid")

        self.gridLayout.addWidget(self.locationInvalid, 1, 0, 1, 3)

        self.verticalLayout_12.addWidget(self.widget_11)

        self.pathPages.addWidget(self.page_6_simple)
        self.page_6_advanced = QWidget()
        self.page_6_advanced.setObjectName("page_6_advanced")
        self.verticalLayout_13 = QVBoxLayout(self.page_6_advanced)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.widget_12 = QWidget(self.page_6_advanced)
        self.widget_12.setObjectName("widget_12")
        self.gridLayout_2 = QGridLayout(self.widget_12)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.browseOverwrite = QToolButton(self.widget_12)
        self.browseOverwrite.setObjectName("browseOverwrite")

        self.gridLayout_2.addWidget(self.browseOverwrite, 4, 3, 1, 1)

        self.browseMods = QToolButton(self.widget_12)
        self.browseMods.setObjectName("browseMods")

        self.gridLayout_2.addWidget(self.browseMods, 2, 3, 1, 1)

        self.label_10 = QLabel(self.widget_12)
        self.label_10.setObjectName("label_10")

        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)

        self.overwrite = QLineEdit(self.widget_12)
        self.overwrite.setObjectName("overwrite")

        self.gridLayout_2.addWidget(self.overwrite, 4, 2, 1, 1)

        self.mods = QLineEdit(self.widget_12)
        self.mods.setObjectName("mods")

        self.gridLayout_2.addWidget(self.mods, 2, 2, 1, 1)

        self.label_13 = QLabel(self.widget_12)
        self.label_13.setObjectName("label_13")

        self.gridLayout_2.addWidget(self.label_13, 4, 0, 1, 1)

        self.label_8 = QLabel(self.widget_12)
        self.label_8.setObjectName("label_8")

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)

        self.browseDownloads = QToolButton(self.widget_12)
        self.browseDownloads.setObjectName("browseDownloads")

        self.gridLayout_2.addWidget(self.browseDownloads, 1, 3, 1, 1)

        self.profiles = QLineEdit(self.widget_12)
        self.profiles.setObjectName("profiles")

        self.gridLayout_2.addWidget(self.profiles, 3, 2, 1, 1)

        self.advancedDirExists = QLabel(self.widget_12)
        self.advancedDirExists.setObjectName("advancedDirExists")
        self.advancedDirExists.setWordWrap(True)

        self.gridLayout_2.addWidget(self.advancedDirExists, 5, 0, 1, 4)

        self.label_9 = QLabel(self.widget_12)
        self.label_9.setObjectName("label_9")

        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)

        self.downloads = QLineEdit(self.widget_12)
        self.downloads.setObjectName("downloads")

        self.gridLayout_2.addWidget(self.downloads, 1, 2, 1, 1)

        self.base = QLineEdit(self.widget_12)
        self.base.setObjectName("base")

        self.gridLayout_2.addWidget(self.base, 0, 2, 1, 1)

        self.label_12 = QLabel(self.widget_12)
        self.label_12.setObjectName("label_12")

        self.gridLayout_2.addWidget(self.label_12, 3, 0, 1, 1)

        self.label_11 = QLabel(self.widget_12)
        self.label_11.setObjectName("label_11")

        self.gridLayout_2.addWidget(self.label_11, 8, 0, 1, 4)

        self.browseBase = QToolButton(self.widget_12)
        self.browseBase.setObjectName("browseBase")

        self.gridLayout_2.addWidget(self.browseBase, 0, 3, 1, 1)

        self.browseProfiles = QToolButton(self.widget_12)
        self.browseProfiles.setObjectName("browseProfiles")

        self.gridLayout_2.addWidget(self.browseProfiles, 3, 3, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.gridLayout_2.addItem(self.verticalSpacer_4, 7, 0, 1, 1)

        self.advancedDirInvalid = QLabel(self.widget_12)
        self.advancedDirInvalid.setObjectName("advancedDirInvalid")
        self.advancedDirInvalid.setWordWrap(True)

        self.gridLayout_2.addWidget(self.advancedDirInvalid, 6, 0, 1, 4)

        self.verticalLayout_13.addWidget(self.widget_12)

        self.pathPages.addWidget(self.page_6_advanced)

        self.verticalLayout_11.addWidget(self.pathPages)

        self.widget_14 = QWidget(self.widget_13)
        self.widget_14.setObjectName("widget_14")
        self.widget_14.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(
            292, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.advancedPathOptions = QCheckBox(self.widget_14)
        self.advancedPathOptions.setObjectName("advancedPathOptions")

        self.horizontalLayout_2.addWidget(self.advancedPathOptions)

        self.verticalLayout_11.addWidget(self.widget_14)

        self.verticalLayout_14.addWidget(self.widget_13)

        self.pages.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName("page_7")
        self.verticalLayout_4 = QVBoxLayout(self.page_7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_4 = QWidget(self.page_7)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_29 = QVBoxLayout(self.widget_4)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.widget_4)
        self.label_7.setObjectName("label_7")

        self.verticalLayout_29.addWidget(self.label_7)

        self.label_18 = QLabel(self.widget_4)
        self.label_18.setObjectName("label_18")
        self.label_18.setWordWrap(True)

        self.verticalLayout_29.addWidget(self.label_18)

        self.verticalLayout_4.addWidget(self.widget_4)

        self.nexusBox = QWidget(self.page_7)
        self.nexusBox.setObjectName("nexusBox")
        self.nexusBox.setMinimumSize(QSize(0, 100))
        self.verticalLayout_30 = QVBoxLayout(self.nexusBox)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 9, 0, 0)
        self.nexusBox_2 = QWidget(self.nexusBox)
        self.nexusBox_2.setObjectName("nexusBox_2")
        self.verticalLayout_27 = QVBoxLayout(self.nexusBox_2)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.widget_22 = QWidget(self.nexusBox_2)
        self.widget_22.setObjectName("widget_22")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.nexusConnect = QPushButton(self.widget_22)
        self.nexusConnect.setObjectName("nexusConnect")

        self.horizontalLayout_7.addWidget(self.nexusConnect)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.nexusManual = QPushButton(self.widget_22)
        self.nexusManual.setObjectName("nexusManual")

        self.horizontalLayout_7.addWidget(self.nexusManual)

        self.verticalLayout_27.addWidget(self.widget_22)

        self.nexusLog = QListWidget(self.nexusBox_2)
        self.nexusLog.setObjectName("nexusLog")

        self.verticalLayout_27.addWidget(self.nexusLog)

        self.verticalLayout_30.addWidget(self.nexusBox_2)

        self.verticalSpacer_8 = QSpacerItem(
            20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding
        )

        self.verticalLayout_30.addItem(self.verticalSpacer_8)

        self.verticalLayout_4.addWidget(self.nexusBox)

        self.pages.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName("page_8")
        self.verticalLayout_22 = QVBoxLayout(self.page_8)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.widget_18 = QWidget(self.page_8)
        self.widget_18.setObjectName("widget_18")
        self.verticalLayout_24 = QVBoxLayout(self.widget_18)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.widget_18)
        self.label_16.setObjectName("label_16")

        self.verticalLayout_24.addWidget(self.label_16)

        self.label_17 = QLabel(self.widget_18)
        self.label_17.setObjectName("label_17")

        self.verticalLayout_24.addWidget(self.label_17)

        self.verticalLayout_22.addWidget(self.widget_18)

        self.widget_19 = QWidget(self.page_8)
        self.widget_19.setObjectName("widget_19")
        self.verticalLayout_23 = QVBoxLayout(self.widget_19)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.review = QTextEdit(self.widget_19)
        self.review.setObjectName("review")
        self.review.setLineWrapMode(QTextEdit.NoWrap)
        self.review.setReadOnly(True)

        self.verticalLayout_23.addWidget(self.review)

        self.creationLog = QTextEdit(self.widget_19)
        self.creationLog.setObjectName("creationLog")
        self.creationLog.setLineWrapMode(QTextEdit.NoWrap)
        self.creationLog.setTextInteractionFlags(
            Qt.TextSelectableByKeyboard | Qt.TextSelectableByMouse
        )

        self.verticalLayout_23.addWidget(self.creationLog)

        self.widget_20 = QWidget(self.widget_19)
        self.widget_20.setObjectName("widget_20")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(
            304, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.launch = QCheckBox(self.widget_20)
        self.launch.setObjectName("launch")
        self.launch.setChecked(True)

        self.horizontalLayout_5.addWidget(self.launch)

        self.verticalLayout_23.addWidget(self.widget_20)

        self.verticalLayout_22.addWidget(self.widget_19)

        self.pages.addWidget(self.page_8)

        self.verticalLayout.addWidget(self.pages)

        self.widget_2 = QWidget(CreateInstanceDialog)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.back = QPushButton(self.widget_2)
        self.back.setObjectName("back")

        self.horizontalLayout.addWidget(self.back)

        self.next = QPushButton(self.widget_2)
        self.next.setObjectName("next")

        self.horizontalLayout.addWidget(self.next)

        self.cancel = QPushButton(self.widget_2)
        self.cancel.setObjectName("cancel")

        self.horizontalLayout.addWidget(self.cancel)

        self.verticalLayout.addWidget(self.widget_2)

        QWidget.setTabOrder(self.next, self.cancel)
        QWidget.setTabOrder(self.cancel, self.hideIntro)
        QWidget.setTabOrder(self.hideIntro, self.createGlobal)
        QWidget.setTabOrder(self.createGlobal, self.createPortable)
        QWidget.setTabOrder(self.createPortable, self.scrollArea_3)
        QWidget.setTabOrder(self.scrollArea_3, self.showAllGames)
        QWidget.setTabOrder(self.showAllGames, self.gamesFilter)
        QWidget.setTabOrder(self.gamesFilter, self.scrollArea_2)
        QWidget.setTabOrder(self.scrollArea_2, self.location)
        QWidget.setTabOrder(self.location, self.browseLocation)
        QWidget.setTabOrder(self.browseLocation, self.advancedPathOptions)
        QWidget.setTabOrder(self.advancedPathOptions, self.base)
        QWidget.setTabOrder(self.base, self.browseBase)
        QWidget.setTabOrder(self.browseBase, self.downloads)
        QWidget.setTabOrder(self.downloads, self.browseDownloads)
        QWidget.setTabOrder(self.browseDownloads, self.mods)
        QWidget.setTabOrder(self.mods, self.browseMods)
        QWidget.setTabOrder(self.browseMods, self.profiles)
        QWidget.setTabOrder(self.profiles, self.browseProfiles)
        QWidget.setTabOrder(self.browseProfiles, self.overwrite)
        QWidget.setTabOrder(self.overwrite, self.browseOverwrite)
        QWidget.setTabOrder(self.browseOverwrite, self.nexusConnect)
        QWidget.setTabOrder(self.nexusConnect, self.nexusManual)
        QWidget.setTabOrder(self.nexusManual, self.nexusLog)
        QWidget.setTabOrder(self.nexusLog, self.review)
        QWidget.setTabOrder(self.review, self.creationLog)
        QWidget.setTabOrder(self.creationLog, self.launch)
        QWidget.setTabOrder(self.launch, self.back)

        self.retranslateUi(CreateInstanceDialog)

        self.pages.setCurrentIndex(0)
        self.pathPages.setCurrentIndex(0)
        self.next.setDefault(True)

        QMetaObject.connectSlotsByName(CreateInstanceDialog)

    # setupUi

    def retranslateUi(self, CreateInstanceDialog):
        CreateInstanceDialog.setWindowTitle(
            QCoreApplication.translate(
                "CreateInstanceDialog", "Creating an instance", None
            )
        )
        self.title.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog", "Creating a new instance", None
            )
        )
        self.label_15.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog",
                "<h3>What is an instance?</h3>\n"
                "<p>An instance is a full set of mods, downloads, profiles and configuration for a game. Each game must be managed in its own instance. Mod Organizer can freely switch between instances.</p>",
                None,
            )
        )
        self.label_19.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog",
                '<html><head/><body><p><a href="https://github.com/ModOrganizer2/modorganizer/wiki/Instances">More information</a></p></body></html>',
                None,
            )
        )
        self.hideIntro.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog", "Never show this page again", None
            )
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog",
                "<h3>Select the type of instance to create.</h3>",
                None,
            )
        )
        self.createGlobal.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog", "Create a global instance", None
            )
        )
        self.createGlobal.setDescription(
            QCoreApplication.translate(
                "CreateInstanceDialog",
                "Global instances are stored in %1, but some paths can be changed to be on a different drive if necessary. A single installation of Mod Organizer can manage multiple global instances.",
                None,
            )
        )
        self.createPortable.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog", "Create a portable instance", None
            )
        )
        self.createPortable.setDescription(
            QCoreApplication.translate(
                "CreateInstanceDialog",
                "A portable instance stores everything in Mod Organizer's installation folder, currently %1. There can only be one portable instance per installation of Mod Organizer.",
                None,
            )
        )
        self.portableExistsLabel.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog", "A portable instance already exists.", None
            )
        )
        self.label_3.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog", "<h3>Select the game to manage.</h3>", None
            )
        )
        self.showAllGames.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog", "Show all supported games", None
            )
        )
        self.gamesFilter.setPlaceholderText(
            QCoreApplication.translate("CreateInstanceDialog", "Filter", None)
        )
        self.label_4.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog", "<h3>Select the game edition.</h3>", None
            )
        )
        self.label_14.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog",
                "This game has multiple variants. The correct one must be selected or Mod Organizer will not be able to launch the game properly.",
                None,
            )
        )
        self.instanceNameLabel.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog",
                '<h3>Customize the name for this <span style="white-space: nowrap;">%1</span> instance.</h3>',
                None,
            )
        )
        self.instanceName.setPlaceholderText(
            QCoreApplication.translate("CreateInstanceDialog", "Instance name", None)
        )
        self.instanceNameExists.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog",
                "There is already an instance with this name.",
                None,
            )
        )
        self.instanceNameInvalid.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog",
                "The name contains invalid characters. It must be a valid folder name.",
                None,
            )
        )
        self.profileSettingsLabel.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog",
                "<h3>Configure your profile settings.</h3>",
                None,
            )
        )
        # if QT_CONFIG(tooltip)
        self.profileInisCheckbox.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.profileInisCheckbox.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog", "Use profile-specific game INI files", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.profileSavesCheckbox.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.profileSavesCheckbox.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog", "Use profile-specific save games", None
            )
        )
        # if QT_CONFIG(tooltip)
        self.archiveInvalidationCheckbox.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.archiveInvalidationCheckbox.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog", "Automatic archive invalidation", None
            )
        )
        self.label_5.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog",
                "<h3>Select a folder where the data should be stored.</h3>",
                None,
            )
        )
        self.pathsLabel.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog",
                "This includes downloads, mods, profiles and overwrite for your <b>%1</b> instance. If there is enough space on this drive, you should use the default folder.",
                None,
            )
        )
        self.browseLocation.setText(
            QCoreApplication.translate("CreateInstanceDialog", "...", None)
        )
        self.label_6.setText(
            QCoreApplication.translate("CreateInstanceDialog", "Location", None)
        )
        self.locationExists.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog", "Warning: This folder already exists.", None
            )
        )
        self.location.setPlaceholderText(
            QCoreApplication.translate("CreateInstanceDialog", "Folder", None)
        )
        self.locationInvalid.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog",
                "Warning: The folder contains invalid characters.",
                None,
            )
        )
        self.browseOverwrite.setText(
            QCoreApplication.translate("CreateInstanceDialog", "...", None)
        )
        self.browseMods.setText(
            QCoreApplication.translate("CreateInstanceDialog", "...", None)
        )
        self.label_10.setText(
            QCoreApplication.translate("CreateInstanceDialog", "Mods", None)
        )
        self.overwrite.setPlaceholderText(
            QCoreApplication.translate("CreateInstanceDialog", "Folder", None)
        )
        self.mods.setPlaceholderText(
            QCoreApplication.translate("CreateInstanceDialog", "Folder", None)
        )
        self.label_13.setText(
            QCoreApplication.translate("CreateInstanceDialog", "Overwrite", None)
        )
        self.label_8.setText(
            QCoreApplication.translate("CreateInstanceDialog", "Base directory", None)
        )
        self.browseDownloads.setText(
            QCoreApplication.translate("CreateInstanceDialog", "...", None)
        )
        self.profiles.setPlaceholderText(
            QCoreApplication.translate("CreateInstanceDialog", "Folder", None)
        )
        self.advancedDirExists.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog", "Warning: The folder %1 already exists.", None
            )
        )
        self.label_9.setText(
            QCoreApplication.translate("CreateInstanceDialog", "Downloads", None)
        )
        self.downloads.setPlaceholderText(
            QCoreApplication.translate("CreateInstanceDialog", "Folder", None)
        )
        self.base.setPlaceholderText(
            QCoreApplication.translate("CreateInstanceDialog", "Folder", None)
        )
        self.label_12.setText(
            QCoreApplication.translate("CreateInstanceDialog", "Profiles", None)
        )
        self.label_11.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog",
                "Use %BASE_DIR% to refer to the Base Directory.",
                None,
            )
        )
        self.browseBase.setText(
            QCoreApplication.translate("CreateInstanceDialog", "...", None)
        )
        self.browseProfiles.setText(
            QCoreApplication.translate("CreateInstanceDialog", "...", None)
        )
        self.advancedDirInvalid.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog",
                "Warning: The folder %1 contains invalid characters.",
                None,
            )
        )
        self.advancedPathOptions.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog", "Show advanced options", None
            )
        )
        self.label_7.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog",
                "<h3>Link Mod Organizer with your Nexus account</h3>",
                None,
            )
        )
        self.label_18.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog",
                "Linking with Nexus allows you to download mods directly from Mod Organizer and automatically check for updates. This is optional.",
                None,
            )
        )
        self.nexusConnect.setText(
            QCoreApplication.translate("CreateInstanceDialog", "Connect to Nexus", None)
        )
        self.nexusManual.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog", "Enter API Key Manually", None
            )
        )
        self.label_16.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog", "<h3>Confirmation</h3>", None
            )
        )
        self.label_17.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog",
                "The instance is about to be created. Review the information below and press 'Finish'.",
                None,
            )
        )
        self.creationLog.setPlaceholderText(
            QCoreApplication.translate(
                "CreateInstanceDialog", "Instance creation log", None
            )
        )
        self.launch.setText(
            QCoreApplication.translate(
                "CreateInstanceDialog", "Launch the new instance", None
            )
        )
        self.back.setText(
            QCoreApplication.translate("CreateInstanceDialog", "< Back", None)
        )
        self.next.setText(
            QCoreApplication.translate("CreateInstanceDialog", "Next >", None)
        )
        self.cancel.setText(
            QCoreApplication.translate("CreateInstanceDialog", "Cancel", None)
        )

    # retranslateUi
