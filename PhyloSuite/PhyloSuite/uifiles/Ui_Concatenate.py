# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Work\python\bioinfo_excercise\PhyloSuite\PhyloSuite\PhyloSuite\uifiles\Concatenate.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Matrix(object):
    def setupUi(self, Matrix):
        Matrix.setObjectName("Matrix")
        Matrix.resize(546, 492)
        Matrix.setSizeGripEnabled(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(Matrix)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_4 = QtWidgets.QGroupBox(Matrix)
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
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_2 = ClickedLableGif(self.groupBox_4)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 3)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox = QtWidgets.QGroupBox(Matrix)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_4.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_12 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_12.setObjectName("checkBox_12")
        self.gridLayout_4.addWidget(self.checkBox_12, 0, 1, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_4.addWidget(self.checkBox_2, 1, 0, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_4.addWidget(self.checkBox_5, 1, 1, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_4.addWidget(self.checkBox_3, 2, 0, 1, 1)
        self.checkBox_13 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_13.setObjectName("checkBox_13")
        self.gridLayout_4.addWidget(self.checkBox_13, 2, 1, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_4.addWidget(self.checkBox_4, 3, 0, 1, 1)
        self.checkBox_9 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout_4.addWidget(self.checkBox_9, 3, 1, 1, 1)
        self.groupBox_top_line = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_top_line.setStyleSheet("")
        self.groupBox_top_line.setFlat(True)
        self.groupBox_top_line.setCheckable(True)
        self.groupBox_top_line.setChecked(False)
        self.groupBox_top_line.setObjectName("groupBox_top_line")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_top_line)
        self.gridLayout.setContentsMargins(0, 9, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_9 = QtWidgets.QLabel(self.groupBox_top_line)
        self.label_9.setEnabled(True)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)
        self.spinBox_5 = QtWidgets.QSpinBox(self.groupBox_top_line)
        self.spinBox_5.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_5.sizePolicy().hasHeightForWidth())
        self.spinBox_5.setSizePolicy(sizePolicy)
        self.spinBox_5.setMinimum(1)
        self.spinBox_5.setMaximum(99999)
        self.spinBox_5.setProperty("value", 5)
        self.spinBox_5.setObjectName("spinBox_5")
        self.gridLayout.addWidget(self.spinBox_5, 0, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_top_line)
        self.label_15.setEnabled(True)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 0, 2, 1, 1)
        self.spinBox_6 = QtWidgets.QSpinBox(self.groupBox_top_line)
        self.spinBox_6.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_6.sizePolicy().hasHeightForWidth())
        self.spinBox_6.setSizePolicy(sizePolicy)
        self.spinBox_6.setMinimum(1)
        self.spinBox_6.setMaximum(99999)
        self.spinBox_6.setProperty("value", 8)
        self.spinBox_6.setObjectName("spinBox_6")
        self.gridLayout.addWidget(self.spinBox_6, 0, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_top_line)
        self.label_10.setEnabled(True)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)
        self.spinBox_7 = QtWidgets.QSpinBox(self.groupBox_top_line)
        self.spinBox_7.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_7.sizePolicy().hasHeightForWidth())
        self.spinBox_7.setSizePolicy(sizePolicy)
        self.spinBox_7.setMinimum(1)
        self.spinBox_7.setMaximum(99999)
        self.spinBox_7.setProperty("value", 15)
        self.spinBox_7.setObjectName("spinBox_7")
        self.gridLayout.addWidget(self.spinBox_7, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_top_line)
        self.label_11.setEnabled(True)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 2, 1, 1)
        self.spinBox_8 = QtWidgets.QSpinBox(self.groupBox_top_line)
        self.spinBox_8.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_8.sizePolicy().hasHeightForWidth())
        self.spinBox_8.setSizePolicy(sizePolicy)
        self.spinBox_8.setSuffix("")
        self.spinBox_8.setMinimum(-360)
        self.spinBox_8.setMaximum(360)
        self.spinBox_8.setProperty("value", 45)
        self.spinBox_8.setObjectName("spinBox_8")
        self.gridLayout.addWidget(self.spinBox_8, 1, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_top_line)
        self.label_12.setEnabled(True)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 2, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_top_line)
        self.comboBox.setEnabled(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 2, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_top_line)
        self.label_13.setEnabled(True)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 2, 2, 1, 1)
        self.pushButton_color = QtWidgets.QPushButton(self.groupBox_top_line)
        self.pushButton_color.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_color.sizePolicy().hasHeightForWidth())
        self.pushButton_color.setSizePolicy(sizePolicy)
        self.pushButton_color.setAutoFillBackground(False)
        self.pushButton_color.setStyleSheet("")
        self.pushButton_color.setObjectName("pushButton_color")
        self.gridLayout.addWidget(self.pushButton_color, 2, 3, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_top_line, 5, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.gridLayout_4.addLayout(self.horizontalLayout, 4, 0, 1, 2)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(Matrix)
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
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_5 = QtWidgets.QGroupBox(Matrix)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_5)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_5.addWidget(self.progressBar, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_5)

        self.retranslateUi(Matrix)
        QtCore.QMetaObject.connectSlotsByName(Matrix)

    def retranslateUi(self, Matrix):
        _translate = QtCore.QCoreApplication.translate
        Matrix.setWindowTitle(_translate("Matrix", "Concatenate Sequence"))
        self.groupBox_4.setTitle(_translate("Matrix", "Input"))
        self.label_4.setText(_translate("Matrix", "Input:"))
        self.label_5.setText(_translate("Matrix", "<html><head/><body><p>Try to drag your <span style=\" font-weight:600; color:#ff0000;\">alignments</span> file and drop here if you want to use custom files</p></body></html>"))
        self.label_2.setToolTip(_translate("Matrix", "Brief example"))
        self.groupBox.setTitle(_translate("Matrix", "Parameter"))
        self.checkBox.setText(_translate("Matrix", "Phylip Format"))
        self.checkBox_12.setText(_translate("Matrix", "Fasta Format"))
        self.checkBox_2.setText(_translate("Matrix", "Nexus Format (sequential)"))
        self.checkBox_5.setText(_translate("Matrix", "Paml Format"))
        self.checkBox_3.setText(_translate("Matrix", "Nexus Format (interleave)"))
        self.checkBox_13.setText(_translate("Matrix", "Axt Format (for KaKs_Calculator2)"))
        self.checkBox_4.setText(_translate("Matrix", "Nexus Format (interleave: delimit by genes)"))
        self.checkBox_9.setText(_translate("Matrix", "Sequence Statistics File"))
        self.groupBox_top_line.setTitle(_translate("Matrix", "Linear figure"))
        self.label_9.setText(_translate("Matrix", "Figure height:"))
        self.spinBox_5.setSuffix(_translate("Matrix", " cm"))
        self.label_15.setText(_translate("Matrix", "Figure width:"))
        self.spinBox_6.setSuffix(_translate("Matrix", " cm"))
        self.label_10.setText(_translate("Matrix", "Label size:"))
        self.label_11.setText(_translate("Matrix", "Label angle:"))
        self.label_12.setText(_translate("Matrix", "Label position:"))
        self.comboBox.setItemText(0, _translate("Matrix", "start"))
        self.comboBox.setItemText(1, _translate("Matrix", "middle"))
        self.comboBox.setItemText(2, _translate("Matrix", "end"))
        self.label_13.setText(_translate("Matrix", "Label color:"))
        self.pushButton_color.setToolTip(_translate("Matrix", "Click to change color"))
        self.pushButton_color.setText(_translate("Matrix", "#F9C997"))
        self.label.setText(_translate("Matrix", "Export file name:"))
        self.lineEdit.setText(_translate("Matrix", "concatenation"))
        self.groupBox_3.setTitle(_translate("Matrix", "Run"))
        self.pushButton.setText(_translate("Matrix", "Start"))
        self.pushButton_2.setText(_translate("Matrix", "Stop"))
        self.groupBox_5.setTitle(_translate("Matrix", "Progress"))

from src.CustomWidget import ArrowPushButton, ClickedLableGif, ListQCombobox
from uifiles import myRes_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Matrix = QtWidgets.QDialog()
    ui = Ui_Matrix()
    ui.setupUi(Matrix)
    Matrix.show()
    sys.exit(app.exec_())

