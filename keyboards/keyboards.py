from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message, PhotoSize)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

from lexicon.lexicon_en import LEXICON_EN






main_menu: InlineKeyboardBuilder = InlineKeyboardBuilder()

start_search_button = InlineKeyboardButton(text='▶️ Start search', callback_data='start_search')

search_setting_button = InlineKeyboardButton(text='⚙️ Search settings', callback_data='search_setting')

settings_data_button = InlineKeyboardButton(text='ℹ️ Settings data', callback_data='settings_data')


main_menu.row(start_search_button, width=2)

main_menu.row(search_setting_button, width=2)

main_menu.row(settings_data_button, width=2)







choose_fleet_menu: InlineKeyboardBuilder = InlineKeyboardBuilder()

fleet_button = InlineKeyboardButton(text='⛵️ Choose Fleet', callback_data='fleet_button')

back_button = InlineKeyboardButton(text='🔙 Back', callback_data='back_button')

choose_fleet_menu.row(fleet_button, width=2)

choose_fleet_menu.row(back_button, width=2)





fleet_menu: InlineKeyboardBuilder = InlineKeyboardBuilder()

offshore_button = InlineKeyboardButton(text='🛳 Offshore Fleet', callback_data='Offshore Fleet')

merchant_button = InlineKeyboardButton(text='🚢 Merchant Fleet', callback_data='Merchant Fleet')

fleet_menu.row(offshore_button, width=1)

fleet_menu.row(merchant_button, width=1)




choose_position_menu: InlineKeyboardBuilder = InlineKeyboardBuilder()

position_button = InlineKeyboardButton(text='👨‍✈️ Choose Position', callback_data='position_button')

choose_position_menu.row(position_button, width=2)





position_menu: InlineKeyboardBuilder = InlineKeyboardBuilder()

master_button = InlineKeyboardButton(text='Master', callback_data=LEXICON_EN['master_button'])

chief_mate_button = InlineKeyboardButton(text='Chief Officer', callback_data=LEXICON_EN['chief_mate_button'])

second_mate_button = InlineKeyboardButton(text='2nd Officer', callback_data='2nd Officer')

third_officer_button = InlineKeyboardButton(text='3rd Officer', callback_data='3rd Officer')

chief_engineer_button = InlineKeyboardButton(text='Chief Engineer', callback_data='Chief Engineer')

second_engineer_button = InlineKeyboardButton(text='2nd Engineer', callback_data='2nd Engineer')

third_engineer_button = InlineKeyboardButton(text='3rd Engineer', callback_data='3rd Engineer')

forth_engineer_button = InlineKeyboardButton(text='4th Engineer', callback_data='4th Engineer')

eto_button = InlineKeyboardButton(text='ETO', callback_data='ETO')

bosun_button = InlineKeyboardButton(text='Bosun', callback_data='Bosun')

ab_button = InlineKeyboardButton(text='AB', callback_data='AB')

motorman_button = InlineKeyboardButton(text='Motorman', callback_data='motorman_button')

cook_button = InlineKeyboardButton(text='Cook', callback_data='cook_button')

messman_button = InlineKeyboardButton(text='Messman', callback_data='messman_button')

cadet_button = InlineKeyboardButton(text='Cadet', callback_data='cadet_button')

position_menu.row(master_button, width=2)

position_menu.row(chief_mate_button, width=2)

position_menu.row(second_mate_button, width=2)

position_menu.row(third_officer_button, width=2)

position_menu.row(chief_engineer_button, width=2)

position_menu.row(second_engineer_button, width=2)

position_menu.row(third_engineer_button, width=2)

position_menu.row(forth_engineer_button, width=2)

position_menu.row(eto_button, width=2)

position_menu.row(bosun_button, width=2)

position_menu.row(ab_button, width=2)

position_menu.row(motorman_button, width=2)

position_menu.row(cook_button, width=2)

position_menu.row(messman_button, width=2)

position_menu.row(cadet_button, width=2)



stop_menu: InlineKeyboardBuilder = InlineKeyboardBuilder()

stop_search_button = InlineKeyboardButton(text='⏸ Stop search', callback_data='stop_search_button')

stop_menu.row(stop_search_button, width=2)




# stop_menu: InlineKeyboardBuilder = InlineKeyboardBuilder()

# search_setting_button = InlineKeyboardButton(text='⚙️ Search settings', callback_data='search_setting')

# settings_data_button = InlineKeyboardButton(text='ℹ️ Settings data', callback_data='settings_data')

# stop_search_button = InlineKeyboardButton(text='⏸ Stop search', callback_data='stop_search_button')

# stop_menu.row(search_setting_button, width=2)

# stop_menu.row(settings_data_button, width=2)

# stop_menu.row(stop_search_button, width=2)




# update_menu : InlineKeyboardBuilder = InlineKeyboardBuilder()

# get_updates_button = InlineKeyboardButton(text='✅ Get Updates', callback_data='get_updates_button')

# cancel_button = InlineKeyboardButton(text='❌ Cancel', callback_data='cancel_button')

# update_menu.row(get_updates_button, width=2)

# update_menu.row(cancel_button, width=2)