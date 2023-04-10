from datetime import datetime
from course_RUB import course_tinkoff, course_raif
from courses_Credo import course_USD_from_Credo, course_EURO_from_Credo_min, \
     course_corona_gel, course_corona_usd  # course_EURO_from_Credo_max
from course_GEL import course_buy_GEL_for_USDT, course_sell_GEL_for_USDT
# , \course_sell_EUR_for_USDT

sum_to_send_USD = 1000  # Оборот в $
course_sell_USDT_for_RUB = max(course_tinkoff, course_raif)
sum_to_send_in_RUB = sum_to_send_USD * course_sell_USDT_for_RUB

course_buy_GEL_for_USDT = course_buy_GEL_for_USDT  # больший курс
course_sell_GEL_for_USDT = course_sell_GEL_for_USDT  # меньший курс
course_USD_from_Credo = course_USD_from_Credo  # курс банка
spred_classic = course_buy_GEL_for_USDT / course_sell_GEL_for_USDT * 100 - 100

course_USD_from_corona = course_corona_usd  # курс USD ЗК
# course_EURO_from_corona = 81.9176  # курс EURO ЗК
course_GEL_from_corona = course_corona_gel  # курс GEL ЗК
course_USD_from_unistream = 82.611  # курс USD юнистрим
course_EURO_from_unistream = 90.26075  # курс EURP юнистрим #
course_GEL_from_unistream = 33.0107  # курс GEL Unistream

# course_USD_from_contact = 77.5097
# course_GEL_from_contact = 30.59471


# Функции расчета прибыльности
def unistream_usd():
    profit = (
        sum_to_send_in_RUB / course_USD_from_unistream
        * course_USD_from_Credo / course_sell_GEL_for_USDT
        * course_sell_USDT_for_RUB * 0.999) - (sum_to_send_in_RUB * 1.005)
    return profit


def corona_usd():
    corona_USD_profit_rub = (
        (
         sum_to_send_in_RUB / course_USD_from_corona * course_USD_from_Credo
         / course_sell_GEL_for_USDT * course_sell_USDT_for_RUB * 0.999
        ) - (sum_to_send_in_RUB * 1.005)
    )
    return corona_USD_profit_rub


# def contact_usd():
#     profit = (
#         sum_to_send_in_RUB / course_USD_from_contact
#         * course_USD_from_Credo / course_sell_GEL_for_USDT
#         * course_sell_USDT_for_RUB * 0.999) - (sum_to_send_in_RUB * 1.005)
#     return profit


def corona_gel():  # Функция подсчета прибыли через отправку GEL по ЗК
    corona_profit_RUB = (
        (
         sum_to_send_in_RUB / course_GEL_from_corona
         / course_sell_GEL_for_USDT * course_sell_USDT_for_RUB * 0.999
        ) - (sum_to_send_in_RUB * 1.005)
    )
    return corona_profit_RUB


def unistream_gel():  # Функция подсчета прибыли через отправку GEL по ЗК
    unistream_profit_RUB = (
        (
         sum_to_send_in_RUB / course_GEL_from_unistream
         / course_sell_GEL_for_USDT * course_sell_USDT_for_RUB * 0.999
        ) - (sum_to_send_in_RUB * 1.005)
        )
    return unistream_profit_RUB

# def contact_gel():  # Функция подсчета прибыли через отправку GEL по ЗК
#     profit = (
#         (sum_to_send_in_RUB / course_GEL_from_contact
#          / course_sell_GEL_for_USDT * course_sell_USDT_for_RUB * 0.999)
#          - (sum_to_send_in_RUB * 1.005)
#     )
#     return profit


# def corona_euro():
#     corona_EURO_profit_rub = (
#         (sum_to_send_in_RUB / course_EURO_from_corona
#         * course_EURO_from_Credo_min / course_sell_GEL_for_USDT
#         * course_sell_USDT_for_RUB * 0.999) - (sum_to_send_in_RUB * 1.005)
#     )
#     return corona_EURO_profit_rub

def unistream_euro():
    unistream_EURO_profit_rub = (
        (
         sum_to_send_in_RUB / course_EURO_from_unistream
         * course_EURO_from_Credo_min / course_sell_GEL_for_USDT
         * course_sell_USDT_for_RUB * 0.999
        ) - (sum_to_send_in_RUB * 1.005)
    )
    return unistream_EURO_profit_rub


# def euro_classic():
#     profit = (
#         (sum_to_send_USD / course_sell_EUR_for_USDT* course_buy_GEL_for_USDT)
#         - (sum_to_send_USD * course_EURO_from_Credo_max)
#     )
#     spred = profit / (sum_to_send_USD * course_EURO_from_Credo_max) * 100
#     return spred


if unistream_usd() > corona_usd():
    print(
        f'\nПрибыль по Unistream USD c {sum_to_send_USD}$ '
        f'составит: {unistream_usd():.2f} рублей. '
        f'Спред: 'f'{unistream_usd() / sum_to_send_in_RUB * 100:.2f}% '
        f'vs ЗК: {corona_usd() / sum_to_send_in_RUB * 100:.2f}%\n'
    )
elif corona_usd() > unistream_usd():
    print(
        f'\nПрибыль по Золотой короне USD c {sum_to_send_USD}$ '
        f'составит: {corona_usd():.2f} рублей. '
        f'Спред: {corona_usd() / sum_to_send_in_RUB * 100:.2f}% '
        f'vs Uni: {unistream_usd() / sum_to_send_in_RUB * 100:.2f}%\n'
    )
# elif contact_usd() > unistream_usd() and contact_usd() > corona_usd():
#     print(
#         f'\nПрибыль по Contact USD c {sum_to_send_USD}$ '
#         f'составит: {contact_usd():.2f} рублей. '
#         f'Спред: {contact_usd() / (sum_to_send_in_RUB) * 100:.2f}%\n'
#     )

if unistream_euro():  # > corona_euro():
    print(
        f'Прибыль по Unistream EURO c {sum_to_send_USD}$ '
        f'составит: {unistream_euro():.2f} рублей. '
        f'Спред: {unistream_euro() / sum_to_send_in_RUB * 100:.2f}%\n'
    )
# elif unistream_euro() < corona_euro():
#     print(
#         f'Прибыль по Золотой короне EURO c {sum_to_send_USD}$ '
#         f'составит: {corona_euro():.2f} рублей. '
#         f'Спред: {corona_euro() / sum_to_send_in_RUB * 100:.2f}%\n'
#         )

if corona_gel() > unistream_gel():
    print(
        f'Прибыль по Золотой короне GEL c {sum_to_send_USD}$ '
        f'составит: {corona_gel():.2f} рублей. '
        f'Спред: {corona_gel() / sum_to_send_in_RUB * 100:.2f}% '
        f'vs Uni: {unistream_gel() / sum_to_send_in_RUB * 100:.2f}%\n'
    )
elif unistream_gel() > corona_gel():
    print(
        f'Прибыль по Unistream GEL c {sum_to_send_USD}$ '
        f'составит: {unistream_gel():.2f} рублей. '
        f'Спред: {unistream_gel() / sum_to_send_in_RUB * 100:.2f}% '
        f'vs ЗК: {corona_gel() / sum_to_send_in_RUB * 100:.2f}%\n'
        )
# elif contact_gel() > corona_gel() and contact_gel() > unistream_gel():
#     print(
#         f'Прибыль по Contact GEL c {sum_to_send_USD}$ '
#         f'составит: {contact_gel():.2f} рублей. '
#         f'Спред: {contact_gel() / sum_to_send_in_RUB * 100:.2f}%\n'
#         )

# Проверка и справочная информация
print(
    f'Местное время: {datetime.now().time().strftime("%H:%M:%S")}     | '
    f'Курс USDT/RUB: {course_sell_USDT_for_RUB:.2f}      | '
    f'Курс ЗК: {course_GEL_from_corona:.5f} '
    f'\nКурс Credo: USD/GEL: {course_USD_from_Credo:.3f}  | '
    f'EURO/GEL: {course_EURO_from_Credo_min}'
    f'\nПокупка GEL за USDT: {course_buy_GEL_for_USDT:.2f}   | '
    f'Покупка USDT за GEL: {course_sell_GEL_for_USDT:.2f} | '
    f'Спред классики: {spred_classic:.2f}% '
    # f'\nКонвертация GEL/EURO: {course_EURO_from_Credo_max:.3f} | '
    # f'Покупка EUR/USDT: {course_sell_EUR_for_USDT}   | '
    # f'Спред EURO/USDT: {euro_classic():.2f}%'
)
