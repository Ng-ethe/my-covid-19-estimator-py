
def estimator(data):
  return data


def get_impact (reportedCases ):
  currentlyInfected = reportedCases * 10
  infectionsByRequestedTime = int (currentlyInfected * (2 ** (timeToElapse / 3)))
  impact = {
    'currentlyInfected': currentlyInfected,
    'infectionsByReportedTime': infectionsByRequestedTime
  }
  return impact


def get_severeImpact (reportedCases):
  currentlyInfected = reportedCases * 50
  infectionsByRequestedTime = currentlyInfected * (2 ** int (timeToElapse/3))
  severeImpact = {
    'currentlyInfected': currentlyInfected,
    'infectionsByReportedTime': infectionsByRequestedTime
  }
  return severeImpact

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


    def get_output():
        output = {
            'data': estimator(data),
            'impact':  get_impact(data["reportedCases"]),
            'severeImpact': get_severeImpact(data["reportedCases"])
        }
        return output





    print ( get_output())
