import time
import threading

import pandas as pd

from ibapi.wrapper import EWrapper
from ibapi.client import EClient
from ibapi.common import TickerId, BarData
from ibapi.contract import Contract
from ibapi.contract import ContractDetails
from ibapi.ticktype import TickTypeEnum


class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.bars = pd.DataFrame()

    def error(self, reqId:TickerId, errorCode:int, errorString:str):
        print(f"error: {reqId} {errorCode} {errorString} ")

    def nextValidId(self, orderId:int):
        print(f"orderId: {orderId}")
        return orderId

    def managedAccounts(self, accountsList:str):
        print(f"managed accounts: {accountsList}")

    def contractDetails(self, reqId:int, contractDetails):#ContractDetails):
        print(f"contractDetails: {reqId} {contractDetails}")

    def tickPrice(self, reqId: int, tickType, price, attrib):
        print(f"Tick Price: Ticker id: {reqId}, tickerType: {TickTypeEnum.to_str(tickType)}, price: {price}")

    def tickSize(self, reqId: int, tickType, size):
        print(f"Tick Price: Ticker id: {reqId}, tickerType: {TickTypeEnum.to_str(tickType)}, size: {size}")

    def historicalData(self, reqId: int, bar: BarData):
        print(f"HistoricalData: {reqId}, {bar.__dict__}")

    def historicalData(self, reqId: int, bar: BarData):
        s = pd.Series(bar.__dict__)
        self.bars = self.bars.append(s, ignore_index=True)

        # print("HistoricalData. ReqId:", reqId, "BarData.", bar)

    def historicalDataEnd(self, reqId: int, start: str, end: str):
        super().historicalDataEnd(reqId, start, end)
        print("HistoricalDataEnd. ReqId:", reqId, "from", start, "to", end)
        print(self.bars)
        print(self.bars.head())
        print(self.bars.shape)


def main():
    app = TestApp()
    # cause API running on same computer as TWS, host is localhost = 127.0.0.1
    app.connect("127.0.0.1", 7497, clientId=4)

    con_thread = threading.Thread(target=app.run, daemon=True)
    con_thread.start()

    contract = Contract()
    contract.symbol = "AAPL"
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"
    contract.primaryExchange = "ISLAND"

    app.reqContractDetails(10, contract)
    app.reqHistoricalData(11, contract, '20210101 01:00:00', '1 M', '5 mins', 'MIDPOINT', 1, 1, False, [])
    app.run()

    # app.reqContractDetails(10, contract)
    # app.reqManagedAccts()
    # app.reqMarketDataType(4)
    # app.reqMktData(1, contract, "", False, False, [])
    # app.run()
    # app.reqHistoricalData(1, contract, "", "1 M", "30 mins", "MIDPOINT", 0, 1, False, [])
    # ReportSnapshot(company overview)
    # ReportsFinSummary(financial summary)
    # ReportRatios(financial ratios)
    # ReportsFinStatements(financial statements)
    # RESC(analyst estimates)
    # app.reqFundamentalData(1, contract, "ReportsFinSummary", [])
    # app.reqFundamentalData(1, contract, "RESC", [])


if __name__ == "__main__":
    main()
