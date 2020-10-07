from typing import TypedDict, List


class DerivedFreqFetchResp(TypedDict):
    isSuccess: bool
    status: int
    message: str
    data: DerivedFreqData


class DerivedFreqData(TypedDict):
    rows: List[DayDerFreq]
    weeklyFDI: float


class DayDerFreq(TypedDict):
    date: float
    max: float
    min: float
    avg: float
    less: float
    bw: float
    great: float
    out: float
    outHrs: float
    fdi: float
