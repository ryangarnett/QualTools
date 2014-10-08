# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_sqlitetranscriber.ui'
#
# Created: Sun Sep 28 22:55:18 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SQLiteTranscriber(object):
    def setupUi(self, SQLiteTranscriber):
        SQLiteTranscriber.setObjectName(_fromUtf8("SQLiteTranscriber"))
        SQLiteTranscriber.resize(472, 346)
        SQLiteTranscriber.setAcceptDrops(False)
        SQLiteTranscriber.setAutoFillBackground(True)
        SQLiteTranscriber.setSizeGripEnabled(True)
        self.gridLayout = QtGui.QGridLayout(SQLiteTranscriber)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.submit_button = QtGui.QPushButton(SQLiteTranscriber)
        self.submit_button.setObjectName(_fromUtf8("submit_button"))
        self.horizontalLayout_3.addWidget(self.submit_button)
        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_2 = QtGui.QLabel(SQLiteTranscriber)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_4.addWidget(self.label_2)
        self.status_label = QtGui.QLabel(SQLiteTranscriber)
        self.status_label.setObjectName(_fromUtf8("status_label"))
        self.horizontalLayout_4.addWidget(self.status_label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.save_button = QtGui.QPushButton(SQLiteTranscriber)
        self.save_button.setObjectName(_fromUtf8("save_button"))
        self.horizontalLayout_2.addWidget(self.save_button)
        self.saveAs_button = QtGui.QPushButton(SQLiteTranscriber)
        self.saveAs_button.setObjectName(_fromUtf8("saveAs_button"))
        self.horizontalLayout_2.addWidget(self.saveAs_button)
        self.load_button = QtGui.QPushButton(SQLiteTranscriber)
        self.load_button.setObjectName(_fromUtf8("load_button"))
        self.horizontalLayout_2.addWidget(self.load_button)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.openDB_button = QtGui.QPushButton(SQLiteTranscriber)
        self.openDB_button.setObjectName(_fromUtf8("openDB_button"))
        self.horizontalLayout.addWidget(self.openDB_button)
        self.dbPath_text = QtGui.QLineEdit(SQLiteTranscriber)
        self.dbPath_text.setObjectName(_fromUtf8("dbPath_text"))
        self.horizontalLayout.addWidget(self.dbPath_text)
        self.table_box = QtGui.QComboBox(SQLiteTranscriber)
        self.table_box.setObjectName(_fromUtf8("table_box"))
        self.horizontalLayout.addWidget(self.table_box)
        self.column_box = QtGui.QComboBox(SQLiteTranscriber)
        self.column_box.setObjectName(_fromUtf8("column_box"))
        self.horizontalLayout.addWidget(self.column_box)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.text_edit = QtGui.QTextEdit(SQLiteTranscriber)
        self.text_edit.setObjectName(_fromUtf8("text_edit"))
        self.gridLayout.addWidget(self.text_edit, 4, 0, 1, 1)

        self.retranslateUi(SQLiteTranscriber)
        QtCore.QMetaObject.connectSlotsByName(SQLiteTranscriber)

    def retranslateUi(self, SQLiteTranscriber):
        SQLiteTranscriber.setWindowTitle(_translate("SQLiteTranscriber", "SQLiteTranscriber", None))
        self.submit_button.setText(_translate("SQLiteTranscriber", "Add Selection", None))
        self.label_2.setText(_translate("SQLiteTranscriber", "Status:", None))
        self.status_label.setText(_translate("SQLiteTranscriber", "Disconnected", None))
        self.save_button.setText(_translate("SQLiteTranscriber", "Save", None))
        self.saveAs_button.setText(_translate("SQLiteTranscriber", "Save As", None))
        self.load_button.setText(_translate("SQLiteTranscriber", "Load", None))
        self.openDB_button.setText(_translate("SQLiteTranscriber", "Open Database", None))

