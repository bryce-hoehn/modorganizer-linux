# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profileinputdialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_ProfileInputDialog(object):
    def setupUi(self, ProfileInputDialog):
        if not ProfileInputDialog.objectName():
            ProfileInputDialog.setObjectName(u"ProfileInputDialog")
        ProfileInputDialog.resize(436, 129)
        self.verticalLayout_2 = QVBoxLayout(ProfileInputDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(ProfileInputDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.nameEdit = QLineEdit(ProfileInputDialog)
        self.nameEdit.setObjectName(u"nameEdit")

        self.verticalLayout_2.addWidget(self.nameEdit)

        self.defaultSettingsBox = QCheckBox(ProfileInputDialog)
        self.defaultSettingsBox.setObjectName(u"defaultSettingsBox")

        self.verticalLayout_2.addWidget(self.defaultSettingsBox)

        self.buttonBox = QDialogButtonBox(ProfileInputDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(ProfileInputDialog)
        self.buttonBox.accepted.connect(ProfileInputDialog.accept)
        self.buttonBox.rejected.connect(ProfileInputDialog.reject)

        QMetaObject.connectSlotsByName(ProfileInputDialog)
    # setupUi

    def retranslateUi(self, ProfileInputDialog):
        ProfileInputDialog.setWindowTitle(QCoreApplication.translate("ProfileInputDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("ProfileInputDialog", u"Please enter a name for the new profile", None))
#if QT_CONFIG(tooltip)
        self.defaultSettingsBox.setToolTip(QCoreApplication.translate("ProfileInputDialog", u"If checked, the new profile will use the default game INI settings.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.defaultSettingsBox.setWhatsThis(QCoreApplication.translate("ProfileInputDialog", u"If checked, the new profile will use the default game INI settings instead of the \"global\" settings. Global settings are the settings you configure when running the game launcher directly, without MO.", None))
#endif // QT_CONFIG(whatsthis)
        self.defaultSettingsBox.setText(QCoreApplication.translate("ProfileInputDialog", u"Default Game INI Settings", None))
    # retranslateUi

