# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'problemsdialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QSpacerItem, QTextBrowser,
    QTextEdit, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_ProblemsDialog(object):
    def setupUi(self, ProblemsDialog):
        if not ProblemsDialog.objectName():
            ProblemsDialog.setObjectName(u"ProblemsDialog")
        ProblemsDialog.resize(574, 376)
        self.verticalLayout = QVBoxLayout(ProblemsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.problemsWidget = QTreeWidget(ProblemsDialog)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(1, u"2");
        __qtreewidgetitem.setText(0, u"1");
        self.problemsWidget.setHeaderItem(__qtreewidgetitem)
        self.problemsWidget.setObjectName(u"problemsWidget")
        self.problemsWidget.setColumnCount(2)
        self.problemsWidget.header().setVisible(False)
        self.problemsWidget.header().setDefaultSectionSize(350)

        self.verticalLayout.addWidget(self.problemsWidget)

        self.descriptionText = QTextBrowser(ProblemsDialog)
        self.descriptionText.setObjectName(u"descriptionText")
        self.descriptionText.setLineWrapMode(QTextEdit.NoWrap)
        self.descriptionText.setReadOnly(True)

        self.verticalLayout.addWidget(self.descriptionText)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.closeButton = QPushButton(ProblemsDialog)
        self.closeButton.setObjectName(u"closeButton")

        self.horizontalLayout.addWidget(self.closeButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ProblemsDialog)
        self.closeButton.clicked.connect(ProblemsDialog.accept)

        QMetaObject.connectSlotsByName(ProblemsDialog)
    # setupUi

    def retranslateUi(self, ProblemsDialog):
        ProblemsDialog.setWindowTitle(QCoreApplication.translate("ProblemsDialog", u"Notifications", None))
        self.descriptionText.setHtml(QCoreApplication.translate("ProblemsDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Click a notification above to get more details...</p></body></html>", None))
        self.closeButton.setText(QCoreApplication.translate("ProblemsDialog", u"Close", None))
    # retranslateUi

