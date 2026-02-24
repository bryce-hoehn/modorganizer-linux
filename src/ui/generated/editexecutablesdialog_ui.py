# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editexecutablesdialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QCheckBox,
    QComboBox, QDialog, QDialogButtonBox, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QSplitter, QToolButton, QVBoxLayout, QWidget)
import resources_rc

class Ui_EditExecutablesDialog(object):
    def setupUi(self, EditExecutablesDialog):
        if not EditExecutablesDialog.objectName():
            EditExecutablesDialog.setObjectName(u"EditExecutablesDialog")
        EditExecutablesDialog.resize(710, 440)
        self.verticalLayout = QVBoxLayout(EditExecutablesDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_3 = QWidget(EditExecutablesDialog)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(0, 100))
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.widget_3)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(9)
        self.splitter.setChildrenCollapsible(False)
        self.widget_2 = QWidget(self.splitter)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.add = QToolButton(self.widget_2)
        self.add.setObjectName(u"add")
        icon = QIcon()
        icon.addFile(u":/MO/gui/add", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add.setIcon(icon)
        self.add.setPopupMode(QToolButton.InstantPopup)

        self.horizontalLayout_2.addWidget(self.add)

        self.remove = QToolButton(self.widget_2)
        self.remove.setObjectName(u"remove")
        icon1 = QIcon()
        icon1.addFile(u":/MO/gui/resources/list-remove.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.remove.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.remove)

        self.up = QToolButton(self.widget_2)
        self.up.setObjectName(u"up")
        icon2 = QIcon()
        icon2.addFile(u":/MO/gui/resources/go-up.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.up.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.up)

        self.down = QToolButton(self.widget_2)
        self.down.setObjectName(u"down")
        icon3 = QIcon()
        icon3.addFile(u":/MO/gui/resources/go-down.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.down.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.down)

        self.reset = QToolButton(self.widget_2)
        self.reset.setObjectName(u"reset")
        icon4 = QIcon()
        icon4.addFile(u":/MO/gui/edit_clear", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.reset.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.reset)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.list = QListWidget(self.widget_2)
        self.list.setObjectName(u"list")
        self.list.setDragDropMode(QAbstractItemView.InternalMove)
        self.list.setDefaultDropAction(Qt.TargetMoveAction)

        self.verticalLayout_3.addWidget(self.list)

        self.splitter.addWidget(self.widget_2)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_5 = QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 10)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(-1, -1, -1, 20)
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.title = QLineEdit(self.widget_4)
        self.title.setObjectName(u"title")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.title)

        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.binary = QLineEdit(self.widget_4)
        self.binary.setObjectName(u"binary")

        self.horizontalLayout.addWidget(self.binary)

        self.browseBinary = QPushButton(self.widget_4)
        self.browseBinary.setObjectName(u"browseBinary")

        self.horizontalLayout.addWidget(self.browseBinary)

        self.horizontalLayout.setStretch(0, 1)

        self.formLayout.setLayout(1, QFormLayout.ItemRole.FieldRole, self.horizontalLayout)

        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.workingDirectory = QLineEdit(self.widget_4)
        self.workingDirectory.setObjectName(u"workingDirectory")

        self.horizontalLayout_6.addWidget(self.workingDirectory)

        self.browseWorkingDirectory = QPushButton(self.widget_4)
        self.browseWorkingDirectory.setObjectName(u"browseWorkingDirectory")

        self.horizontalLayout_6.addWidget(self.browseWorkingDirectory)

        self.horizontalLayout_6.setStretch(0, 1)

        self.formLayout.setLayout(2, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_6)

        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.arguments = QLineEdit(self.widget_4)
        self.arguments.setObjectName(u"arguments")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.arguments)


        self.verticalLayout_5.addLayout(self.formLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.overwriteSteamAppID = QCheckBox(self.widget_4)
        self.overwriteSteamAppID.setObjectName(u"overwriteSteamAppID")

        self.horizontalLayout_5.addWidget(self.overwriteSteamAppID)

        self.steamAppID = QLineEdit(self.widget_4)
        self.steamAppID.setObjectName(u"steamAppID")
        self.steamAppID.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.steamAppID)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.createFilesInMod = QCheckBox(self.widget_4)
        self.createFilesInMod.setObjectName(u"createFilesInMod")

        self.horizontalLayout_9.addWidget(self.createFilesInMod)

        self.mods = QComboBox(self.widget_4)
        self.mods.setObjectName(u"mods")
        self.mods.setEnabled(False)
        self.mods.setEditable(True)

        self.horizontalLayout_9.addWidget(self.mods)

        self.horizontalLayout_9.setStretch(1, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.forceLoadLibraries = QCheckBox(self.widget_4)
        self.forceLoadLibraries.setObjectName(u"forceLoadLibraries")

        self.horizontalLayout_8.addWidget(self.forceLoadLibraries)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.configureLibraries = QPushButton(self.widget_4)
        self.configureLibraries.setObjectName(u"configureLibraries")
        self.configureLibraries.setEnabled(False)

        self.horizontalLayout_8.addWidget(self.configureLibraries)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.useApplicationIcon = QCheckBox(self.widget_4)
        self.useApplicationIcon.setObjectName(u"useApplicationIcon")

        self.verticalLayout_5.addWidget(self.useApplicationIcon)

        self.hide = QCheckBox(self.widget_4)
        self.hide.setObjectName(u"hide")

        self.verticalLayout_5.addWidget(self.hide)

        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMargin(5)

        self.verticalLayout_5.addWidget(self.label_5)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.splitter.addWidget(self.widget)

        self.verticalLayout_4.addWidget(self.splitter)


        self.verticalLayout.addWidget(self.widget_3)

        self.buttons = QDialogButtonBox(EditExecutablesDialog)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttons)

        QWidget.setTabOrder(self.add, self.remove)
        QWidget.setTabOrder(self.remove, self.up)
        QWidget.setTabOrder(self.up, self.down)
        QWidget.setTabOrder(self.down, self.reset)
        QWidget.setTabOrder(self.reset, self.list)
        QWidget.setTabOrder(self.list, self.title)
        QWidget.setTabOrder(self.title, self.binary)
        QWidget.setTabOrder(self.binary, self.browseBinary)
        QWidget.setTabOrder(self.browseBinary, self.workingDirectory)
        QWidget.setTabOrder(self.workingDirectory, self.browseWorkingDirectory)
        QWidget.setTabOrder(self.browseWorkingDirectory, self.arguments)
        QWidget.setTabOrder(self.arguments, self.overwriteSteamAppID)
        QWidget.setTabOrder(self.overwriteSteamAppID, self.steamAppID)
        QWidget.setTabOrder(self.steamAppID, self.createFilesInMod)
        QWidget.setTabOrder(self.createFilesInMod, self.mods)
        QWidget.setTabOrder(self.mods, self.forceLoadLibraries)
        QWidget.setTabOrder(self.forceLoadLibraries, self.configureLibraries)
        QWidget.setTabOrder(self.configureLibraries, self.useApplicationIcon)

        self.retranslateUi(EditExecutablesDialog)

        QMetaObject.connectSlotsByName(EditExecutablesDialog)
    # setupUi

    def retranslateUi(self, EditExecutablesDialog):
        EditExecutablesDialog.setWindowTitle(QCoreApplication.translate("EditExecutablesDialog", u"Modify Executables", None))
        self.label_6.setText(QCoreApplication.translate("EditExecutablesDialog", u"Executables", None))
#if QT_CONFIG(tooltip)
        self.add.setToolTip(QCoreApplication.translate("EditExecutablesDialog", u"Add an executable", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.add.setStatusTip(QCoreApplication.translate("EditExecutablesDialog", u"Add an executable", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.add.setWhatsThis(QCoreApplication.translate("EditExecutablesDialog", u"Add an executable", None))
#endif // QT_CONFIG(whatsthis)
        self.add.setText(QCoreApplication.translate("EditExecutablesDialog", u"Add", None))
#if QT_CONFIG(tooltip)
        self.remove.setToolTip(QCoreApplication.translate("EditExecutablesDialog", u"Remove the selected executable", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.remove.setStatusTip(QCoreApplication.translate("EditExecutablesDialog", u"Remove the selected executable", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.remove.setWhatsThis(QCoreApplication.translate("EditExecutablesDialog", u"Remove the selected executable", None))
#endif // QT_CONFIG(whatsthis)
        self.remove.setText(QCoreApplication.translate("EditExecutablesDialog", u"Remove", None))
#if QT_CONFIG(tooltip)
        self.up.setToolTip(QCoreApplication.translate("EditExecutablesDialog", u"Move the executable up in the list", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.up.setStatusTip(QCoreApplication.translate("EditExecutablesDialog", u"Move the executable up in the list", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.up.setWhatsThis(QCoreApplication.translate("EditExecutablesDialog", u"Move the executable up in the list", None))
#endif // QT_CONFIG(whatsthis)
        self.up.setText(QCoreApplication.translate("EditExecutablesDialog", u"Up", None))
#if QT_CONFIG(tooltip)
        self.down.setToolTip(QCoreApplication.translate("EditExecutablesDialog", u"Move the executable down in the list", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.down.setStatusTip(QCoreApplication.translate("EditExecutablesDialog", u"Move the executable down in the list", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.down.setWhatsThis(QCoreApplication.translate("EditExecutablesDialog", u"Move the executable down in the list", None))
#endif // QT_CONFIG(whatsthis)
        self.down.setText(QCoreApplication.translate("EditExecutablesDialog", u"Down", None))
#if QT_CONFIG(tooltip)
        self.reset.setToolTip(QCoreApplication.translate("EditExecutablesDialog", u"Adds the executables provided by the game plugin and moves any existing executables out of the way", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.reset.setStatusTip(QCoreApplication.translate("EditExecutablesDialog", u"Adds the executables provided by the game plugin and moves any existing executables out of the way", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.reset.setWhatsThis(QCoreApplication.translate("EditExecutablesDialog", u"Adds the executables provided by the game plugin and moves any existing executables out of the way", None))
#endif // QT_CONFIG(whatsthis)
        self.reset.setText(QCoreApplication.translate("EditExecutablesDialog", u"Reset", None))
#if QT_CONFIG(tooltip)
        self.list.setToolTip(QCoreApplication.translate("EditExecutablesDialog", u"List of configured executables", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.list.setWhatsThis(QCoreApplication.translate("EditExecutablesDialog", u"This is a list of your configured executables. Executables in grey are automatically recognised and can not be modified.", None))
#endif // QT_CONFIG(whatsthis)
        self.label_3.setText(QCoreApplication.translate("EditExecutablesDialog", u"Title", None))
#if QT_CONFIG(tooltip)
        self.title.setToolTip(QCoreApplication.translate("EditExecutablesDialog", u"Name of the executable. This is only for display purposes.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.title.setWhatsThis(QCoreApplication.translate("EditExecutablesDialog", u"Name of the executable. This is only for display purposes.", None))
#endif // QT_CONFIG(whatsthis)
        self.label.setText(QCoreApplication.translate("EditExecutablesDialog", u"Binary", None))
#if QT_CONFIG(tooltip)
        self.binary.setToolTip(QCoreApplication.translate("EditExecutablesDialog", u"Binary to run", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.binary.setWhatsThis(QCoreApplication.translate("EditExecutablesDialog", u"Binary to run", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.browseBinary.setToolTip(QCoreApplication.translate("EditExecutablesDialog", u"Browse filesystem", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.browseBinary.setWhatsThis(QCoreApplication.translate("EditExecutablesDialog", u"Browse filesystem for the executable to run.", None))
#endif // QT_CONFIG(whatsthis)
        self.browseBinary.setText(QCoreApplication.translate("EditExecutablesDialog", u"...", None))
        self.label_4.setText(QCoreApplication.translate("EditExecutablesDialog", u"Start in", None))
        self.browseWorkingDirectory.setText(QCoreApplication.translate("EditExecutablesDialog", u"...", None))
        self.label_2.setText(QCoreApplication.translate("EditExecutablesDialog", u"Arguments", None))
#if QT_CONFIG(tooltip)
        self.arguments.setToolTip(QCoreApplication.translate("EditExecutablesDialog", u"Arguments to pass to the application", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.arguments.setWhatsThis(QCoreApplication.translate("EditExecutablesDialog", u"Arguments to pass to the application", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.overwriteSteamAppID.setToolTip(QCoreApplication.translate("EditExecutablesDialog", u"Allow the Steam AppID to be used for this executable to be changed.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.overwriteSteamAppID.setWhatsThis(QCoreApplication.translate("EditExecutablesDialog", u"Allow the Steam AppID to be used for this executable to be changed.\n"
"Every game/tool distributed through Steam has a unique ID. MO needs to know this ID to start those programs directly, otherwise the program is started by steam and then MO will not work. By default, MO will use the AppID for the game.\n"
"Right now the only case I know of where this needs to be overwritten is for the Skyrim Creation Kit which has its own AppID. This overwrite is already preconfigured.", None))
#endif // QT_CONFIG(whatsthis)
        self.overwriteSteamAppID.setText(QCoreApplication.translate("EditExecutablesDialog", u"Overwrite Steam AppID", None))
#if QT_CONFIG(tooltip)
        self.steamAppID.setToolTip(QCoreApplication.translate("EditExecutablesDialog", u"Steam AppID to use for this executable that differs from the games AppID.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.steamAppID.setWhatsThis(QCoreApplication.translate("EditExecutablesDialog", u"Steam AppID to use for this executable that differs from the games AppID.\n"
"Every game/tool distributed through Steam has a unique ID. MO needs to know this ID to start those programs directly, otherwise the program is started by steam and then MO will not work. By default, MO will use the AppID for the game (usually 72850).\n"
"Right now the only case I know of where this needs to be overwritten is for the Skyrim Creation Kit which has its own AppID (usually 202480). This overwrite is already preconfigured.", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.createFilesInMod.setToolTip(QCoreApplication.translate("EditExecutablesDialog", u"If this is enabled, new files are created in the specified mod instead of the \"Overwrite\" mod.", None))
#endif // QT_CONFIG(tooltip)
        self.createFilesInMod.setText(QCoreApplication.translate("EditExecutablesDialog", u"Create files in mod instead of overwrite (*)", None))
#if QT_CONFIG(tooltip)
        self.forceLoadLibraries.setToolTip(QCoreApplication.translate("EditExecutablesDialog", u"If this is enabled, the configured libraries will be automatically loaded when this executable is launched.", None))
#endif // QT_CONFIG(tooltip)
        self.forceLoadLibraries.setText(QCoreApplication.translate("EditExecutablesDialog", u"Force load libraries (*)", None))
        self.configureLibraries.setText(QCoreApplication.translate("EditExecutablesDialog", u"Configure Libraries", None))
        self.useApplicationIcon.setText(QCoreApplication.translate("EditExecutablesDialog", u"Use application's icon for desktop shortcuts", None))
#if QT_CONFIG(tooltip)
        self.hide.setToolTip(QCoreApplication.translate("EditExecutablesDialog", u"This executable will not appear in the list, on the toolbar or in the menu. It will still be visible in this dialog.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.hide.setWhatsThis(QCoreApplication.translate("EditExecutablesDialog", u"This executable will not appear in the list, on the toolbar or in the menu. It will still be visible in this dialog.", None))
#endif // QT_CONFIG(whatsthis)
        self.hide.setText(QCoreApplication.translate("EditExecutablesDialog", u"Hide in user interface", None))
        self.label_5.setText(QCoreApplication.translate("EditExecutablesDialog", u"(*) Profile specific", None))
    # retranslateUi

