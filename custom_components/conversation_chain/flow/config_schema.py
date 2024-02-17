import voluptuous as vol

from homeassistant import const

__all__ = [
    "CONF_COUNT",
    "CONF_NAME",
    "config_schema"
]

CONF_NAME = const.CONF_NAME
CONF_COUNT = const.CONF_COUNT

config_schema = vol.Schema({
    vol.Required(CONF_NAME): str,
    vol.Required(CONF_COUNT, default=1): int
})
