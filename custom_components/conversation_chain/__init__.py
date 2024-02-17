from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .agent import ConversationChainAgent
from .const import DOMAIN as INTERNAL_DOMAIN

DOMAIN = INTERNAL_DOMAIN


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    ConversationChainAgent.install(hass, entry)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    ConversationChainAgent.uninstall(hass, entry)
    return True
