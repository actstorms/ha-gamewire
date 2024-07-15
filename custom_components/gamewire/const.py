from homeassistant.const import Platform

DOMAIN = "gamewire"
API_URL = "https://api.gamewire.gg"

PLATFORMS = [Platform.SENSOR, Platform.SWITCH]

# Translation keys
KEY_STATUS = "status"
KEY_POWER = "power"