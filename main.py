import time
import xlrd
from collections.abc import Iterable

from plyer import notification

loc = "/home/saurav/Documents/setReminderFile.xls"

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

list_of_start_time_of_each_reminder = []
list_of_reminder_time = sheet.col_values(1, 1, sheet.nrows)

for i in range(0, len(list_of_reminder_time)):
    reminder_time = list_of_reminder_time[i]
    if len(list_of_start_time_of_each_reminder)-1 >=i and list_of_start_time_of_each_reminder[i]:
        # convert the reminder time into timeout
        timeout = get_timeout_time(reminder_time)
    else:
        list_of_start_time_of_each_reminder.


    times_loop_run = sheet.col_values(0, i, )
    notification.notify(

    )
#TODO: get the time from the excel sheet and print its description and run in background.
#TODO:
#print(sheet.cell_value(0, 0))

'''
if __name__ == '__main__':
    while True:
        notification.notify(
            title=" please Drink water",
            message=" Water is healthy for body",
            app_icon="/home/saurav/PycharmProjects/pythonProject/NotificationReminder/icon.ico",
            timeout=10
        )
        time.sleep(6)
'''



# command to run python program in background is : python filename &