# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'savetextasdialog.ui'
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
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_SaveTextAsDialog(object):
    def setupUi(self, SaveTextAsDialog):
        if not SaveTextAsDialog.objectName():
            SaveTextAsDialog.setObjectName(u"SaveTextAsDialog")
        SaveTextAsDialog.resize(631, 578)
        self.verticalLayout = QVBoxLayout(SaveTextAsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(SaveTextAsDialog)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setLineWrapMode(QTextEdit.NoWrap)
        self.textEdit.setAcceptRichText(False)

        self.verticalLayout.addWidget(self.textEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.clipboardBtn = QPushButton(SaveTextAsDialog)
        self.clipboardBtn.setObjectName(u"clipboardBtn")

        self.horizontalLayout.addWidget(self.clipboardBtn)

        self.saveAsBtn = QPushButton(SaveTextAsDialog)
        self.saveAsBtn.setObjectName(u"saveAsBtn")

        self.horizontalLayout.addWidget(self.saveAsBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.closeBtn = QPushButton(SaveTextAsDialog)
        self.closeBtn.setObjectName(u"closeBtn")

        self.horizontalLayout.addWidget(self.closeBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(SaveTextAsDialog)

        QMetaObject.connectSlotsByName(SaveTextAsDialog)
    # setupUi

    def retranslateUi(self, SaveTextAsDialog):
        SaveTextAsDialog.setWindowTitle(QCoreApplication.translate("SaveTextAsDialog", u"Dialog", None))
        self.clipboardBtn.setText(QCoreApplication.translate("SaveTextAsDialog", u"Copy To Clipboard", None))
        self.saveAsBtn.setText(QCoreApplication.translate("SaveTextAsDialog", u"Save As...", None))
        self.closeBtn.setText(QCoreApplication.translate("SaveTextAsDialog", u"Close", None))
    # retranslateUi

