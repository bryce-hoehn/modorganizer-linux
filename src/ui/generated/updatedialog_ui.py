# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'updatedialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_UpdateDialog(object):
    def setupUi(self, UpdateDialog):
        if not UpdateDialog.objectName():
            UpdateDialog.setObjectName(u"UpdateDialog")
        UpdateDialog.resize(578, 539)
        UpdateDialog.setMinimumSize(QSize(460, 0))
        UpdateDialog.setWindowTitle(u"Update available")
        UpdateDialog.setSizeGripEnabled(True)
        UpdateDialog.setModal(True)
        self.verticalLayout_2 = QVBoxLayout(UpdateDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, -1, 9, -1)
        self.iconLabel = QLabel(UpdateDialog)
        self.iconLabel.setObjectName(u"iconLabel")
        self.iconLabel.setMinimumSize(QSize(32, 32))
        self.iconLabel.setMaximumSize(QSize(32, 32))
        self.iconLabel.setText(u"<?>")
        self.iconLabel.setAlignment(Qt.AlignCenter)
        self.iconLabel.setMargin(0)

        self.horizontalLayout_2.addWidget(self.iconLabel)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.updateLabel = QLabel(UpdateDialog)
        self.updateLabel.setObjectName(u"updateLabel")
        self.updateLabel.setText(u"Update text placeholder")
        self.updateLabel.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.updateLabel)

        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.detailsButton = QToolButton(UpdateDialog)
        self.detailsButton.setObjectName(u"detailsButton")

        self.horizontalLayout.addWidget(self.detailsButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.installButton = QPushButton(UpdateDialog)
        self.installButton.setObjectName(u"installButton")

        self.horizontalLayout.addWidget(self.installButton)

        self.cancelButton = QPushButton(UpdateDialog)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.cancelButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.detailsWidget = QWidget(UpdateDialog)
        self.detailsWidget.setObjectName(u"detailsWidget")
        self.verticalLayout = QVBoxLayout(self.detailsWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.detailsWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.detailsWebView = QWebEngineView(self.frame)
        self.detailsWebView.setObjectName(u"detailsWebView")
        self.detailsWebView.setMinimumSize(QSize(650, 450))
        self.detailsWebView.setProperty(u"url", QUrl(u"about:blank"))

        self.verticalLayout_3.addWidget(self.detailsWebView)


        self.verticalLayout.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.detailsWidget)

        self.verticalLayout_2.setStretch(2, 1)

        self.retranslateUi(UpdateDialog)

        self.installButton.setDefault(True)


        QMetaObject.connectSlotsByName(UpdateDialog)
    # setupUi

    def retranslateUi(self, UpdateDialog):
        self.detailsButton.setText(QCoreApplication.translate("UpdateDialog", u"Changelog", None))
        self.installButton.setText(QCoreApplication.translate("UpdateDialog", u"Install", None))
        self.cancelButton.setText(QCoreApplication.translate("UpdateDialog", u"Cancel", None))
        pass
    # retranslateUi

