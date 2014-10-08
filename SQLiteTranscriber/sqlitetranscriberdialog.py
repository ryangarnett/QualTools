# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SQLiteTranscriberDialog
                                 A QGIS plugin
 SQLite Transcriber allows you to add highlighted text as entries into a database
                             -------------------
        begin                : 2014-09-28
        copyright            : (C) 2014 by Thomas Pendergrass
        email                : thedragoshi@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
#import sqlite library

from PyQt4 import QtCore, QtGui
from ui_sqlitetranscriber import Ui_SQLiteTranscriber
import sqlite3
# create the dialog for zoom to point


class SQLiteTranscriberDialog(QtGui.QDialog, Ui_SQLiteTranscriber):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.textSource = ""
        self.setupUi(self)
        
        self.openDB_button.clicked.connect(self.openDatabase)
        self.save_button.clicked.connect(self.Save)
        self.saveAs_button.clicked.connect(self.SaveAs)
        self.load_button.clicked.connect(self.Load)
        self.submit_button.clicked.connect(self.Submit)
        self.table_box.currentIndexChanged.connect(self.update_columns)
        self.sqlite_connection = ""
        self.sql_cursor = ""
        self.shortcut = QtGui.QShortcut(QtGui.QKeySequence("Ctrl+D"), self, self.Submit)
        self.shortcut = QtGui.QShortcut(QtGui.QKeySequence("Ctrl+S"), self, self.Save)
        
    def openDatabase(self):
        #Open Dialog to connect to sqlite database
        newPath = QtGui.QFileDialog.getOpenFileName(self, "Open Database", "/home", "Database (*.sqlite *.db)")
        if newPath == "":
            self.status_label.setText("Disconnected")
            return
        self.dbPath_text.setText(newPath)
        self.sqlite_connection = sqlite3.connect(newPath)
        self.sql_cursor = self.sqlite_connection.cursor()
        #Fill combo boxes
        #fill tables box
        self.table_box.clear()
        self.sql_cursor.execute("SELECT name from sqlite_master WHERE type = 'table'")
        response = self.sql_cursor.fetchall()
        print response
        #Fail if database is empty
        if response == None:
            self.status_label.setText("Can't connect to empty database!")
            return
        for item in response:
            self.table_box.addItem(item[0])
        #fill columns box
        self.update_columns()
        self.status_label.setText("Connected")
        
    #on select table, load new column sets
    def update_columns(self):
        tableName = self.table_box.currentText()
        self.column_box.clear()
        self.sql_cursor.execute("SELECT * from %s" % tableName)
        columns = self.sql_cursor.description
        for col in columns:
            self.column_box.addItem(col[0])
       
    
    #OnSave, if no previous .txt detected OR not loaded in, do saveAs, otherwise: save.
    def Save(self):
        print "Saving..."
        if self.textSource == "":
            self.SaveAs()
            return
        f = open(self.textSource, 'w')
        f.write(self.text_edit.toPlainText())
        f.close()
        print "Saved."
        self.status_label.setText("Saved current session.")
    
    #Ask to overwrite if file exists
    
    #On saveAs
    def SaveAs(self):
        print "Save As"
        newPath = QtGui.QFileDialog.getSaveFileName(self, "Save .txt File", "/home")
        if newPath == "":
            return
        f = open(newPath, 'w')
        f.write(self.text_edit.toPlainText())
        f.close()
        self.textSource = newPath
        print "Saved to: " + newPath
        self.status_label.setText("Saved session to new file.")
     #Ask to overwrite if file exists
     
    #On Load, fill text_edit with .txt contents
    def Load(self):
        print "loading..."
        newPath = QtGui.QFileDialog.getOpenFileName(self, "Open .txt File", "/home", "Text Document (*.txt)")
        if newPath == "":
            return
        f = open(newPath, 'r')
        contents = f.read()
        f.close
        self.text_edit.setText(contents)
        print "loaded " + newPath
        self.status_label.setText("Loaded a text file.")
    
    #On Submit: Add entry into a database
    def Submit(self):
        thisText = self.text_edit.textCursor().selectedText().strip()
        print thisText
        self.sql_cursor.execute("insert into %s (%s) values ('%s')" % (self.table_box.currentText(), self.column_box.currentText(), thisText))
        self.sqlite_connection.commit()
        print "Submit: " + thisText
        self.status_label.setText("Submitted a word: " + thisText)
