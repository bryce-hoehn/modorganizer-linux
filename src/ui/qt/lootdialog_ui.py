# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lootdialog.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QHBoxLayout, QLabel, QPlainTextEdit,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_LootDialog(object):
    def setupUi(self, LootDialog):
        if not LootDialog.objectName():
            LootDialog.setObjectName(u"LootDialog")
        LootDialog.resize(457, 600)
        self.verticalLayout = QVBoxLayout(LootDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(LootDialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.progressText = QLabel(self.widget_2)
        self.progressText.setObjectName(u"progressText")

        self.verticalLayout_2.addWidget(self.progressText)

        self.progressBar = QProgressBar(self.widget_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)
        self.progressBar.setTextVisible(False)

        self.verticalLayout_2.addWidget(self.progressBar)

        self.frame = QFrame(self.widget_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.report = QWebEngineView(self.frame)
        self.report.setObjectName(u"report")
        self.report.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_6.addWidget(self.report)


        self.verticalLayout_2.addWidget(self.frame)

        self.verticalLayout_2.setStretch(2, 1)

        self.verticalLayout_5.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.details = QToolButton(self.widget_3)
        self.details.setObjectName(u"details")

        self.verticalLayout_4.addWidget(self.details)

        self.detailsPanel = QWidget(self.widget_3)
        self.detailsPanel.setObjectName(u"detailsPanel")
        self.verticalLayout_3 = QVBoxLayout(self.detailsPanel)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.detailsPanel)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout = QHBoxLayout(self.widget_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.openJsonReport = QPushButton(self.widget_5)
        self.openJsonReport.setObjectName(u"openJsonReport")

        self.horizontalLayout.addWidget(self.openJsonReport)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addWidget(self.widget_5)

        self.output = QPlainTextEdit(self.detailsPanel)
        self.output.setObjectName(u"output")

        self.verticalLayout_3.addWidget(self.output)


        self.verticalLayout_4.addWidget(self.detailsPanel)


        self.verticalLayout_5.addWidget(self.widget_3)

        self.verticalLayout_5.setStretch(0, 1)

        self.verticalLayout.addWidget(self.widget)

        self.buttons = QDialogButtonBox(LootDialog)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setOrientation(Qt.Horizontal)
        self.buttons.setStandardButtons(QDialogButtonBox.Close)

        self.verticalLayout.addWidget(self.buttons)


        self.retranslateUi(LootDialog)
        self.buttons.accepted.connect(LootDialog.accept)
        self.buttons.rejected.connect(LootDialog.reject)

        QMetaObject.connectSlotsByName(LootDialog)
    # setupUi

    def retranslateUi(self, LootDialog):
        LootDialog.setWindowTitle(QCoreApplication.translate("LootDialog", u"LOOT", None))
        self.progressText.setText(QCoreApplication.translate("LootDialog", u"Progress", None))
        self.details.setText(QCoreApplication.translate("LootDialog", u"Details", None))
        self.openJsonReport.setText(QCoreApplication.translate("LootDialog", u"Open JSON report", None))
    # retranslateUi

