import matplotlib.pyplot as plt
import yfinance as yf

yf.pdr_override()

print("Please enter the stock symbol: ", end = '')
symbol = input()
print("Please enter Start date (yyyy-mm-dd): ", end = '')
start = input()
print("Please enter End date (yyyy-mm-dd): ", end = '')
end = input()

data = yf.download(symbol,start,end)

plt.figure(figsize=(12,8))
plt.plot(data['Adj Close'])
plt.title(symbol + " Line Chart")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()

