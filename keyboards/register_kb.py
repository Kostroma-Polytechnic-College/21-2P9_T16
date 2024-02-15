from aiogram.utils.keyboard import InlineKeyboardBuilder
import os

def IlKeyBoard():
    kb = InlineKeyboardBuilder()
    kb.button(text='Да', callback_data='Да')
    kb.button(text='Нет', callback_data='Нет')
    return kb.as_markup()

def SpecConfKeyBoard():
    kb = InlineKeyboardBuilder()
    kb.button(text='Далее', callback_data='Да')
    kb.button(text='Вернутся', callback_data='Нет')
    return kb.as_markup()

def SpecKeyBoard():
    kb = InlineKeyboardBuilder()
    kb.button(text='Архитектор', callback_data='Ar')
    kb.button(text='Гидрач', callback_data='Gu')
    kb.button(text='Програмист', callback_data='Pr')
    kb.button(text='Электронщик', callback_data='El')
    kb.button(text='Радиоэлектронщик', callback_data='Ra')
    kb.button(text='Электроразраб', callback_data='ER')
    kb.button(text='Монтажник-радиоэлектрик', callback_data='MR')
    kb.button(text='Цифровой куратор', callback_data='CK')

    kb.adjust(1)
    return kb.as_markup()