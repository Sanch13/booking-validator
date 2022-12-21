from aiogram.types import ChatMember


def check_sub_channel(chat_member: ChatMember) -> bool:
    """Return True otherwise False"""
    return chat_member['status'] != 'left'
