
--------------------------------------------------------------------------------
--
--------------------------------------------------------------------------------

local CommonColorTable = {}
local defaultColor = { 1, 1, 1, 1 }

function addColor( name, r, g, b, a )
	CommonColorTable[ name ] = { r, g, b, a }
end

function addHexColor( name, hex, alpha )
	return addColor( name, hexcolor(hex, alpha) )
end

function applyColor( name )
	MOAIGfxDevice.setPenColor( getColor( name ) )
end

function getColor( name )
	local color = CommonColorTable[ name ] or defaultColor
	return unpack( color )
end
