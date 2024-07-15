from homeassistant.components.switch import SwitchEntity
from homeassistant.helpers.entity import EntityCategory

from .const import DOMAIN, KEY_POWER

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the switch platform."""
    api = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([GameWireSwitch(api, hass)], True)

class GameWireSwitch(SwitchEntity):
    """Representation of a Gamewire switch."""

    def __init__(self, api, hass):
        """Initialize the switch."""
        self.api = api
        self._attr_has_entity_name = True
        self._attr_translation_key = KEY_POWER
        self._attr_entity_category = EntityCategory.CONFIG
        self._attr_unique_id = f"{DOMAIN}_{KEY_POWER}"
        self._is_on = False

    @property
    def is_on(self):
        """Return true if the switch is on."""
        return self._is_on

    def update(self):
        """Fetch new state data for the switch."""
        instance_info = self.api.get_instance_info()
        if instance_info:
            self._is_on = instance_info['status'].lower() in ['initializing', 'running']

    def turn_on(self, **kwargs):
        """Turn the switch on."""
        if self.api.start_instance():
            self._is_on = True

    def turn_off(self, **kwargs):
        """Turn the switch off."""
        if self.api.stop_instance():
            self._is_on = False