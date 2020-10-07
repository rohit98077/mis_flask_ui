import requests
import datetime as dt
from src.typeDefs.derFrequencyCreationResp import DerFrequencyCreationResp


class DerivedFrequencyCreationHandler():
    derivedFrequencyCreationUrl = ''

    def __init__(self, derivedFrequencyCreationUrl):
        self.derivedFrequencyCreationUrl = derivedFrequencyCreationUrl

    def createDerivedFrequency(self, startDate: dt.datetime, endDate: dt.datetime) -> DerFrequencyCreationResp:
        """create derived Frequency using the api service
        Args:
            startDate (dt.datetime): start date
            endDate (dt.datetime): end date
        Returns:
            DerivedFrequencyCreationResp: Result of the derivedFrequency creation operation
        """
        createDerivedFrequencyPayload = {
            "startDate": dt.datetime.strftime(startDate, '%Y-%m-%d'),
            "endDate": dt.datetime.strftime(endDate, '%Y-%m-%d')
        }
        res = requests.post(self.derivedFrequencyCreationUrl,
                            json=createDerivedFrequencyPayload)

        operationResult: DerFrequencyCreationResp = {
            "isSuccess": False,
            'status': res.status_code,
            'message': 'Unable to create derived frequency...'
        }

        if res.status_code == requests.codes['ok']:
            resJSON = res.json()
            operationResult['isSuccess'] = True
            operationResult['message'] = resJSON['message']
        else:
            operationResult['isSuccess'] = False
            try:
                resJSON = res.json()
                print(resJSON['message'])
                operationResult['message'] = resJSON['message']
            except ValueError:
                operationResult['message'] = res.text
                # print(res.text)
        return operationResult
