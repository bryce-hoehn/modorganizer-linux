# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profilesdialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QHBoxLayout,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_ProfilesDialog(object):
    def setupUi(self, ProfilesDialog):
        if not ProfilesDialog.objectName():
            ProfilesDialog.setObjectName(u"ProfilesDialog")
        ProfilesDialog.resize(482, 332)
        self.verticalLayout_3 = QVBoxLayout(ProfilesDialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(ProfilesDialog)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.profilesList = QListWidget(self.widget)
        self.profilesList.setObjectName(u"profilesList")

        self.verticalLayout_2.addWidget(self.profilesList)

        self.localSavesBox = QCheckBox(self.widget)
        self.localSavesBox.setObjectName(u"localSavesBox")

        self.verticalLayout_2.addWidget(self.localSavesBox)

        self.localIniFilesBox = QCheckBox(self.widget)
        self.localIniFilesBox.setObjectName(u"localIniFilesBox")
        self.localIniFilesBox.setChecked(False)

        self.verticalLayout_2.addWidget(self.localIniFilesBox)

        self.invalidationBox = QCheckBox(self.widget)
        self.invalidationBox.setObjectName(u"invalidationBox")

        self.verticalLayout_2.addWidget(self.invalidationBox)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.addProfileButton = QPushButton(self.widget)
        self.addProfileButton.setObjectName(u"addProfileButton")

        self.verticalLayout.addWidget(self.addProfileButton)

        self.copyProfileButton = QPushButton(self.widget)
        self.copyProfileButton.setObjectName(u"copyProfileButton")
        self.copyProfileButton.setEnabled(False)

        self.verticalLayout.addWidget(self.copyProfileButton)

        self.removeProfileButton = QPushButton(self.widget)
        self.removeProfileButton.setObjectName(u"removeProfileButton")
        self.removeProfileButton.setEnabled(False)

        self.verticalLayout.addWidget(self.removeProfileButton)

        self.renameButton = QPushButton(self.widget)
        self.renameButton.setObjectName(u"renameButton")
        self.renameButton.setEnabled(False)

        self.verticalLayout.addWidget(self.renameButton)

        self.transferButton = QPushButton(self.widget)
        self.transferButton.setObjectName(u"transferButton")
        self.transferButton.setEnabled(False)

        self.verticalLayout.addWidget(self.transferButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.widget)

        self.widget_2 = QWidget(ProfilesDialog)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.select = QPushButton(self.widget_2)
        self.select.setObjectName(u"select")

        self.horizontalLayout.addWidget(self.select)

        self.close = QPushButton(self.widget_2)
        self.close.setObjectName(u"close")

        self.horizontalLayout.addWidget(self.close)


        self.verticalLayout_3.addWidget(self.widget_2)


        self.retranslateUi(ProfilesDialog)

        QMetaObject.connectSlotsByName(ProfilesDialog)
    # setupUi

    def retranslateUi(self, ProfilesDialog):
        ProfilesDialog.setWindowTitle(QCoreApplication.translate("ProfilesDialog", u"Profiles", None))
#if QT_CONFIG(tooltip)
        self.profilesList.setToolTip(QCoreApplication.translate("ProfilesDialog", u"List of Profiles", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.profilesList.setWhatsThis(QCoreApplication.translate("ProfilesDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">This is the list of profiles. Each profile contains its own list and installation order of enabled mods (from a shared pool), its own list and load order of enabled plugins (esps/esms), a copy of the games ini-file and an optional savegame filter.</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.localSavesBox.setToolTip(QCoreApplication.translate("ProfilesDialog", u"<html><head/><body><p>If checked, save games are stored locally to this profile and will not appear when starting with a different profile.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.localSavesBox.setWhatsThis(QCoreApplication.translate("ProfilesDialog", u"If checked, save games are local to this profile and will not appear when starting with a different profile.", None))
#endif // QT_CONFIG(whatsthis)
        self.localSavesBox.setText(QCoreApplication.translate("ProfilesDialog", u"Use profile-specific Save Games", None))
#if QT_CONFIG(tooltip)
        self.localIniFilesBox.setToolTip(QCoreApplication.translate("ProfilesDialog", u"<html><head/><body><p>If checked MO2 will use his own profile-specific game INI files, so that the &quot;Global&quot; ones in MyGames can be left vanilla. This different set of INI files is then offered to the game instead of the default one.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.localIniFilesBox.setWhatsThis(QCoreApplication.translate("ProfilesDialog", u"<html><head/><body><p>If checked, MO2 will use a local set of game INI files (configuration and settings files), different from the default ones found in MyGames. This way changes to the INI settings will only affect this profile and the Global INI files can remain vanilla. MO2 will then show the profile INI files to the game instead of the Global ones.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.localIniFilesBox.setText(QCoreApplication.translate("ProfilesDialog", u"Use profile-specific Game INI Files", None))
#if QT_CONFIG(tooltip)
        self.invalidationBox.setToolTip(QCoreApplication.translate("ProfilesDialog", u"This ensures data files from mods are actually used. You want to enable this unless you use a different tool for Archive Invalidation.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.invalidationBox.setWhatsThis(QCoreApplication.translate("ProfilesDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">The games Oblivion, Fallout 3 and Fallout NV contain a bug which prevents texture and mesh replacers (that is: all modifications to meshes and textures already in game) from working.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">The Mod Organizer uses a workaround called &quot;BSA redirection&quot; (google is your friend) to fix this issue reliably and without further work. Simply activate and forget.</"
                        "span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">With Skyrim this bug seems to be fixed to a degree but whether a mod becomes active still depends on file dates. Therefore, it still makes sense to activate this.</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.invalidationBox.setText(QCoreApplication.translate("ProfilesDialog", u"Automatic Archive Invalidation", None))
#if QT_CONFIG(tooltip)
        self.addProfileButton.setToolTip(QCoreApplication.translate("ProfilesDialog", u"Create a new profile from scratch", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.addProfileButton.setWhatsThis(QCoreApplication.translate("ProfilesDialog", u"Create a new profile from scratch", None))
#endif // QT_CONFIG(whatsthis)
        self.addProfileButton.setText(QCoreApplication.translate("ProfilesDialog", u"Create", None))
#if QT_CONFIG(tooltip)
        self.copyProfileButton.setToolTip(QCoreApplication.translate("ProfilesDialog", u"Clone the selected profile", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.copyProfileButton.setWhatsThis(QCoreApplication.translate("ProfilesDialog", u"This creates a new profile with the same settings and active mods as the selected one.", None))
#endif // QT_CONFIG(whatsthis)
        self.copyProfileButton.setText(QCoreApplication.translate("ProfilesDialog", u"Copy", None))
#if QT_CONFIG(tooltip)
        self.removeProfileButton.setToolTip(QCoreApplication.translate("ProfilesDialog", u"Delete the selected Profile. This can not be un-done!", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.removeProfileButton.setWhatsThis(QCoreApplication.translate("ProfilesDialog", u"Delete the selected Profile. This can not be un-done!", None))
#endif // QT_CONFIG(whatsthis)
        self.removeProfileButton.setText(QCoreApplication.translate("ProfilesDialog", u"Remove", None))
        self.renameButton.setText(QCoreApplication.translate("ProfilesDialog", u"Rename", None))
#if QT_CONFIG(tooltip)
        self.transferButton.setToolTip(QCoreApplication.translate("ProfilesDialog", u"Transfer save games to the selected profile.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.transferButton.setWhatsThis(QCoreApplication.translate("ProfilesDialog", u"Transfer save games to the selected profile.", None))
#endif // QT_CONFIG(whatsthis)
        self.transferButton.setText(QCoreApplication.translate("ProfilesDialog", u"Transfer Saves", None))
        self.select.setText(QCoreApplication.translate("ProfilesDialog", u"Select", None))
        self.close.setText(QCoreApplication.translate("ProfilesDialog", u"Close", None))
    # retranslateUi

