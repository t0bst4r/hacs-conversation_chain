from typing import Literal

from homeassistant.components import conversation
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import MATCH_ALL
from homeassistant.core import HomeAssistant

from .load_manifest import load_manifest
from ..flow import CONF_COUNT, conf_agent

__all__ = [
    "ConversationChainAgent"
]


class ConversationChainAgent(conversation.AbstractConversationAgent):

    @staticmethod
    def install(hass: HomeAssistant, entry: ConfigEntry):
        agent = ConversationChainAgent(hass, entry)
        conversation.async_set_agent(agent)

    @staticmethod
    def uninstall(hass: HomeAssistant, entry: ConfigEntry):
        conversation.async_unset_agent(hass, entry)

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry):
        self.hass = hass
        self.entry = entry
        self.manifest = load_manifest()

    @property
    def attribution(self):
        return {"name": self.manifest["name"], "url": self.manifest["documentation"]}

    @property
    def supported_languages(self) -> list[str] | Literal["*"]:
        return MATCH_ALL

    async def async_process(self, user_input: conversation.ConversationInput) -> conversation.ConversationResult:
        count = self.entry.data.get(CONF_COUNT) + 1
        agents = [self.entry.options.get(conf_agent(i)) for i in range(1, count)]
        last_result = None
        for agent in agents:
            result = await conversation.async_converse(self.hass, user_input.text, user_input.conversation_id,
                                                       user_input.context, None, agent)
            if result.response.error_code is None:
                return result
            last_result = result
        return last_result
