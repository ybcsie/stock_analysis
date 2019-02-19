import stock
import os

listed_sid_path = "listed.sid"
trade_data_dir = "smd"
dtd_dir = "dtd"
sfd_dir = "sfd"

months = 150
attack_delta_percentage_min = 9

work_arr = None
ready = False


def init(display_func):
    global work_arr

    logger = stock.Logger("work", display_func)

    logger.logp("update_listed_list : start")
    stock.updater.update_listed_list(listed_sid_path)
    logger.logp("update_listed_list : done\n")

    stock.updater.update_dtd(dtd_dir, months)

    logger.logp("read_stock_data_cptr_list : start")
    listed_list = stock.reader.read_stock_data_cptr_list(
        listed_sid_path, months * 30)
    logger.logp("read_stock_data_cptr_list : done\n")

    logger.logp("update_smd_in_list : start")
    stock.updater.update_smd_in_list(listed_list, trade_data_dir)
    logger.logp("update_smd_in_list : done\n")

    logger.logp("read_trade_data_in_list : start")
    stock.reader.read_trade_data_in_list(trade_data_dir, listed_list, months)
    logger.logp("read_trade_data_in_list : done\n")

    logger.logp("read_sfd_in_list : start")
    stock.reader.read_sfd_in_list(sfd_dir, listed_list)
    logger.logp("read_sfd_in_list : done\n")

    stock.reader.read_all_dtd(dtd_dir, listed_list)

    work_arr = stock.init_work_arr(listed_list)
    logger.logp("Init: OK\n")

    if not os.path.exists("imgopt"):
        os.makedirs("imgopt")


if __name__ == '__main__':
    init(print)

    days_range_in = 120
    buy_rule_no = 2
    roi_rule_no = 3
    price_limit = 500
    rang_months = 12
    while True:

        stock.stock.set_price_limit(price_limit)

    # stock.figure.plot_3months_percentage(
    #     work_arr, days_range_in, attack_delta_percentage_min, months, buy_rule_no, roi_rule_no)

        stock.figure.plot_months(work_arr, days_range_in, attack_delta_percentage_min, rang_months, buy_rule_no, roi_rule_no)
        buy_rule_no = int(input("buy_rule_no: "))
        roi_rule_no = int(input("roi_rule_no: "))
        price_limit = int(input("price_limit: "))
        rang_months = int(input("rang_months: "))
    # stock.figure.plot_months_percentage(
    #     work_arr, days_range_in, attack_delta_percentage_min, months, buy_rule_no, roi_rule_no)
    #
    # stock.figure.plot_days(
    #     work_arr, days_range_in, attack_delta_percentage_min, months * 20, buy_rule_no, roi_rule_no)
    #
    # stock.figure.plot(work_arr, days_range_in,
    #                   attack_delta_percentage_min, buy_rule_no, roi_rule_no)

