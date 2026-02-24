# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'validationprogressdialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_ValidationProgressDialog(object):
    def setupUi(self, ValidationProgressDialog):
        if not ValidationProgressDialog.objectName():
            ValidationProgressDialog.setObjectName(u"ValidationProgressDialog")
        ValidationProgressDialog.resize(305, 93)
        self.verticalLayout_2 = QVBoxLayout(ValidationProgressDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(ValidationProgressDialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.progress = QProgressBar(self.widget)
        self.progress.setObjectName(u"progress")
        self.progress.setValue(24)
        self.progress.setTextVisible(False)

        self.verticalLayout.addWidget(self.progress)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.widget)

        self.widget_2 = QWidget(ValidationProgressDialog)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.cancel = QPushButton(self.widget_2)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout.addWidget(self.cancel)

        self.horizontalSpacer = QSpacerItem(122, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.hide = QPushButton(self.widget_2)
        self.hide.setObjectName(u"hide")

        self.horizontalLayout.addWidget(self.hide)


        self.verticalLayout_2.addWidget(self.widget_2)


        self.retranslateUi(ValidationProgressDialog)

        self.hide.setDefault(True)


        QMetaObject.connectSlotsByName(ValidationProgressDialog)
    # setupUi

    def retranslateUi(self, ValidationProgressDialog):
        ValidationProgressDialog.setWindowTitle(QCoreApplication.translate("ValidationProgressDialog", u"Validating Nexus Connection", None))
        self.label.setText(QCoreApplication.translate("ValidationProgressDialog", u"Connecting to Nexus...", None))
        self.cancel.setText(QCoreApplication.translate("ValidationProgressDialog", u"Cancel", None))
        self.hide.setText(QCoreApplication.translate("ValidationProgressDialog", u"Hide", None))
    # retranslateUi

