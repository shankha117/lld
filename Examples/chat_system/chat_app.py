import random
from enum import Enum
import datetime


class Singleton(type):
    _instance = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instance:
            self._instance[self] = super(Singleton, self).__call__(*args, **kwargs)

        return self._instance[self]


class IdGenerator(metaclass=Singleton):
    __current_id = 0
    __message_id = 0
    __group_id = 0

    def get_new_id(self, custom_id=None):

        if not custom_id:
            self.__current_id += 1
            return str(self.__current_id + random.randint(0, 100000))
        else:
            return str(custom_id + random.randint(0, 100000))

    def __get_new_message_id(self):
        self.__message_id += 1
        return "message" + "_" + self.get_new_id(custom_id=self.__message_id)

    def __get_new_group_id(self):
        self.__group_id += 1
        return "group" + "_" + self.get_new_id(custom_id=self.__group_id)

    def __get_new_default_id(self, prefix):
        return prefix + "_" + self.get_new_id()

    def get_new_id_with_refix(self, prefix: str):

        prefixtypeTomethod = {"message": self.__get_new_message_id,
                              "group": self.__get_new_group_id,
                              "default": self.__get_new_default_id}

        return prefixtypeTomethod.get(prefix, "default")()


class UserServices(metaclass=Singleton):
    __all_users = {}

    def add_user(self, user):

        self.__all_users[user.name] = user

    # @validate_admin_status
    def show_users(self):
        for key, val in self.__all_users.items():
            print(val)

    def get_user_by_id(self, user_name):
        if user_name in self.__all_users:
            return self.__all_users[user_name]
        raise KeyError("User Not Found")

    def remove_user(self, user_id):
        pass

    def add_friend_request(self, from_user_id, to_user_id):
        pass

    def approve_friend_request(self, from_user_id, to_user_id):
        pass

    def reject_friend_request(self, from_user_id, to_user_id):
        pass


class User():
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.id = IdGenerator().get_new_id()
        self.friends_by_id = {}  # key: friend id, value: User
        self.friend_ids_to_private_chats = {}  # key: friend id, value: private chats
        self.group_chats_by_id = {}  # key: chat id, value: GroupChat
        self.received_friend_requests_by_friend_id = {}  # key: friend id, value: AddRequest
        self.sent_friend_requests_by_friend_id = {}  # key: friend id, value: AddRequest
        # add this user to the UserServices
        UserServices().add_user(self)

    def message_user(self, friend_id, message):
        pass

    def message_group(self, group_id, message):
        pass

    def send_friend_request(self, friend_id):
        pass

    def receive_friend_request(self, friend_id):
        pass

    def approve_friend_request(self, friend_id):
        pass

    def reject_friend_request(self, friend_id):
        pass

    def message_received_from_group(self, group_name, message):
        print(f"{message} received from {group_name}")

    def message_received_from_friend(self, friend_name, message):
        print(f"{message} received from {friend_name}")

    def __str__(self):
        return f"{self.name} -- {self.password}"


from abc import ABCMeta


class RequestStatus(Enum):
    UNREAD = 0
    READ = 1
    ACCEPTED = 2
    REJECTED = 3


class Message(object):

    def __init__(self, message):
        self.message_id = IdGenerator().get_new_id_with_refix(prefix="message")
        self.text = message
        self.timestamp = datetime.datetime.utcnow()


class Chat(metaclass=ABCMeta):

    def __init__(self, chat_id):
        self.chat_id = chat_id
        self.users = []
        self.messages = []


class GroupChat(Chat):

    def __init__(self, name):
        super(PrivateChat, self).__init__(chat_id=IdGenerator().get_new_id_with_refix(prefix="group"))
        self.group_name = name
        self.id = IdGenerator().get_new_id_with_refix("group")

    def add_user(self, user: User):
        self.users.append(user)
        user.group_chats_by_id[self.chat_id] = self

    def remove_user(self, user):
        pass

    def __notify_all(self, sender, message):
        for i in self.users:
            if i != sender:
                i.message_received_from_group(self.group_name, message.text)

    def send_message(self, user: User, message: Message):
        self.messages.append(message)
        self.__notify_all(sender=User, message=message)


class PrivateChat(Chat):

    def __init__(self, first_user, second_user):
        super(PrivateChat, self).__init__(chat_id=IdGenerator().get_new_id_with_refix(prefix="private"))
        self.users.append(first_user)
        self.users.append(second_user)


class AddRequest(object):

    def __init__(self, from_user_id, to_user_id, request_status, timestamp):
        self.from_user_id = from_user_id
        self.to_user_id = to_user_id
        self.request_status = request_status
        self.timestamp = timestamp
