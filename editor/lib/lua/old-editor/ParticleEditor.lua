--------------------------------------------------------------------------------
--
--
--
--------------------------------------------------------------------------------

local ParticleState = require("ParticleState")
local ParticleEmitter = require("ParticleEmitter")
local ParticleEditorScene = require("ParticleEditorScene")
local ParticleComponent = require("ParticleComponent")
local ParticleProject = require("ParticleProject")
local ParticleSerializer = require("ParticleSerializer")

local ParticleEditor = {}

local system
local scene
local regMax = 0
local particleLimit = 0
local spriteLimit = 0
local wrapParticles = false
local wrapSprites = false
local reverseDraw = false
local textureInfo = {}

local emitters = {}
local states = {}

function ParticleEditor.addEmitter()
	local emitter = ParticleEmitter()
	emitter:setParticleSystem(system)
	table.insert(emitters, emitter)
end


function ParticleEditor.addComponent(stateId, component)
	local state = states[stateId]
	if not state then
		log.error("Particle state not found")
		return
	end

	state:addComponent(component)
end

function ParticleEditor.addGizmo(gizmo)
	scene:addGizmo(gizmo)
end

function ParticleEditor.addState()
	local state = ParticleState()
	table.insert(states, state)
	ParticleEditor.updateStates()
end

function ParticleEditor.clear()
	for i, e in pairs(emitters) do
		log.info('destroy emitter')
		e:destroy()
	end

	for i, s in pairs(states) do
		log.info('destroy state')
		s:destroy()
	end

	emitters = {}
	states = {}

	regMax = 0

	ParticleEditor.updateStates()
	system:clearSprites()
	ParticleEditor.setParticleLimit(particleLimit)
end


function ParticleEditor.createScene()
	scene = ParticleEditorScene()
	system = scene:getSystem()
	SceneMgr:pushScene(scene)
end

function ParticleEditor.duplicateState(idx)
	local state = states[idx]
	if state then
		local new = ParticleState()
		new:copyFrom(state)
		table.insert(states, new)
		ParticleEditor.updateStates()
	end
end

function ParticleEditor.findEmitter(idx)
	return emitters[idx]
end

function ParticleEditor.findState(idx)
	return states[idx]
end

function ParticleEditor.getComponentList()
	local list = {}
	for k, v in pairs(ParticleComponent) do
		table.insert(list, k)
	end
	table.insert(list, "Force")
	table.sort(list)
	return list
end

function ParticleEditor.getEmitterData(idx)
	local emitter = emitters[idx]
	if not emitter then
		log.error("emitter not found")
		return
	end
	
	return emitter:getModelData()
end

function ParticleEditor.getEmitterIdx(emitter)
	for i, e in ipairs(emitters) do
		if e == emitter then
			return i
		end
	end
	return 0
end

function ParticleEditor.getEmitterParam(emitterId, paramId)
	return emitters[emitterId]:getParam(paramId)
end


function ParticleEditor.getStateData(idx)
	local state = states[idx]
	if not state then
		log.error("state not found")
		return
	end

	return state:getModelData()
end


function ParticleEditor.getStateIdx(state)
	for i, s in ipairs(states) do
		if s == state then
			return i
		end
	end
	return 0
end

function ParticleEditor.getBgColor()
	return scene:getBgColor()
end

function ParticleEditor.getEmitterParam(emitterId, paramId, value)
	return emitters[emitterId]:setParam(paramId, value)
end


function ParticleEditor.getParticleLimit()
	return particleLimit
end

function ParticleEditor.getReverseDrawOrder()
	return reverseDraw
end

function ParticleEditor.getSpriteLimit()
	return spriteLimit
end

function ParticleEditor.getWrapParticles()
	return wrapParticles
end

function ParticleEditor.getWrapSprites()
	return wrapSprites
end

function ParticleEditor.getInitScript(stateId)
	local state = states[stateId]
	if state then
		return state:getInitScript()
	end
end

function ParticleEditor.getRenderScript(stateId)
	local state = states[stateId]
	if state then
		return state:getRenderScript()
	end
end

function ParticleEditor.getUserInitScript(stateId)
	local state = states[stateId]
	if state then
		return state:getUserInitScript()
	end
end

function ParticleEditor.getUserRenderScript(stateId)
	local state = states[stateId]
	if state then
		return state:getUserRenderScript()
	end
end


function ParticleEditor.getStateParam(stateId, paramId)
	return states[stateId]:getParam(paramId)
end


function ParticleEditor.hideGizmos()
	for _, emitter in pairs(emitters) do
		emitter:hideGizmos()
	end

	for _, state in pairs(states) do
		state:hideGizmos()
	end
end


function ParticleEditor.listEmitters()
	local list = {}
	for k, v in ipairs(emitters) do
		table.insert(list, v.name)
	end
	return list
end


function ParticleEditor.listStates()
	local list = {}
	for k, v in ipairs(states) do
		table.insert(list, v.name)
	end
	return list
end

function ParticleEditor.loadImage(filepath)
	local texture = ResourceMgr:getTexture(filepath)
	if not texture then
		log.error("Texture cannot be loaded: " .. tostring(filepath))
		return
	end

	textureInfo.atlas = false
	textureInfo.path = filepath

	texture.scale = App:getContentScale()
	local deck = ResourceMgr:getImageDeck(texture)
	system:setDeck(deck)
end

function ParticleEditor.loadTextureAtlas(filepath)
	local deck = ResourceMgr:getAtlasDeck(filepath)
	if not deck then
		log.error("Texture atlas cannot be loaded: " .. tostring(filepath))
	end

	textureInfo.atlas = true
	textureInfo.path = filepath

	system:setDeck(deck)
end

function ParticleEditor.loadProject(path)
	local components = require("ParticleComponent")
	local project = ParticleSerializer.load(path, components)

	ParticleEditor.clear()

	ParticleEditor.setParticleLimit(project.particleLimit)
	ParticleEditor.setSpriteLimit(project.spriteLimit)
	ParticleEditor.setWrapParticles(project.wrapParticles)
	ParticleEditor.setWrapSprites(project.wrapSprites)
	ParticleEditor.setReverseDrawOrder(project.reverseDraw)
	ParticleEditor.setBgColor(unpack(project.bgColor))

	emitters = project.emitters
	states = project.states

	for _, emitter in pairs(emitters) do
		emitter:setParticleSystem(system)
	end

	for _, state in pairs(states) do
		state:syncComponents()
		state:syncForces()
	end

	local tex = project.texture
	if tex.atlas then
		ParticleEditor.loadTextureAtlas(tex.path)
	else
		ParticleEditor.loadImage(tex.path)
	end

	ParticleEditor.updateStates()
	ParticleEditor.hideGizmos()
end

function ParticleEditor.saveProject(path)
	local project = ParticleProject()
	
	project.particleLimit = ParticleEditor.getParticleLimit()
	project.spriteLimit = ParticleEditor.getSpriteLimit()
	project.wrapParticles = ParticleEditor.getWrapParticles()
	project.wrapSprites = ParticleEditor.getWrapSprites()
	project.reverseDraw = ParticleEditor.getReverseDrawOrder()
	project.bgColor = { ParticleEditor.getBgColor() }
	project.texture = textureInfo

	project.emitters = emitters
	project.states = states

	ParticleSerializer.save(path, project)
end

function ParticleEditor.removeEmitter(idx)
	local emitter = emitters[idx]
	if emitter then
		emitter:destroy()
		table.remove(emitters, idx)
	end
end

function ParticleEditor.removeComponent(stateId, componentId)
	local state = states[stateId]
	if not state then return end

	return state:removeComponent(componentId)
end

function ParticleEditor.removeState(idx)
	local state = states[idx]
	if state then
		state:destroy()

		-- update state references
		for i, emitter in pairs(emitters) do
			local sIdx = emitter:getState()
			if sIdx == idx then
				emitter:setState(0)
			elseif sIdx > idx then
				emitter:setState(sIdx - 1)
			end
		end

		for i, s in pairs(states) do
			local sIdx = s:getNext()
			if sIdx == idx then
				s:setNext(0)
			elseif sIdx > idx then
				s:setNext(sIdx - 1)
			end
		end
		table.remove(states, idx)
	end
	ParticleEditor.updateStates()
end

function ParticleEditor.setBgColor(r, g, b, a)
	scene:setBgColor(r, g, b, a)
end

function ParticleEditor.setEmitterParam(emitterId, paramId, value)
	return emitters[emitterId]:setParam(paramId, value)
end

function ParticleEditor.setStateParam(stateId, paramId, value)
	return states[stateId]:setParam(paramId, value)
end

function ParticleEditor.setParticleLimit(num)
	num = num or 0
	particleLimit = num
	system:reserveParticles(num, regMax)
end

function ParticleEditor.setReverseDrawOrder(flag)
	reverseDraw = flag
	if flag then
		system:setDrawOrder(MOAIParticleSystem.ORDER_REVERSE)
	else
		system:setDrawOrder(MOAIParticleSystem.ORDER_NORMAL)
	end
end

function ParticleEditor.setSpriteLimit(num)
	spriteLimit = num
	system:reserveSprites(num)
end

function ParticleEditor.setWrapParticles(flag)
	wrapParticles = flag
	system:capParticles(not flag)
end

function ParticleEditor.setWrapSprites(flag)
	wrapSprites = flag
	system:capSprites(not flag)
end

function ParticleEditor.setUserInitScript(stateId, script)
	local state = states[stateId]
	if state then
		state:setUserInitScript(script)
	end
end

function ParticleEditor.setUserRenderScript(stateId, script)
	local state = states[stateId]
	if state then
		state:setUserRenderScript(script)
	end
end

function ParticleEditor.startEmitter(emitterId)
	local emitter = emitters[emitterId]
	if emitter then
		emitter:start()
	end
end

function ParticleEditor.stopEmitter(emitterId)
	local emitter = emitters[emitterId]
	if emitter then
		emitter:stop()
	end
end


function ParticleEditor.updateRegCount()
	local regCount = 0
	for _, s in pairs(states) do
		regCount = math.max(regCount, s:getRegisterCount())
	end

	log.info("REGISTERS", regCount)
	if regCount ~= regMax then
		regMax = regCount
		ParticleEditor.setParticleLimit(particleLimit)
	end
end

function ParticleEditor.updateStates()
	system:reserveStates(#states)
	for i, state in ipairs(states) do
		system:setState(i, state.state)
	end
end

return ParticleEditor
