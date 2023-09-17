import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope and credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("YOUR_KEY_FILE.json", scope)

# Authenticate with Google Sheets
gc = gspread.authorize(credentials)

# Open the Google Sheets document by its title or URL
# Replace 'YOUR_SPREADSHEET_TITLE' with the title of your Google Sheets document
# or use the URL if you prefer
spreadsheet = gc.open("YOUR_SPREADSHEET_TITLE")

# Select the specific worksheet within the document
# Replace 'Sheet1' with the name of your worksheet
worksheet = spreadsheet.worksheet("Sheet1")