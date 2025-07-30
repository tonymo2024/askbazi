#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
八字計算模組
實現天干地支計算、八字排盤、大運計算等功能
"""

import datetime
from lunar_python import Lunar, Solar
from typing import Tuple, List, Dict

class BaziCalculator:
    """八字計算器"""
    
    # 天干
    TIANGAN = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
    
    # 地支
    DIZHI = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
    
    # 五行對應
    WUXING_TIANGAN = {
        '甲': '木', '乙': '木', '丙': '火', '丁': '火', '戊': '土',
        '己': '土', '庚': '金', '辛': '金', '壬': '水', '癸': '水'
    }
    
    WUXING_DIZHI = {
        '子': '水', '丑': '土', '寅': '木', '卯': '木', '辰': '土', '巳': '火',
        '午': '火', '未': '土', '申': '金', '酉': '金', '戌': '土', '亥': '水'
    }
    
    # 生肖對應
    SHENGXIAO = ['鼠', '牛', '虎', '兔', '龍', '蛇', '馬', '羊', '猴', '雞', '狗', '豬']
    
    # 時辰對應
    SHICHEN = {
        '子': (23, 1), '丑': (1, 3), '寅': (3, 5), '卯': (5, 7),
        '辰': (7, 9), '巳': (9, 11), '午': (11, 13), '未': (13, 15),
        '申': (15, 17), '酉': (17, 19), '戌': (19, 21), '亥': (21, 23)
    }
    
    def __init__(self):
        """初始化計算器"""
        pass
    
    def get_lunar_date(self, solar_date: datetime.date, solar_time: datetime.time) -> Lunar:
        """獲取農曆日期"""
        solar = Solar(solar_date.year, solar_date.month, solar_date.day, 
                     solar_time.hour, solar_time.minute, solar_time.second)
        return solar.getLunar()
    
    def get_hour_dizhi(self, hour: int) -> str:
        """根據小時獲取時支"""
        for dizhi, (start, end) in self.SHICHEN.items():
            if start <= hour < end or (dizhi == '子' and (hour >= 23 or hour < 1)):
                return dizhi
        return '子'  # 默認返回子時
    
    def get_hour_tiangan(self, day_tiangan: str, hour_dizhi: str) -> str:
        """根據日干和時支獲取時干"""
        # 時干推算表
        day_gan_index = self.TIANGAN.index(day_tiangan)
        hour_zhi_index = self.DIZHI.index(hour_dizhi)
        
        # 時干計算公式：(日干序號 * 2 + 時支序號) % 10
        hour_gan_index = (day_gan_index * 2 + hour_zhi_index) % 10
        return self.TIANGAN[hour_gan_index]
    
    def calculate_bazi(self, birth_date: datetime.date, birth_time: datetime.time) -> Dict:
        """計算八字"""
        # 獲取農曆日期
        lunar = self.get_lunar_date(birth_date, birth_time)
        
        # 年柱
        year_gan = lunar.getYearGan()
        year_zhi = lunar.getYearZhi()
        year_pillar = year_gan + year_zhi
        
        # 月柱
        month_gan = lunar.getMonthGan()
        month_zhi = lunar.getMonthZhi()
        month_pillar = month_gan + month_zhi
        
        # 日柱
        day_gan = lunar.getDayGan()
        day_zhi = lunar.getDayZhi()
        day_pillar = day_gan + day_zhi
        
        # 時柱
        hour_zhi = self.get_hour_dizhi(birth_time.hour)
        hour_gan = self.get_hour_tiangan(day_gan, hour_zhi)
        hour_pillar = hour_gan + hour_zhi
        
        # 生肖
        year_zhi_index = self.DIZHI.index(year_zhi)
        shengxiao = self.SHENGXIAO[year_zhi_index]
        
        # 日主五行
        day_master_wuxing = self.WUXING_TIANGAN[day_gan]
        
        return {
            'year_pillar': year_pillar,
            'month_pillar': month_pillar,
            'day_pillar': day_pillar,
            'hour_pillar': hour_pillar,
            'day_master': day_gan,
            'day_master_wuxing': day_master_wuxing,
            'shengxiao': shengxiao,
            'lunar_date': lunar,
            'tiangan': [year_gan, month_gan, day_gan, hour_gan],
            'dizhi': [year_zhi, month_zhi, day_zhi, hour_zhi]
        }
    
    def calculate_dayun(self, bazi_info: Dict, gender: str, birth_date: datetime.date) -> List[Dict]:
        """計算大運"""
        dayun_list = []
        
        # 獲取月柱天干地支
        month_gan = bazi_info['tiangan'][1]
        month_zhi = bazi_info['dizhi'][1]
        
        # 判斷順逆
        year_gan = bazi_info['tiangan'][0]
        year_gan_index = self.TIANGAN.index(year_gan)
        is_yang_year = year_gan_index % 2 == 0  # 甲丙戊庚壬為陽年
        
        # 男命陽年順排，陰年逆排；女命相反
        if gender == '男':
            shun_ni = is_yang_year
        else:
            shun_ni = not is_yang_year
        
        # 起運年齡（簡化計算，實際應考慮節氣）
        qiyun_age = 7  # 簡化為7歲起運
        
        # 計算10步大運
        month_gan_index = self.TIANGAN.index(month_gan)
        month_zhi_index = self.DIZHI.index(month_zhi)
        
        for i in range(10):
            if shun_ni:  # 順排
                gan_index = (month_gan_index + i + 1) % 10
                zhi_index = (month_zhi_index + i + 1) % 12
            else:  # 逆排
                gan_index = (month_gan_index - i - 1) % 10
                zhi_index = (month_zhi_index - i - 1) % 12
            
            dayun_gan = self.TIANGAN[gan_index]
            dayun_zhi = self.DIZHI[zhi_index]
            dayun_pillar = dayun_gan + dayun_zhi
            
            start_age = qiyun_age + i * 10
            end_age = start_age + 9
            
            dayun_list.append({
                'pillar': dayun_pillar,
                'gan': dayun_gan,
                'zhi': dayun_zhi,
                'start_age': start_age,
                'end_age': end_age,
                'wuxing': self.WUXING_TIANGAN[dayun_gan]
            })
        
        return dayun_list
    
    def analyze_wuxing_balance(self, bazi_info: Dict) -> Dict:
        """分析五行平衡"""
        wuxing_count = {'木': 0, '火': 0, '土': 0, '金': 0, '水': 0}
        
        # 統計天干五行
        for gan in bazi_info['tiangan']:
            wuxing = self.WUXING_TIANGAN[gan]
            wuxing_count[wuxing] += 1
        
        # 統計地支五行
        for zhi in bazi_info['dizhi']:
            wuxing = self.WUXING_DIZHI[zhi]
            wuxing_count[wuxing] += 1
        
        # 找出最強和最弱的五行
        max_wuxing = max(wuxing_count, key=wuxing_count.get)
        min_wuxing = min(wuxing_count, key=wuxing_count.get)
        
        # 簡化的喜用神判斷（實際應更複雜）
        day_master_wuxing = bazi_info['day_master_wuxing']
        
        # 如果日主五行偏弱，則喜生扶；如果偏強，則喜克洩
        if wuxing_count[day_master_wuxing] <= 2:
            # 日主偏弱，喜生扶
            if day_master_wuxing == '木':
                favorable_elements = ['水', '木']
            elif day_master_wuxing == '火':
                favorable_elements = ['木', '火']
            elif day_master_wuxing == '土':
                favorable_elements = ['火', '土']
            elif day_master_wuxing == '金':
                favorable_elements = ['土', '金']
            else:  # 水
                favorable_elements = ['金', '水']
        else:
            # 日主偏強，喜克洩
            if day_master_wuxing == '木':
                favorable_elements = ['金', '火']
            elif day_master_wuxing == '火':
                favorable_elements = ['水', '土']
            elif day_master_wuxing == '土':
                favorable_elements = ['木', '金']
            elif day_master_wuxing == '金':
                favorable_elements = ['火', '水']
            else:  # 水
                favorable_elements = ['土', '木']
        
        return {
            'wuxing_count': wuxing_count,
            'max_wuxing': max_wuxing,
            'min_wuxing': min_wuxing,
            'favorable_elements': favorable_elements
        }

# 測試代碼
if __name__ == "__main__":
    calculator = BaziCalculator()
    
    # 測試數據
    birth_date = datetime.date(1985, 5, 29)
    birth_time = datetime.time(14, 5)
    gender = '男'
    
    # 計算八字
    bazi_info = calculator.calculate_bazi(birth_date, birth_time)
    print("八字信息：", bazi_info)
    
    # 計算大運
    dayun = calculator.calculate_dayun(bazi_info, gender, birth_date)
    print("大運信息：", dayun[:3])  # 只顯示前3步大運
    
    # 分析五行
    wuxing_analysis = calculator.analyze_wuxing_balance(bazi_info)
    print("五行分析：", wuxing_analysis)

