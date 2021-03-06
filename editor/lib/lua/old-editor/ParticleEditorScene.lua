--------------------------------------------------------------------------------
--
--
--
--------------------------------------------------------------------------------

local Scene = require("core.Scene")

local ParticleEditorScene = class(Scene)

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
function ParticleEditorScene:addGizmo(gizmo)
    gizmo.prop:setLayer(self.layer)
end

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
function ParticleEditorScene:init(params)
    Scene.init(self, params)

    self:addEventListener(Event.ENTER, self.onEnter, self)
    self:addEventListener(Event.EXIT, self.onExit, self)
    self:addEventListener(Event.DID_EXIT, self.onDidExit, self)
    self:addEventListener(Event.WILL_ENTER, self.onWillEnter, self)

    self:createLayer()
end

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
function ParticleEditorScene:getBgColor()
    return self.color:getColor()
end

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
function ParticleEditorScene:getSystem()
    return self.system
end

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- called before transition
function ParticleEditorScene:onWillEnter(event)
    self.system:start()
end

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- called after transition
function ParticleEditorScene:onEnter()

end

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- called before transition
function ParticleEditorScene:onExit()

end

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- called after transition
function ParticleEditorScene:onDidExit()
    self.system:stop()
end

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
function ParticleEditorScene:createLayer()
    local layer = Display.Layer()

    layer:setTouchEnabled(true)
    self.layer = layer
    self:addLayer(layer)

    self.color = MOAIColor.new()
    self.color:setColor(0, 0, 0, 1)
    layer:setClearColor(self.color)

    local system = MOAIParticleSystem.new()
    system:setLayer(layer)
    self.system = system
end

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
function ParticleEditorScene:setBgColor(r, g, b, a)
    self.color:setColor(r, g, b, a)
end



return ParticleEditorScene
