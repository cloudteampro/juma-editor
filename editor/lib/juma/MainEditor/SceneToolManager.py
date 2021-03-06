#!/usr/bin/env python

import logging
import weakref

from PySide             import QtCore, QtGui, QtOpenGL
from PySide.QtCore      import Qt

from juma.core 							import app, signals
from juma.qt.IconCache 					import getIcon
from juma.core.EditorModule				import EditorModule

##----------------------------------------------------------------##
class SceneToolMeta( type ):
	def __init__( cls, name, bases, dict ):
		super( SceneToolMeta, cls ).__init__( name, bases, dict )
		fullname = dict.get( 'name', None )
		shortcut = dict.get( 'shortcut', None )
		if not fullname: return
		app.getModule( 'scene_tool_manager' ).registerSceneTool( 
			fullname,
			cls,
			shortcut = shortcut
		 )

##----------------------------------------------------------------##
class SceneTool():
	__metaclass__ = SceneToolMeta

	def __init__( self ):
		self.category = None
		self.lastUseTime = -1

	def getId( self ):
		return 'unknown'

	def getName( self ):
		return 'Tool'

	def getIcon( self ):
		return 'null_thumbnail'

	def __repr__( self ):
		return '%s::%s' % ( repr(self.category), self.getId() )

	def onStart( self, **context ):
		pass

	def onStop( self ):
		pass

##----------------------------------------------------------------##

_SceneToolButtons = weakref.WeakKeyDictionary()

##----------------------------------------------------------------##
class SceneToolButton( QtGui.QToolButton ):
	def __init__( self, toolId, **options ):
		super( SceneToolButton, self ).__init__()
		self.toolId = toolId
		iconPath = options.get( 'icon', 'tools/' + toolId )
		self.setIcon( getIcon( iconPath ) )
		_SceneToolButtons[ self ] = toolId
		self.setObjectName( 'SceneToolButton' )

	def mousePressEvent( self, event ):
		if self.isDown(): return;
		super( SceneToolButton, self ).mousePressEvent( event )
		app.getModule( 'scene_tool_manager' ).changeTool( self.toolId )

	def mouseReleaseEvent( self, event ):
		return

##----------------------------------------------------------------##
class SceneToolManager( EditorModule ):
	_name = 'scene_tool_manager'
	_dependency = [ 'moai', 'main_editor' ]

	def __init__( self ):				
		super( SceneToolManager, self ).__init__()
		self.toolRegistry = {}
		self.currentToolId = None
		self.currentTool  = None

	def onLoad( self ):
		pass

	def onStart( self ):
		for toolId, entry in self.toolRegistry.items():
			clas, options = entry
			shortcut = options.get( 'shortcut', None )
			if shortcut:
				self.addSceneToolShortcut( toolId, shortcut, context = 'main' )

	def registerSceneTool( self, toolId, clas, **options ):
		if self.toolRegistry.has_key( toolId ):
			logging.warning( 'duplicated scene tool id %s' % toolId )
			return
		self.toolRegistry[ toolId ] = ( clas, options )

	def addSceneToolShortcut( self, toolId, shortcut, **kwargs ):
		def shortcutAction():
			return self.changeTool( toolId )
		context = kwargs.get( 'context', 'main' )
		self.getModule( 'main_editor' ).addShortcut( context, shortcut, shortcutAction )

	def changeTool( self, toolId, **context ):
		if self.currentToolId == toolId:
			return

		toolClass, options = self.toolRegistry.get( toolId, None )
		if not toolClass:
			logging.warning( 'No scene tool found: %s' % toolId )
			return
		toolObj = toolClass()
		toolObj._toolId = toolId

		if self.currentTool:
			self.currentTool.onStop()

		self.currentTool = toolObj
		self.currentToolId = toolId

		toolObj.onStart( **context )

		for button, buttonToolId in _SceneToolButtons.items():
			if buttonToolId == toolId:
				button.setDown( True )
			else:
				button.setDown( False )
		signals.emit( 'scene_tool.change', self.currentToolId )

	def getCurrentTool( self ):
		return self.currentTool

	def getCurrentToolId( self ):
		return self.currentToolId

##----------------------------------------------------------------##

SceneToolManager().register()
