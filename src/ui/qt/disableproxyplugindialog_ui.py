# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'disableproxyplugindialog.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_DisableProxyPluginDialog(object):
    def setupUi(self, DisableProxyPluginDialog):
        if not DisableProxyPluginDialog.objectName():
            DisableProxyPluginDialog.setObjectName(u"DisableProxyPluginDialog")
        DisableProxyPluginDialog.resize(522, 417)
        self.verticalLayout = QVBoxLayout(DisableProxyPluginDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalWidget = QWidget(DisableProxyPluginDialog)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.horizontalWidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setTextFormat(Qt.PlainText)
        self.label_2.setPixmap(QPixmap(u":/MO/gui/remove"))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.topLabel = QLabel(self.horizontalWidget)
        self.topLabel.setObjectName(u"topLabel")

        self.horizontalLayout.addWidget(self.topLabel)


        self.verticalLayout.addWidget(self.horizontalWidget)

        self.requiredPlugins = QTableWidget(DisableProxyPluginDialog)
        if (self.requiredPlugins.columnCount() < 2):
            self.requiredPlugins.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.requiredPlugins.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.requiredPlugins.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.requiredPlugins.setObjectName(u"requiredPlugins")
        self.requiredPlugins.setColumnCount(2)
        self.requiredPlugins.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.requiredPlugins)

        self.label = QLabel(DisableProxyPluginDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.buttons = QWidget(DisableProxyPluginDialog)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_2 = QHBoxLayout(self.buttons)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.yesBtn = QPushButton(self.buttons)
        self.yesBtn.setObjectName(u"yesBtn")
        self.yesBtn.setMinimumSize(QSize(80, 0))
        icon = QIcon()
        icon.addFile(u":/MO/gui/remove", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.yesBtn.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.yesBtn)

        self.noBtn = QPushButton(self.buttons)
        self.noBtn.setObjectName(u"noBtn")
        sizePolicy.setHeightForWidth(self.noBtn.sizePolicy().hasHeightForWidth())
        self.noBtn.setSizePolicy(sizePolicy)
        self.noBtn.setMinimumSize(QSize(80, 0))
        self.noBtn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.noBtn)


        self.verticalLayout.addWidget(self.buttons)


        self.retranslateUi(DisableProxyPluginDialog)

        self.noBtn.setDefault(True)


        QMetaObject.connectSlotsByName(DisableProxyPluginDialog)
    # setupUi

    def retranslateUi(self, DisableProxyPluginDialog):
        DisableProxyPluginDialog.setWindowTitle(QCoreApplication.translate("DisableProxyPluginDialog", u"Really disable plugin?", None))
        self.label_2.setText("")
        self.topLabel.setText(QCoreApplication.translate("DisableProxyPluginDialog", u"Disabling the '%1' plugin will prevent the following plugins from working:", None))
        ___qtablewidgetitem = self.requiredPlugins.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DisableProxyPluginDialog", u"Plugin", None));
        ___qtablewidgetitem1 = self.requiredPlugins.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DisableProxyPluginDialog", u"Description", None));
        self.label.setText(QCoreApplication.translate("DisableProxyPluginDialog", u"Do you want to continue? You will need to restart Mod Organizer for the change to take effect.", None))
        self.yesBtn.setText(QCoreApplication.translate("DisableProxyPluginDialog", u"Yes", None))
        self.noBtn.setText(QCoreApplication.translate("DisableProxyPluginDialog", u"No", None))
    # retranslateUi

