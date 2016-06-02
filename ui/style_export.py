# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from PyQt4 import QtGui, uic
from PyQt4.QtCore import Qt
from qgis.gui import QgsMessageBar
from qgis.utils import iface


STYLE_EXPORT_CLASS, STYLE_EXPORT_WIDGET = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'StyleExport.ui'))


class ExportStyles(STYLE_EXPORT_WIDGET, STYLE_EXPORT_CLASS):

    def __init__(self, parent=None):
        super(ExportStyles, self).__init__(parent)
        self.setupUi(self)
        self.pathBtn.clicked.connect(lambda: self.pickFolder(os.getcwd(), self.pathToFolderLine))

    def pickFolder(self, search_directory, where_display):
        '''
        Opens an Open Folder dialogue

        Parameters
        ----------

        search_directory: string,
            initial directory to search for folders

        where_display: QLineEdit widget,
            widget where selected option have to be displayed
        '''
        dir_name = QtGui.QFileDialog.getExistingDirectory(self, 'Export to folder...', search_directory)
        where_display.setText(dir_name)



if __name__ == '__main__':
    pass