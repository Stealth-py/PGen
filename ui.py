# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):


        '''
        IncludeLeetCheck -
            CheckBox for including Leet combinations
        IncludeWLCheck -
            CheckBox for including a word list
        CustomWordsText -
            A text box for making combinations of a custom word
        AddPrefixText -
            A text box for adding a prefix before the combinations
        AddSuffixText -
            A text box for adding a suffix after the combinations
        IncludeCombosCheck -
            A check box for giving the option to add combinations of prefix
        IncludeNumsPreCheck -
            A check box for including numbers as prefix
        IncludeNumsSufCheck -
            A check box for including numbers as suffix
        PrefixNumLenCheck -
            A spin box for setting the length of numbers as the prefix
        SuffixNumLenCheck -
            A spin box for setting the length of numbers as the suffix
        IncludeNumsCheck -
            A check box for including numbers in the wordlist
        DefaultListCheck -
            A check box for using the default character list (abcdefghizjklmonpqrstuvqxyz)
        MinComboLenCheck -
            A spin box for setting the minimum length of combinations
        MaxComboLenCheck -
            A spin box for setting the maximum length of combinations
        CustomListText -
            A text box for making a custom character list
        ExtendDefaultListText -
            A text box for extending the default character list
        Generate -
            A button to make the combinations
        '''

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(543, 905)
        MainWindow.setAutoFillBackground(True)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Setting for CustomListText
        self.CustomListText = QtWidgets.QTextEdit(self.centralwidget)
        self.CustomListText.setGeometry(QtCore.QRect(40, 680, 101, 31))
        self.CustomListText.setObjectName("CustomListText")


        #Setting for Generate
        self.Generate = QtWidgets.QPushButton(self.centralwidget)
        self.Generate.setGeometry(QtCore.QRect(190, 800, 141, 41))
        self.Generate.setObjectName("Generate")


        #Setting for IncludeWLCheck
        self.IncludeWLCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.IncludeWLCheck.setGeometry(QtCore.QRect(40, 110, 16, 17))
        self.IncludeWLCheck.setText("")
        self.IncludeWLCheck.setChecked(False)
        self.IncludeWLCheck.setObjectName("IncludeWLCheck")


        #Setting for DefaultListLabel
        self.DefaultListLabel = QtWidgets.QLabel(self.centralwidget)
        self.DefaultListLabel.setGeometry(QtCore.QRect(70, 570, 161, 16))
        self.DefaultListLabel.setObjectName("DefaultListLabel")
        self.MaxComboLenLabel = QtWidgets.QLabel(self.centralwidget)
        self.MaxComboLenLabel.setGeometry(QtCore.QRect(100, 640, 101, 20))
        self.MaxComboLenLabel.setObjectName("MaxComboLenLabel")


        #Setting for LeetCombinationsLabel
        self.LeetCombinationsLabel = QtWidgets.QLabel(self.centralwidget)
        self.LeetCombinationsLabel.setGeometry(QtCore.QRect(70, 80, 131, 21))
        self.LeetCombinationsLabel.setAutoFillBackground(True)
        self.LeetCombinationsLabel.setObjectName("LeetCombinationsLabel")


        #Setting for WLSettingsLabel
        self.WLSettingsLabel = QtWidgets.QLabel(self.centralwidget)
        self.WLSettingsLabel.setGeometry(QtCore.QRect(30, 490, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.WLSettingsLabel.setFont(font)
        self.WLSettingsLabel.setObjectName("WLSettingsLabel")


        #Setting for CustomListLabel
        self.CustomListLabel = QtWidgets.QLabel(self.centralwidget)
        self.CustomListLabel.setGeometry(QtCore.QRect(160, 685, 271, 21))
        self.CustomListLabel.setObjectName("CustomListLabel")


        #Setting for IncludeNumsCheck
        self.IncludeNumsCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.IncludeNumsCheck.setGeometry(QtCore.QRect(40, 540, 16, 17))
        self.IncludeNumsCheck.setText("")
        self.IncludeNumsCheck.setObjectName("IncludeNumsCheck")


        #Setting for GenWordListLabel
        self.GenWordListLabel = QtWidgets.QLabel(self.centralwidget)
        self.GenWordListLabel.setGeometry(QtCore.QRect(70, 110, 111, 16))
        self.GenWordListLabel.setAutoFillBackground(True)
        self.GenWordListLabel.setObjectName("GenWordListLabel")
 

        #Setting for IncludeLeetCheck
        self.IncludeLeetCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.IncludeLeetCheck.setGeometry(QtCore.QRect(40, 80, 16, 17))
        self.IncludeLeetCheck.setText("")
        self.IncludeLeetCheck.setObjectName("IncludeLeetCheck")


        #Setting for IncludeNumsLabel
        self.IncludeNumsLabel = QtWidgets.QLabel(self.centralwidget)
        self.IncludeNumsLabel.setGeometry(QtCore.QRect(70, 540, 91, 16))
        self.IncludeNumsLabel.setObjectName("IncludeNumsLabel")


        #Setting for DefaultListCheck
        self.DefaultListCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.DefaultListCheck.setGeometry(QtCore.QRect(40, 570, 16, 17))
        self.DefaultListCheck.setText("")
        self.DefaultListCheck.setObjectName("DefaultListCheck")

 
        #Setting for MinComboLenlabel
        self.MinComboLenLabel = QtWidgets.QLabel(self.centralwidget)
        self.MinComboLenLabel.setGeometry(QtCore.QRect(100, 600, 91, 20))
        self.MinComboLenLabel.setObjectName("MinComboLenLabel")


        #Setting for GenralSettingsLabel
        self.GenralSettingsLabel = QtWidgets.QLabel(self.centralwidget)
        self.GenralSettingsLabel.setGeometry(QtCore.QRect(30, 30, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.GenralSettingsLabel.setFont(font)
        self.GenralSettingsLabel.setObjectName("GenralSettingsLabel")


        #Setting for ExtendDefaultListText
        self.ExtendDefaultListText = QtWidgets.QTextEdit(self.centralwidget)
        self.ExtendDefaultListText.setGeometry(QtCore.QRect(40, 720, 101, 31))
        self.ExtendDefaultListText.setObjectName("ExtendDefaultListText")
        self.ExtandDefaultListLabel = QtWidgets.QLabel(self.centralwidget)
        self.ExtandDefaultListLabel.setGeometry(QtCore.QRect(160, 719, 161, 31))
        self.ExtandDefaultListLabel.setObjectName("ExtandDefaultListLabel")


        #Setting for PrefixSuffixSettingsLabel
        self.PrefixSuffixSettingsLabel = QtWidgets.QLabel(self.centralwidget)
        self.PrefixSuffixSettingsLabel.setGeometry(QtCore.QRect(30, 200, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PrefixSuffixSettingsLabel.setFont(font)
        self.PrefixSuffixSettingsLabel.setObjectName("PrefixSuffixSettingsLabel")


        #Setting for CustomWordsText
        self.CustomWordsText = QtWidgets.QTextEdit(self.centralwidget)
        self.CustomWordsText.setGeometry(QtCore.QRect(40, 140, 104, 31))
        self.CustomWordsText.setObjectName("CustomWordsText")
        self.CustomWordsLabel = QtWidgets.QLabel(self.centralwidget)
        self.CustomWordsLabel.setGeometry(QtCore.QRect(160, 140, 231, 31))
        self.CustomWordsLabel.setObjectName("CustomWordsLabel")


        #Setting for AddPrefixText
        self.AddPrefixText = QtWidgets.QTextEdit(self.centralwidget)
        self.AddPrefixText.setGeometry(QtCore.QRect(40, 230, 104, 31))
        self.AddPrefixText.setObjectName("AddPrefixText")


        #Setting for AddSuffixText
        self.AddSuffixText = QtWidgets.QTextEdit(self.centralwidget)
        self.AddSuffixText.setGeometry(QtCore.QRect(40, 280, 104, 31))
        self.AddSuffixText.setObjectName("AddSuffixText")


        #Setting for IncludeCombosCheck
        self.IncludeCombosCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.IncludeCombosCheck.setGeometry(QtCore.QRect(40, 320, 16, 17))
        self.IncludeCombosCheck.setText("")
        self.IncludeCombosCheck.setChecked(False)
        self.IncludeCombosCheck.setObjectName("IncludeCombosCheck")


        #Setting for IncludeNumsPreCheck
        self.IncludeNumsPreCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.IncludeNumsPreCheck.setGeometry(QtCore.QRect(40, 350, 16, 17))
        self.IncludeNumsPreCheck.setText("")
        self.IncludeNumsPreCheck.setChecked(False)
        self.IncludeNumsPreCheck.setObjectName("IncludeNumsPreCheck")


        #Setting for AddPrefixLabel
        self.AddPrefixLabel = QtWidgets.QLabel(self.centralwidget)
        self.AddPrefixLabel.setGeometry(QtCore.QRect(170, 240, 61, 21))
        self.AddPrefixLabel.setObjectName("AddPrefixLabel")
        self.AddSuffixLabel = QtWidgets.QLabel(self.centralwidget)
        self.AddSuffixLabel.setGeometry(QtCore.QRect(170, 290, 71, 21))
        self.AddSuffixLabel.setObjectName("AddSuffixLabel")


        #Setting for IncludeCombosLabel
        self.IncludeCombosLabel = QtWidgets.QLabel(self.centralwidget)
        self.IncludeCombosLabel.setGeometry(QtCore.QRect(80, 320, 211, 16))
        self.IncludeCombosLabel.setObjectName("IncludeCombosLabel")


        #Setting for IncludeNumsPreLabel
        self.IncludeNumsPreLabel = QtWidgets.QLabel(self.centralwidget)
        self.IncludeNumsPreLabel.setGeometry(QtCore.QRect(80, 346, 131, 20))
        self.IncludeNumsPreLabel.setObjectName("IncludeNumsPreLabel")


        #Setting for IncludeNumsSufCheck
        self.IncludeNumsSufCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.IncludeNumsSufCheck.setGeometry(QtCore.QRect(40, 380, 16, 17))
        self.IncludeNumsSufCheck.setText("")
        self.IncludeNumsSufCheck.setObjectName("IncludeNumsSufCheck")


        #Setting for IncludeNumsSufLabel
        self.IncludeNumsSufLabel = QtWidgets.QLabel(self.centralwidget)
        self.IncludeNumsSufLabel.setGeometry(QtCore.QRect(80, 380, 131, 20))
        self.IncludeNumsSufLabel.setObjectName("IncludeNumsSufLabel")


        #Setting for SuffixNumLenLabel
        self.SuffixNumLenLabel = QtWidgets.QLabel(self.centralwidget)
        self.SuffixNumLenLabel.setGeometry(QtCore.QRect(100, 460, 111, 20))
        self.SuffixNumLenLabel.setObjectName("SuffixNumLenLabel")


        #Setting for PrefixNumLenLabel
        self.PrefixNumLenLabel = QtWidgets.QLabel(self.centralwidget)
        self.PrefixNumLenLabel.setGeometry(QtCore.QRect(100, 420, 111, 20))
        self.PrefixNumLenLabel.setObjectName("PrefixNumLenLabel")


        #Setting for MinComboLenCheck
        self.MinComboLenCheck = QtWidgets.QSpinBox(self.centralwidget)
        self.MinComboLenCheck.setGeometry(QtCore.QRect(40, 600, 42, 22))
        self.MinComboLenCheck.setObjectName("MinComboLenCheck")


        #Setting for MacComboLenCheck
        self.MaxComboLenCheck = QtWidgets.QSpinBox(self.centralwidget)
        self.MaxComboLenCheck.setGeometry(QtCore.QRect(40, 640, 42, 22))
        self.MaxComboLenCheck.setObjectName("MaxComboLenCheck")


        #Setting for PrefixNumLenCheck
        self.PrefixNumLenCheck = QtWidgets.QSpinBox(self.centralwidget)
        self.PrefixNumLenCheck.setGeometry(QtCore.QRect(40, 420, 42, 22))
        self.PrefixNumLenCheck.setObjectName("PrefixNumLenCheck")


        #Setting for SuffixNumLenCheck
        self.SuffixNumLenCheck = QtWidgets.QSpinBox(self.centralwidget)
        self.SuffixNumLenCheck.setGeometry(QtCore.QRect(40, 460, 42, 22))
        self.SuffixNumLenCheck.setObjectName("SuffixNumLenCheck")



        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 543, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        #Texts for the widgets
        self.Generate.setText(_translate("MainWindow", "Generate Combinations"))
        self.DefaultListLabel.setText(_translate("MainWindow", "Use default alphabet list (abc...)"))
        self.MaxComboLenLabel.setText(_translate("MainWindow", "Max. Combo Length"))
        self.LeetCombinationsLabel.setText(_translate("MainWindow", "Include Leet Combinatons"))
        self.WLSettingsLabel.setText(_translate("MainWindow", "Settings for word list"))
        self.CustomListLabel.setText(_translate("MainWindow", "Custom Characters (Overrides the default alphabet list)"))
        self.GenWordListLabel.setText(_translate("MainWindow", "Generate a word list"))
        self.IncludeNumsLabel.setText(_translate("MainWindow", "Include Numbers"))
        self.MinComboLenLabel.setText(_translate("MainWindow", "Min. Combo length"))
        self.GenralSettingsLabel.setText(_translate("MainWindow", "General Settings"))
        self.ExtandDefaultListLabel.setText(_translate("MainWindow", "Extend the default alphabet list"))
        self.PrefixSuffixSettingsLabel.setText(_translate("MainWindow", "Prefix and Suffix settings"))
        self.CustomWordsLabel.setText(_translate("MainWindow", "Custom word (Combinations for a custom word)"))
        self.AddPrefixLabel.setText(_translate("MainWindow", "Add Prefix"))
        self.AddSuffixLabel.setText(_translate("MainWindow", "Add Suffix"))
        self.IncludeCombosLabel.setText(_translate("MainWindow", "Add combinations of prefixes and suffixes"))
        self.IncludeNumsPreLabel.setText(_translate("MainWindow", "Add Numbers as prefix"))
        self.IncludeNumsSufLabel.setText(_translate("MainWindow", "Add Numbers as suffix"))
        self.SuffixNumLenLabel.setText(_translate("MainWindow", "Suffix Number Length"))
        self.PrefixNumLenLabel.setText(_translate("MainWindow", "Prefix Number Length"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
