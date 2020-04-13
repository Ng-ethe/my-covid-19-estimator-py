
def estimator(data):
  return data


def impact (reportedCases ):
  currentlyInfected = reportedCases * 10
  infectionsByRequestedTime = currentlyInfected * (2 ** int(timeToElapse / 3))
  impacts = {
    'currentlyInfected': currentlyInfected,
    'infectionsByReportedTime': infectionsByRequestedTime
  }
  return impacts


def severeImpact (reportedCases):
  currentlyInfected = reportedCases * 50
  infectionsByRequestedTime = currentlyInfected * (2 ** int (timeToElapse/3))
  severeImpacts = {
    'currentlyInfected': currentlyInfected,
    'infectionsByReportedTime': infectionsByRequestedTime
  }
  return severeImpacts

def period_conversion (periodType, timeToElapse):
  periodType = periodType.lower()
  if periodType == "months":
    timeToElapse = timeToElapse * 30
  elif periodType == "weeks":
    timeToElapse = timeToElapse * 7
  return timeToElapse




if __name__ == "__main__":
    pass
    data = { 'region': { 'name': input("Region: "),
                         'avgAge': float (input ("Average age: ")),
                         'avgDailyIncomeInUSD': int(input("Average daily income in US $: ")),
                         'avgDailyIncomePopulation': float ( input ("Average daily income of population: "))},
             'periodType': input ("days\weeks\months: "),
             'timeToElapse': int ( input ("Time to elapse: ")),
             'reportedCases': int ( input ("Reported cases: ")),
             'population': int ( input ("Population size: ")),
             'totalHospitalBeds': int ( input ("Total number of hospital beds: ")) }
    timeToElapse = period_conversion(data["periodType"], data["timeToElapse"])

    print (estimator(data))
    print (impact(data["reportedCases"]))
    print (severeImpact(data["reportedCases"]))
