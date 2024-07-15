"""The Gamewire integration."""
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN, API_URL
from .api import InstanceAPI

PLATFORMS = ["sensor", "switch"]

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Gamewire component."""
    hass.data[DOMAIN] = {}
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up Gamewire from a config entry."""
    api = InstanceAPI(
        API_URL,
        entry.data["email"],
        entry.data["password"]
    )
    hass.data[DOMAIN][entry.entry_id] = api

    for platform in PLATFORMS:
        hass.async_create_task(
            hass.config_entries.async_forward_entry_setup(entry, platform)
        )

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""
    unload_ok = all(
        await asyncio.gather(
            *[
                hass.config_entries.async_forward_entry_unload(entry, platform)
                for platform in PLATFORMS
            ]
        )
    )
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok