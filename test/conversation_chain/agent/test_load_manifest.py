from custom_components.conversation_chain.agent.load_manifest import load_manifest
from custom_components.conversation_chain.const import DOMAIN


def test_load_manifest():
    manifest = load_manifest()
    assert manifest["domain"] == DOMAIN
    assert manifest["name"] == "Conversation Chain"
    assert manifest["documentation"] == "https://github.com/t0bst4r/hacs-conversation_chain"
