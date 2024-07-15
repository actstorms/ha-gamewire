from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity import EntityCategory

from .const import DOMAIN, KEY_STATUS

async def async_setup_entry(hass, entry, async_add_entities):

    api = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([GameWireSensor(api, hass)], True)

class GameWireSensor(SensorEntity):

    def __init__(self, api, hass):
        """Initialize the sensor."""
        self.api = api
        self._attr_has_entity_name = True
        self._attr_translation_key = KEY_STATUS
        self._attr_entity_category = EntityCategory.DIAGNOSTIC
        self._attr_unique_id = f"{DOMAIN}_{KEY_STATUS}"
        self._state = None
        self._attributes = {}

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return self._attributes

    def update(self):
        """Fetch new state data for the sensor."""
        instance_info = self.api.get_instance_info()
        if instance_info:
            self._state = instance_info['status']
            self._attributes = {
                'instance_id': instance_info['instanceid'],
                'ip': instance_info['ip'],
                'location': instance_info['location'],
                'username': instance_info['username'],
                'os': instance_info['os'],
                'cpus': instance_info['cpus'],
                'ram': instance_info['ram'],
                'disk': instance_info['disk'],
                'gpu': instance_info['gpu'],
            }
        else:
            self._state = "Unavailable"
            self._attributes = {}