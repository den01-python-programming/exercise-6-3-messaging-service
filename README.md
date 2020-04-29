# Exercise 6.3 Messaging Service

The exercise template comes with a pre-defined `Message` class that can be used to create objects representing messages. Each message has a sender and some content.

Implement the `MessagingService` class. The class must have a parameterless constructor and contain a list of `Message` objects. After that, add the following two methods to the class:

- `def add(self, message)` - adds a message passed as a parameter to the messaging service as long as the message content is at most 280 characters long.

- `def get_messages()` - returns the messages added to the messaging service.

Tip! You can find out the length of the string using the `len()` method associated with the string.
