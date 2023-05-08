#from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart, StateFilter, Text
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message, PhotoSize)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboards.keyboards import main_menu, choose_fleet_menu, fleet_menu, choose_position_menu, position_menu, stop_menu
#from Services.services import json_correction
#from config_data.config import load_config, Config
from marine_website.job_at_sea import check_vacancy_update_merchant_jobatsea, check_vacancy_update_offshore_jobatsea
from marine_website.maritime_zone import check_vacancy_update_merchant, check_vacancy_update_offshore
from aiogram import Router
import json
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
import asyncio
from time import sleep
import logging
from keyboards.set_menu import  set_main_menu
from lexicon.lexicon_en import LEXICON_EN

#storage: MemoryStorage = MemoryStorage()

#config: Config = load_config()

#bot: Bot = Bot(token=config.tg_bot.token,
               #parse_mode = 'HTML')

#dp: Dispatcher = Dispatcher(storage=storage)

router: Router = Router()


user_dict: dict[int, dict[str, str | int | bool]] = {}


class FSMFillForm(StatesGroup):

    fill_fleet = State()
    fill_position = State()
    clear_storage = State()


@router.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message):

    await message.answer(text= LEXICON_EN['start'],
                         reply_markup=main_menu.as_markup())


@router.message(Command(commands=['edit_settings']), StateFilter(default_state))
async def process_start_command(message: Message):

    await message.answer(text=LEXICON_EN['edit_settings'],
                         reply_markup=main_menu.as_markup())




@router.callback_query(Text(text='search_setting'), StateFilter(default_state))
async def process_setting_press(callback: CallbackQuery):

    await callback.message.answer(text=LEXICON_EN['search_settings'],
                                  reply_markup=choose_fleet_menu.as_markup())




@router.callback_query(Text(text='fleet_button'), StateFilter(default_state))
async def process_fleet_press(callback: CallbackQuery, state: FSMContext):

    await callback.message.answer(text=LEXICON_EN['fleet_button'],
                                  reply_markup=fleet_menu.as_markup())

    await state.set_state(FSMFillForm.fill_fleet)



@router.callback_query(StateFilter(FSMFillForm.fill_fleet),
                    Text(text=LEXICON_EN['fleets']))
async def save_fleet_press(callback: CallbackQuery, state: FSMContext):

    await state.update_data(fleet = callback.data)

    user_dict[callback.from_user.id] = await state.get_data()

    await state.clear()

    await callback.message.answer(text=LEXICON_EN['select_fleet'],
                                  reply_markup=choose_position_menu.as_markup())



@router.callback_query(Text(text='position_button'), StateFilter(default_state))
async def process_position_press(callback: CallbackQuery, state: FSMContext):

    await callback.message.answer(text=LEXICON_EN['position_button'],
                                  reply_markup=position_menu.as_markup())


    await state.set_state(FSMFillForm.fill_position)





@router.callback_query(StateFilter(FSMFillForm.fill_position),
                   Text(text=LEXICON_EN['positions']))
async def process_search_press(callback: CallbackQuery, state: FSMContext):

    await state.update_data(position = callback.data)

    user_dict[callback.from_user.id].update(await state.get_data())

    await state.clear()

    await callback.message.answer(text=LEXICON_EN['select_fleet'],
                                  reply_markup=main_menu.as_markup())
    print(user_dict[callback.from_user.id]['fleet'])
    print(user_dict[callback.from_user.id]['position'])





@router.callback_query(Text(text='start_search'), StateFilter(default_state))
async def save_position_press(callback: CallbackQuery, state: FSMContext):
    if callback.from_user.id in user_dict:
        if user_dict[callback.from_user.id]['fleet']!=None and user_dict[callback.from_user.id]['position']!= None:

            await callback.message.answer(text=f'Fleet: {user_dict[callback.from_user.id]["fleet"]}\n'
                            f'Position: {user_dict[callback.from_user.id]["position"]}\n')

            if user_dict[callback.from_user.id]['position'] == LEXICON_EN['master_button']:
                user_dict[callback.from_user.id]['position']  = LEXICON_EN['master_var']

            if user_dict[callback.from_user.id]['position'] == LEXICON_EN['chief_mate_button']:
                user_dict[callback.from_user.id]['position'] = LEXICON_EN['chief_mate_var']

            if user_dict[callback.from_user.id]['position'] == LEXICON_EN['second_mate_button']:
                user_dict[callback.from_user.id]['position'] = LEXICON_EN['second_mate_var']

            if user_dict[callback.from_user.id]['position'] == LEXICON_EN['third_mate_button']:
                user_dict[callback.from_user.id]['position'] = LEXICON_EN['third_mate_var']

            if user_dict[callback.from_user.id]['position'] == LEXICON_EN['chief_engineer_button']:
                user_dict[callback.from_user.id]['position'] = LEXICON_EN['chief_engineer_var']


            if user_dict[callback.from_user.id]['position'] == LEXICON_EN['second_engineer_button']:
                user_dict[callback.from_user.id]['position'] = LEXICON_EN['second_engineer_var']

            if user_dict[callback.from_user.id]['position'] == LEXICON_EN['third_engineer_button']:
                user_dict[callback.from_user.id]['position'] = LEXICON_EN['third_engineer_var']

            if user_dict[callback.from_user.id]['position'] == LEXICON_EN['forth_engineer_button']:
                user_dict[callback.from_user.id]['position'] = LEXICON_EN['forth_engineer_var']

            if user_dict[callback.from_user.id]['position'] == LEXICON_EN['eto_button']:
                user_dict[callback.from_user.id]['position'] = LEXICON_EN['eto_var']

            if user_dict[callback.from_user.id]['position'] == LEXICON_EN['bosun_button']:
                user_dict[callback.from_user.id]['position'] = LEXICON_EN['bosun_var']

            if user_dict[callback.from_user.id]['position'] == LEXICON_EN['ab_button']:
                user_dict[callback.from_user.id]['position'] = LEXICON_EN['ab_var']

            if user_dict[callback.from_user.id]['position'] == LEXICON_EN['motorman_button']:
                user_dict[callback.from_user.id]['position'] = LEXICON_EN['motorman_var']

            if user_dict[callback.from_user.id]['position'] == LEXICON_EN['cook_button']:
                user_dict[callback.from_user.id]['position'] = LEXICON_EN['cook_var']

            if user_dict[callback.from_user.id]['position'] == LEXICON_EN['messman_button']:
                user_dict[callback.from_user.id]['position'] == LEXICON_EN['messman_var']

            if user_dict[callback.from_user.id]['position'] == LEXICON_EN['cadet_button']:
                user_dict[callback.from_user.id]['position'] = LEXICON_EN['cadet_var']

            with open('vacancy_dict.json', "r") as file:

                corrected_dict = file.read()

                corrected_dict = corrected_dict.replace('\n', '')

                corrected_dict = corrected_dict.replace('}{', ',')

                vacancy_dict_fleet = json.loads(corrected_dict)

            for k, v in sorted(vacancy_dict_fleet.items()):

                if 'offshore_fleet' in v:
                    vacancy_dict_fleet = f"{v['offshore_fleet']}\n" \
                                            f"{v['vacancy_info']}\n" \
                                            f"{v['vacancy_article']}\n" \
                                            f"{v['vacancy_url']}"

                    for i in user_dict[callback.from_user.id]['position']:

                        if user_dict[callback.from_user.id]['fleet'] in vacancy_dict_fleet and i in vacancy_dict_fleet:

                            await callback.message.answer(vacancy_dict_fleet, reply_markup=stop_menu.as_markup())
                            await state.set_state(FSMFillForm.clear_storage)


                if 'merchant_fleet' in v:
                    vacancy_dict_fleet = f"{v['merchant_fleet']}\n" \
                                            f"{v['vacancy_info']}\n" \
                                            f"{v['vacancy_article']} \n" \
                                            f"{v['vacancy_url']}"

                    print(user_dict[callback.from_user.id]['position'])

                    for i in user_dict[callback.from_user.id]['position']:

                        if user_dict[callback.from_user.id]['fleet'] in vacancy_dict_fleet and i in vacancy_dict_fleet:

                            await callback.message.answer(vacancy_dict_fleet, reply_markup=stop_menu.as_markup())
                            await state.set_state(FSMFillForm.clear_storage)


            while user_dict[callback.from_user.id]['fleet']!=None and user_dict[callback.from_user.id]['position']!= None:
                fresh_vacancies_offshore = check_vacancy_update_offshore()
                fresh_vacancies_merchant = check_vacancy_update_merchant()
                fresh_vacancies_merchant_jobatsea = check_vacancy_update_merchant_jobatsea()
                fresh_vacancies_offshore_jobatsea = check_vacancy_update_offshore_jobatsea()


                if len(fresh_vacancies_offshore)>=1:
                    for s, r in sorted(fresh_vacancies_offshore.items()):
                        if 'offshore_fleet' in r:
                            vacancy_dict_offshore = f"{r['offshore_fleet']}\n\n" \
                                                f"{hbold(r['vacancy_article'])}\n\n" \
                                                f"{r['vacancy_info']}\n\n" \
                                                f"{r['vacancy_url']}"

                            for i in user_dict[callback.from_user.id]['position']:
                                if user_dict[callback.from_user.id]['fleet'] in vacancy_dict_offshore and i in vacancy_dict_offshore:
                                    await callback.message.answer(vacancy_dict_offshore, reply_markup=stop_menu.as_markup())
                                    await state.set_state(FSMFillForm.clear_storage)

                if len(fresh_vacancies_merchant)>=1:
                    for t, m in sorted(fresh_vacancies_merchant.items()):
                        if 'merchant_fleet' in m:
                            vacancy_dict_merchant = f"{m['merchant_fleet']}\n\n" \
                                                f"{hbold(m['vacancy_article'])}\n\n" \
                                                f"{m['vacancy_info']}\n\n" \
                                                f"{m['vacancy_url']}"

                            for i in user_dict[callback.from_user.id]['position']:
                                if user_dict[callback.from_user.id]['fleet'] in vacancy_dict_merchant and i in vacancy_dict_merchant:
                                    await callback.message.answer(vacancy_dict_merchant, reply_markup=stop_menu.as_markup())
                                    await state.set_state(FSMFillForm.clear_storage)

                if len(fresh_vacancies_merchant_jobatsea)>=1:
                    for a, b in sorted(fresh_vacancies_merchant_jobatsea.items()):
                        if 'merchant_fleet' in b:
                            vacancy_dict_merchant_jobatsea = f"{b['merchant_fleet']}\n\n" \
                                                f"{hbold(b['vacancy_article'])}\n\n" \
                                                f"{b['vacancy_info']}\n\n" \
                                                f"{b['vacancy_url']}"

                            for i in user_dict[callback.from_user.id]['position']:
                                if user_dict[callback.from_user.id]['fleet'] in vacancy_dict_merchant_jobatsea and i in vacancy_dict_merchant_jobatsea:
                                    await callback.message.answer(vacancy_dict_merchant_jobatsea, reply_markup=stop_menu.as_markup())
                                    await state.set_state(FSMFillForm.clear_storage)

                if len(fresh_vacancies_offshore_jobatsea)>=1:
                    for c, d in sorted(fresh_vacancies_offshore_jobatsea.items()):
                        if 'offshore_fleet' in d:
                            vacancy_dict_offshore_jobatsea = f"{d['offshore_fleet']}\n\n" \
                                                f"{hbold(d['vacancy_article'])}\n\n" \
                                                f"{d['vacancy_info']}\n\n" \
                                                f"{d['vacancy_url']}"

                            for i in user_dict[callback.from_user.id]['position']:
                                if user_dict[callback.from_user.id]['fleet'] in vacancy_dict_offshore_jobatsea and i in vacancy_dict_offshore_jobatsea:
                                    await callback.message.answer(vacancy_dict_offshore_jobatsea, reply_markup=stop_menu.as_markup())
                                    await state.set_state(FSMFillForm.clear_storage)


                await asyncio.sleep(600)
        else:
            await callback.answer(text='Please fill the data '
                                'by pressing "Search settings"', show_alert=True)


    else:
        await callback.answer(text='Please fill the data '
                            'by pressing "Search settings"', show_alert=True)






@router.callback_query(Text(text='stop_search_button'), StateFilter(FSMFillForm.clear_storage))
async def process_stop_press(callback: CallbackQuery, state: FSMContext):

    await state.update_data(fleet = None, position = None)

    user_dict[callback.from_user.id].update(await state.get_data())

    await state.clear()

    await callback.message.answer(text='You can customize the parameters'
                        ' of what you are looking for by clicking'
                        ' on the <b>"Search Settings"</b> button.',
                         reply_markup=main_menu.as_markup())



@router.callback_query(Text(text='back_button'))
async def process_back_press(callback: CallbackQuery):

    await callback.message.answer(text='You can customize the parameters'
                        ' of what you are looking for by clicking'
                        ' on the <b>"Search Settings"</b> button.',
                         reply_markup=main_menu.as_markup())


@router.callback_query(Text(text='settings_data'))
async def process_back_press(callback: CallbackQuery):

    if callback.from_user.id in user_dict:
        if user_dict[callback.from_user.id]['fleet']!=None and user_dict[callback.from_user.id]['position']!= None:
            await callback.message.answer(text=f'Fleet: {user_dict[callback.from_user.id]["fleet"]}\n'
                        f'Position: {user_dict[callback.from_user.id]["position"]}\n')
        else:
            await callback.answer(text='Please fill the data '
                                    'by pressing "Search settings"', show_alert=True)
    else:
        await callback.answer(text='Please fill the data '
                                  'by pressing "Search settings"', show_alert=True)
