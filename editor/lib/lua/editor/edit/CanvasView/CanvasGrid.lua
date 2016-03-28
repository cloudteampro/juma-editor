
FIXME !!!

local ScriptProp = require("ui.ScriptProp")

---------------------------------------------------------------------------------
--
-- @type CanvasFrame
--
---------------------------------------------------------------------------------

local CanvasFrame = Class( ScriptProp, "CanvasFrame" )

function CanvasFrame:init()
	self.FLAG_EDITOR_OBJECT = true
	self.deckSize = { 1024, 1024 }
	self.frameWidth = 320
	self.frameHeight = 480
	ScriptProp.init(self)
end

---------------------------------------------------------------------------------
function CanvasFrame:onLoad()
	self.layer:insertProp( self._prop )
	self:attach()
end

function CanvasFrame:onDraw()
	applyColor 'background-frame'
	local w, h = self.frameWidth, self.frameHeight

	MOAIGfxDevice.setPenWidth( 2 )
	MOAIDraw.drawRect( -w*0.5, -h*0.5, w*0.5, h*0.5 )

	MOAIGfxDevice.setPenWidth( 1 )
	MOAIDraw.drawLine( 0, -h*0.5, 0, h*0.5 )
	MOAIDraw.drawLine( -w*0.5, 0, w*0.5, 0 )
end

---------------------------------------------------------------------------------
function CanvasFrame:resize( width, height )
	self.frameWidth = width or 320
	self.frameHeight = height or 480
end

---------------------------------------------------------------------------------

return CanvasFrame


module 'mock_edit'
--------------------------------------------------------------------
--CanvasGrid
--------------------------------------------------------------------
CLASS: CanvasGrid( EditorEntity )
function CanvasGrid:onLoad()
	self:attach( mock.DrawScript{	priority = -1	} )
	self.gridSize = { 100, 100 }
end

function CanvasGrid:onDraw()
	local context = gii.getCurrentRenderContext()
	local w, h = MOAIGfxDevice:getViewSize()
	local x0, y1 = self:wndToWorld( 0, 0 )
	local x1, y0 = self:wndToWorld( w, h )
	if w and h then
		--sub grids
		MOAIGfxDevice.setPenWidth( 1 )
		MOAIGfxDevice.setPenColor( .4, .4, .4, .5 )
		local dx = x1-x0
		local dy = y1-y0
		local gw, gh = self.gridSize[1], self.gridSize[2]
		x0, y1 = self:wndToWorld( 0, 0 )
		x1, y0 = self:wndToWorld( w, h )
		local col = math.ceil( dx/gw )
		local row = math.ceil( dy/gh )
		local cx0 = math.floor( x0/gw ) * gw
		local cy0 = math.floor( y0/gh ) * gh
		for x = cx0, cx0 + col*gw, gw do
			MOAIDraw.drawLine( x, y0, x, y1 )
		end
		for y = cy0, cy0 + row*gh, gh do
			MOAIDraw.drawLine( x0, y, x1, y )
		end
	else
		x0, y0 = -100000, -100000
		x1, y1 =  100000,  100000
	end
	--Axis
	MOAIGfxDevice.setPenWidth( 1 )
	MOAIGfxDevice.setPenColor( .5, .5, .7, .7 )
	MOAIDraw.drawLine( x0, 0, x1, 0 )
	MOAIDraw.drawLine( 0, y0, 0, y1 )

	MOAIGfxDevice.setPenWidth( 1 )
end

function CanvasGrid:getWidth()
	return self.gridSize[1]
end

function CanvasGrid:getHeight()
	return self.gridSize[2]
end

function CanvasGrid:setWidth( w )
	self:setSize( w, self:getHeight() )
end

function CanvasGrid:setHeight( h )
	self:setSize( self:getWidth(), h )
end

function CanvasGrid:setSize( w, h )
	self.gridSize = { w, h }
end

function CanvasGrid:getSize()
	return self.gridSize[1], self.gridSize[2]
end

