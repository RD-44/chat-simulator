import os
import tempfile

from models import Message
from parser import extract_participant_stats, parse_chat


def _write_chat(lines: list[str]) -> str:
    """Write lines to a temp file and return the path."""
    fd, path = tempfile.mkstemp(suffix=".txt")
    with os.fdopen(fd, "w") as f:
        f.write("\n".join(lines))
    return path


def test_parse_chat_basic():
    path = _write_chat([
        "[18/06/2026, 18:54:33] Alice: Hello everyone",
        "[18/06/2026, 18:54:53] Bob: Hey Alice!",
        "[18/06/2026, 18:55:03] Charlie: What's up",
    ])
    messages = parse_chat(path)
    os.unlink(path)

    assert len(messages) == 3
    assert messages[0] == Message(sender="Alice", content="Hello everyone")
    assert messages[1] == Message(sender="Bob", content="Hey Alice!")
    assert messages[2] == Message(sender="Charlie", content="What's up")


def test_parse_chat_filters_group_name():
    path = _write_chat([
        "[18/06/2026, 18:54:33] Alice: Hello",
        "[18/06/2026, 18:54:53] SpaceIQ gang: System message",
        "[18/06/2026, 18:55:03] Bob: Hi",
    ])
    messages = parse_chat(path, group_name="SpaceIQ gang")
    os.unlink(path)

    assert len(messages) == 2
    assert messages[0].sender == "Alice"
    assert messages[1].sender == "Bob"


def test_parse_chat_skips_non_matching_lines():
    path = _write_chat([
        "[18/06/2026, 18:54:33] Alice: First message",
        "this is not a valid line",
        "",
        "[18/06/2026, 18:55:03] Bob: Second message",
    ])
    messages = parse_chat(path)
    os.unlink(path)

    assert len(messages) == 2
    assert messages[0].sender == "Alice"
    assert messages[1].sender == "Bob"


def test_parse_chat_empty_file():
    path = _write_chat([])
    messages = parse_chat(path)
    os.unlink(path)

    assert messages == []


def test_extract_participant_stats():
    messages = [
        Message(sender="Alice", content="hi"),
        Message(sender="Bob", content="hello world"),
        Message(sender="Alice", content="hey"),
        Message(sender="Bob", content="yo"),
        Message(sender="Bob", content="what's up"),
    ]
    stats = extract_participant_stats(messages)

    assert len(stats) == 2

    assert stats["Alice"].message_count == 2
    assert stats["Alice"].avg_msg_length == 2.5  # ("hi" + "hey") / 2

    assert stats["Bob"].message_count == 3
    assert stats["Bob"].avg_msg_length == 22 / 3


def test_extract_participant_stats_empty():
    stats = extract_participant_stats([])
    assert stats == {}
