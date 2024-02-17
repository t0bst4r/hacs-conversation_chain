from __future__ import annotations

from typing import Any

import voluptuous as vol
from homeassistant import config_entries, data_entry_flow
from homeassistant.helpers.selector import ConversationAgentSelector, ConversationAgentSelectorConfig

from .const import DOMAIN, CONF_INTEGRATION_NAME, CONF_AGENT_COUNT, conf_agent


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(
            self, user_input: dict[str, Any] | None = None
    ) -> data_entry_flow.FlowResult:
        if user_input is None:
            return self.async_show_form(step_id="user", data_schema=self._data_schema())
        count = user_input.get(CONF_AGENT_COUNT, 0)
        if count < 1 or count > 10:
            self.async_show_form(step_id="user", data_schema=self._data_schema(),
                                 errors={CONF_AGENT_COUNT: "invalid_count"})
        return self.async_create_entry(title=user_input.get(CONF_INTEGRATION_NAME), data=user_input)

    @staticmethod
    def _data_schema():
        return vol.Schema({
            vol.Required(CONF_INTEGRATION_NAME): str,
            vol.Required(CONF_AGENT_COUNT, default=1): int
        })

    @staticmethod
    def async_get_options_flow(config_entry: config_entries.ConfigEntry) -> config_entries.OptionsFlow:
        return OptionsFlow(config_entry)


class OptionsFlow(config_entries.OptionsFlow):

    def __init__(self, config_entry: config_entries.ConfigEntry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> data_entry_flow.FlowResult:
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)
        schema = self._data_schema(self.config_entry)
        return self.async_show_form(step_id="init", data_schema=vol.Schema(schema))

    @staticmethod
    def _data_schema(config_entry: config_entries.ConfigEntry) -> dict:
        schema = {}
        count = config_entry.data.get(CONF_AGENT_COUNT) + 1
        for i in range(1, count):
            key = conf_agent(i)
            field = vol.Required(key, default=config_entry.options.get(key))
            schema[field] = ConversationAgentSelector(ConversationAgentSelectorConfig())
        return schema
