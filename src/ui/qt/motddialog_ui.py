# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'motddialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MotDDialog(object):
    def setupUi(self, MotDDialog):
        if not MotDDialog.objectName():
            MotDDialog.setObjectName(u"MotDDialog")
        MotDDialog.resize(483, 372)
        self.verticalLayout = QVBoxLayout(MotDDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.motdView = QTextBrowser(MotDDialog)
        self.motdView.setObjectName(u"motdView")
        self.motdView.setOpenLinks(False)

        self.verticalLayout.addWidget(self.motdView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.okButton = QPushButton(MotDDialog)
        self.okButton.setObjectName(u"okButton")

        self.horizontalLayout.addWidget(self.okButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(MotDDialog)

        QMetaObject.connectSlotsByName(MotDDialog)
    # setupUi

    def retranslateUi(self, MotDDialog):
        MotDDialog.setWindowTitle(QCoreApplication.translate("MotDDialog", u"Message of the Day", None))
        self.okButton.setText(QCoreApplication.translate("MotDDialog", u"OK", None))
    # retranslateUi

