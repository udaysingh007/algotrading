from lumibot.traders import Trader

# Import interactive brokers
from lumibot.brokers import InteractiveBrokers
from lumibot.strategies.examples import Strangle
from creds import INTERACTIVE_BROKERS_CONFIG


trader = Trader()
# Initialize interactive brokers
interactive_brokers = InteractiveBrokers(INTERACTIVE_BROKERS_CONFIG)

strategy = Strangle(broker=interactive_brokers)
trader.add_strategy(strategy)
trader.run_all()
