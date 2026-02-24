# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'forcedloaddialogwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_ForcedLoadDialogWidget(object):
    def setupUi(self, ForcedLoadDialogWidget):
        if not ForcedLoadDialogWidget.objectName():
            ForcedLoadDialogWidget.setObjectName(u"ForcedLoadDialogWidget")
        ForcedLoadDialogWidget.resize(400, 41)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ForcedLoadDialogWidget.sizePolicy().hasHeightForWidth())
        ForcedLoadDialogWidget.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(ForcedLoadDialogWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.enabledBox = QCheckBox(ForcedLoadDialogWidget)
        self.enabledBox.setObjectName(u"enabledBox")

        self.horizontalLayout.addWidget(self.enabledBox)

        self.processEdit = QLineEdit(ForcedLoadDialogWidget)
        self.processEdit.setObjectName(u"processEdit")

        self.horizontalLayout.addWidget(self.processEdit)

        self.processBrowseButton = QPushButton(ForcedLoadDialogWidget)
        self.processBrowseButton.setObjectName(u"processBrowseButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.processBrowseButton.sizePolicy().hasHeightForWidth())
        self.processBrowseButton.setSizePolicy(sizePolicy1)
        self.processBrowseButton.setMinimumSize(QSize(32, 0))
        self.processBrowseButton.setMaximumSize(QSize(32, 16777215))

        self.horizontalLayout.addWidget(self.processBrowseButton)

        self.libraryPathEdit = QLineEdit(ForcedLoadDialogWidget)
        self.libraryPathEdit.setObjectName(u"libraryPathEdit")

        self.horizontalLayout.addWidget(self.libraryPathEdit)

        self.libraryPathBrowseButton = QPushButton(ForcedLoadDialogWidget)
        self.libraryPathBrowseButton.setObjectName(u"libraryPathBrowseButton")
        self.libraryPathBrowseButton.setMaximumSize(QSize(32, 16777215))

        self.horizontalLayout.addWidget(self.libraryPathBrowseButton)

        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(3, 2)

        self.retranslateUi(ForcedLoadDialogWidget)

        QMetaObject.connectSlotsByName(ForcedLoadDialogWidget)
    # setupUi

    def retranslateUi(self, ForcedLoadDialogWidget):
#if QT_CONFIG(tooltip)
        self.enabledBox.setToolTip(QCoreApplication.translate("ForcedLoadDialogWidget", u"If checked, the specified library will be force loaded for the specified process.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.enabledBox.setWhatsThis(QCoreApplication.translate("ForcedLoadDialogWidget", u"If checked, the specified library will be force loaded for the specified process.", None))
#endif // QT_CONFIG(whatsthis)
        self.enabledBox.setText("")
#if QT_CONFIG(tooltip)
        self.processEdit.setToolTip(QCoreApplication.translate("ForcedLoadDialogWidget", u"The name of the process that should be forced to load a library.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.processEdit.setWhatsThis(QCoreApplication.translate("ForcedLoadDialogWidget", u"The name of the process that should be forced to load a library.", None))
#endif // QT_CONFIG(whatsthis)
        self.processEdit.setPlaceholderText(QCoreApplication.translate("ForcedLoadDialogWidget", u"Process name", None))
#if QT_CONFIG(tooltip)
        self.processBrowseButton.setToolTip(QCoreApplication.translate("ForcedLoadDialogWidget", u"Browse for a process.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.processBrowseButton.setWhatsThis(QCoreApplication.translate("ForcedLoadDialogWidget", u"Browse for a process.", None))
#endif // QT_CONFIG(whatsthis)
        self.processBrowseButton.setText(QCoreApplication.translate("ForcedLoadDialogWidget", u"...", None))
#if QT_CONFIG(tooltip)
        self.libraryPathEdit.setToolTip(QCoreApplication.translate("ForcedLoadDialogWidget", u"The path to the library to be loaded.  This may be a path relative to the managed game's directory or may be an absolute path to somewhere else.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.libraryPathEdit.setWhatsThis(QCoreApplication.translate("ForcedLoadDialogWidget", u"The path to the library to be loaded.  This may be a path relative to the managed game's directory or may be an absolute path to somewhere else.", None))
#endif // QT_CONFIG(whatsthis)
        self.libraryPathEdit.setPlaceholderText(QCoreApplication.translate("ForcedLoadDialogWidget", u"Library to load", None))
#if QT_CONFIG(tooltip)
        self.libraryPathBrowseButton.setToolTip(QCoreApplication.translate("ForcedLoadDialogWidget", u"Browse for a library.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.libraryPathBrowseButton.setWhatsThis(QCoreApplication.translate("ForcedLoadDialogWidget", u"Browse for a library.", None))
#endif // QT_CONFIG(whatsthis)
        self.libraryPathBrowseButton.setText(QCoreApplication.translate("ForcedLoadDialogWidget", u"...", None))
        pass
    # retranslateUi

