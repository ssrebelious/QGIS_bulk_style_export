# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from PyQt4.QtCore import QObject, SIGNAL, Qt
from PyQt4.QtGui import QIcon
from PyQt4.Qt import QAction

from ui.style_export import ExportStyles


class BulkStylesExport:
    def __init__(self, iface):
        self.iface = iface
        self.dialogue_window = ExportStyles()

    def initGui(self):
        iconPath = os.path.join(os.path.dirname(__file__), 'icon.png')
        icon = QIcon(iconPath)
        # Create action
        self.action = QAction(icon, 'Bulk Export Styles', self.iface.mainWindow())
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)
        # Add toolbar
        # self.toolbar = self.iface.addToolBar('Bulk Export Styles')
        # self.toolbar.addAction(self.action)
        # self.iface.registerMainWindowAction(self.action, 'F3')
        self.iface.addPluginToMenu("&Bulk Export Styles", self.action)
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        self.iface.removePluginMenu("&Bulk Export Styles", self.action)
        self.iface.removeToolBarIcon(self.action)
        self.iface.unregisterMainWindowAction(self.action)
        # del self.toolbar

    def run(self):
        self.dialogue_window.show()
        self.dialogue_window.addLayersToCbox()


