# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Work\python\bioinfo_excercise\PhyloSuite\PhyloSuite\PhyloSuite\uifiles\ModelFinder.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ModelFinder(object):
    def setupUi(self, ModelFinder):
        ModelFinder.setObjectName("ModelFinder")
        ModelFinder.resize(518, 526)
        self.gridLayout_4 = QtWidgets.QGridLayout(ModelFinder)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_4 = QtWidgets.QGroupBox(ModelFinder)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEdit = InputQLineEdit(self.groupBox_4)
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit.setText("")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(30, 26))
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 26))
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.lineEdit_2 = InputQLineEdit(self.groupBox_4)
        self.lineEdit_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(30, 26))
        self.pushButton_4.setMaximumSize(QtCore.QSize(30, 26))
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 2, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 2, 0, 1, 1)
        self.lineEdit_3 = InputQLineEdit(self.groupBox_4)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_22.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_22.sizePolicy().hasHeightForWidth())
        self.pushButton_22.setSizePolicy(sizePolicy)
        self.pushButton_22.setMinimumSize(QtCore.QSize(30, 26))
        self.pushButton_22.setMaximumSize(QtCore.QSize(30, 26))
        self.pushButton_22.setStyleSheet("")
        self.pushButton_22.setText("")
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout.addWidget(self.pushButton_22, 2, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setOpenExternalLinks(True)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_2.addWidget(self.label_14)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_2 = ClickedLableGif(self.groupBox_4)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 0, 1, 3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 2)
        self.gridLayout_4.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(ModelFinder)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_24 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 0, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setMinimumSize(QtCore.QSize(13, 26))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_3, 0, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.gridLayout_2.addWidget(self.label_27, 0, 2, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_6.sizePolicy().hasHeightForWidth())
        self.comboBox_6.setSizePolicy(sizePolicy)
        self.comboBox_6.setMinimumSize(QtCore.QSize(13, 26))
        self.comboBox_6.setObjectName("comboBox_6")
        self.gridLayout_2.addWidget(self.comboBox_6, 0, 3, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 1, 0, 1, 1)
        self.comboBox_9 = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_9.sizePolicy().hasHeightForWidth())
        self.comboBox_9.setSizePolicy(sizePolicy)
        self.comboBox_9.setMinimumSize(QtCore.QSize(114, 26))
        self.comboBox_9.setMaximumSize(QtCore.QSize(16777215, 26))
        self.comboBox_9.setStyleSheet("")
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_9, 1, 1, 1, 3)
        self.label_25 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout_2.addWidget(self.label_25, 2, 0, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy)
        self.comboBox_4.setMinimumSize(QtCore.QSize(13, 26))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_4, 2, 1, 1, 3)
        self.label_26 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 3, 0, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy)
        self.comboBox_5.setMinimumSize(QtCore.QSize(13, 26))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_5, 3, 1, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setAutoRepeat(False)
        self.checkBox_2.setAutoExclusive(False)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_2.addWidget(self.checkBox_2, 3, 2, 1, 2)
        self.gridLayout_4.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(ModelFinder)
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
        self.groupBox_6 = QtWidgets.QGroupBox(ModelFinder)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_6)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/picture/resourses/Eye_Care_Services-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_7.addWidget(self.pushButton_9, 1, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_6)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_7.addWidget(self.progressBar, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_6, 3, 0, 1, 1)
        self.label_24.setBuddy(self.comboBox_3)
        self.label_27.setBuddy(self.comboBox_3)
        self.label_25.setBuddy(self.comboBox_3)
        self.label_26.setBuddy(self.comboBox_3)

        self.retranslateUi(ModelFinder)
        QtCore.QMetaObject.connectSlotsByName(ModelFinder)
        ModelFinder.setTabOrder(self.pushButton_3, self.lineEdit_3)
        ModelFinder.setTabOrder(self.lineEdit_3, self.pushButton_4)
        ModelFinder.setTabOrder(self.pushButton_4, self.pushButton_9)
        ModelFinder.setTabOrder(self.pushButton_9, self.lineEdit_2)
        ModelFinder.setTabOrder(self.lineEdit_2, self.comboBox_3)
        ModelFinder.setTabOrder(self.comboBox_3, self.pushButton_22)
        ModelFinder.setTabOrder(self.pushButton_22, self.lineEdit)
        ModelFinder.setTabOrder(self.lineEdit, self.comboBox_4)
        ModelFinder.setTabOrder(self.comboBox_4, self.comboBox_5)
        ModelFinder.setTabOrder(self.comboBox_5, self.comboBox_6)
        ModelFinder.setTabOrder(self.comboBox_6, self.pushButton_2)
        ModelFinder.setTabOrder(self.pushButton_2, self.pushButton)

    def retranslateUi(self, ModelFinder):
        _translate = QtCore.QCoreApplication.translate
        ModelFinder.setWindowTitle(_translate("ModelFinder", "ModelFinder"))
        self.groupBox_4.setTitle(_translate("ModelFinder", "Input"))
        self.label_5.setText(_translate("ModelFinder", "Alignment File:"))
        self.lineEdit.setPlaceholderText(_translate("ModelFinder", "PHYLIP, FASTA, NEXUS, CLUSTAL format is ok"))
        self.label_8.setText(_translate("ModelFinder", "Tree File:"))
        self.lineEdit_2.setPlaceholderText(_translate("ModelFinder", "Optional! (in newick format)"))
        self.checkBox.setText(_translate("ModelFinder", "Partition Mode:"))
        self.lineEdit_3.setPlaceholderText(_translate("ModelFinder", "Optional!"))
        self.label_7.setText(_translate("ModelFinder", "Partition Style:"))
        self.label_14.setText(_translate("ModelFinder", "<html><head/><body><p>Click <a href=\"http://www.iqtree.org/doc/\"><span style=\" text-decoration: underline; color:#0000ff;\">here</span></a> to learn more about <span style=\" font-weight:600; color:#ff0000;\">IQ-TREE</span></p></body></html>"))
        self.label_2.setToolTip(_translate("ModelFinder", "Brief example"))
        self.radioButton.setText(_translate("ModelFinder", "Edge-linked"))
        self.radioButton_2.setText(_translate("ModelFinder", "Edge-unlinked"))
        self.groupBox.setTitle(_translate("ModelFinder", "Parameters"))
        self.label_24.setText(_translate("ModelFinder", "Sequence Type:"))
        self.comboBox_3.setItemText(0, _translate("ModelFinder", "Auto detect"))
        self.comboBox_3.setItemText(1, _translate("ModelFinder", "DNA"))
        self.comboBox_3.setItemText(2, _translate("ModelFinder", "Protein"))
        self.comboBox_3.setItemText(3, _translate("ModelFinder", "Codon"))
        self.comboBox_3.setItemText(4, _translate("ModelFinder", "Binary"))
        self.comboBox_3.setItemText(5, _translate("ModelFinder", "Morphology"))
        self.comboBox_3.setItemText(6, _translate("ModelFinder", "DNA-->AA"))
        self.label_27.setText(_translate("ModelFinder", "Threads:"))
        self.label_22.setText(_translate("ModelFinder", "Code Table:"))
        self.comboBox_9.setItemText(0, _translate("ModelFinder", "1 The standard code"))
        self.comboBox_9.setItemText(1, _translate("ModelFinder", "2 Vertebrate mitochondrial code"))
        self.comboBox_9.setItemText(2, _translate("ModelFinder", "3 The Yeast Mitochondrial Code"))
        self.comboBox_9.setItemText(3, _translate("ModelFinder", "4 Mold, Protozoan, and Coelenterate Mitochondrial code and Mycoplasma/Spiroplasma code"))
        self.comboBox_9.setItemText(4, _translate("ModelFinder", "5 Invertebrate mitochondrial"))
        self.comboBox_9.setItemText(5, _translate("ModelFinder", "6 The Ciliate, Dasycladacean and Hexamita Nuclear Code"))
        self.comboBox_9.setItemText(6, _translate("ModelFinder", "9 Echinoderm and Flatworm mitochondrial code"))
        self.comboBox_9.setItemText(7, _translate("ModelFinder", "10 The Euplotid Nuclear Code"))
        self.comboBox_9.setItemText(8, _translate("ModelFinder", "11 The Bacterial, Archaeal and Plant Plastid Code"))
        self.comboBox_9.setItemText(9, _translate("ModelFinder", "12 The Alternative Yeast Nuclear Code"))
        self.comboBox_9.setItemText(10, _translate("ModelFinder", "13 Ascidian mitochondrial code"))
        self.comboBox_9.setItemText(11, _translate("ModelFinder", "14 Alternative flatworm mitochondrial code"))
        self.comboBox_9.setItemText(12, _translate("ModelFinder", "16 Chlorophycean Mitochondrial Code"))
        self.comboBox_9.setItemText(13, _translate("ModelFinder", "21 Trematode Mitochondrial Code"))
        self.comboBox_9.setItemText(14, _translate("ModelFinder", "22 Scenedesmus obliquus Mitochondrial Code"))
        self.comboBox_9.setItemText(15, _translate("ModelFinder", "23 Thraustochytrium Mitochondrial Code"))
        self.comboBox_9.setItemText(16, _translate("ModelFinder", "24 Pterobranchia Mitochondrial Code"))
        self.comboBox_9.setItemText(17, _translate("ModelFinder", "25 Candidate Division SR1 and Gracilibacteria Code"))
        self.label_25.setText(_translate("ModelFinder", "Criterion:"))
        self.comboBox_4.setItemText(0, _translate("ModelFinder", "Bayesian information criterion (BIC)"))
        self.comboBox_4.setItemText(1, _translate("ModelFinder", "Corrected AIC (AICc)"))
        self.comboBox_4.setItemText(2, _translate("ModelFinder", "Akaike information criterion (AIC)"))
        self.label_26.setText(_translate("ModelFinder", "Model for:"))
        self.comboBox_5.setItemText(0, _translate("ModelFinder", "IQ-TREE"))
        self.comboBox_5.setItemText(1, _translate("ModelFinder", "Mrbayes"))
        self.comboBox_5.setItemText(2, _translate("ModelFinder", "RAxML"))
        self.comboBox_5.setItemText(3, _translate("ModelFinder", "PhyML"))
        self.comboBox_5.setItemText(4, _translate("ModelFinder", "BEAST1"))
        self.comboBox_5.setItemText(5, _translate("ModelFinder", "BEAST2"))
        self.checkBox_2.setText(_translate("ModelFinder", "FreeRate heterogeneity [+R]"))
        self.groupBox_3.setTitle(_translate("ModelFinder", "Run"))
        self.pushButton.setText(_translate("ModelFinder", "Start"))
        self.pushButton_2.setText(_translate("ModelFinder", "Stop"))
        self.groupBox_6.setTitle(_translate("ModelFinder", "Progress"))
        self.pushButton_9.setText(_translate("ModelFinder", "Show log"))

from src.CustomWidget import ArrowPushButton, ClickedLableGif, InputQLineEdit
from uifiles import myRes_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ModelFinder = QtWidgets.QDialog()
    ui = Ui_ModelFinder()
    ui.setupUi(ModelFinder)
    ModelFinder.show()
    sys.exit(app.exec_())

