"""Программа подсчета прибыли по покупке и продаже BTC, ETH, BNB на P2P с
с дальнейшей реализацией ее через Спот.
"""
from parsing.course_GEL import course_buy_GEL_for_USDT,\
    course_sell_GEL_for_USDT
from parsing.course_crypto import courses
from parsing.course_p2p_crypto import course_sell_GEL_for_BTC,\
    course_sell_GEL_for_ETH, course_sell_GEL_for_BNB, course_buy_GEL_for_BTC,\
    course_buy_GEL_for_ETH


sum_to_send = 1000  # сумма GEL
course_BTC = courses[0]
course_ETH = courses[1]
course_BNB = courses[2]
course_p2p_BTC_buy = course_buy_GEL_for_BTC
course_p2p_BTC = course_sell_GEL_for_BTC
course_p2p_ETH_buy = course_buy_GEL_for_ETH
course_p2p_ETH = course_sell_GEL_for_ETH
course_p2p_BNB = course_sell_GEL_for_BNB
buy_usdt = course_buy_GEL_for_USDT
sell_usdt = course_sell_GEL_for_USDT
sum_to_send_as_usdt = sum_to_send / buy_usdt
sum_to_send_as_usdt_for_buy = sum_to_send / sell_usdt


def profit_btc():
    amount_usdt_finish = sum_to_send / course_p2p_BTC * course_BTC
    profit = amount_usdt_finish - sum_to_send_as_usdt
    return profit


def profit_btc_buy():
    profit = (
        sum_to_send_as_usdt_for_buy / course_BTC * course_p2p_BTC_buy
        / sell_usdt
    ) - sum_to_send_as_usdt_for_buy
    return profit


def profit_eth():
    amount_usdt_finish = sum_to_send / course_p2p_ETH * course_ETH * 0.999
    profit = amount_usdt_finish - sum_to_send_as_usdt
    return profit


def profit_eth_buy():
    profit = (
        sum_to_send_as_usdt_for_buy / course_ETH * course_p2p_ETH_buy
        / sell_usdt
    ) - sum_to_send_as_usdt_for_buy
    return profit


def profit_bnb():
    amount_usdt_finish = sum_to_send / course_p2p_BNB * course_BNB * 0.999
    profit = amount_usdt_finish - sum_to_send_as_usdt
    return profit


print(
    f'Курс P2P USDT: {sell_usdt:.2f} / {buy_usdt:.2f}\n'
    f'Спот BTC, ETH, BNB:    {course_BTC}, {course_ETH}, {course_BNB}\n'
)

print(
    f'P2P buy BTC, ETH, BNB: {course_p2p_BTC}, {course_p2p_ETH}, '
    f'{course_p2p_BNB}'
    f'\nПрибыль по buy BTC, ETH, BNB: {profit_btc():.2f}$, '
    f'{profit_eth():.2f}$, {profit_bnb():.2f}$'
    f'\nСпред по buy BTC, ETH, BNB:   '
    f'{profit_btc() / sum_to_send_as_usdt  * 100:.2f}%, '
    f'{profit_eth() / sum_to_send_as_usdt  * 100:.2f}%, '
    f'{profit_bnb() / sum_to_send_as_usdt  * 100:.2f}%\n'
)
print(
    f'P2P sell BTC, ETH:     {course_p2p_BTC_buy}, {course_p2p_ETH_buy}\n'
    f'Прибыль по sell BTC, ETH: {profit_btc_buy():.2f}$, '
    f'{profit_eth_buy():.2f}$'
    f'\nСпред по sell BTC, ETH:   '
    f'{profit_btc_buy() / sum_to_send_as_usdt_for_buy  * 100:.2f}%, '
    f'{profit_eth_buy() / sum_to_send_as_usdt_for_buy  * 100:.2f}%'
)
