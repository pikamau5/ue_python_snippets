"""
    Example of extending a menu in Unreal using Python
"""

import unreal

@unreal.uclass()
class MyEntryScript(unreal.ToolMenuEntryScript):
    @unreal.ufunction(override=True)
    def execute(self, context):
        print("Hell, World!")

def main():

    menus = unreal.ToolMenus.get()

    # Find the 'edit' menu, this should not fail,
    # but if we're looking for a menu we're unsure about 'if not'
    # works as nullptr check,
    edit = menus.find_menu("LevelEditor.MainMenu.Edit")
    main_menu = menus.find_menu("LevelEditor.MainMenu")
    if not edit:
        print("Failed to find the 'Edit' menu")

    entry = unreal.ToolMenuEntry(
        name = "MyEntry2",
        type = unreal.MultiBlockType.MENU_ENTRY, # If you pass a type that is not supported Unreal will let you know,
        insert_position = unreal.ToolMenuInsert("Delete", unreal.ToolMenuInsertType.AFTER), # this will tell unreal to insert this entry after the 'Delete' menu item, if found in section we define later,'

    )

    entry.set_label("My Entry")
    entry.set_tool_tip("This is a Tool Menu Entry made in Python!")


    edit.add_menu_entry("EditMain", entry) # section name, ToolMenuInsert, Unreal will add the section name if it can't find it, otherwise call AddEntry for the found section,

    my_menu = main_menu.add_sub_menu("My.Menu", "Python", "My Menu", "Custom Menu")

    #for name, fn in [("Foo", MyEntryScript()), ("Bar", MyEntryScript()), ("Baz", MyEntryScript())]:
    e = unreal.ToolMenuEntry(
        name = "Hell",
        type = unreal.MultiBlockType.MENU_ENTRY, # If you pass a type that is not supported Unreal will let you know,
        #script_object=MyEntryScript()
    )

    e.set_label("bla")
    CUSTOM_TYPE = custom_type = unreal.Name("")
    e.set_string_command(unreal.ToolMenuStringCommandType.PYTHON, CUSTOM_TYPE, string=("print('asfdfsdf')"))
    my_menu.add_menu_entry("Items", e)

    menus.refresh_all_widgets()

if __name__ == '__main__':
    main()