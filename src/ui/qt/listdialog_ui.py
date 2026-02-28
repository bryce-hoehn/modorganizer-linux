# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'listdialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QDialog,
    QDialogButtonBox, QLineEdit, QListWidget, QListWidgetItem,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_ListDialog(object):
    def setupUi(self, ListDialog):
        if not ListDialog.objectName():
            ListDialog.setObjectName(u"ListDialog")
        ListDialog.resize(260, 380)
        self.verticalLayout = QVBoxLayout(ListDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.choiceList = QListWidget(ListDialog)
        self.choiceList.setObjectName(u"choiceList")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choiceList.sizePolicy().hasHeightForWidth())
        self.choiceList.setSizePolicy(sizePolicy)
        self.choiceList.setMinimumSize(QSize(240, 280))
        self.choiceList.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout.addWidget(self.choiceList)

        self.filterEdit = QLineEdit(ListDialog)
        self.filterEdit.setObjectName(u"filterEdit")

        self.verticalLayout.addWidget(self.filterEdit)

        self.buttonBox = QDialogButtonBox(ListDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setLayoutDirection(Qt.LeftToRight)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(ListDialog)
        self.buttonBox.accepted.connect(ListDialog.accept)
        self.buttonBox.rejected.connect(ListDialog.reject)

        QMetaObject.connectSlotsByName(ListDialog)
    # setupUi

    def retranslateUi(self, ListDialog):
        ListDialog.setWindowTitle(QCoreApplication.translate("ListDialog", u"Select an item...", None))
        self.filterEdit.setText("")
        self.filterEdit.setPlaceholderText(QCoreApplication.translate("ListDialog", u"Filter", None))
    # retranslateUi

