# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'previewdialog.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_PreviewDialog(object):
    def setupUi(self, PreviewDialog):
        if not PreviewDialog.objectName():
            PreviewDialog.setObjectName(u"PreviewDialog")
        PreviewDialog.resize(736, 583)
        self.verticalLayout = QVBoxLayout(PreviewDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.nameLabel = QLabel(PreviewDialog)
        self.nameLabel.setObjectName(u"nameLabel")

        self.horizontalLayout_2.addWidget(self.nameLabel)

        self.modLabel = QLabel(PreviewDialog)
        self.modLabel.setObjectName(u"modLabel")

        self.horizontalLayout_2.addWidget(self.modLabel)

        self.previousButton = QPushButton(PreviewDialog)
        self.previousButton.setObjectName(u"previousButton")
        icon = QIcon()
        icon.addFile(u":/MO/gui/previous", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.previousButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.previousButton)

        self.nextButton = QPushButton(PreviewDialog)
        self.nextButton.setObjectName(u"nextButton")
        icon1 = QIcon()
        icon1.addFile(u":/MO/gui/next", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.nextButton.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.nextButton)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.variantsStack = QStackedWidget(PreviewDialog)
        self.variantsStack.setObjectName(u"variantsStack")

        self.verticalLayout.addWidget(self.variantsStack)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.closeButton = QPushButton(PreviewDialog)
        self.closeButton.setObjectName(u"closeButton")

        self.horizontalLayout.addWidget(self.closeButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(PreviewDialog)

        QMetaObject.connectSlotsByName(PreviewDialog)
    # setupUi

    def retranslateUi(self, PreviewDialog):
        PreviewDialog.setWindowTitle(QCoreApplication.translate("PreviewDialog", u"Preview", None))
        self.nameLabel.setText("")
        self.modLabel.setText("")
        self.previousButton.setText("")
        self.nextButton.setText("")
        self.closeButton.setText(QCoreApplication.translate("PreviewDialog", u"Close", None))
    # retranslateUi

