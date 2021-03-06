# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod

import colorama
from colorama import Fore, Back, Style

import logging
import string
import json
import os
import os.path
import sys
import imp

import signals
import globalSignals
import jsonHelper

from MainModulePath import getMainModulePath

##----------------------------------------------------------------##

_DEFAULT_TOOL_PATH = 'editor/tools'
_INFO_FILE_NAME    = '__config__.json'
_TOOLS = []

_libTools = []
_prjTools = []

def loadToolSetting( path ):
	infoFilePath = path + '/' + _INFO_FILE_NAME
	if not os.path.exists( infoFilePath ): return False
	logging.debug( 'try loading tool: %s ' % path )
	try:
		data = json.load( file( infoFilePath, 'r' ) )
		if not data.get( 'active', True ): return False
		data[ 'module_path' ] = path
	except Exception, e:
		return False
	return data	

def scanToolsInPath( path ):
	toolList = []
	path = os.path.abspath( path )
	for currentDir, dirs, files in os.walk( unicode(path) ):
		for dirname in dirs:
			fullpath = currentDir + '/' + dirname
			data = loadToolSetting( fullpath )
			if data: toolList.append( data )
	return toolList

def scanTools( path ):
	global _libTools, _prjTools
	mainPath  = getMainModulePath()
	_libTools = scanToolsInPath( mainPath + '/' + _DEFAULT_TOOL_PATH )
	if path:
		_prjTools = scanToolsInPath( path + '/' + _DEFAULT_TOOL_PATH )
	return ( _libTools, _prjTools )

def startTool( toolInfo ):
	path = toolInfo[ 'module_path' ]
	toolModuleName = 'juma_tool_' + toolInfo['name']
	logging.info( 'start tool: %s <%s>' % ( toolInfo['name'], path ) )
	sys.path.insert( 0, path )
	m = imp.load_source( toolModuleName, path + '/__init__.py' )
	if hasattr( m, 'main' ):
		m.main( sys.argv[ 1: ] )

##----------------------------------------------------------------##
def printHeader():
	output = Fore.YELLOW + Style.BRIGHT +"""
&b---&y JUMA MOAI Editor &b---
 """

	output = string.replace( output, '&y', Fore.YELLOW + Style.BRIGHT )
	output = string.replace( output, '&r', Fore.BLUE + Style.NORMAL )
	output = string.replace( output, '&w', Fore.BLUE + Style.NORMAL )
	output = string.replace( output, '&b', Fore.BLUE + Style.NORMAL )
	print output
	print Style.RESET_ALL + ''

def printToolInfo( info ):
	output = '    %s \t %s' % ( Fore.RED + info.get('name', '???') + Fore.RESET, info.get('help','') )
	output = output.expandtabs( 16 )
	print output

def printAvailTools():	
	print Fore.GREEN+'  available tool(s):'
	print Style.DIM+''
	print Fore.WHITE + '    + BUILTIN TOOLS'
	print Style.RESET_ALL + ''
	for info in _libTools:
		printToolInfo( info )	
	if _prjTools:
		print Style.DIM + ''
		print '    + PROJECT TOOLS'
		print Style.RESET_ALL + ''
		for info in _prjTools:
			printToolInfo( info )	
	print ''

def printUsage():
	print 'Usage:  juma <tool-name> ...'
	print ''
	printAvailTools()

def printMissingCommand( cmd ):
	printAvailTools( )
	print '  [ERROR] TOOL NOT FOUND: ' + cmd
	print ''

##----------------------------------------------------------------##
def startupTool( info ):	
	colorama.init()

	scanTools( info and info['path'] or None )

	argv = sys.argv
	cmd = None
	if len( argv ) < 2:
		printHeader()
		printUsage()
		cmd = 'ide' # start ide tool if not argv
		# return False
	else:
		cmd = argv[1]

	for toolInfo in _prjTools + _libTools:
		if toolInfo.get('name') == cmd:
			return startTool( toolInfo )
	#show help
	printHeader()
	printMissingCommand( cmd )
