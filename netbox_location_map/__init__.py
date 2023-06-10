from extras.plugins import PluginConfig


class LocationMapConfig(PluginConfig):
    name = 'netbox_location_map'
    verbose_name = 'Netbox Location Map'
    description = ''
    version = '0.1'
    base_url = 'netbox_location_map'
    min_version = '3.4.1'


config = LocationMapConfig
