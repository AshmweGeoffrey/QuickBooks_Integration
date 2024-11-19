from datetime import datetime, timedelta
def get_transactions_with_date_range(target_date, days_range):
    target_datetime = datetime.strptime(target_date, '%Y-%m-%d')
    start_date = (target_datetime - timedelta(days=days_range)).strftime('%Y-%m-%d')
    end_date = (target_datetime + timedelta(days=days_range)).strftime('%Y-%m-%d')
    return_list = [start_date, end_date]
    return return_list
def main():
   print(get_transactions_with_date_range('2021-01-01', 3))
if __name__ == "__main__":
    main()