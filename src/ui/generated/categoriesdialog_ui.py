# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'categoriesdialog.ui'
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
    QDialogButtonBox, QGridLayout, QGroupBox, QHeaderView,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_CategoriesDialog(object):
    def setupUi(self, CategoriesDialog):
        if not CategoriesDialog.objectName():
            CategoriesDialog.setObjectName(u"CategoriesDialog")
        CategoriesDialog.resize(711, 434)
        self.gridLayout = QGridLayout(CategoriesDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(CategoriesDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 4, 3, 1, 1)

        self.nexusRefresh = QPushButton(CategoriesDialog)
        self.nexusRefresh.setObjectName(u"nexusRefresh")

        self.gridLayout.addWidget(self.nexusRefresh, 4, 5, 1, 1)

        self.nexusImportButton = QPushButton(CategoriesDialog)
        self.nexusImportButton.setObjectName(u"nexusImportButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nexusImportButton.sizePolicy().hasHeightForWidth())
        self.nexusImportButton.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.nexusImportButton, 4, 4, 1, 1)

        self.categoriesTable = QTableWidget(CategoriesDialog)
        if (self.categoriesTable.columnCount() < 4):
            self.categoriesTable.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.categoriesTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.categoriesTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.categoriesTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.categoriesTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.categoriesTable.setObjectName(u"categoriesTable")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.categoriesTable.sizePolicy().hasHeightForWidth())
        self.categoriesTable.setSizePolicy(sizePolicy1)
        self.categoriesTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.categoriesTable.setAcceptDrops(True)
        self.categoriesTable.setDragEnabled(False)
        self.categoriesTable.setDragDropOverwriteMode(False)
        self.categoriesTable.setDragDropMode(QAbstractItemView.DropOnly)
        self.categoriesTable.setDefaultDropAction(Qt.IgnoreAction)
        self.categoriesTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.categoriesTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.categoriesTable.setGridStyle(Qt.DashLine)
        self.categoriesTable.setSortingEnabled(True)
        self.categoriesTable.setWordWrap(False)
        self.categoriesTable.horizontalHeader().setVisible(True)
        self.categoriesTable.horizontalHeader().setMinimumSectionSize(26)
        self.categoriesTable.horizontalHeader().setDefaultSectionSize(100)
        self.categoriesTable.horizontalHeader().setHighlightSections(True)
        self.categoriesTable.horizontalHeader().setStretchLastSection(False)
        self.categoriesTable.verticalHeader().setVisible(True)

        self.gridLayout.addWidget(self.categoriesTable, 0, 3, 1, 1)

        self.groupBox = QGroupBox(CategoriesDialog)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.nexusCategoryList = QListWidget(self.groupBox)
        self.nexusCategoryList.setObjectName(u"nexusCategoryList")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.nexusCategoryList.sizePolicy().hasHeightForWidth())
        self.nexusCategoryList.setSizePolicy(sizePolicy3)
        self.nexusCategoryList.setDragEnabled(True)
        self.nexusCategoryList.setDragDropMode(QAbstractItemView.DragOnly)

        self.verticalLayout.addWidget(self.nexusCategoryList)


        self.gridLayout.addWidget(self.groupBox, 0, 4, 1, 2)


        self.retranslateUi(CategoriesDialog)
        self.buttonBox.accepted.connect(CategoriesDialog.accept)
        self.buttonBox.rejected.connect(CategoriesDialog.reject)

        QMetaObject.connectSlotsByName(CategoriesDialog)
    # setupUi

    def retranslateUi(self, CategoriesDialog):
        CategoriesDialog.setWindowTitle(QCoreApplication.translate("CategoriesDialog", u"Categories", None))
        self.nexusRefresh.setText(QCoreApplication.translate("CategoriesDialog", u"Refresh from Nexus", None))
        self.nexusImportButton.setText(QCoreApplication.translate("CategoriesDialog", u"<-- Import Nexus Cats", None))
        ___qtablewidgetitem = self.categoriesTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("CategoriesDialog", u"ID", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem.setToolTip(QCoreApplication.translate("CategoriesDialog", u"Internal ID for the category.", None));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        ___qtablewidgetitem.setWhatsThis(QCoreApplication.translate("CategoriesDialog", u"Internal ID for the category. The categories a mod belongs to are stored by this ID. It is recommended you use new IDs for categories you add instead of re-using existing ones.", None));
#endif // QT_CONFIG(whatsthis)
        ___qtablewidgetitem1 = self.categoriesTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("CategoriesDialog", u"Name", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem1.setToolTip(QCoreApplication.translate("CategoriesDialog", u"The display name of the category.", None));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        ___qtablewidgetitem1.setWhatsThis(QCoreApplication.translate("CategoriesDialog", u"The display name of the category.", None));
#endif // QT_CONFIG(whatsthis)
        ___qtablewidgetitem2 = self.categoriesTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("CategoriesDialog", u"Parent ID", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem2.setToolTip(QCoreApplication.translate("CategoriesDialog", u"If set, the category is defined as a sub-category of another one. Parent ID needs to be a valid category ID.", None));
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem3 = self.categoriesTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("CategoriesDialog", u"Nexus Categories", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem3.setToolTip(QCoreApplication.translate("CategoriesDialog", u"Comma-Separated list of Nexus IDs to be matched to the internal ID.", None));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        ___qtablewidgetitem3.setWhatsThis(QCoreApplication.translate("CategoriesDialog", u"\n"
"                <!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"                <html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"                p, li { white-space: pre-wrap; }\n"
"                </style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"                <p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">You can match one or multiple nexus categories to an internal ID. Whenever you download a mod from a Nexus Page, Mod Organizer will try to resolve the category defined on the Nexus to one available in MO.</span></p>\n"
"                <p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"></p>\n"
"                <p style=\" margin-to"
                        "p:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">To find out a category id used by the nexus, visit the categories list of the nexus page and hover over the links there.</span></p></body></html>\n"
"              ", None));
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(tooltip)
        self.groupBox.setToolTip(QCoreApplication.translate("CategoriesDialog", u"Drag & drop nexus categories from this pane onto the target category on the left.", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("CategoriesDialog", u"Nexus Categories (Drag && Drop to Assign)", None))
    # retranslateUi

