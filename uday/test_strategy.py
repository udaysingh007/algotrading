import backtrader as bt

# Create a Stratey
class TestStrategy(bt.Strategy):

    def log(self, txt, ts=None):
        ''' Logging function for this strategy'''
        ts = ts or self.datas[0].datetime.datetime(0)
        print(f'{ts}, {txt}')

    def __init__(self):
        self.close0 = self.datas[0].close
        self.name0 = self.datas[0]._name

        self.close1 = self.datas[1].close
        self.name1 = self.datas[1]._name

    def next(self):
        # Current close dataset0
        self.log(f'{self.name0} Close:{self.close0[0]:.2f}' )
        if self.close0[0] < self.close0[-1]:
             # current close less than previous close, think about buying
             if self.close0[-1] < self.close0[-2]:
                # previous close less than previous close, so buy
                self.log(f"BUY {self.name0} @ {self.close0[0]:.2f}")
                self.buy()

        # Current close dataset1
        self.log(f'{self.name1} Close:{self.close1[0]:.2f}' )
        if self.close1[0] < self.close1[-1]:
             # current close less than previous close, think about buying
             if self.close1[-1] < self.close1[-2]:
                # previous close less than previous close, so buy
                self.log(f"BUY {self.name1} @ {self.close1[0]:.2f}")
                self.buy()