# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'browserdialog.ui'
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
    QLineEdit, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_BrowserDialog(object):
    def setupUi(self, BrowserDialog):
        if not BrowserDialog.objectName():
            BrowserDialog.setObjectName(u"BrowserDialog")
        BrowserDialog.resize(1008, 750)
        self.verticalLayout = QVBoxLayout(BrowserDialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.toolBar = QWidget(BrowserDialog)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMaximumSize(QSize(16777215, 22))
        palette = QPalette()
        brush = QBrush(QColor(226, 226, 226, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(106, 106, 106, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        brush2 = QBrush(QColor(199, 199, 199, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush2)
        brush3 = QBrush(QColor(255, 255, 255, 255))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush3)
        brush4 = QBrush(QColor(81, 81, 81, 255))
        brush4.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush4)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush2)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush3)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush4)
        brush5 = QBrush(QColor(120, 120, 120, 255))
        brush5.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush5)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush5)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush4)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush4)
        self.toolBar.setPalette(palette)
        self.toolBar.setAutoFillBackground(True)
        self.horizontalLayout = QHBoxLayout(self.toolBar)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.backBtn = QPushButton(self.toolBar)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u":/MO/gui/previous", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.backBtn.setIcon(icon)
        self.backBtn.setAutoDefault(False)
        self.backBtn.setFlat(True)

        self.horizontalLayout.addWidget(self.backBtn)

        self.fwdBtn = QPushButton(self.toolBar)
        self.fwdBtn.setObjectName(u"fwdBtn")
        icon1 = QIcon()
        icon1.addFile(u":/MO/gui/next", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.fwdBtn.setIcon(icon1)
        self.fwdBtn.setAutoDefault(False)
        self.fwdBtn.setFlat(True)

        self.horizontalLayout.addWidget(self.fwdBtn)

        self.refreshBtn = QPushButton(self.toolBar)
        self.refreshBtn.setObjectName(u"refreshBtn")
        icon2 = QIcon()
        icon2.addFile(u":/MO/gui/refresh", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.refreshBtn.setIcon(icon2)
        self.refreshBtn.setAutoDefault(False)
        self.refreshBtn.setFlat(True)

        self.horizontalLayout.addWidget(self.refreshBtn)

        self.urlEdit = QLineEdit(self.toolBar)
        self.urlEdit.setObjectName(u"urlEdit")
        self.urlEdit.setEnabled(True)

        self.horizontalLayout.addWidget(self.urlEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.toolBar)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.searchEdit = QLineEdit(self.toolBar)
        self.searchEdit.setObjectName(u"searchEdit")

        self.horizontalLayout.addWidget(self.searchEdit)


        self.verticalLayout.addWidget(self.toolBar)

        self.browserTabWidget = QTabWidget(BrowserDialog)
        self.browserTabWidget.setObjectName(u"browserTabWidget")
        self.browserTabWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.browserTabWidget.setTabsClosable(True)

        self.verticalLayout.addWidget(self.browserTabWidget)

        self.loadProgress = QProgressBar(BrowserDialog)
        self.loadProgress.setObjectName(u"loadProgress")
        self.loadProgress.setValue(0)

        self.verticalLayout.addWidget(self.loadProgress)


        self.retranslateUi(BrowserDialog)

        QMetaObject.connectSlotsByName(BrowserDialog)
    # setupUi

    def retranslateUi(self, BrowserDialog):
        BrowserDialog.setWindowTitle(QCoreApplication.translate("BrowserDialog", u"Some Page", None))
        self.backBtn.setText("")
        self.fwdBtn.setText("")
        self.refreshBtn.setText("")
        self.label_2.setText(QCoreApplication.translate("BrowserDialog", u"Search", None))
    # retranslateUi

