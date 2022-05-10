import time
import xlrd
from collections.abc import Iterable

from plyer import notification

loc = "/home/saurav/Documents/setReminderFile.xls"

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

for c in range(0, sheet.ncols):
    l = sheet.col_values(c, 1, sheet.nrows)
    print("list: ", l)
#TODO: get the time from the excel sheet and print its description and run in background.

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