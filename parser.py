import re

from models import Message, ParticipantStats

WHATSAPP_PATTERN = re.compile(
    r"^\[(?:\d{1,2}/\d{1,2}/\d{2,4},\s*\d{1,2}:\d{2}(?::\d{2})?)\]"
    r"\s*(.+?):\s*(.+)$"
)


def parse_chat(file_path: str, group_name: str = "NONE") -> list[Message]:
    """Parse a WhatsApp chat export file into a list of Message objects.

    Args:
        file_path: Path to the exported .txt file.
        group_name: Sender name to filter out (optional).

    Returns:
        List of Message objects with sender and content.
    """
    messages = []
    with open(file_path) as file:
        for line in file:
            parts = WHATSAPP_PATTERN.match(line)
            if not parts:
                continue
            sender, content = parts.group(1), parts.group(2)
            if sender == group_name:
                continue
            messages.append(Message(sender, content))
    return messages


def extract_participant_stats(messages: list[Message]) -> dict[str, ParticipantStats]:
    """Extract activity statistics for each participant in the chat.

    Args:
        messages: List of parsed Message objects.

    Returns:
        Dictionary mapping participant names to their ParticipantStats.
    """
    senders = set()
    for message in messages:
        senders.add(message.sender)

    counts = {sender: 0 for sender in senders}
    total_characters = {sender: 0 for sender in senders}

    for message in messages:
        counts[message.sender] += 1
        total_characters[message.sender] += len(message.content)

    stats = {}
    for sender in senders:
        stats[sender] = ParticipantStats(
            name=sender,
            message_count=counts[sender],
            avg_msg_length=total_characters[sender] / counts[sender],
        )

    return stats


    return stats
        


def get_recent_messages(messages: list[Message], n: int = 20) -> list[Message]:
    """Get the last N messages from the chat.

    Args:
        messages: List of all parsed Message objects.
        n: Number of recent messages to return (default: 20).

    Returns:
        List of the most recent n messages.
    """
    pass
