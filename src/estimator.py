
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
    data = { 'region': { 'name': "Africa",
                         'avgAge': 19.7,
                         'avgDailyIncomeInUSD': 5,
                         'avgDailyIncomePopulation': 0.71},
             'periodType': "days",
             'timeToElapse': 58,
             'reportedCases': 674,
             'population': 66622705,
             'totalHospitalBeds': 1380614 }
    timeToElapse = period_conversion(data["periodType"], data["timeToElapse"])

    print (estimator(data))
    print (impact(data["reportedCases"]))
    print (severeImpact(data["reportedCases"]))
