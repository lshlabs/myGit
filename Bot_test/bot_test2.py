import ccxt
import pandas as pd
import mplfinance as mpf
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt

# 바이낸스 객체 생성
exchange = ccxt.binance()

# 데이터 가져오기
symbol = 'BTC/USDT'
timeframe = '1h'  # 1일 간격
since = exchange.parse8601('2024-12-21 T00:00:00Z')  # 시작 날짜
limit = 100  # 가져올 데이터 수

# OHLCV 데이터 가져오기
ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since, limit)

# 데이터프레임으로 변환
df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

# 타임스탬프를 날짜 형식으로 변환
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
df.set_index('timestamp', inplace=True)  # 타임스탬프를 인덱스로 설정

# y축 숫자 포맷 설정
def format_price(x, pos):
   return f'{int(x):,}'  # 천 단위 구분 기호 추가

# y축 숫자 포맷 설정
def invisible_ticker(x, pos):
   return f' '  # 천 단위 구분 기호 추가


fig, axes = mpf.plot(df, type='candle', style='tradingview', volume=True, figscale=1.5, figratio=(12,12),
        datetime_format='%H:%M', xrotation=0, xlim=(-1, len(df)+1), returnfig=True)


# y축 포맷 설정
#axes[0].yaxis.set_major_formatter(ticker.FuncFormatter(format_price))  # 가격 y축에 format_price 적용

# 그리드 간격 설정
axes[0].yaxis.set_major_locator(ticker.MultipleLocator(1000))  # y축 그리드 간격을 1000으로 설정
#axes[0].yaxis.set_major_locator(ticker.M)  # y축의 최대 눈금 수를 10으로 설정
axes[0].xaxis.set_major_locator(ticker.MaxNLocator(10))  # x축의 최대 눈금 수를 10으로 설정

# 그리드 표시
axes[0].grid(True)  # 그리드 표시

# 현재가 표시
current_price = df['close'].iloc[-1]
axes[0].axhline(y=current_price, color='red', linestyle='dotted', linewidth=0.8)  # 현재가 수평선

# 가격차트 포맷 설정
axes[0].set_title('BTCUSDT · 1H\n', fontsize=16, color='black', loc='center',
                  fontdict={'fontname': 'Arial', 'weight': 'bold'})  # 제목 속성 설정
axes[0].yaxis.tick_left()
axes[0].set_ylabel(' ')
axes[0].yaxis.set_label_position("left")

# 볼륨 차트 포맷 설정
axes[2].set_ylabel(' ')
axes[2].yaxis.set_ticks([])

plt.show()  # 차트를 화면에 표시