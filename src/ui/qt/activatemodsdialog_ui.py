# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'activatemodsdialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHeaderView, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_ActivateModsDialog(object):
    def setupUi(self, ActivateModsDialog):
        if not ActivateModsDialog.objectName():
            ActivateModsDialog.setObjectName(u"ActivateModsDialog")
        ActivateModsDialog.resize(400, 562)
        self.verticalLayout = QVBoxLayout(ActivateModsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.modsTable = QTableWidget(ActivateModsDialog)
        if (self.modsTable.columnCount() < 2):
            self.modsTable.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.modsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.modsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.modsTable.setObjectName(u"modsTable")
        self.modsTable.setColumnCount(2)

        self.verticalLayout.addWidget(self.modsTable)

        self.buttonBox = QDialogButtonBox(ActivateModsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(ActivateModsDialog)
        self.buttonBox.accepted.connect(ActivateModsDialog.accept)
        self.buttonBox.rejected.connect(ActivateModsDialog.reject)

        QMetaObject.connectSlotsByName(ActivateModsDialog)
    # setupUi

    def retranslateUi(self, ActivateModsDialog):
        ActivateModsDialog.setWindowTitle(QCoreApplication.translate("ActivateModsDialog", u"Activate Mods", None))
        ___qtablewidgetitem = self.modsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ActivateModsDialog", u"Missing ESP", None));
        ___qtablewidgetitem1 = self.modsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ActivateModsDialog", u"Mod", None));
#if QT_CONFIG(tooltip)
        self.modsTable.setToolTip(QCoreApplication.translate("ActivateModsDialog", u"This is a list of esps, esms, and esls that were active when the save game was created.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.modsTable.setWhatsThis(QCoreApplication.translate("ActivateModsDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">This is a list of esps, esms, and esls that were active when the save game was created.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">For each esp, the right column contains the mod (or mods) that can be enabled to make the missing esps/esms available.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent"
                        ":0px;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">If you hit Ok, all the mods selected in the right columns and all missing esps that have become available will be activated.</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
    # retranslateUi

