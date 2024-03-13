# Form implementation generated from reading ui file 'diskIDMainGUI.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_kryoMain(object):
    def setupUi(self, kryoMain):
        kryoMain.setObjectName("kryoMain")
        kryoMain.resize(770, 600)
        self.centralwidget = QtWidgets.QWidget(parent=kryoMain)
        self.centralwidget.setObjectName("centralwidget")
        self.chooseFormats = QtWidgets.QPushButton(parent=self.centralwidget)
        self.chooseFormats.setGeometry(QtCore.QRect(30, 10, 201, 27))
        self.chooseFormats.setObjectName("chooseFormats")
        self.createImages = QtWidgets.QPushButton(parent=self.centralwidget)
        self.createImages.setGeometry(QtCore.QRect(30, 50, 201, 71))
        self.createImages.setObjectName("createImages")
        self.tryMounting = QtWidgets.QPushButton(parent=self.centralwidget)
        self.tryMounting.setGeometry(QtCore.QRect(30, 330, 191, 27))
        self.tryMounting.setObjectName("tryMounting")
        self.imageCreationResults = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.imageCreationResults.setGeometry(QtCore.QRect(30, 140, 711, 181))
        self.imageCreationResults.setObjectName("imageCreationResults")
        self.MountingResults = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.MountingResults.setGeometry(QtCore.QRect(31, 360, 711, 192))
        self.MountingResults.setObjectName("MountingResults")
        self.deleteUnmountable = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.deleteUnmountable.setGeometry(QtCore.QRect(225, 333, 171, 22))
        self.deleteUnmountable.setChecked(False)
        self.deleteUnmountable.setObjectName("deleteUnmountable")
        self.browseOutputDir = QtWidgets.QPushButton(parent=self.centralwidget)
        self.browseOutputDir.setGeometry(QtCore.QRect(250, 80, 141, 27))
        self.browseOutputDir.setObjectName("browseOutputDir")
        self.browseInpDir = QtWidgets.QPushButton(parent=self.centralwidget)
        self.browseInpDir.setGeometry(QtCore.QRect(250, 46, 141, 27))
        self.browseInpDir.setObjectName("browseInpDir")
        self.browseDTCDir = QtWidgets.QPushButton(parent=self.centralwidget)
        self.browseDTCDir.setGeometry(QtCore.QRect(250, 10, 141, 27))
        self.browseDTCDir.setObjectName("browseDTCDir")
        self.inputDir = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.inputDir.setGeometry(QtCore.QRect(410, 46, 331, 27))
        self.inputDir.setObjectName("inputDir")
        self.outputDir = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.outputDir.setGeometry(QtCore.QRect(410, 80, 331, 27))
        self.outputDir.setObjectName("outputDir")
        self.DTCDir = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.DTCDir.setGeometry(QtCore.QRect(410, 11, 331, 27))
        self.DTCDir.setObjectName("DTCDir")
        self.saveMountingResults = QtWidgets.QPushButton(parent=self.centralwidget)
        self.saveMountingResults.setGeometry(QtCore.QRect(601, 330, 141, 27))
        self.saveMountingResults.setObjectName("saveMountingResults")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 319, 711, 16))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.saveDTCResults = QtWidgets.QPushButton(parent=self.centralwidget)
        self.saveDTCResults.setGeometry(QtCore.QRect(601, 109, 141, 27))
        self.saveDTCResults.setObjectName("saveDTCResults")
        self.DTCInstances = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.DTCInstances.setGeometry(QtCore.QRect(503, 109, 41, 27))
        self.DTCInstances.setObjectName("DTCInstances")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(253, 115, 261, 17))
        self.label.setObjectName("label")
        kryoMain.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=kryoMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 770, 25))
        self.menubar.setObjectName("menubar")
        kryoMain.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=kryoMain)
        self.statusbar.setObjectName("statusbar")
        kryoMain.setStatusBar(self.statusbar)

        self.retranslateUi(kryoMain)
        self.chooseFormats.clicked.connect(kryoMain.choose_formats) # type: ignore
        self.createImages.clicked.connect(kryoMain.create_images) # type: ignore
        self.tryMounting.clicked.connect(kryoMain.try_mounting) # type: ignore
        self.browseDTCDir.clicked.connect(kryoMain.browse_dtc_dir) # type: ignore
        self.browseInpDir.clicked.connect(kryoMain.browse_inp_dir) # type: ignore
        self.browseOutputDir.clicked.connect(kryoMain.browse_output_dir) # type: ignore
        self.deleteUnmountable.stateChanged['int'].connect(kryoMain.delete_unmountable_change) # type: ignore
        self.saveMountingResults.clicked.connect(kryoMain.save_mounting_results) # type: ignore
        self.saveDTCResults.clicked.connect(kryoMain.save_dtc_results) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(kryoMain)

    def retranslateUi(self, kryoMain):
        _translate = QtCore.QCoreApplication.translate
        kryoMain.setWindowTitle(_translate("kryoMain", "Disk format identifier"))
        self.chooseFormats.setText(_translate("kryoMain", "Choose formats to create"))
        self.createImages.setText(_translate("kryoMain", "Create images"))
        self.tryMounting.setText(_translate("kryoMain", "Try mounting"))
        self.deleteUnmountable.setText(_translate("kryoMain", "Delete unmountable"))
        self.browseOutputDir.setText(_translate("kryoMain", "Output Directory"))
        self.browseInpDir.setText(_translate("kryoMain", "Input Directory"))
        self.browseDTCDir.setText(_translate("kryoMain", "DTC Directory"))
        self.saveMountingResults.setText(_translate("kryoMain", "Save Results"))
        self.saveDTCResults.setText(_translate("kryoMain", "Save Results"))
        self.label.setText(_translate("kryoMain", "Maximum concurrent DTC instances:"))
