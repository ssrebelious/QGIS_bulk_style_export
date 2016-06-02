# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Bulk Style Export
                                 A QGIS plugin
 Bulk export of the styles for the current project into QML or SLD formats
                             -------------------
        begin                : 2016-05-02
        copyright            : (C) 2016 by Yury Ryabov
        email                : riabovvv@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
from __future__ import unicode_literals


# noinspection PyPep8Naming


def classFactory(iface):
    """
    Load RoadService class from file RoadService.

        iface : QgsInterface,
            A QGIS interface instance.
    """
    #
    from bulk_style_export import BulkStylesExport
    return BulkStylesExport(iface)
