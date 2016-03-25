local Sprite = require("ui.Sprite")
local Label = require("ui.Label")
local ButtonColor = require("ui.ButtonColor")
local Button = require("ui.Button")
local Widget = require("ui.Widget")

---------------------------------------------------------------------------------
--
-- @type GraphEditor
--
---------------------------------------------------------------------------------

local GraphEditor = Class("GraphEditor")

---------------------------------------------------------------------------------
function GraphEditor:init()
	-- print("GraphEditor inited")
end

---------------------------------------------------------------------------------
function GraphEditor:getScene()
	return EditorSceneMgr:getCurrentScene()
end

function GraphEditor:getSceneRootNode()
	local scene = EditorSceneMgr:getCurrentScene()
	return scene:getRootNode()
end

function GraphEditor:createWidget( widget_type )
	local widget = nil
	if widget_type == "Sprite" then
		widget = Sprite()
	elseif widget_type == "Label" then
		widget = Label()
	elseif widget_type == "ButtonColor" then
		widget = ButtonColor()
	elseif widget_type == "Button" then
		widget = Button()
	elseif widget_type == "Widget" then
		widget = Widget()
	end

	if widget then
		local scene = self:getScene()
		scene:addWidgetToActiveGroup( widget )
		widget:setLoc( scene.camera:getLoc() )
	end
	return widget
end

function GraphEditor:removeWidget( widget )
	local success = false

	if widget then
		local scene = self:getScene()
		success = scene:removeWidgetToActiveGroup( widget )
	end

	return success
end

function GraphEditor:saveScene()
	local scene = self:getScene()
	if scene then
		return LayoutManager:save( scene:getRootNode() )
	end
	return nil
end

function GraphEditor:loadScene( path )
	local scene = self:getScene()
	if scene then
		local node = LayoutManager:load( path )
		self:setRootNode( node )
		return scene.node
	end
	return nil
end

---------------------------------------------------------------------------------

graphEditor = GraphEditor()