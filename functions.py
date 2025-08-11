from compare_requests import *


def compare_group_journal_with_report33_data(report33_data: dict, group_journal_data: dict) ->dict:
    report_data = report33_data['data']
    journal_data = group_journal_data['data']
    compared_data = []
    not_compared_data = []
    result_compared = {"compared": None, "not_compared": None}
    for d in journal_data:
        if d in report_data:
            compared_data.append(d)
        else:
            not_compared_data.append(d)

    result_compared['compared'] = compared_data
    result_compared['not_compared'] = not_compared_data

    return result_compared
