import gspread
import datetime
import sys

from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('gspread_config.json', scope)

def log(comment):
    gs = gspread.authorize(credentials)
    wks = gs.open('Tasks Completed').sheet1
    moment = datetime.datetime.now()
    date = moment.strftime("%d-%b-%Y")
    time = moment.strftime("%H:%M")
    try:
        wks.append_row([date,time,comment])
        print("\n\nTask logged.\n{}\t{}\t{}".format(comment,date,time))
        return True
    except:
        return False

if __name__ == "__main__":
    try:
        option = sys.argv[1]
    except:
        option = None
    if not option:
        comment = input("\nWhat have you accomplished?\n")
        while not log(comment) and cont.lower() != "n":
            cont = input("Continue? (n to exit) ")
    else:
        log(sys.argv[1])
    print("\n\nThanks for using Task Logger!\n")
