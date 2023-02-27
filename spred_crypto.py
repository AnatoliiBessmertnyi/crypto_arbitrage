from course_GEL import course_buy_GEL_for_USDT
from course_crypto import courses
from course_p2p_crypto import course_sell_GEL_for_BTC, course_sell_GEL_for_ETH, \
    course_sell_GEL_for_BNB

sum_to_send = 128 # сумма GEL

course_BTC = courses[0]
course_ETH = courses[1]
course_BNB = courses[2]
course_p2p_BTC = course_sell_GEL_for_BTC
course_p2p_ETH = course_sell_GEL_for_ETH
course_p2p_BNB = course_sell_GEL_for_BNB
course_USDT = course_buy_GEL_for_USDT
sum_to_send_as_usdt = sum_to_send / course_USDT

def profit_btc():
    amount_usdt_finish = sum_to_send / course_p2p_BTC * course_BTC
    profit = amount_usdt_finish - sum_to_send_as_usdt
    return profit

def profit_eth():
    amount_usdt_finish = sum_to_send / course_p2p_ETH * course_ETH * 0.999
    profit = amount_usdt_finish - sum_to_send_as_usdt
    return profit

def profit_bnb():
    amount_usdt_finish = sum_to_send / course_p2p_BNB * course_BNB * 0.999
    profit = amount_usdt_finish - sum_to_send_as_usdt
    return profit

print(
    f'Прибыль по BTC, ETH, BNB: {profit_btc():.2f}$, {profit_eth():.2f}$, {profit_bnb():.2f}$'
    f'\nСпред по BTC, ETH, BNB:   {profit_btc() / sum_to_send_as_usdt  * 100:.2f}%, {profit_eth() / sum_to_send_as_usdt  * 100:.2f}%, {profit_bnb() / sum_to_send_as_usdt  * 100:.2f}%'
)

print('Курс USDT:', course_USDT)
print('Спот BTC, ETH, BNB:', course_BTC, course_ETH, course_BNB)
print('P2P BTC, ETH, BNB:', course_p2p_BTC, course_p2p_ETH, course_p2p_BNB)