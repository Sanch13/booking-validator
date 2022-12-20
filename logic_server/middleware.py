from aiogram.types import ChatMember


def check_sub_channel(chat_member: ChatMember) -> bool:
    """Checks if there is a user in the group. If there is a return True otherwise False"""
    return True if chat_member['status'] != 'left' else False
