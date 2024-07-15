"""Config flow for Gamewire integration."""
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_EMAIL, CONF_PASSWORD

from .const import DOMAIN, API_URL
from .api import InstanceAPI

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Gamewire."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            try:
                await self.hass.async_add_executor_job(
                    self._validate_credentials,
                    user_input[CONF_EMAIL],
                    user_input[CONF_PASSWORD]
                )
            except InvalidAuth:
                errors["base"] = "invalid_auth"
            except CannotConnect:
                errors["base"] = "cannot_connect"
            else:
                return self.async_create_entry(
                    title=user_input[CONF_EMAIL],
                    data=user_input
                )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_EMAIL): str,
                    vol.Required(CONF_PASSWORD): str,
                }
            ),
            errors=errors,
        )

    def _validate_credentials(self, email, password):
        """Validate the credentials."""
        api = InstanceAPI(API_URL, email, password)
        if not api.authenticate():
            raise InvalidAuth
        if not api.get_instance_info():
            raise CannotConnect

class InvalidAuth(Exception):
    """Error to indicate there is invalid auth."""

class CannotConnect(Exception):
    """Error to indicate we cannot connect."""