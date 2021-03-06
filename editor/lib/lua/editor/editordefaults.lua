--------------------------------------------------------------------------------
-- # from tommo gii
--------------------------------------------------------------------------------

addColor( 'white', 1,1,1,1 )
addColor( 'black', 0,0,0,1 )

local alpha = 0.8

addColor( 'selection', 0,1,1, alpha )
addColor( 'handle-x',  1,0,0, alpha )
addColor( 'handle-y',  0,1,0, alpha )
addColor( 'handle-z',  0,0,1, alpha )
addColor( 'handle-all', 1,1,0, alpha )
addColor( 'handle-active', 1,1,0, alpha )

addColor( 'handle-previous', 1,0,0, .3 )

addColor( 'gizmo_trigger', hexcolor( '#6695ff', 0.1 ) )
addColor( 'gizmo_trigger_border', hexcolor( '#6695ff', 0.7 ) )

addColor( 'cp',  0,1,0, alpha )
addColor( 'cp-border',  1,1,1, alpha )

addColor( 'misc',  hexcolor( '#6695ff', 0.1 ) )
addColor( 'misc-transform',  hexcolor( '#b8ff00', 1 ) )

addColor( 'camera-bound', hexcolor( '#ffc900', alpha ) )

addColor( 'background-frame', 0.286, 0.11, 0.31, alpha )

addColor( 'grid-zero', 0.53, 0.0, 0.09, 0.5 )
addColor( 'grid', 0.4, 0.4, 0.4, 0.5 )

--------------------------------------------------------------------------------
-- UI Register
--------------------------------------------------------------------------------
editorRegistryClassType( "UISprite", "ui" )
editorRegistryClassType( "UILabel", "ui" )
editorRegistryClassType( "UILabelSDF", "ui" )
editorRegistryClassType( "UIButton", "ui" )
editorRegistryClassType( "UIButtonColor", "ui" )
editorRegistryClassType( "UIToggle", "ui" )
editorRegistryClassType( "UIWidget", "ui" )

--------------------------------------------------------------------------------
-- UI Register
--------------------------------------------------------------------------------
editorRegistryClassType( "Entity", "entity" )
editorRegistryClassType( "Prefab", "entity" )
editorRegistryClassType( "PropComponent", "component" )

--------------------------------------------------------------------------------
-- register Entities
--------------------------------------------------------------------------------
registerEntity( 'Entity', require("entity.Entity") )
registerEntity( 'Prefab', require("entity.Prefab") )

--------------------------------------------------------------------------------
-- register Components
--------------------------------------------------------------------------------
registerComponent( 'PropComponent', require("entity.components.PropComponent") )

---------------------------------------------------------------------------------

registerEditorSceneCanvasForType("scenes.BaseEditorScene", "canvas.CanvasView", "scene")
registerEditorSceneCanvasForType("scenes.UIEditorScene", "canvas.ui.CanvasView", "ui")
registerEditorSceneCanvasForType("scenes.PrefabUIEditorScene", "canvas.ui.CanvasView", "prefabUI")
registerEditorSceneCanvasForType("scenes.BaseEditorScene", "canvas.3d.CanvasView", "scene3d")
registerEditorSceneCanvasForType("scenes.BaseEditorScene", "canvas.preview.CanvasView", "preview3d")
