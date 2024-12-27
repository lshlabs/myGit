import logging
import requests
import mplfinance as mpf
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.ticker as ticker
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import asyncio

# 로깅 설정
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# API 토큰 입력
TOKEN = '7533494717:AAGeUDhojuN0XH4nZtEdeEHL-zsSQjsujWo'  # 여기에 텔레그램 봇 토큰을 입력하세요.

# # 한글 폰트 설정
# font_path = 'C:/Windows/Fonts/malgun.ttf'  # Malgun Gothic 폰트 경로
# font_prop = fm.FontProperties(fname=font_path, size=12)
# plt.rc('font', family=font_prop.get_name())
# plt.rcParams['axes.unicode_minus'] = False  # 음수 기호 표시

# 이전 BTC 가격 저장
previous_btc_price = None

# Kline 데이터 가져오기
def get_historical_data(symbol, interval, limit):
    url = f"https://api.binance.com/api/v3/klines"
    params = {
        'symbol': symbol,
        'interval': interval,
        'limit': limit  # 가져올 데이터의 개수
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if response.status_code == 200:
        return data  # 가격 데이터 반환
    else:
        return None

# BTC 가격 가져오기
async def get_btc_price(chat_id):
    global previous_btc_price  # 전역 변수로 선언
    historical_data = get_historical_data('BTCUSDT', '1s', 1)  # 1분 간격으로 최근 60개 데이터 가져오기
    if historical_data:
        close_price = float(historical_data[0][4])  # 종료 가격
        message = f"현재 BTC 가격은 {close_price:.2f} USDT입니다."
        return message
    else:
        return "가격 정보를 가져오는 데 실패했습니다."
    
# ETH 가격 가져오기
async def get_eth_price(chat_id):
    logging.info('Received /eth command')  # 로그 추가
    historical_data = get_historical_data('ETHUSDT', '1s', 1)  # 1분 간격으로 최근 60개 데이터 가져오기
    if historical_data:
        close_price = float(historical_data[0][4])  # 종료 가격
        message = f"현재 ETH 가격은 {close_price:.2f} USDT입니다."  # 소수점 둘째 자리까지 출력
        return message  # 메시지 반환
    else:
        return "가격 정보를 가져오는 데 실패했습니다."

# # 주기적으로 BTC 가격 메시지 보내기
# async def send_btc_price(context: ContextTypes.DEFAULT_TYPE):
#     chat_id = context.job.context
#     message = await get_btc_price(chat_id)
#     await context.bot.send_message(chat_id=chat_id, text=message)

# # /start 명령어 처리
# async def start_command(update, context):
#     await update.message.reply_text("봇이 시작되었습니다. 1분마다 BTC 가격을 업데이트합니다.")
#     context.job_queue.run_repeating(send_btc_price, interval=60, first=0, context=update.message.chat.id)



# 캔들스틱 차트 생성
async def create_candle_chart(symbol, interval='1m'):
    historical_data = get_historical_data(symbol, interval, 120)  # 선택한 간격으로 데이터 가져오기
    if historical_data is None:
        return None

    # 데이터프레임으로 변환
    df = pd.DataFrame(historical_data, columns=['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 
                                                 'Close Time', 'Quote Asset Volume', 'Number of Trades', 
                                                 'Taker Buy Base Asset Volume', 'Taker Buy Quote Asset Volume', 'Ignore'])
    
    # 필요한 열만 선택하고 데이터 타입 변환
    df = df[['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume']]
    df['Open Time'] = pd.to_datetime(df['Open Time'], unit='ms').dt.tz_localize('UTC').dt.tz_convert('Asia/Seoul')  # Open Time을 datetime으로 변환
    df.set_index('Open Time', inplace=True)  # Open Time을 인덱스로 설정
    df = df.astype(float)  # 모든 열을 float로 변환

    # 차트 생성
    fig, axes = mpf.plot(df, type='candle', style='tradingview', volume=False, figscale=1.5, figratio=(12,10),
        datetime_format='%H:%M', xrotation=0, xlim=(-1, len(df)+1), returnfig=True)

    # axes를 활용하여 추가적인 설정
    # 그리드 간격 설정
    if symbol == 'BTCUSDT':
        if interval == '1m':
            axes[0].yaxis.set_major_locator(ticker.MultipleLocator(50))  # y축 그리드 간격을 50으로 설정
        elif interval == '5m':
            axes[0].yaxis.set_major_locator(ticker.MultipleLocator(250))  # y축 그리드 간격을 250으로 설정
        elif interval == '15m':
            axes[0].yaxis.set_major_locator(ticker.MultipleLocator(500))  # y축 그리드 간격을 500으로 설정
    elif symbol == 'ETHUSDT':
        if interval == '1m':
            axes[0].yaxis.set_major_locator(ticker.MultipleLocator(5))  # y축 그리드 간격을 10으로 설정
        elif interval == '5m':
            axes[0].yaxis.set_major_locator(ticker.MultipleLocator(10))  # y축 그리드 간격을 25으로 설정
        elif interval == '15m':
            axes[0].yaxis.set_major_locator(ticker.MultipleLocator(25))  # y축 그리드 간격을 50으로 설정
    
    #axes[0].xaxis.set_major_locator(ticker.MultipleLocator(15))
    axes[0].grid(True)  # 그리드 표시
    
    # 현재가 표시
    current_price = df['Close'].iloc[-1]
    axes[0].axhline(y=current_price, color='red', linestyle='dotted', linewidth=0.8)  # 현재가 수평선
    
    # 가격차트 포맷 설정
    axes[0].set_title(f'{symbol} · {interval}\n', fontsize=16, color='black', loc='center',
                  fontdict={'fontname': 'Arial', 'weight': 'bold'})  # 제목 속성 설정
    axes[0].yaxis.tick_left()
    axes[0].set_ylabel(' ')

    # 볼륨 차트 포맷 설정
    #axes[2].set_ylabel(' ')
    #axes[2].yaxis.set_ticks([])
    

    # 차트 저장
    chart_path = f'{symbol}_candle_chart.png'
    plt.savefig(chart_path)  # 차트 저장
    plt.close(fig)  # 차트 닫기
    
    return chart_path

# /chart 명령어 처리
async def chart_command(update, context):
    logging.info('Received /chart command')  # 로그 추가
    symbol = context.args[0] if context.args else 'BTCUSDT'  # 기본값은 BTCUSDT
    chart_path = await create_candle_chart(symbol)  # 캔들스틱 차트 생성
    if chart_path:
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(chart_path, 'rb'))  # 차트 전송
        os.remove(chart_path)  # 차트 파일 삭제
    else:
        await update.message.reply_text("차트를 생성하는 데 실패했습니다.")

# /help 명령어 처리
async def help_command(update, context):
    logging.info('Received /help command')  # 로그 추가

    # 버튼 생성
    keyboard = [
        [InlineKeyboardButton("BTC 가격 조회", callback_data='btc_price'), InlineKeyboardButton("BTC 차트 보기", callback_data='btc_chart')], 
        [InlineKeyboardButton("ETH 가격 조회", callback_data='eth_price'), InlineKeyboardButton("ETH 차트 보기", callback_data='eth_chart')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('도움이 필요하신가요? 아래 버튼을 클릭하세요:', reply_markup=reply_markup)

# 버튼 클릭 시 처리
async def button_callback(update, context):
    query = update.callback_query
    await query.answer()  # 콜백 쿼리 응답

    # 이전 메시지를 삭제하기 위해 chat_id와 message_id를 저장
    chat_id = query.message.chat.id

    # 사용자 상태를 저장하기 위한 딕셔너리 (context.user_data 사용)
    if 'btc_price_last_message_id' not in context.user_data:
        context.user_data['btc_price_last_message_id'] = None  # BTC 가격 메시지 ID 초기화
    if 'eth_price_last_message_id' not in context.user_data:
        context.user_data['eth_price_last_message_id'] = None  # ETH 가격 메시지 ID 초기화

    # 클릭한 버튼에 따라 처리
    if query.data == 'btc_price':
        message = await get_btc_price(chat_id)  # 최신 BTC 가격 가져오기
        
        # 두 번째 클릭부터 이전 메시지 삭제 후 새로운 메시지 전송
        if context.user_data['btc_price_last_message_id'] is not None:
            last_message_id = context.user_data['btc_price_last_message_id']
            try:
                await context.bot.delete_message(chat_id=chat_id, message_id=last_message_id)  # 이전 메시지 삭제
            except Exception as e:
                # 메시지 삭제 중 오류가 발생한 경우 무시
                pass
        
        # 새로운 메시지 전송
        new_message = await query.message.reply_text(message)  # 새로운 BTC 가격 메시지 전송
        context.user_data['btc_price_last_message_id'] = new_message.message_id  # 새로운 메시지 ID 저장
        
    elif query.data == 'eth_price':
        message = await get_eth_price(chat_id)  # 최신 ETH 가격 가져오기
        
        # 두 번째 클릭부터 이전 메시지 삭제 후 새로운 메시지 전송
        if context.user_data['eth_price_last_message_id'] is not None:
            last_message_id = context.user_data['eth_price_last_message_id']
            try:
                await context.bot.delete_message(chat_id=chat_id, message_id=last_message_id)  # 이전 메시지 삭제
            except Exception as e:
                # 메시지 삭제 중 오류가 발생한 경우 무시
                pass
        
        # 새로운 메시지 전송
        new_message = await query.message.reply_text(message)  # 새로운 ETH 가격 메시지 전송
        context.user_data['eth_price_last_message_id'] = new_message.message_id  # 새로운 메시지 ID 저장

    elif query.data == 'btc_chart':
        # BTC 차트 옵션 버튼 생성
        keyboard = [
            [InlineKeyboardButton("1분 차트", callback_data='btc_chart_1m'), InlineKeyboardButton("5분 차트", callback_data='btc_chart_5m')],
            [InlineKeyboardButton("15분 차트", callback_data='btc_chart_15m')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text('차트 간격을 선택하세요:', reply_markup=reply_markup)
        
    elif query.data == 'eth_chart':
        # ETH 차트 옵션 버튼 생성
        keyboard = [
            [InlineKeyboardButton("1분 차트", callback_data='eth_chart_1m'), InlineKeyboardButton("5분 차트", callback_data='eth_chart_5m')],
            [InlineKeyboardButton("15분 차트", callback_data='eth_chart_15m')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text('차트 간격을 선택하세요:', reply_markup=reply_markup)
    
    elif query.data.startswith('btc_chart_'):  # BTC 차트 간격 선택 처리
        interval = query.data.split('_')[-1]  # 차트 간격 추출
        await create_candle_chart('BTCUSDT', interval)  # 선택한 간격으로 차트 생성
        await context.bot.send_photo(chat_id=query.message.chat.id, photo=open('BTCUSDT_candle_chart.png', 'rb'))  # 차트 전송
        message = await get_btc_price(query.message.chat.id)
        await query.message.reply_text(message)
        
    elif query.data.startswith('eth_chart_'):   # ETH 차트 간격 선택 처리
        interval = query.data.split('_')[-1]  # 차트 간격 추출
        await create_candle_chart('ETHUSDT', interval)  # 선택한 간격으로 차트 생성
        await context.bot.send_photo(chat_id=query.message.chat.id, photo=open('ETHUSDT_candle_chart.png', 'rb'))  # 차트 전송
        message = await get_eth_price(query.message.chat.id)
        await query.message.reply_text(message)

    # /help 명령어를 사용한 경우, 클릭 상태 초기화
    if query.data == 'help':
        context.user_data['btc_price_last_message_id'] = None  # BTC 가격 메시지 ID 초기화
        context.user_data['eth_price_last_message_id'] = None  # ETH 가격 메시지 ID 초기화

    # 마지막 명령어 상태 업데이트
    context.user_data['last_command'] = query.data

# 메인 함수
def main():
    app = ApplicationBuilder().token(TOKEN).build()  # ApplicationBuilder 사용

    # 핸러 추가
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CallbackQueryHandler(button_callback))
    
    # 봇 시작
    logging.info('Bot is starting...')  # 로그 추가
    app.run_polling()

if __name__ == '__main__':
    main()