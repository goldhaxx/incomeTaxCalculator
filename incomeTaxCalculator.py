from pip._vendor import requests
from pprint import pprint as pp

#collect your data or set default values
try:
  yourTaxYear = int(input("Enter the year you would like to check taxes for. Leave blank for 2020."))
except:
  yourTaxYear = 2020
try:
  yourPayRate = int(input("Enter your annual pay rate, numerical characters only, like 20000, or 50000. Leave blank for 50000"))
except:
  yourPayRate = 50
try:
  yourFilingStatus = str(input("Enter your marital filing status ('single', 'married', 'married_separately', or 'head_of_household'. Leave blank for single."))
except:
  yourFilingStatus = str('single')
try:
  yourState = str(input("Enter the abbreviated state where you will be filing(ie CA/IA/NC). Leave blank for CA."))
except:
  yourState = str('CA')
try:
  yourPayPeriods = int(input("Enter how many pay periods you will have in one year. Leave blank for 26."))
except:
  yourPayPeriods = 26
try:
  yourExemptions = int(input("EnterThe number of exemptions. Defaults to 1 if the filing_status is 'single', 'married_separately', or 'head_of_household'. Defaults to 2 if filing_status is set to 'married'. Leave blank for 1."))
except:
    yourExemptions = 1
#yourPreTaxContributions = int(input("Please enter any pre-tax contributions (Medical/401(k))"))

#Set default values

if yourPayRate == None:
    yourPayRate = 50
if yourFilingStatus == None:
  yourFilingStatus = str('single')
if yourState == None:
   yourState = str('CA')
if yourPayPeriods == None:
  yourPayPeriods = 26
if yourExemptions == None:
  yourExemptions = 1

#Prepare API call
taxeeApiKey = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJBUElfS0VZX01BTkFHRVIiLCJodHRwOi8vdGF4ZWUuaW8vdXNlcl9pZCI6IjVmNzQyMTEzYjgyZGRkNjlmZWU3YTg0ZCIsImh0dHA6Ly90YXhlZS5pby9zY29wZXMiOlsiYXBpIl0sImlhdCI6MTYwMTQ0NjE2M30.JyWlc3jGOU0RSETbq8CZyf7J_vzn7xUbHA8mBEKAKTc"
url = 'https://taxee.io/api/v2/calculate/2020'
headers = {
    'Authorization': 'Bearer ' + taxeeApiKey,
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {
  'year':yourTaxYear,
  'pay_rate': yourPayRate,
  'filing_status': yourFilingStatus,
  'state':yourState,
  'pay_periods': yourPayPeriods,
  'exemptions': yourExemptions
  }

#Review entries
entryConfirmation = 'n'

while (entryConfirmation == None or 'n' or 'N'):
  print("Your Tax Year: " + str(yourTaxYear))
  print("Your Pay Rate: " + str(yourPayRate))
  print("Your Filing Status: " + str(yourFilingStatus))
  print("Your Filing State: " + str(yourState))
  print("Your Pay Periods: " + str(yourPayPeriods))
  print("Your Exemptions: " + str(yourExemptions))
  entryConfirmation = str(input("Does this look right?(Y/N)"))
  if entryConfirmation == 'Y':
    break

taxeeResponse = requests.post(url, headers=headers, data=data).json()
pp(taxeeResponse)