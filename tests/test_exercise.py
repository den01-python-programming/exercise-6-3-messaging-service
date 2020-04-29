import pytest
from src.messaging_service import MessagingService
from src.message import Message

def test_exercise():
    message = Message("Grace","Hello there!")
    service = MessagingService()

    service.add(message)

    assert service.get_messages() == ["Grace: Hello there!"]
