import requests
import datetime as dt
from src.typeDefs.derVdiCreationResp import DerivedVdiCreationResp


class DerivedVdiCreationHandler():
    derivedVdiCreationUrl = ''

    def __init__(self, derivedVdiCreationUrl):
        self.derivedVdiCreationUrl = derivedVdiCreationUrl

    def createDerivedVdi(self, startDate: dt.datetime, endDate: dt.datetime) -> DerivedVdiCreationResp:
        """create derived Vdi using the api service
        Args:
            startDate (dt.datetime): start date
            endDate (dt.datetime): end date
        Returns:
            derivedVdiCreationResp: Result of the derived Vdi creation operation
        """
        createDerivedVdiPayload = {
            "startDate": dt.datetime.strftime(startDate, '%Y-%m-%d'),
            "endDate": dt.datetime.strftime(endDate, '%Y-%m-%d')
        }
        res = requests.post(self.derivedVdiCreationUrl,
                            json=createDerivedVdiPayload)

        operationResult: DerivedVdiCreationResp = {
            "isSuccess": False,
            'status': res.status_code,
            'message': 'Unable to create derivedVdi...'
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
