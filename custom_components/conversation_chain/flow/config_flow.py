from __future__ import annotations

from typing import Any

from homeassistant import config_entries, data_entry_flow

from ..const import DOMAIN
from .options_flow import OptionsFlow
from .config_schema import config_schema, CONF_NAME, CONF_COUNT

__all__ = [
    "ConfigFlow"
]


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(
            self, user_input: dict[str, Any] | None = None
    ) -> data_entry_flow.FlowResult:
        if user_input is None:
            return self.async_show_form(step_id="user", data_schema=config_schema)
        count = user_input.get(CONF_COUNT, 0)
        if count < 1 or count > 10:
            self.async_show_form(step_id="user", data_schema=config_schema,
                                 errors={CONF_COUNT: "invalid_count"})
        return self.async_create_entry(title=user_input.get(CONF_NAME), data=user_input)

    @staticmethod
    def async_get_options_flow(config_entry: config_entries.ConfigEntry) -> config_entries.OptionsFlow:
        return OptionsFlow(config_entry)
