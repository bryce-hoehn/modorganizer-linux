# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutdialog.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTextBrowser, QVBoxLayout, QWidget)

from linklabel import LinkLabel
import resources_rc

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        if not AboutDialog.objectName():
            AboutDialog.setObjectName(u"AboutDialog")
        AboutDialog.resize(1010, 477)
        self.verticalLayout = QVBoxLayout(AboutDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.iconLabel = QLabel(AboutDialog)
        self.iconLabel.setObjectName(u"iconLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iconLabel.sizePolicy().hasHeightForWidth())
        self.iconLabel.setSizePolicy(sizePolicy)
        self.iconLabel.setMinimumSize(QSize(250, 250))
        self.iconLabel.setMaximumSize(QSize(250, 250))
        self.iconLabel.setPixmap(QPixmap(u":/MO/gui/splash"))
        self.iconLabel.setScaledContents(True)
        self.iconLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.iconLabel)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.tabWidget = QTabWidget(AboutDialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.about = QWidget()
        self.about.setObjectName(u"about")
        self.verticalLayout_2 = QVBoxLayout(self.about)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.nameLabel = QLabel(self.about)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setText(u"Mod Organizer")

        self.verticalLayout_2.addWidget(self.nameLabel)

        self.revisionLabel = QLabel(self.about)
        self.revisionLabel.setObjectName(u"revisionLabel")

        self.verticalLayout_2.addWidget(self.revisionLabel)

        self.usvfsLabel = QLabel(self.about)
        self.usvfsLabel.setObjectName(u"usvfsLabel")

        self.verticalLayout_2.addWidget(self.usvfsLabel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_3 = QLabel(self.about)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setText(u"<html><head/><body><p>Copyright \u00a9 2011-2016 Sebastian Herbord<br/>Copyright \u00a9 2016-2023 Mod Organizer 2 Contributors</p></body></html>")

        self.verticalLayout_2.addWidget(self.label_3)

        self.copyrightText = QLabel(self.about)
        self.copyrightText.setObjectName(u"copyrightText")
        self.copyrightText.setText(u"<html><head/><body><p>This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p><p>See the GNU General Public License for more details.</p></body></html>")
        self.copyrightText.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.copyrightText)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.sourceText = LinkLabel(self.about)
        self.sourceText.setObjectName(u"sourceText")

        self.verticalLayout_2.addWidget(self.sourceText)

        self.tabWidget.addTab(self.about, "")
        self.software = QWidget()
        self.software.setObjectName(u"software")
        self.verticalLayout_4 = QVBoxLayout(self.software)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.creditsList = QListWidget(self.software)
        self.creditsList.setObjectName(u"creditsList")

        self.verticalLayout_4.addWidget(self.creditsList)

        self.licenseText = QTextBrowser(self.software)
        self.licenseText.setObjectName(u"licenseText")

        self.verticalLayout_4.addWidget(self.licenseText)

        self.tabWidget.addTab(self.software, "")
        self.credits = QWidget()
        self.credits.setObjectName(u"credits")
        self.gridLayout_0 = QGridLayout(self.credits)
        self.gridLayout_0.setObjectName(u"gridLayout_0")
        self.groupBox = QGroupBox(self.credits)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.listWidget_2 = QListWidget(self.groupBox)
        QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem.setText(u"AL12");
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem1.setText(u"Silarn");
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem2.setText(u"LostDragonist");
        __qlistwidgetitem3 = QListWidgetItem(self.listWidget_2)
        __qlistwidgetitem3.setText(u"isa");
        QListWidgetItem(self.listWidget_2)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setSelectionMode(QAbstractItemView.NoSelection)

        self.verticalLayout_6.addWidget(self.listWidget_2)


        self.gridLayout_0.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.credits)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.listWidget_3 = QListWidget(self.groupBox_2)
        __qlistwidgetitem4 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem4.setText(u"AnyOldName3");
        __qlistwidgetitem5 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem5.setText(u"erasmux");
        __qlistwidgetitem6 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem6.setText(u"Project579");
        __qlistwidgetitem7 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem7.setText(u"przester");
        __qlistwidgetitem8 = QListWidgetItem(self.listWidget_3)
        __qlistwidgetitem8.setText(u"Qudix");
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setSelectionMode(QAbstractItemView.NoSelection)

        self.verticalLayout_7.addWidget(self.listWidget_3)


        self.gridLayout_0.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.credits)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_61 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.listWidget_4 = QListWidget(self.groupBox_3)
        __qlistwidgetitem9 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem9.setText(u"Scythe1912 (Chinese)");
        __qlistwidgetitem10 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem10.setText(u"yc0620shen (Chinese)");
        __qlistwidgetitem11 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem11.setText(u"miraclefreak (Czech)");
        __qlistwidgetitem12 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem12.setText(u"Meiton (Czech)");
        QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem13 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem13.setText(u"madmedic (Dutch)");
        __qlistwidgetitem14 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem14.setText(u"Ilja (Finnish)");
        __qlistwidgetitem15 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem15.setText(u"Mikmet (Finnish)");
        __qlistwidgetitem16 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem16.setText(u"Alyndiar (French)");
        QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem17 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem17.setText(u"Jlkawaii (French)");
        __qlistwidgetitem18 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem18.setText(u"Rigoletto (French)");
        QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem19 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem19.setText(u"CircleOfDao (German)");
        QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem20 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem20.setText(u"pndrev (German)");
        __qlistwidgetitem21 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem21.setText(u"Xahtax (German)");
        __qlistwidgetitem22 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem22.setText(u"Ypselon (German)");
        QListWidgetItem(self.listWidget_4)
        QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem23 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem23.setText(u"Ren (Korean)");
        QListWidgetItem(self.listWidget_4)
        QListWidgetItem(self.listWidget_4)
        QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem24 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem24.setText(u"tokcdk  (Russian)");
        __qlistwidgetitem25 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem25.setText(u"DaWul (Spanish)");
        __qlistwidgetitem26 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem26.setText(u"Fiama (Spanish)");
        QListWidgetItem(self.listWidget_4)
        QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem27 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem27.setText(u"Hakan \"Nyks45\" Albayrak (Turkish)");
        __qlistwidgetitem28 = QListWidgetItem(self.listWidget_4)
        __qlistwidgetitem28.setText(u"Kato (Turkish)");
        QListWidgetItem(self.listWidget_4)
        self.listWidget_4.setObjectName(u"listWidget_4")
        self.listWidget_4.setSelectionMode(QAbstractItemView.NoSelection)

        self.verticalLayout_61.addWidget(self.listWidget_4)


        self.gridLayout_0.addWidget(self.groupBox_3, 0, 1, 2, 1)

        self.groupBox_4 = QGroupBox(self.credits)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_71 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.listWidget = QListWidget(self.groupBox_4)
        __qlistwidgetitem29 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem29.setText(u"Tannin (Original Creator)");
        __qlistwidgetitem30 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem30.setText(u"6788");
        __qlistwidgetitem31 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem31.setText(u"blacksol");
        __qlistwidgetitem32 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem32.setText(u"BlueAmulet");
        __qlistwidgetitem33 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem33.setText(u"Bridger");
        __qlistwidgetitem34 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem34.setText(u"Brixified");
        __qlistwidgetitem35 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem35.setText(u"ddbb07");
        __qlistwidgetitem36 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem36.setText(u"deathneko11");
        __qlistwidgetitem37 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem37.setText(u"dekart811");
        __qlistwidgetitem38 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem38.setText(u"DoubleYou");
        __qlistwidgetitem39 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem39.setText(u"Drew Warwick");
        __qlistwidgetitem40 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem40.setText(u"erri120");
        __qlistwidgetitem41 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem41.setText(u"ianpatt");
        __qlistwidgetitem42 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem42.setText(u"Falsellyu");
        __qlistwidgetitem43 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem43.setText(u"foresto");
        __qlistwidgetitem44 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem44.setText(u"GamerPoet");
        __qlistwidgetitem45 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem45.setText(u"Gopher");
        __qlistwidgetitem46 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem46.setText(u"GrantSP");
        __qlistwidgetitem47 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem47.setText(u"GSDFan");
        __qlistwidgetitem48 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem48.setText(u"JayLCypher");
        __qlistwidgetitem49 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem49.setText(u"jimfcarroll");
        __qlistwidgetitem50 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem50.setText(u"Luca|EzioTheDeadPoet");
        __qlistwidgetitem51 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem51.setText(u"ogrotten");
        __qlistwidgetitem52 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem52.setText(u"outdatedtv");
        __qlistwidgetitem53 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem53.setText(u"Patchier");
        __qlistwidgetitem54 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem54.setText(u"PurpleFez");
        __qlistwidgetitem55 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem55.setText(u"reedts");
        __qlistwidgetitem56 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem56.setText(u"Schilduin");
        __qlistwidgetitem57 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem57.setText(u"SuperSandro2000");
        __qlistwidgetitem58 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem58.setText(u"Trosski");
        __qlistwidgetitem59 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem59.setText(u"Uhuru");
        __qlistwidgetitem60 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem60.setText(u"Wolverine2710");
        __qlistwidgetitem61 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem61.setText(u"thosrtanner");
        __qlistwidgetitem62 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem62.setText(u"z929669");
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setSelectionMode(QAbstractItemView.NoSelection)

        self.verticalLayout_71.addWidget(self.listWidget)


        self.gridLayout_0.addWidget(self.groupBox_4, 0, 2, 2, 1)

        self.tabWidget.addTab(self.credits, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.closeButton = QPushButton(AboutDialog)
        self.closeButton.setObjectName(u"closeButton")

        self.horizontalLayout.addWidget(self.closeButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(AboutDialog)
        self.closeButton.clicked.connect(AboutDialog.accept)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AboutDialog)
    # setupUi

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QCoreApplication.translate("AboutDialog", u"About", None))
        self.iconLabel.setText("")
        self.revisionLabel.setText(QCoreApplication.translate("AboutDialog", u"Revision:", None))
        self.usvfsLabel.setText(QCoreApplication.translate("AboutDialog", u"usvfs:", None))
        self.sourceText.setText(QCoreApplication.translate("AboutDialog", u"<html><head/><body><p>Source code can be found at <a href=\"https://github.com/ModOrganizer2/modorganizer\">GitHub</a>.</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.about), QCoreApplication.translate("AboutDialog", u"About", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.software), QCoreApplication.translate("AboutDialog", u"Used Software", None))
        self.groupBox.setTitle(QCoreApplication.translate("AboutDialog", u"Lead Developers && Maintainers", None))

        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_2.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("AboutDialog", u"LePresidente (Project Lead)", None));
        ___qlistwidgetitem1 = self.listWidget_2.item(5)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("AboutDialog", u"Holt59", None));
        self.listWidget_2.setSortingEnabled(__sortingEnabled)

        self.groupBox_2.setTitle(QCoreApplication.translate("AboutDialog", u"MO2 Developers && Contributors", None))

        __sortingEnabled1 = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        self.listWidget_3.setSortingEnabled(__sortingEnabled1)

        self.groupBox_3.setTitle(QCoreApplication.translate("AboutDialog", u"Translators", None))

        __sortingEnabled2 = self.listWidget_4.isSortingEnabled()
        self.listWidget_4.setSortingEnabled(False)
        ___qlistwidgetitem2 = self.listWidget_4.item(4)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("AboutDialog", u"Cyb3r (Dutch)", None));
        ___qlistwidgetitem3 = self.listWidget_4.item(9)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("AboutDialog", u"fruttyx (French)", None));
        ___qlistwidgetitem4 = self.listWidget_4.item(12)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("AboutDialog", u"Yoplala (French)", None));
        ___qlistwidgetitem5 = self.listWidget_4.item(14)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("AboutDialog", u"Faron (German)", None));
        ___qlistwidgetitem6 = self.listWidget_4.item(18)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("AboutDialog", u"yohru (Japanese)", None));
        ___qlistwidgetitem7 = self.listWidget_4.item(19)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("AboutDialog", u"Mordan (Greek)", None));
        ___qlistwidgetitem8 = self.listWidget_4.item(21)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("AboutDialog", u"Yoosk (Polish)", None));
        ___qlistwidgetitem9 = self.listWidget_4.item(22)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("AboutDialog", u"Brgodfx (Portuguese)", None));
        ___qlistwidgetitem10 = self.listWidget_4.item(23)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("AboutDialog", u"zDas (Portuguese)", None));
        ___qlistwidgetitem11 = self.listWidget_4.item(27)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("AboutDialog", u"Jax (Swedish)", None));
        ___qlistwidgetitem12 = self.listWidget_4.item(28)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("AboutDialog", u"Nubbie (Swedish)", None));
        ___qlistwidgetitem13 = self.listWidget_4.item(31)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("AboutDialog", u"...and all other contributors!", None));
        self.listWidget_4.setSortingEnabled(__sortingEnabled2)

        self.groupBox_4.setTitle(QCoreApplication.translate("AboutDialog", u"Other Supporters && Contributors", None))

        __sortingEnabled3 = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled3)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.credits), QCoreApplication.translate("AboutDialog", u"Thanks", None))
        self.closeButton.setText(QCoreApplication.translate("AboutDialog", u"Close", None))
    # retranslateUi

