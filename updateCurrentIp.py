import datetime
from requests import get

import gspread
from oauth2client.service_account import ServiceAccountCredentials

def GetSheetClient():
    scope = ["https://spreadsheets.google.com/feeds"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
    client = gspread.authorize(creds)

    return client

def GetSheet():
    c = GetSheetClient()
    return c.open("rpi-public-ip")#.sheet1

def WriteNewIp(sheet, oldIp, newIp):
    sheetCurrent = sheet.get_worksheet(0)
    sheetLog = sheet.get_worksheet(1)

    sheetCurrent.update_acell("A2", newIp)
    sheetCurrent.update_acell("B2", datetime.date.today())

    values = [oldIp, newIp, datetime.date.today()]
    sheetLog.append_row(values)

def GetIp():
    ip = get("https://api.ipify.org").text
    return ip

print("Fetching ip from sheet")
ws = GetSheet()
sheet = ws.get_worksheet(0)
sheetIp = sheet.acell("A2").value
print("Fetching public ip")
currentIp = GetIp()

if sheetIp != currentIp:
    print("A new IP was found: %s (old ip: %s)" % (currentIp, sheetIp))
    WriteNewIp(ws, sheetIp, currentIp)
    print("New IP written to google sheet document.")
else:
    print("No new IP was found. IP is still %s" % sheetIp)
