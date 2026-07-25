from dataclasses import dataclass


@dataclass
class Message:
    sender: str
    content: str


@dataclass
class ParticipantStats:
    name: str
    message_count: int = 0
    avg_msg_length: float = 0.0
