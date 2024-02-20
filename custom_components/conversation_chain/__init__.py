from __future__ import annotations

from homeassistant.components import conversation
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .agent import ConversationChainAgent
from .const import DOMAIN as INTERNAL_DOMAIN

DOMAIN = INTERNAL_DOMAIN


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    conversation_agent = ConversationChainAgent(hass, entry)
    conversation.async_set_agent(hass, entry, conversation_agent)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    conversation.async_unset_agent(hass, entry)
    return True
