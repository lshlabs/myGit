import os
import json

class TradingSettings:
    """매매 설정 데이터를 관리하는 클래스"""
    
    def __init__(self, is_short=False):
        """초기화 메서드: 기본 설정값 지정"""
        self.is_short = is_short
        self.position_type = "숏" if is_short else "롱"
        
        # 코인 선택
        self.coin_selection = ""
        
        # 시그널 1 설정
        self.signal1 = {
            "type": "",       # 시그널 유형 (RSI, MACD 등)
            "timeframe": "",  # 봉타입 (1분봉, 5분봉 등)
            "settings": {}    # 세부 설정 (다이얼로그에서 반환된 값)
        }
        
        # 시그널 2 설정
        self.signal2 = {
            "type": "",       # 시그널 유형
            "timeframe": "",  # 봉타입
            "settings": {}    # 세부 설정
        }
        
        # 매수 금액 설정
        self.buy_amount = {
            "base_amount": 0,        # 기본 매수 금액
            "leverage": 0,            # 레버리지
            "use_split": False,      # 분할 매수 사용 여부
            "split_criteria": "",    # 분할 매수 기준 (rsi 또는 price)
            "rsi_level1": 0,         # RSI 기준값
            "rsi_amount1": 0,        # RSI 조건1 매수 비율
            "rsi_amount2": 0,        # RSI 조건2 매수 비율
            "price_drop1": 0,        # 가격 하락 기준값
            "price_amount1": 0,      # 가격 하락 조건1 매수 비율
            "price_amount2": 0       # 가격 하락 조건2 매수 비율
        }
        
        # 손절 설정
        self.stop_loss = {
            "type": "",              # 손절 방식 (rate, indicator)
            "rate": 0.0,             # 손절 비율 (%)
            "indicator": 0           # 지표 기준 손절
        }
        
        # 익절 설정
        self.take_profit = {
            "type": "",              # 익절 방식 (rate, indicator)
            "rate": 0.0,             # 익절 비율 (%)
            "indicator": 0           # 지표 기준 익절
        }
    
    def to_dict(self):
        """설정값을 딕셔너리로 변환"""
        return {
            "coin_selection": self.coin_selection,
            "signal1": self.signal1,
            "signal2": self.signal2,
            "buy_amount": self.buy_amount,
            "stop_loss": self.stop_loss,
            "take_profit": self.take_profit
        }
    
    def from_dict(self, data):
        """딕셔너리에서 설정값 로드"""
        if not data:
            return False
            
        self.coin_selection = data.get("coin_selection", self.coin_selection)
        self.signal1 = data.get("signal1", self.signal1)
        self.signal2 = data.get("signal2", self.signal2)
        self.buy_amount = data.get("buy_amount", self.buy_amount)
        self.stop_loss = data.get("stop_loss", self.stop_loss)
        self.take_profit = data.get("take_profit", self.take_profit)
        return True
    
    def to_text(self):
        """설정 요약을 텍스트로 반환"""
        txt = f"{self.position_type} 포지션 설정 요약:\n"
        txt += f"코인: {self.coin_selection}\n"
        
        txt += f"시그널1: {self.signal1['type']} ({self.signal1['timeframe']})\n"
        if self.signal1['settings']:
            txt += f"  설정: {str(self.signal1['settings'])}\n"
            
        txt += f"시그널2: {self.signal2['type']} ({self.signal2['timeframe']})\n"
        if self.signal2['settings']:
            txt += f"  설정: {str(self.signal2['settings'])}\n"
            
        txt += f"매수금액: {self.buy_amount['base_amount']} USDT\n"
        
        if self.buy_amount['use_split']:
            txt += "분할매수: 사용함\n"
            if self.buy_amount['split_criteria'] == 'rsi':
                txt += f"  방식: RSI 기준 (레벨:{self.buy_amount['rsi_level1']})\n"
                txt += f"  비율: {self.buy_amount['rsi_amount1']}% / {self.buy_amount['rsi_amount2']}%\n"
            elif self.buy_amount['split_criteria'] == 'price':
                txt += f"  방식: 가격하락 기준 (하락률:{self.buy_amount['price_drop1']}%)\n"
                txt += f"  비율: {self.buy_amount['price_amount1']}% / {self.buy_amount['price_amount2']}%\n"
        else:
            txt += "분할매수: 사용안함\n"
            
        if self.stop_loss['type'] == 'rate':
            txt += f"손절: {self.stop_loss['rate']}% 손실 시\n"
        elif self.stop_loss['type'] == 'indicator':
            txt += f"손절: 지표값 {self.stop_loss['indicator']} 기준\n"
            
        if self.take_profit['type'] == 'rate':
            txt += f"익절: {self.take_profit['rate']}% 이익 시\n"
        elif self.take_profit['type'] == 'indicator':
            txt += f"익절: 지표값 {self.take_profit['indicator']} 기준\n"
            
        return txt
        
    def save_to_file(self, filename=None):
        """설정 객체를 JSON 파일에 저장"""
        if filename is None:
            # 기본 저장 경로 설정
            filename = "neworder_proto/data/data.json"
            
        # 디렉토리가 없으면 생성
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        # 기존 파일이 있으면 먼저 읽기
        all_settings = {}
        if os.path.exists(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    all_settings = json.load(f)
            except:
                # 파일 읽기 실패시 빈 딕셔너리로 초기화
                all_settings = {}
        
        # 롱/숏 설정 구분하여 저장
        if self.is_short:
            all_settings["short_settings"] = self.to_dict()
        else:
            all_settings["long_settings"] = self.to_dict()
        
        # 파일에 저장
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(all_settings, f, ensure_ascii=False, indent=4)
            return True
        except Exception as e:
            print(f"설정 파일 저장 중 오류 발생: {e}")
            return False
    
    def load_from_file(self, filename=None):
        """JSON 파일에서 설정 로드"""
        if filename is None:
            # 기본 저장 경로 설정
            filename = "neworder_proto/data/data.json"
            
        if not os.path.exists(filename):
            print(f"설정 파일이 존재하지 않습니다: {filename}")
            return False
            
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                all_settings = json.load(f)
                
                # 롱/숏 설정 구분하여 로드
                if self.is_short:
                    if "short_settings" in all_settings:
                        return self.from_dict(all_settings["short_settings"])
                else:
                    if "long_settings" in all_settings:
                        return self.from_dict(all_settings["long_settings"])
                        
                return False
        except Exception as e:
            print(f"설정 파일 로드 중 오류 발생: {e}")
            return False