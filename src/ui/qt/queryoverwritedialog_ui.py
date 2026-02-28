# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'queryoverwritedialog.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QDialog,
    QFrame, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QTextBrowser, QVBoxLayout, QWidget)

class Ui_QueryOverwriteDialog(object):
    def setupUi(self, QueryOverwriteDialog):
        if not QueryOverwriteDialog.objectName():
            QueryOverwriteDialog.setObjectName(u"QueryOverwriteDialog")
        QueryOverwriteDialog.resize(423, 153)
        self.verticalLayout = QVBoxLayout(QueryOverwriteDialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(QueryOverwriteDialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_1 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.iconLabel = QLabel(self.frame_2)
        self.iconLabel.setObjectName(u"iconLabel")
        self.iconLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_1.addWidget(self.iconLabel)

        self.textBrowser = QTextBrowser(self.frame_2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setFrameShape(QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QFrame.Plain)
        self.textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.horizontalLayout_1.addWidget(self.textBrowser)


        self.verticalLayout.addWidget(self.frame_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(7, 7, 7, 7)
        self.backupBox = QCheckBox(QueryOverwriteDialog)
        self.backupBox.setObjectName(u"backupBox")

        self.horizontalLayout.addWidget(self.backupBox)

        self.mergeBtn = QPushButton(QueryOverwriteDialog)
        self.mergeBtn.setObjectName(u"mergeBtn")

        self.horizontalLayout.addWidget(self.mergeBtn)

        self.replaceBtn = QPushButton(QueryOverwriteDialog)
        self.replaceBtn.setObjectName(u"replaceBtn")

        self.horizontalLayout.addWidget(self.replaceBtn)

        self.renameBtn = QPushButton(QueryOverwriteDialog)
        self.renameBtn.setObjectName(u"renameBtn")

        self.horizontalLayout.addWidget(self.renameBtn)

        self.cancelBtn = QPushButton(QueryOverwriteDialog)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.horizontalLayout.addWidget(self.cancelBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 1)

        self.retranslateUi(QueryOverwriteDialog)

        self.renameBtn.setDefault(True)


        QMetaObject.connectSlotsByName(QueryOverwriteDialog)
    # setupUi

    def retranslateUi(self, QueryOverwriteDialog):
        QueryOverwriteDialog.setWindowTitle(QCoreApplication.translate("QueryOverwriteDialog", u"Mod Exists", None))
        self.iconLabel.setText("")
        self.textBrowser.setHtml(QCoreApplication.translate("QueryOverwriteDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This mod seems to be installed already, what would you like to do?</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /><span style=\" font-weight:600;\">Merge:</span> Add files from this archive overwriting existing ones.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Replace:</span> Completely replace the existing mod (old files are deleted).</p>\n"
"<p styl"
                        "e=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Rename:</span> Install this as a separate mod with a new name<span style=\" font-style:italic;\"> (recommended)</span>.</p></body></html>", None))
        self.backupBox.setText(QCoreApplication.translate("QueryOverwriteDialog", u"Keep Backup", None))
        self.mergeBtn.setText(QCoreApplication.translate("QueryOverwriteDialog", u"Merge", None))
        self.replaceBtn.setText(QCoreApplication.translate("QueryOverwriteDialog", u"Replace", None))
        self.renameBtn.setText(QCoreApplication.translate("QueryOverwriteDialog", u"Rename", None))
        self.cancelBtn.setText(QCoreApplication.translate("QueryOverwriteDialog", u"Cancel", None))
    # retranslateUi

