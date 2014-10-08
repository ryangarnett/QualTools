# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SQLiteTranscriber
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
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load SQLiteTranscriber class from file SQLiteTranscriber
    from sqlitetranscriber import SQLiteTranscriber
    return SQLiteTranscriber(iface)
