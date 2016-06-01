
local EditorComponent = require("core.EditorComponent")
local InputEvent = require("input.InputEvent")

local function _cameraZoomControlNodeCallback( node )
	return node.navigate:updateZoom()
end

---------------------------------------------------------------------------------
--
-- @type Canvas3DLookAtObject
--
---------------------------------------------------------------------------------

local Canvas3DLookAtObject = Class( EditorComponent, "Canvas3DLookAtObject" )

function Canvas3DLookAtObject:init( option )
	self.option = option
	option.name = option.name or "Canvas3DLookAtObject"

	EditorComponent.init( self, option )
end

---------------------------------------------------------------------------------
function Canvas3DLookAtObject:onLoad()
	local option = self.option or {}
	local inputDevice = option.inputDevice
	self.targetCamera = option.camera
	self.alpha = 0
	self.beta = math.pi/2
	self:updateCameraPos( self.alpha, self.beta )

	assert( inputDevice )
	inputDevice:addListener( self )
	self.inputDevice = inputDevice

	--zoom control
	self.zoomControlNode = MOAIScriptNode.new()
	self.zoomControlNode:reserveAttrs( 1 )
	self.zoomControlNode.navigate = self
	self:setZoom( 1 )
	self.zoomControlNode:setCallback( _cameraZoomControlNodeCallback )

	self.dragging = false
end

---------------------------------------------------------------------------------
function Canvas3DLookAtObject:startDrag( btn, x, y )
	self.dragFrom = { x, y }
	self.cameraFrom = { self.targetCamera:getLoc() }
	self.dragging = btn
	-- self.entity:getScene():setCursor( 'closed-hand' )
end

function Canvas3DLookAtObject:stopDrag( x, y )
	self.dragging = false

	local a, b = self:getAngles( x, y )
	self.alpha = a
	self.beta = b

	self:updateCameraPos( a, b )
	-- self.entity:getScene():setCursor( 'arrow' )
end


function Canvas3DLookAtObject:getZoom()
	return self.zoomControlNode:getAttr( 1 )
end

function Canvas3DLookAtObject:setZoom( zoom )
	zoom = math.clamp( zoom, 1 / 16, 16 )
	self.zoom = zoom
	self.zoomControlNode:setAttr( 1, zoom or 1 )
	self.zoomControlNode:forceUpdate()
end

function Canvas3DLookAtObject:updateZoom()
	local zoom = self:getZoom()
	self.targetCamera:setScl( 1/zoom, 1/zoom, 1 )
	self:updateCanvas()
end

function Canvas3DLookAtObject:getView()
	return self.entity
end

function Canvas3DLookAtObject:updateCanvas()
	self:getView():updateCanvas()
end

---------------------------------------------------------------------------------
function Canvas3DLookAtObject:getAngles( wx, wy )
	local x0, y0 = unpack( self.dragFrom )
	local dx, dy = wx - x0, wy - y0
	local factor = 0.01
	local a = self.alpha + dx * factor
	local b = self.beta + dy * factor
	b = math.clamp( b, 0, math.pi )
	return a, b
end

function Canvas3DLookAtObject:updateCameraPos( a, b )
	local x, y, z = 0, 0, 0
	local radius = 500
	x = math.sin(b) * math.sin(a) * radius
	z = math.sin(b) * math.cos(a) * radius
	y = math.cos(b) * radius

	-- print("move camera to", x, y, z, "angle:", a, b)
	local camera = self.targetCamera
	camera:setLoc( x, y, z )
	camera:lookAt( 0, 0, 0 )

	self:updateCanvas()
end

---------------------------------------------------------------------------------
function Canvas3DLookAtObject:onInputEvent( event )
	if event.id == InputEvent.MOUSE_EVENT then
		self:onMouseEvent( event )
	end
end

function Canvas3DLookAtObject:onMouseEvent( event )
	if event.eventName == InputEvent.DOWN then
		self:onMouseDown( event.idx, event.wx, event.wy )
	elseif event.eventName == InputEvent.UP then
		self:onMouseUp( event.idx, event.wx, event.wy )
	elseif event.eventName == InputEvent.MOVE then
		self:onMouseMove( event.wx, event.wy )
	elseif event.eventName == InputEvent.MOUSE_SCROLL then
		self:onMouseScroll( event.wx, event.wy )
	end
end

function Canvas3DLookAtObject:onMouseDown( btn, wx, wy )
	if btn == 'right' then
		if self.dragging then return end
		self:startDrag( btn, wx, wy )

	elseif btn == 'left' then
		if self.dragging then return end
		if self.inputDevice:isKeyDown( 'space' ) then
			self:startDrag( btn, wx, wy )
		end
	end
end

function Canvas3DLookAtObject:onMouseUp( btn, wx, wy )
	if btn == self.dragging then
		self:stopDrag( wx, wy )
	end
end

function Canvas3DLookAtObject:onMouseMove( wx, wy )
	if not self.dragging then return end
	local a, b = self:getAngles( wx, wy )
	self:updateCameraPos( a, b )
end

function Canvas3DLookAtObject:onMouseScroll( x, y )
	if self.dragging then return end

	if y > 0 then
		self:setZoom( self.zoom + 0.02 )
	else
		self:setZoom( self.zoom - 0.02 )
	end
end

---------------------------------------------------------------------------------

return Canvas3DLookAtObject
