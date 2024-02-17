import voluptuous as vol

from homeassistant import const, config_entries
from homeassistant.helpers.selector import ConversationAgentSelector, ConversationAgentSelectorConfig

CONF_NAME = const.CONF_NAME
CONF_COUNT = const.CONF_COUNT

__all__ = [
    "conf_agent",
    "options_schema"
]


def conf_agent(i: int):
    return f"agent_{i}"


def options_schema(config_entry: config_entries.ConfigEntry):
    schema = {}
    count = config_entry.data.get(CONF_COUNT) + 1
    for i in range(1, count):
        key = conf_agent(i)
        field = vol.Required(key, default=config_entry.options.get(key))
        schema[field] = ConversationAgentSelector(ConversationAgentSelectorConfig())
    return vol.Schema(schema)
