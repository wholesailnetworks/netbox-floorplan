from extras.plugins import PluginMenuButton, PluginMenuItem, PluginMenu
from utilities.choices import ButtonColorChoices

plugin_buttons = [
    # PluginMenuButton(
    #     link='plugins:netbox_floorplan:floorplan_add',
    #     title='Add Floorplan',
    #     icon_class='mdi mdi-plus-thick',
    #     color=ButtonColorChoices.GREEN
    # )
]

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_floorplan:floorplan_list',
        link_text='Floorplans',
        buttons = plugin_buttons
    ),
)

