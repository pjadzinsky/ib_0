import time

from ibapi.wrapper import EWrapper
from ibapi.client import EClient
from ibapi.common import TickerId, BarData
from ibapi.contract import Contract
from ibapi.contract import ContractDetails
from ibapi.ticktype import TickTypeEnum


class TestApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId:TickerId, errorCode:int, errorString:str):
        print(f"error: {reqId} {errorCode} {errorString} ")

    # def nextValidId(self, orderId:int):
    def contractDetails(self, reqId:int, contractDetails):#ContractDetails):
        print(f"contractDetails: {reqId} {contractDetails}")

    def tickPrice(self, reqId: int, tickType, price, attrib):
        print(f"Tick Price: Ticker id: {reqId}, tickerType: {TickTypeEnum.to_str(tickType)}, price: {price}")

    def tickSize(self, reqId: int, tickType, size):
        print(f"Tick Price: Ticker id: {reqId}, tickerType: {TickTypeEnum.to_str(tickType)}, size: {size}")

    def historicalData(self, reqId: int, bar: BarData):
        print(f"HistoricalData: {reqId}, {bar.__dict__}")

    def fundamentalData(self, reqId: TickerId, data: str):
        data = ET.fromstring(data)
        for datum in data:
            print(f"Fundamental Data: {datum.tag}, {datum.attrib}")

def main():
    app = TestApp()

    # cause API running on same computer as TWS, host is localhost = 127.0.0.1
    app.connect("127.0.0.1", 7497, clientId=4)
    time.sleep(1)

    contract = Contract()
    contract.symbol = "AAPL"
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"
    contract.primaryExchange = "NASDAQ"

    # app.reqContractDetails(10, contract)
    # app.run()

    app.reqContractDetails(10, contract)
    app.reqMarketDataType(4)
    app.reqMktData(1, contract, "", False, False, [])
    app.run()
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
