from __future__ import annotations

from typing import Any

from homeassistant import config_entries, data_entry_flow

from .options_schema import options_schema

__all__ = [
    "OptionsFlow"
]


class OptionsFlow(config_entries.OptionsFlow):

    def __init__(self, config_entry: config_entries.ConfigEntry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> data_entry_flow.FlowResult:
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)
        return self.async_show_form(step_id="init", data_schema=options_schema(self.config_entry))
