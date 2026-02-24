# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'categoryimportdialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QButtonGroup, QCheckBox,
    QDialog, QDialogButtonBox, QGroupBox, QHBoxLayout,
    QLabel, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_CategoryImportDialog(object):
    def setupUi(self, CategoryImportDialog):
        if not CategoryImportDialog.objectName():
            CategoryImportDialog.setObjectName(u"CategoryImportDialog")
        CategoryImportDialog.resize(400, 193)
        self.verticalLayout = QVBoxLayout(CategoryImportDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(CategoryImportDialog)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(CategoryImportDialog)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.mergeOption = QRadioButton(self.groupBox)
        self.strategyGroup = QButtonGroup(CategoryImportDialog)
        self.strategyGroup.setObjectName(u"strategyGroup")
        self.strategyGroup.addButton(self.mergeOption)
        self.mergeOption.setObjectName(u"mergeOption")

        self.verticalLayout_2.addWidget(self.mergeOption)

        self.replaceOption = QRadioButton(self.groupBox)
        self.strategyGroup.addButton(self.replaceOption)
        self.replaceOption.setObjectName(u"replaceOption")
        self.replaceOption.setChecked(True)

        self.verticalLayout_2.addWidget(self.replaceOption)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(CategoryImportDialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.assignOption = QCheckBox(self.groupBox_2)
        self.assignOption.setObjectName(u"assignOption")
        self.assignOption.setChecked(True)

        self.verticalLayout_3.addWidget(self.assignOption)

        self.remapOption = QCheckBox(self.groupBox_2)
        self.remapOption.setObjectName(u"remapOption")
        self.remapOption.setEnabled(False)

        self.verticalLayout_3.addWidget(self.remapOption)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.groupBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(CategoryImportDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(CategoryImportDialog)

        QMetaObject.connectSlotsByName(CategoryImportDialog)
    # setupUi

    def retranslateUi(self, CategoryImportDialog):
        CategoryImportDialog.setWindowTitle(QCoreApplication.translate("CategoryImportDialog", u"Nexus Category Import", None))
        self.label.setText(QCoreApplication.translate("CategoryImportDialog", u"<h3>How do you want to import the categories?</h3>", None))
        self.groupBox.setTitle(QCoreApplication.translate("CategoryImportDialog", u"Import Strategy", None))
        self.mergeOption.setText(QCoreApplication.translate("CategoryImportDialog", u"Merge", None))
        self.replaceOption.setText(QCoreApplication.translate("CategoryImportDialog", u"Replace", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("CategoryImportDialog", u"Options", None))
        self.assignOption.setText(QCoreApplication.translate("CategoryImportDialog", u"Assign nexus mappings", None))
        self.remapOption.setText(QCoreApplication.translate("CategoryImportDialog", u"Remap existing mappings", None))
    # retranslateUi

