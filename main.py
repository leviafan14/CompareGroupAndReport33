from compare_requests import *
from functions import *


if __name__ == "__main__":
    auth_data = auth_request(auth_url, auth_domen, login, password)
    report33_data = get_report33_data("e:academic_years:23", "e:academic_years:22", auth_data)
    group_journal = get_group_journal(auth_data, "2025-04-01", "2025-04-30", "e:groups:68343")
    compare_result = compare_group_journal_with_report33_data(report33_data, group_journal)

    print(compare_result['not_compared'])