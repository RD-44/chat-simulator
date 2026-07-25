from ollama import Client

from models import Message, ParticipantStats

SYSTEM_PROMPT = """You are simulating a WhatsApp group chat. Continue the conversation naturally.

RULES:
1. Pick the most likely person to respond next based on conversation flow
2. Match their typical message style and length
3. Output ONLY in this exact format: "Name: their message"
4. No timestamps, no quotes, no extra text
5. Keep messages casual and natural like real WhatsApp chats"""


def build_participant_context(stats: dict[str, ParticipantStats]) -> str:
    """Format participant statistics for the system prompt.

    Args:
        stats: Dictionary mapping names to ParticipantStats objects.

    Returns:
        Formatted string with participant activity info.
    """
    pass


def build_chat_context(messages: list[Message]) -> str:
    """Format recent messages as chat context for the LLM.

    Args:
        messages: List of recent Message objects.

    Returns:
        Formatted string of chat messages.
    """
    pass


def generate_next_message(
    client: Client,
    model: str,
    participant_context: str,
    chat_context: str,
) -> str:
    """Generate the next chat message using the LLM.

    Args:
        client: Ollama client instance.
        model: Model name to use (e.g., "llama3.2").
        participant_context: Formatted participant stats.
        chat_context: Formatted recent chat messages.

    Returns:
        Generated message in "Name: message" format.
    """
    pass
