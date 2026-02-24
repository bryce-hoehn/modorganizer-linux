# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'credentialsdialog.ui'
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
    QDialogButtonBox, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_CredentialsDialog(object):
    def setupUi(self, CredentialsDialog):
        if not CredentialsDialog.objectName():
            CredentialsDialog.setObjectName(u"CredentialsDialog")
        CredentialsDialog.resize(294, 156)
        self.verticalLayout = QVBoxLayout(CredentialsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(CredentialsDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_3)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(CredentialsDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.usernameEdit = QLineEdit(CredentialsDialog)
        self.usernameEdit.setObjectName(u"usernameEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.usernameEdit)

        self.label_2 = QLabel(CredentialsDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.passwordEdit = QLineEdit(CredentialsDialog)
        self.passwordEdit.setObjectName(u"passwordEdit")
        self.passwordEdit.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.passwordEdit)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.rememberCheck = QCheckBox(CredentialsDialog)
        self.rememberCheck.setObjectName(u"rememberCheck")

        self.horizontalLayout_3.addWidget(self.rememberCheck)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.dontaskBox = QCheckBox(CredentialsDialog)
        self.dontaskBox.setObjectName(u"dontaskBox")

        self.horizontalLayout_4.addWidget(self.dontaskBox)

        self.buttonBox = QDialogButtonBox(CredentialsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout_4.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.retranslateUi(CredentialsDialog)
        self.buttonBox.accepted.connect(CredentialsDialog.accept)
        self.buttonBox.rejected.connect(CredentialsDialog.reject)

        QMetaObject.connectSlotsByName(CredentialsDialog)
    # setupUi

    def retranslateUi(self, CredentialsDialog):
        CredentialsDialog.setWindowTitle(QCoreApplication.translate("CredentialsDialog", u"Login", None))
        self.label_3.setText(QCoreApplication.translate("CredentialsDialog", u"This feature may not work unless you're logged in with Nexus", None))
        self.label.setText(QCoreApplication.translate("CredentialsDialog", u"Username", None))
        self.label_2.setText(QCoreApplication.translate("CredentialsDialog", u"Password", None))
        self.rememberCheck.setText(QCoreApplication.translate("CredentialsDialog", u"Remember", None))
        self.dontaskBox.setText(QCoreApplication.translate("CredentialsDialog", u"Never ask again", None))
    # retranslateUi

