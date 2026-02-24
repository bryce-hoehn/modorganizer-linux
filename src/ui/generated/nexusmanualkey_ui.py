# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nexusmanualkey.ui'
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
    QHBoxLayout, QLabel, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_NexusManualKeyDialog(object):
    def setupUi(self, NexusManualKeyDialog):
        if not NexusManualKeyDialog.objectName():
            NexusManualKeyDialog.setObjectName(u"NexusManualKeyDialog")
        NexusManualKeyDialog.resize(452, 236)
        self.verticalLayout_2 = QVBoxLayout(NexusManualKeyDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(NexusManualKeyDialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.openBrowser = QPushButton(self.widget_2)
        self.openBrowser.setObjectName(u"openBrowser")

        self.verticalLayout_3.addWidget(self.openBrowser)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(115, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.paste = QPushButton(self.widget_4)
        self.paste.setObjectName(u"paste")

        self.horizontalLayout.addWidget(self.paste)

        self.clear = QPushButton(self.widget_4)
        self.clear.setObjectName(u"clear")

        self.horizontalLayout.addWidget(self.clear)


        self.verticalLayout_4.addWidget(self.widget_4)

        self.key = QPlainTextEdit(self.widget_3)
        self.key.setObjectName(u"key")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.key.sizePolicy().hasHeightForWidth())
        self.key.setSizePolicy(sizePolicy)
        self.key.setMinimumSize(QSize(1, 1))

        self.verticalLayout_4.addWidget(self.key)

        self.verticalLayout_4.setStretch(1, 1)

        self.verticalLayout.addWidget(self.widget_3)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_5 = QVBoxLayout(self.widget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_3)


        self.verticalLayout.addWidget(self.widget_5)

        self.verticalLayout.setStretch(1, 1)

        self.verticalLayout_2.addWidget(self.widget)

        self.buttonBox = QDialogButtonBox(NexusManualKeyDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)

        self.verticalLayout_2.setStretch(0, 1)

        self.retranslateUi(NexusManualKeyDialog)
        self.buttonBox.accepted.connect(NexusManualKeyDialog.accept)
        self.buttonBox.rejected.connect(NexusManualKeyDialog.reject)

        QMetaObject.connectSlotsByName(NexusManualKeyDialog)
    # setupUi

    def retranslateUi(self, NexusManualKeyDialog):
        NexusManualKeyDialog.setWindowTitle(QCoreApplication.translate("NexusManualKeyDialog", u"Manual Nexus API Key", None))
        self.label.setText(QCoreApplication.translate("NexusManualKeyDialog", u"1. Get your personal API key", None))
        self.openBrowser.setText(QCoreApplication.translate("NexusManualKeyDialog", u"Open Browser", None))
        self.label_2.setText(QCoreApplication.translate("NexusManualKeyDialog", u"2. Enter your personal API key", None))
        self.paste.setText(QCoreApplication.translate("NexusManualKeyDialog", u"Paste", None))
        self.clear.setText(QCoreApplication.translate("NexusManualKeyDialog", u"Clear", None))
        self.key.setPlaceholderText(QCoreApplication.translate("NexusManualKeyDialog", u"Enter API key here", None))
        self.label_3.setText(QCoreApplication.translate("NexusManualKeyDialog", u"<b>Sharing this key with anyone could get your Nexus account banned. You can always revoke this key from your account on the Nexus website.</b>", None))
    # retranslateUi

