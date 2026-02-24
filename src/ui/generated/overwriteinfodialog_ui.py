# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'overwriteinfodialog.ui'
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
    QDialogButtonBox, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTreeView, QVBoxLayout, QWidget)

class Ui_OverwriteInfoDialog(object):
    def setupUi(self, OverwriteInfoDialog):
        if not OverwriteInfoDialog.objectName():
            OverwriteInfoDialog.setObjectName(u"OverwriteInfoDialog")
        OverwriteInfoDialog.resize(710, 418)
        self.verticalLayout = QVBoxLayout(OverwriteInfoDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.explorerButton = QPushButton(OverwriteInfoDialog)
        self.explorerButton.setObjectName(u"explorerButton")

        self.verticalLayout.addWidget(self.explorerButton, 0, Qt.AlignLeft)

        self.filesView = QTreeView(OverwriteInfoDialog)
        self.filesView.setObjectName(u"filesView")
        self.filesView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.filesView.setDragEnabled(True)
        self.filesView.setDragDropMode(QAbstractItemView.DragDrop)
        self.filesView.setDefaultDropAction(Qt.MoveAction)
        self.filesView.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.filesView.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.filesView)

        self.label = QLabel(OverwriteInfoDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.buttonBox = QDialogButtonBox(OverwriteInfoDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(OverwriteInfoDialog)
        self.buttonBox.accepted.connect(OverwriteInfoDialog.accept)
        self.buttonBox.rejected.connect(OverwriteInfoDialog.reject)

        QMetaObject.connectSlotsByName(OverwriteInfoDialog)
    # setupUi

    def retranslateUi(self, OverwriteInfoDialog):
        OverwriteInfoDialog.setWindowTitle(QCoreApplication.translate("OverwriteInfoDialog", u"Overwrite", None))
        self.explorerButton.setText(QCoreApplication.translate("OverwriteInfoDialog", u"Open in Explorer", None))
        self.label.setText(QCoreApplication.translate("OverwriteInfoDialog", u"You can use drag&drop to move files and directories to regular mods.", None))
    # retranslateUi

