def estimator(data):
    return data


def get_impact(reportedCases, timeToElapse, totalHospitalBeds, avgDailyIncomePopulation, avgDailyIncomeInUSD):
    currentlyInfected = reportedCases * 10
    infectionsByRequestedTime = (currentlyInfected * (2 ** int(timeToElapse / 3)))
    severeCasesByRequestedTime = int(infectionsByRequestedTime * 0.15)
    hospitalBedsByRequestedTime = int(severeCasesByRequestedTime - (totalHospitalBeds * 0.35))
    casesForICUByRequestedTime = int(infectionsByRequestedTime * 0.05)
    casesForVentilatorsByRequestedTime = int(infectionsByRequestedTime * 0.02)
    dollarsInFlight = int((infectionsByRequestedTime * avgDailyIncomePopulation) * avgDailyIncomeInUSD * timeToElapse)
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
    hospitalBedsByRequestedTime = int(severeCasesByRequestedTime - (totalHospitalBeds * 0.35))
    casesForICUByRequestedTime = int(infectionsByRequestedTime * 0.05)
    casesForVentilatorsByRequestedTime = int(infectionsByRequestedTime * 0.02)
    dollarsInFlight = int((infectionsByRequestedTime * avgDailyIncomePopulation) * avgDailyIncomeInUSD * timeToElapse)

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
"""
    data = {
        'region': {
            'name': "Africa",
            'avgAge': 19.7,
            'avgDailyIncomeInUSD': 5,
            'avgDailyIncomePopulation': 0.71
        },
        'periodType': "days",
        'timeToElapse': 58,
        'reportedCases': 674,
        'population': 66622705,
        'totalHospitalBeds': 1380614
    } """


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
            'data': estimator(data),
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
