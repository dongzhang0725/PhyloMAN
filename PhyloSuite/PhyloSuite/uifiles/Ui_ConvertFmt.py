# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Work\python\bioinfo_excercise\PhyloSuite\PhyloSuite\PhyloSuite\uifiles\ConvertFmt.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConverFMT(object):
    def setupUi(self, ConverFMT):
        ConverFMT.setObjectName("ConverFMT")
        ConverFMT.resize(536, 362)
        ConverFMT.setSizeGripEnabled(True)
        self.gridLayout_4 = QtWidgets.QGridLayout(ConverFMT)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_4 = QtWidgets.QGroupBox(ConverFMT)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.comboBox_4 = ListQCombobox(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy)
        self.comboBox_4.setAcceptDrops(True)
        self.comboBox_4.setEditable(True)
        self.comboBox_4.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout_2.addWidget(self.comboBox_4, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = ClickedLableGif(self.groupBox_4)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 3)
        self.gridLayout_4.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(ConverFMT)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 0, 1, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 1, 0, 1, 1)
        self.checkBox_12 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_12.setObjectName("checkBox_12")
        self.gridLayout.addWidget(self.checkBox_12, 1, 1, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 2, 0, 1, 1)
        self.checkBox_9 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout.addWidget(self.checkBox_9, 2, 1, 1, 1)
        self.checkBox_13 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_13.setObjectName("checkBox_13")
        self.gridLayout.addWidget(self.checkBox_13, 3, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(ConverFMT)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton = ArrowPushButton(self.groupBox_3)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/picture/resourses/if_start_60207.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/picture/resourses/if_Delete_1493279.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 2, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(ConverFMT)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_5)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_5.addWidget(self.progressBar, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_5, 3, 0, 1, 1)

        self.retranslateUi(ConverFMT)
        QtCore.QMetaObject.connectSlotsByName(ConverFMT)

    def retranslateUi(self, ConverFMT):
        _translate = QtCore.QCoreApplication.translate
        ConverFMT.setWindowTitle(_translate("ConverFMT", "Convert Sequence format"))
        self.groupBox_4.setTitle(_translate("ConverFMT", "Input"))
        self.label_4.setText(_translate("ConverFMT", "Input:"))
        self.label_5.setText(_translate("ConverFMT", "<html><head/><body><p>Try to drag your <span style=\" font-weight:600; color:#ff0000;\">alignments</span> file and drop here if you want to use custom files</p></body></html>"))
        self.label_2.setToolTip(_translate("ConverFMT", "Brief example"))
        self.groupBox.setTitle(_translate("ConverFMT", "Parameter"))
        self.checkBox.setText(_translate("ConverFMT", "Phylip Format"))
        self.checkBox_5.setText(_translate("ConverFMT", "Paml Format"))
        self.checkBox_2.setText(_translate("ConverFMT", "Nexus Format (sequential)"))
        self.checkBox_12.setText(_translate("ConverFMT", "Fasta Format"))
        self.checkBox_3.setText(_translate("ConverFMT", "Nexus Format (interleave)"))
        self.checkBox_9.setText(_translate("ConverFMT", "Sequence Statistics File"))
        self.checkBox_13.setText(_translate("ConverFMT", "Axt Format (for KaKs_Calculator2)"))
        self.groupBox_3.setTitle(_translate("ConverFMT", "Run"))
        self.pushButton.setText(_translate("ConverFMT", "Start"))
        self.pushButton_2.setText(_translate("ConverFMT", "Stop"))
        self.groupBox_5.setTitle(_translate("ConverFMT", "Progress"))

from src.CustomWidget import ArrowPushButton, ClickedLableGif, ListQCombobox
from uifiles import myRes_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConverFMT = QtWidgets.QDialog()
    ui = Ui_ConverFMT()
    ui.setupUi(ConverFMT)
    ConverFMT.show()
    sys.exit(app.exec_())

