import sys

from ollama import Client

from parser import extract_participant_stats, parse_chat


def print_header(message_count: int, stats: dict) -> None:
    """Print the program header with chat stats.

    Args:
        message_count: Total number of messages loaded.
        stats: Participant statistics dictionary.
    """
    pass


def print_recent_messages(messages: list) -> None:
    """Display recent messages to the user.

    Args:
        messages: List of recent Message objects to display.
    """
    pass


def run_simulation(client: Client, model: str, messages: list, stats: dict) -> None:
    """Run the main simulation loop.

    Args:
        client: Ollama client instance.
        model: Model name to use.
        messages: All parsed messages from the chat.
        stats: Participant statistics.
    """
    pass


def main():
    if len(sys.argv) < 2:
        print("Usage: uv run main.py <chat_file.txt>")
        sys.exit(1)

    chat_file = sys.argv[1]
    model = "llama3.2"

    messages = parse_chat(chat_file)
    stats = extract_participant_stats(messages)
    client = Client()

    print_header(len(messages), stats)
    run_simulation(client, model, messages, stats)


if __name__ == "__main__":
    main()
