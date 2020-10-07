import requests
import datetime as dt
from src.typeDefs.rawFrequencyCreationResp import RawFrequencyCreationResp


class RawFrequencyCreationHandler():
    rawFrequencyCreationUrl = ''

    def __init__(self, rawFrequencyCreationUrl):
        self.rawFrequencyCreationUrl = rawFrequencyCreationUrl

    def createRawFrequency(self, startDate: dt.datetime, endDate: dt.datetime) ->RawFrequencyCreationResp:
        """create raw freq using the api service
        Args:
            startDate (dt.datetime): start date
            endDate (dt.datetime): end date
        Returns:
            RawFrequencyCreationResp: Result of the raw frequency creation operation
        """        
        createrawFrequencyPayload = {
            "startDate": dt.datetime.strftime(startDate, '%Y-%m-%d'),
            "endDate": dt.datetime.strftime(endDate, '%Y-%m-%d')
        }
        res = requests.post(self.rawFrequencyCreationUrl,
                            json=createrawFrequencyPayload)
        
        operationResult: RawFrequencyCreationResp = {
            "isSuccess": False,
            'status': res.status_code,
            'message': 'Unable to create raw frequency...'
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