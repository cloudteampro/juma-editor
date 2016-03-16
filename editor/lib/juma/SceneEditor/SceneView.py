import os.path

from PySide  import QtCore, QtGui, QtOpenGL

from juma.core 					import signals, app
from juma.moai.MOAIEditCanvas 	import  MOAIEditCanvas
from SceneEditor             	import SceneEditorModule



##----------------------------------------------------------------##
def _getModulePath( path ):
	return os.path.dirname( __file__ ) + '/' + path

##----------------------------------------------------------------##
class SceneView( SceneEditorModule ):
	_name       = 'scene_view'
	_dependency = [ 'scene_editor', 'scenegraph_editor' ]

	def __init__(self):
		super( SceneView, self ).__init__()

	def onLoad( self ):
		self.window = self.requestDocumentWindow(
				title = 'Scene'
			)

		self.tool = self.addToolBar( 'scene_view_config', self.window.addToolBar() )

		self.canvas = self.window.addWidget(
				SceneViewCanvas()
			)
		self.canvas.loadScript( _getModulePath('SceneView.lua') )

		self.window.show()

##----------------------------------------------------------------##

SceneView().register()

##----------------------------------------------------------------##
class SceneViewCanvas( MOAIEditCanvas ):
	def __init__( self, *args, **kwargs ):
		super( SceneViewCanvas, self ).__init__( *args, **kwargs )