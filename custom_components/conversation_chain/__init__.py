from __future__ import annotations

from typing import Literal

from homeassistant.components import conversation
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import MATCH_ALL
from homeassistant.core import HomeAssistant

from .const import DOMAIN, CONF_AGENT_COUNT, conf_agent


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    conversation.async_set_agent(hass, entry, ConversationChainAgent(hass, entry))
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    conversation.async_unset_agent(hass, entry)
    return True


class ConversationChainAgent(conversation.AbstractConversationAgent):
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry):
        self.hass = hass
        self.entry = entry

    @property
    def attribution(self):
        return {"name": "ConversationChain", "url": "https://github.com/t0bst4r"}

    @property
    def supported_languages(self) -> list[str] | Literal["*"]:
        return MATCH_ALL

    async def async_process(self, user_input: conversation.ConversationInput) -> conversation.ConversationResult:
        count = self.entry.data.get(CONF_AGENT_COUNT) + 1
        agents = [self.entry.options.get(conf_agent(i)) for i in range(1, count)]
        last_result = None
        for agent in agents:
            result = await conversation.async_converse(self.hass, user_input.text, user_input.conversation_id,
                                                       user_input.context, None, agent)
            if result.response.error_code is None:
                return result
            last_result = result
        return last_result
