# the program estimates the number of COVID-19 cases in the future 
# using related data that has already been collected on the same


def estimator(data_input):
    return data_input


def get_impact(reportedCases, timeToElapse, totalHospitalBeds, avgDailyIncomePopulation, avgDailyIncomeInUSD):
    currentlyInfected = reportedCases * 10
    infectionsByRequestedTime = (currentlyInfected * (2 ** int(timeToElapse / 3)))
    severeCasesByRequestedTime = int(infectionsByRequestedTime * 0.15)
    hospitalBedsByRequestedTime = int((totalHospitalBeds * 0.35) - severeCasesByRequestedTime )
    casesForICUByRequestedTime = int(infectionsByRequestedTime * 0.05)
    casesForVentilatorsByRequestedTime = int(infectionsByRequestedTime * 0.02)
    dollarsInFlight = round (((infectionsByRequestedTime * avgDailyIncomePopulation) * avgDailyIncomeInUSD * timeToElapse), 1)
    impact = {
        'currentlyInfected': currentlyInfected,
        'infectionsByReportedTime': infectionsByRequestedTime,
        'severeCasesByRequestedTime': severeCasesByRequestedTime,
        'hospitalBedsByRequestedTime': hospitalBedsByRequestedTime,
        'casesForICUByRequestedTime': casesForICUByRequestedTime,
        'casesForVentilatorsByRequestedTime': casesForVentilatorsByRequestedTime,
        'dollarsInFlight': dollarsInFlight
    }
    return impact


def get_severeImpact(reportedCases, timeToElapse, totalHospitalBeds, avgDailyIncomePopulation, avgDailyIncomeInUSD):
    currentlyInfected = reportedCases * 50
    infectionsByRequestedTime = currentlyInfected * (2 ** int(timeToElapse / 3))
    severeCasesByRequestedTime = int(infectionsByRequestedTime * 0.15)
    hospitalBedsByRequestedTime = int((totalHospitalBeds * 0.35) - severeCasesByRequestedTime )
    casesForICUByRequestedTime = int(infectionsByRequestedTime * 0.05)
    casesForVentilatorsByRequestedTime = int(infectionsByRequestedTime * 0.02)
    dollarsInFlight = round (((infectionsByRequestedTime * avgDailyIncomePopulation) * avgDailyIncomeInUSD * timeToElapse), 1)

    severeImpact = {
        'currentlyInfected': currentlyInfected,
        'infectionsByRequestedTime': infectionsByRequestedTime,
        'severeCasesByRequestedTime': severeCasesByRequestedTime,
        'hospitalBedsByRequestedTime': hospitalBedsByRequestedTime,
        'casesForICUByRequestedTime': casesForICUByRequestedTime,
        'casesForVentilatorsByRequestedTime': casesForVentilatorsByRequestedTime,
        'dollarsInFlight': dollarsInFlight
    }
    return severeImpact


def period_conversion(periodType, timeToElapse):
    periodType = periodType.lower()
    if periodType == "months":
        timeToElapse = timeToElapse * 30
    elif periodType == "weeks":
        timeToElapse = timeToElapse * 7
    else:
        timeToElapse = timeToElapse
    return timeToElapse


if __name__ == "__main__":
    pass
    data = {}
    output = {}
    data = {'region': {'name': input("Region: "),
                       'avgAge': float(input("Average age: ")),
                       'avgDailyIncomeInUSD': int(input("Average daily income in US $: ")),
                       'avgDailyIncomePopulation': float(input("Average daily income of population: "))},
            'periodType': input("days\weeks\months: "),
            'timeToElapse': int(input("Time to elapse: ")),
            'reportedCases': int(input("Reported cases: ")),
            'population': int(input("Population size: ")),
            'totalHospitalBeds': int(input("Total number of hospital beds: "))}
    timeToElapse = period_conversion(data["periodType"], data["timeToElapse"])


    def get_output():
        output = {
            'data': data,
            'impact': get_impact(
                                 data["reportedCases"],
                                 data["timeToElapse"],
                                 data["totalHospitalBeds"],
                                 data["region"]["avgDailyIncomePopulation"],
                                 data["region"]["avgDailyIncomeInUSD"]
                                 ),
            'severeImpact': get_severeImpact(
                                             data["reportedCases"],
                                             data["timeToElapse"],
                                             data["totalHospitalBeds"],
                                             data["region"]["avgDailyIncomePopulation"],
                                             data["region"]["avgDailyIncomeInUSD"]
                                           )
        }
        return output


    print(get_output())
