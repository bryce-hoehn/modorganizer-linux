# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transfersavesdialog.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_TransferSavesDialog(object):
    def setupUi(self, TransferSavesDialog):
        if not TransferSavesDialog.objectName():
            TransferSavesDialog.setObjectName(u"TransferSavesDialog")
        TransferSavesDialog.resize(882, 528)
        self.horizontalLayout = QHBoxLayout(TransferSavesDialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(TransferSavesDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.globalCharacterList = QListWidget(TransferSavesDialog)
        self.globalCharacterList.setObjectName(u"globalCharacterList")

        self.verticalLayout.addWidget(self.globalCharacterList)

        self.globalSavesList = QListWidget(TransferSavesDialog)
        self.globalSavesList.setObjectName(u"globalSavesList")
        self.globalSavesList.setSelectionMode(QAbstractItemView.NoSelection)

        self.verticalLayout.addWidget(self.globalSavesList)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.moveToLocalBtn = QPushButton(TransferSavesDialog)
        self.moveToLocalBtn.setObjectName(u"moveToLocalBtn")
        self.moveToLocalBtn.setEnabled(False)

        self.verticalLayout_3.addWidget(self.moveToLocalBtn)

        self.copyToLocalBtn = QPushButton(TransferSavesDialog)
        self.copyToLocalBtn.setObjectName(u"copyToLocalBtn")
        self.copyToLocalBtn.setEnabled(False)

        self.verticalLayout_3.addWidget(self.copyToLocalBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.moveToGlobalBtn = QPushButton(TransferSavesDialog)
        self.moveToGlobalBtn.setObjectName(u"moveToGlobalBtn")
        self.moveToGlobalBtn.setEnabled(False)

        self.verticalLayout_3.addWidget(self.moveToGlobalBtn)

        self.copyToGlobalBtn = QPushButton(TransferSavesDialog)
        self.copyToGlobalBtn.setObjectName(u"copyToGlobalBtn")
        self.copyToGlobalBtn.setEnabled(False)

        self.verticalLayout_3.addWidget(self.copyToGlobalBtn)

        self.verticalSpacer_3 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.doneButton = QPushButton(TransferSavesDialog)
        self.doneButton.setObjectName(u"doneButton")

        self.verticalLayout_3.addWidget(self.doneButton)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(TransferSavesDialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.localCharacterList = QListWidget(TransferSavesDialog)
        self.localCharacterList.setObjectName(u"localCharacterList")

        self.verticalLayout_2.addWidget(self.localCharacterList)

        self.localSavesList = QListWidget(TransferSavesDialog)
        self.localSavesList.setObjectName(u"localSavesList")
        self.localSavesList.setSelectionMode(QAbstractItemView.NoSelection)

        self.verticalLayout_2.addWidget(self.localSavesList)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(TransferSavesDialog)

        QMetaObject.connectSlotsByName(TransferSavesDialog)
    # setupUi

    def retranslateUi(self, TransferSavesDialog):
        TransferSavesDialog.setWindowTitle(QCoreApplication.translate("TransferSavesDialog", u"Transfer Save Games", None))
        self.label.setText(QCoreApplication.translate("TransferSavesDialog", u"Global Characters", None))
#if QT_CONFIG(tooltip)
        self.globalCharacterList.setToolTip(QCoreApplication.translate("TransferSavesDialog", u"This is a list of characters in the global location.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.globalCharacterList.setWhatsThis(QCoreApplication.translate("TransferSavesDialog", u"This is a list of characters in the global location.\n"
"\n"
"On Windows Vista/Windows 7:\n"
"  C:\\Users\\[UserName]\\Documents\\My Games\\Skyrim\\Saves\n"
"\n"
"On Windows XP:\n"
"  C:\\Documents and Settings\\[UserName]\\My Documents\\My Games\\Skyrim\\Saves\n"
"", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(whatsthis)
        self.globalSavesList.setWhatsThis(QCoreApplication.translate("TransferSavesDialog", u"This is a list of save games for the selected character in the global location.\n"
"\n"
"On Windows Vista/Windows 7:\n"
"  C:\\Users\\[UserName]\\Documents\\My Games\\Skyrim\\Saves\n"
"\n"
"On Windows XP:\n"
"  C:\\Documents and Settings[UserName]\\My Documents\\My Games\\Skyrim\\Saves\n"
"\n"
"", None))
#endif // QT_CONFIG(whatsthis)
        self.moveToLocalBtn.setText(QCoreApplication.translate("TransferSavesDialog", u"Move ->", None))
        self.copyToLocalBtn.setText(QCoreApplication.translate("TransferSavesDialog", u"Copy ->", None))
        self.moveToGlobalBtn.setText(QCoreApplication.translate("TransferSavesDialog", u"<- Move", None))
        self.copyToGlobalBtn.setText(QCoreApplication.translate("TransferSavesDialog", u"<- Copy", None))
        self.doneButton.setText(QCoreApplication.translate("TransferSavesDialog", u"Done", None))
        self.label_2.setText(QCoreApplication.translate("TransferSavesDialog", u"Profile Characters", None))
    # retranslateUi

