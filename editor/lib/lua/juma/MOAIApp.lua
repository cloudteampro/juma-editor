--------------------------------------------------------------------------------
--
--
--
--------------------------------------------------------------------------------


local MOAIApp = {}

MOAIApp.APP_OPENED_FROM_URL = 0
MOAIApp.SESSION_START = 1
MOAIApp.SESSION_END = 2
MOAIApp.DID_BECOME_ACTIVE = 3
MOAIApp.WILL_RESIGN_ACTIVE = 4
MOAIApp.BACK_BUTTON_PRESSED = 5
MOAIApp.ACTIVITY_ON_START = 6
MOAIApp.ACTIVITY_ON_STOP = 7

local listenerTable = {}

function MOAIApp.setListener(event, callback)
    if event then
        listenerTable[event] = callback
    end
end

function MOAIApp.dispatchEvent(event, ...)
    if listenerTable[event] then
        listenerTable[event](...)
    end
end

function MOAIApp.exitGame()
    os.exit()
end

function MOAIApp.getSystemUptime()
    return os.time() % (7*86400)
end

return MOAIApp
