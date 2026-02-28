# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'forcedloaddialog.ui'
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
    QDialogButtonBox, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_ForcedLoadDialog(object):
    def setupUi(self, ForcedLoadDialog):
        if not ForcedLoadDialog.objectName():
            ForcedLoadDialog.setObjectName(u"ForcedLoadDialog")
        ForcedLoadDialog.resize(700, 400)
        self.verticalLayout = QVBoxLayout(ForcedLoadDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(ForcedLoadDialog)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addRowButton = QPushButton(ForcedLoadDialog)
        self.addRowButton.setObjectName(u"addRowButton")

        self.horizontalLayout.addWidget(self.addRowButton)

        self.deleteRowButton = QPushButton(ForcedLoadDialog)
        self.deleteRowButton.setObjectName(u"deleteRowButton")

        self.horizontalLayout.addWidget(self.deleteRowButton)

        self.buttonBox = QDialogButtonBox(ForcedLoadDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ForcedLoadDialog)
        self.buttonBox.accepted.connect(ForcedLoadDialog.accept)
        self.buttonBox.rejected.connect(ForcedLoadDialog.reject)

        QMetaObject.connectSlotsByName(ForcedLoadDialog)
    # setupUi

    def retranslateUi(self, ForcedLoadDialog):
        ForcedLoadDialog.setWindowTitle(QCoreApplication.translate("ForcedLoadDialog", u"Forced Load Settings", None))
#if QT_CONFIG(tooltip)
        self.addRowButton.setToolTip(QCoreApplication.translate("ForcedLoadDialog", u"Adds a row to the table.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.addRowButton.setWhatsThis(QCoreApplication.translate("ForcedLoadDialog", u"Adds a row to the table.", None))
#endif // QT_CONFIG(whatsthis)
        self.addRowButton.setText(QCoreApplication.translate("ForcedLoadDialog", u"Add Row", None))
#if QT_CONFIG(tooltip)
        self.deleteRowButton.setToolTip(QCoreApplication.translate("ForcedLoadDialog", u"Deletes the selected row from the table.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.deleteRowButton.setWhatsThis(QCoreApplication.translate("ForcedLoadDialog", u"Deletes the selected row from the table.", None))
#endif // QT_CONFIG(whatsthis)
        self.deleteRowButton.setText(QCoreApplication.translate("ForcedLoadDialog", u"Delete Row", None))
    # retranslateUi

