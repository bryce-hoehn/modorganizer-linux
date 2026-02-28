# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'syncoverwritedialog.ui'
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
    QHeaderView, QSizePolicy, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_SyncOverwriteDialog(object):
    def setupUi(self, SyncOverwriteDialog):
        if not SyncOverwriteDialog.objectName():
            SyncOverwriteDialog.setObjectName(u"SyncOverwriteDialog")
        SyncOverwriteDialog.resize(537, 430)
        self.verticalLayout = QVBoxLayout(SyncOverwriteDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.syncTree = QTreeWidget(SyncOverwriteDialog)
        self.syncTree.setObjectName(u"syncTree")
        self.syncTree.setSortingEnabled(True)
        self.syncTree.header().setDefaultSectionSize(300)

        self.verticalLayout.addWidget(self.syncTree)

        self.buttonBox = QDialogButtonBox(SyncOverwriteDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(SyncOverwriteDialog)
        self.buttonBox.accepted.connect(SyncOverwriteDialog.accept)
        self.buttonBox.rejected.connect(SyncOverwriteDialog.reject)

        QMetaObject.connectSlotsByName(SyncOverwriteDialog)
    # setupUi

    def retranslateUi(self, SyncOverwriteDialog):
        SyncOverwriteDialog.setWindowTitle(QCoreApplication.translate("SyncOverwriteDialog", u"Sync Overwrite", None))
        ___qtreewidgetitem = self.syncTree.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("SyncOverwriteDialog", u"Sync To", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("SyncOverwriteDialog", u"Name", None));
    # retranslateUi

