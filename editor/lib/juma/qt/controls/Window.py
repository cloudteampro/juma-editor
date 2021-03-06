#!/usr/bin/env python

import os

from PySide import QtCore, QtGui
from PySide.QtGui import QApplication, QMainWindow
from PySide.QtCore import Qt, QSettings, QCoreApplication, QLocale

from juma.qt.helpers import restrainWidgetToScreen

from juma.core import signals
from juma.qt.controls.Menu import MenuManager

def getWindowScreenId(window):
    desktop=QtGui.QApplication.desktop()
    return desktop.screenNumber(window)
    
def moveWindowToCenter(window):
    desktop=QtGui.QApplication.desktop()
    geom=desktop.availableGeometry(window)
    x=(geom.width()-window.width())/2 +geom.x()
    y=(geom.height()-window.height())/2+geom.y()
    window.move(x,y)

##----------------------------------------------------------------##
class MainWindow( QMainWindow ):
    tabChanged = QtCore.Signal( QtGui.QWidget )
    tabRemoved = QtCore.Signal( QtGui.QWidget )

    def __init__(self, parent=None, script=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle( 'JUMA' )

        self.setBaseSize( 800, 600 )
        self.resize( 800, 600 )

        self.setUnifiedTitleAndToolBarOnMac( False )
        self.setDockOptions( QtGui.QMainWindow.AllowNestedDocks | QtGui.QMainWindow.AllowTabbedDocks )
        self.setDockNestingEnabled(True)
        self.setWindowModality(QtCore.Qt.NonModal)
        self.setMouseTracking(True)
        self.setFocusPolicy(QtCore.Qt.ClickFocus)

        self.defaultToolBarIconSize = 32
        font=QtGui.QFont()
        font.setPointSize(11)
        self.setFont(font)

        self.centerTabWidget = QtGui.QTabWidget( None )
        self.centerTabWidget.setTabsClosable( True )
        self.centerTabWidget.setMovable( True )

        self.setCentralWidget( self.centerTabWidget )

        self.centerTabWidget.currentChanged.connect( self.onDocumentTabChanged )
        self.centerTabWidget.tabCloseRequested.connect( self.onTabCloseRequested )


    def moveToCenter(self):
        moveWindowToCenter( self )

    def ensureVisible(self):
        restrainWidgetToScreen( self )

    def requestToolBar( self, name, **options ):
        toolbar = QtGui.QToolBar()
        toolbar.setFloatable( options.get( 'floatable', False ) )
        toolbar.setMovable(   options.get( 'movable',   True ) )        
        toolbar.setObjectName( 'toolbar-%s' % name )
        iconSize = options.get('icon_size', self.defaultToolBarIconSize )
        self.addToolBar( toolbar )
        toolbar.setIconSize( QtCore.QSize( iconSize, iconSize ) )
        toolbar._icon_size = iconSize
        return toolbar

    def requestSubWindow(self, id, **windowOption ):
        title = windowOption.get('title',id)
        
        window = SubWindow(self)
        window.setWindowTitle(title)

        window.windowMode = 'sub'
        window.titleBase = title

        minSize=windowOption.get('minSize',None)
        if minSize:
            window.setMinimumSize(*minSize)

        maxSize=windowOption.get('minSize',None)
        if maxSize:
            window.setMaximumSize( *maxSize )

        size=windowOption.get('size',None)
        if size:
            window.resize(*size)
        return window

    def requestDocumentWindow(self, id, **windowOption ):
        title  = windowOption.get('title',id)
        
        window = DocumentWindow( self.centerTabWidget )
        window.parentWindow = self
        window.setWindowTitle( title )

        window.windowMode = 'tab'
        window.titleBase = title

        minSize = windowOption.get('minSize',None)
        if minSize:
            window.setMinimumSize(*minSize)
        else:
            window.setMinimumSize(20,20)

        size = windowOption.get('size',None)
        if size:
            window.resize(*size)

        return window

    def requestDockWindow(self, id, **dockOptions ):
        title=dockOptions.get( 'title', id )

        dockArea=dockOptions.get('dock','left')
        
        if dockArea=='left':
            dockArea=Qt.LeftDockWidgetArea
        elif dockArea=='right':
            dockArea=Qt.RightDockWidgetArea
        elif dockArea=='top':
            dockArea=Qt.TopDockWidgetArea
        elif dockArea=='bottom':
            dockArea=Qt.BottomDockWidgetArea
        elif dockArea=='main':
            dockArea='center'
        elif dockArea=='float':
            dockArea = False
        elif dockArea:
            raise Exception('unsupported dock area:%s'%dockArea)
        
        window=DockWindow(self)
        if title:
            window.setWindowTitle(title)
        window.setObjectName('_dock_'+id)
        
        window.windowMode = 'dock'
        window.titleBase = title

        if dockOptions.get( 'allowDock', True ):
            window.setAllowedAreas( Qt.AllDockWidgetAreas )
        else:
            window.setAllowedAreas( Qt.NoDockWidgetArea )
            dockArea = None
            
        if dockArea and dockArea!='center':
            self.addDockWidget(dockArea, window)
        elif dockArea=='center':
            self.setCentralWidget(window)
            window.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
            window.hideTitleBar()
        else:
            window.setFloating(True)

        minSize=dockOptions.get('minSize',None)
        if minSize:
            window.setMinimumSize(*minSize)
        else:
            window.setMinimumSize(20,20)

        size=dockOptions.get('size',None)
        if size:
            window.resize(*size)

        if not dockOptions.get('autohide',False):
            window._useWindowFlags()

        window.dockOptions=dockOptions

        return window

    def requestToolWindow(self, id, **option ):
        pass

    def onTabCloseRequested( self, idx ):
        subwindow = self.centerTabWidget.widget( idx )
        if subwindow.close():
            self.tabRemoved.emit( subwindow )
            self.centerTabWidget.removeTab( idx )
        
    def onDocumentTabChanged( self, idx ):
        w = self.centerTabWidget.currentWidget()
        if w:
            self.tabChanged.emit( w )
            w.setFocus()

##----------------------------------------------------------------##
class SubWindow( QtGui.QMainWindow ):
    """docstring for DockWindow"""
    callbackOnClose = None
    
    def __init__(self, parent):
        super(SubWindow, self).__init__(parent)
        self.setupBasicUi()
        self.stayOnTop = False
        self.setFocusPolicy( Qt.WheelFocus )

    def setDocumentName( self, name ):
        self.documentName = name
        if name:
            title = '%s - %s' % ( self.documentName, self.titleBase )
            self.setWindowTitle( title )
        else:
            self.setWindowTitle( self.titleBase )

    def hideTitleBar(self):
        pass

    def startTimer(self, step, trigger):
        assert(hasattr(trigger,'__call__'))
        interval = 1000 * step
        timer=QtCore.QTimer(self)
        timer.timeout.connect(trigger)
        timer.start(interval)
        return timer

    def setupBasicUi(self):
        self.callbackOnClose = None
        self.container = self.createContainer()
        self.mainLayout = QtGui.QVBoxLayout(self.container)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setObjectName('MainLayout')

    def createContainer(self):
        container=QtGui.QWidget(self)
        self.setCentralWidget(container)
        return container

    def addWidget(self, widget, **layoutOption):
        if layoutOption.get('fixed', False):
            widget.setSizePolicy(
                QtGui.QSizePolicy.Fixed,
                QtGui.QSizePolicy.Fixed
                )
        elif layoutOption.get('expanding', True):
            widget.setSizePolicy(
                QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Expanding
                )       
        self.mainLayout.addWidget(widget)
        return widget

    def moveToCenter(self):
        moveWindowToCenter(self)

    def ensureVisible(self):
        restrainWidgetToScreen(self)

    def setCallbackOnClose( self, callback ):
        self.callbackOnClose = callback

    def onClose( self ):
        if self.callbackOnClose:
            return self.callbackOnClose()
        return True

    def focusOutEvent(self, event):
        pass

    def focusInEvent(self, event):
        pass

    def closeEvent( self, event ):
        if self.onClose():
            return super( SubWindow, self ).closeEvent( event )
        else:
            event.ignore()

##----------------------------------------------------------------##
class DocumentWindow( SubWindow ):
    def show( self, *args ):
        tab = self.parentWindow.centerTabWidget
        idx = tab.indexOf( self )
        if idx < 0:
            idx = tab.addTab( self, self.windowTitle() )
        super( DocumentWindow, self ).show( *args )
        tab.setCurrentIndex( idx )

    def setWindowTitle( self, title ):
        super( DocumentWindow, self ).setWindowTitle( title )
        tabParent = self.parentWindow.centerTabWidget
        idx = tabParent.indexOf( self )
        tabParent.setTabText( idx, title )
        
    def addToolBar(self):
        return self.addWidget( QtGui.QToolBar(), expanding = False ) 

    
##----------------------------------------------------------------##
class DockWindowTitleBar( QtGui.QWidget ):
    """docstring for DockWindowTitleBar"""
    def __init__(self, *args):
        super(DockWindowTitleBar, self).__init__(*args)

    def sizeHint(self):
        return QtCore.QSize(20,15)

    def minimumSizeHint(self):
        return QtCore.QSize(20,15)

##----------------------------------------------------------------##
class DockWindow( QtGui.QDockWidget ):
    """docstring for DockWindow"""
    callbackOnClose = None

    def __init__(self, parent):
        super(DockWindow, self).__init__(parent)
        self.setupBasicUi()
        font = QtGui.QFont()
        font.setPointSize(11)
        self.setFont(font)
        self.topLevel  = False
        self.stayOnTop = False

    def setupCustomTitleBar(self):
        self.originTitleBar = self.titleBarWidget()
        self.customTitleBar = DockWindowTitleBar( self )
        self.customTitleBar = self.originTitleBar
        self.setTitleBarWidget( self.customTitleBar )

    def _useWindowFlags(self):
        pass

    def setStayOnTop( self, stayOnTop ):
        self.stayOnTop = stayOnTop
        if stayOnTop and self.topLevel:
            self.setWindowFlags( Qt.Window | Qt.WindowStaysOnTopHint )
        
    def hideTitleBar(self):
        emptyTitle = QtGui.QWidget()
        self.setTitleBarWidget(emptyTitle)

    def startTimer(self, step, trigger):
        assert(hasattr(trigger,'__call__'))
        interval = 1000 * step
        timer=QtCore.QTimer(self)
        timer.timeout.connect(trigger)
        timer.start(interval)
        return timer

    def setupBasicUi(self):
        self.callbackOnClose = None
        self.container = self.createContainer()
        self.mainLayout = QtGui.QVBoxLayout(self.container)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setObjectName('MainLayout')

    def createContainer(self):
        container = QtGui.QWidget(self)
        self.setWidget(container)
        return container

    def addWidget(self, widget, **layoutOption):
        if layoutOption.get('fixed', False):
            widget.setSizePolicy(
                QtGui.QSizePolicy.Fixed,
                QtGui.QSizePolicy.Fixed
                )
        elif layoutOption.get('expanding', True):
            widget.setSizePolicy(
                QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Expanding
                )       
        self.mainLayout.addWidget(widget)
        return widget

    def onTopLevelChanged(self, toplevel):
        self.topLevel = toplevel
        if toplevel:
            self.setTitleBarWidget( self.originTitleBar )
            flag = Qt.Window
            if self.stayOnTop:
                flag |= Qt.WindowStaysOnTopHint
            self.setWindowFlags( flag )
            self.show()
        else:
            self.setTitleBarWidget( self.customTitleBar )
            pass

    def addToolBar(self):
        return self.addWidget( QtGui.QToolBar(), expanding = False ) 

    def closeEvent( self, event ):
        if self.onClose():
            return super( DockWindow, self ).closeEvent( event )
        else:
            event.ignore()

    def moveToCenter(self):
        moveWindowToCenter(self)

    def ensureVisible(self):
        restrainWidgetToScreen(self)

    def setCallbackOnClose( self, callback ):
        self.callbackOnClose = callback

    def onClose( self ):
        if self.callbackOnClose:
            return self.callbackOnClose()
        return True