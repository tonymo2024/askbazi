#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
算命內容生成模組
根據八字信息生成各章節的算命內容
"""

import random
from typing import Dict, List

class ContentGenerator:
    """內容生成器"""
    
    # 天干地支常量
    TIANGAN = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
    DIZHI = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
    
    def __init__(self):
        """初始化內容生成器"""
        self.load_content_templates()
    
    def load_content_templates(self):
        """加載內容模板"""
        # 性格特質模板
        self.personality_templates = {
            '木': {
                '正面': ['仁慈善良', '積極進取', '富有創造力', '適應能力強', '有理想抱負'],
                '負面': ['固執己見', '容易急躁', '缺乏耐性', '過於理想化'],
                '特質': ['喜歡自然', '重視成長', '具有領導才能', '善於規劃']
            },
            '火': {
                '正面': ['熱情開朗', '積極主動', '富有感染力', '勇於表達', '樂觀向上'],
                '負面': ['性情急躁', '容易衝動', '缺乏持久力', '過於直率'],
                '特質': ['喜歡熱鬧', '重視名聲', '具有表演天賦', '善於交際']
            },
            '土': {
                '正面': ['穩重踏實', '忠誠可靠', '勤勞務實', '包容寬厚', '責任心強'],
                '負面': ['過於保守', '缺乏變通', '行動遲緩', '容易固執'],
                '特質': ['重視安全感', '善於理財', '具有組織能力', '注重實際']
            },
            '金': {
                '正面': ['意志堅強', '果斷決絕', '重視原則', '追求完美', '執行力強'],
                '負面': ['過於嚴厲', '缺乏彈性', '容易孤僻', '過分挑剔'],
                '特質': ['重視品質', '善於分析', '具有領導威嚴', '注重效率']
            },
            '水': {
                '正面': ['聰明機智', '靈活變通', '善於溝通', '富有智慧', '適應性強'],
                '負面': ['缺乏恆心', '容易多變', '過於圓滑', '缺乏原則'],
                '特質': ['重視學習', '善於思考', '具有洞察力', '注重人際關係']
            }
        }
        
        # 事業運模板
        self.career_templates = {
            '木': ['教育培訓', '文化創意', '環保綠化', '醫療保健', '農林牧漁'],
            '火': ['媒體傳播', '娛樂表演', '廣告行銷', '電子科技', '能源化工'],
            '土': ['房地產', '建築工程', '農業種植', '礦業開採', '物流運輸'],
            '金': ['金融投資', '機械製造', '軍警執法', '珠寶首飾', '五金工具'],
            '水': ['貿易商業', '旅遊服務', '水產養殖', '清潔環衛', '運輸物流']
        }
        
        # 財運模板
        self.wealth_templates = {
            '偏財': ['投資理財運佳', '容易有意外之財', '適合多元化投資', '財來財去較頻繁'],
            '正財': ['穩定收入來源', '勤勞致富', '適合長期投資', '財富累積穩健'],
            '劫財': ['財運起伏較大', '容易破財', '需謹慎理財', '避免借貸擔保'],
            '比肩': ['財運平穩', '適合合夥經營', '收入穩定', '開支有度']
        }
        
        # 婚姻模板
        self.marriage_templates = {
            '正官': ['婚姻穩定', '配偶品格端正', '家庭責任感強', '夫妻恩愛'],
            '七殺': ['感情波折較多', '配偶性格強勢', '需要磨合', '晚婚較佳'],
            '正印': ['配偶賢慧', '家庭和睦', '子女孝順', '婚姻美滿'],
            '偏印': ['感情複雜', '容易有第三者', '需要包容理解', '溝通重要']
        }
    
    def generate_personal_info(self, name: str, bazi_info: Dict, wuxing_analysis: Dict, 
                              birth_date, birth_time, gender: str) -> str:
        """生成命主資料"""
        lunar_date = bazi_info['lunar_date']
        shengxiao = bazi_info['shengxiao']
        day_master_wuxing = bazi_info['day_master_wuxing']
        favorable_elements = wuxing_analysis['favorable_elements']
        
        content = f"""命主：{name}

出生日期(西曆)：{birth_date.year}年{birth_date.month}月{birth_date.day}日
出生時間：{birth_time.hour}時{birth_time.minute}分
性別：{gender}
生肖：{shengxiao}

日主五行：{day_master_wuxing}
喜用神五行：{', '.join(favorable_elements)}

八字：{bazi_info['year_pillar']} {bazi_info['month_pillar']} {bazi_info['day_pillar']} {bazi_info['hour_pillar']}
天干：{' '.join(bazi_info['tiangan'])}
地支：{' '.join(bazi_info['dizhi'])}"""
        
        return content
    
    def generate_life_summary(self, bazi_info: Dict, wuxing_analysis: Dict) -> str:
        """生成人生總論"""
        day_master_wuxing = bazi_info['day_master_wuxing']
        personality = self.personality_templates[day_master_wuxing]
        
        positive_traits = random.sample(personality['正面'], 3)
        negative_traits = random.sample(personality['負面'], 2)
        special_traits = random.sample(personality['特質'], 2)
        
        content = f"""● 命主性格分析

您的日主五行為{day_master_wuxing}，具有{day_master_wuxing}性人的典型特質。在性格方面，您{positive_traits[0]}，{positive_traits[1]}，{positive_traits[2]}，這些都是您的優勢所在。

● 人生特點

從八字組合來看，您{special_traits[0]}，{special_traits[1]}。在人生道路上，您容易因為{negative_traits[0]}而遇到一些挫折，但只要能夠克服{negative_traits[1]}的缺點，必能在人生路上取得不錯的成就。

● 總體運勢

您的八字中{day_master_wuxing}氣較為{self._get_strength_description(wuxing_analysis)}，這表示您在人生中{self._get_life_pattern_description(wuxing_analysis)}。建議您在日常生活中多接觸{wuxing_analysis['favorable_elements'][0]}、{wuxing_analysis['favorable_elements'][1]}相關的事物，有助於提升整體運勢。

● 人際關係

在人際交往方面，您{self._get_relationship_description(day_master_wuxing)}。與人相處時，建議您發揮{positive_traits[0]}的優點，同時注意控制{negative_traits[0]}的傾向，這樣能夠建立更好的人際關係網絡。"""
        
        return content
    
    def generate_career_summary(self, bazi_info: Dict, wuxing_analysis: Dict) -> str:
        """生成事業總論"""
        day_master_wuxing = bazi_info['day_master_wuxing']
        favorable_elements = wuxing_analysis['favorable_elements']
        
        suitable_careers = []
        for element in favorable_elements:
            suitable_careers.extend(self.career_templates.get(element, []))
        
        selected_careers = random.sample(suitable_careers, min(5, len(suitable_careers)))
        
        content = f"""● 事業運勢分析

從您的八字來看，事業發展方面具有一定的優勢。您的日主{day_master_wuxing}性，在工作中展現出{self._get_work_style_description(day_master_wuxing)}的特點。

● 適合的職業方向

根據您的八字喜用神分析，比較適合從事與{favorable_elements[0]}、{favorable_elements[1]}相關的行業，具體包括：{', '.join(selected_careers)}等領域。

● 事業發展建議

在事業發展過程中，建議您{self._get_career_advice(day_master_wuxing)}。同時要注意發揮自身{self.personality_templates[day_master_wuxing]['正面'][0]}的優勢，避免因{self.personality_templates[day_master_wuxing]['負面'][0]}而影響事業進展。

● 創業與就業

從命理角度來看，您{self._get_entrepreneurship_advice(wuxing_analysis)}。無論選擇創業還是就業，都要充分考慮自身的五行喜忌，選擇合適的合作夥伴和工作環境。"""
        
        return content
    
    def generate_wealth_summary(self, bazi_info: Dict, wuxing_analysis: Dict) -> str:
        """生成財運總論"""
        day_master = bazi_info['day_master']
        wealth_type = self._analyze_wealth_star(bazi_info)
        
        content = f"""● 財運基本分析

您的八字中財星{self._get_wealth_star_description(wealth_type)}，這表示您在財富累積方面{self._get_wealth_pattern_description(wealth_type)}。

● 求財方式

根據您的命理特點，比較適合通過{self._get_wealth_method_description(wealth_type)}的方式來獲取財富。在投資理財方面，建議您{self._get_investment_advice(wealth_type)}。

● 財運週期

從大運流年來看，您的財運會有一定的週期性變化。一般來說，在{wuxing_analysis['favorable_elements'][0]}、{wuxing_analysis['favorable_elements'][1]}當旺的年份，財運會相對較好。

● 理財建議

在日常理財方面，建議您{self._get_financial_advice(wealth_type)}。同時要注意避免在{self._get_unfavorable_period()}期間進行大額投資，以免造成不必要的損失。"""
        
        return content
    
    def generate_marriage_summary(self, bazi_info: Dict, gender: str) -> str:
        """生成姻緣總論"""
        spouse_star = self._analyze_spouse_star(bazi_info, gender)
        
        content = f"""● 婚姻基本分析

從您的八字來看，配偶星{self._get_spouse_star_description(spouse_star)}，這表示您在感情婚姻方面{self._get_marriage_pattern_description(spouse_star)}。

● 配偶特徵

根據命理分析，您的配偶可能具有{self._get_spouse_characteristics(spouse_star)}的特點。在選擇伴侶時，建議您{self._get_spouse_selection_advice(spouse_star)}。

● 婚姻時機

從大運流年來看，您比較適合在{self._get_marriage_timing(bazi_info)}歲左右考慮婚姻大事。這個時期的感情運勢相對較好，容易遇到合適的對象。

● 感情建議

在感情交往中，建議您{self._get_relationship_advice(spouse_star)}。同時要注意{self._get_marriage_precautions(spouse_star)}，這樣有助於維持穩定和諧的感情關係。"""
        
        return content
    
    def generate_health_summary(self, bazi_info: Dict, wuxing_analysis: Dict) -> str:
        """生成健康總論"""
        day_master_wuxing = bazi_info['day_master_wuxing']
        weak_elements = [k for k, v in wuxing_analysis['wuxing_count'].items() if v == 0]
        
        content = f"""● 健康基本分析

從您的八字五行配置來看，{self._get_health_constitution_description(day_master_wuxing, wuxing_analysis)}。整體而言，您的體質{self._get_constitution_type(wuxing_analysis)}。

● 易患疾病

根據五行理論，您需要特別注意{self._get_health_concerns(day_master_wuxing, weak_elements)}方面的健康問題。平時應該{self._get_health_prevention_advice(day_master_wuxing)}。

● 養生建議

在日常養生方面，建議您{self._get_wellness_advice(day_master_wuxing, wuxing_analysis['favorable_elements'])}。飲食上宜{self._get_dietary_advice(wuxing_analysis['favorable_elements'])}，避免{self._get_dietary_restrictions(day_master_wuxing)}。

● 運動保健

適合您的運動方式包括{self._get_exercise_recommendations(day_master_wuxing)}。定期進行這些運動有助於調和五行，增強體質，預防疾病。"""
        
        return content
    
    def generate_family_summary(self, bazi_info: Dict) -> str:
        """生成六親總論"""
        content = f"""● 父母關係

從您的八字來看，與父母的關係{self._get_parent_relationship_description(bazi_info)}。在家庭中，您{self._get_family_role_description(bazi_info)}。

● 兄弟姊妹

兄弟姊妹方面，{self._get_sibling_relationship_description(bazi_info)}。與兄弟姊妹的相處{self._get_sibling_interaction_description(bazi_info)}。

● 子女運勢

子女方面，{self._get_children_fortune_description(bazi_info)}。在教育子女時，建議您{self._get_parenting_advice(bazi_info)}。

● 人際貴人

在人際關係中，您的貴人多為{self._get_benefactor_description(bazi_info)}。與這些人保持良好關係，對您的人生發展會有很大幫助。"""
        
        return content
    
    def generate_dayun_summary(self, dayun_list: List[Dict], current_age: int = 30) -> str:
        """生成五十年大運總論"""
        content = "● 大運總體分析\n\n"
        
        for i, dayun in enumerate(dayun_list[:5]):  # 顯示前5步大運，共50年
            pillar = dayun['pillar']
            start_age = dayun['start_age']
            end_age = dayun['end_age']
            wuxing = dayun['wuxing']
            
            content += f"第{i+1}步大運：{pillar}（{start_age}-{end_age}歲）\n"
            content += f"這個大運期間，{wuxing}氣當旺，{self._get_dayun_description(dayun, i)}。"
            content += f"{self._get_dayun_advice(dayun, i)}\n\n"
        
        return content
    
    def generate_liunian_prediction(self, birth_year: int, current_year: int = 2024) -> str:
        """生成十年流年預測"""
        content = "● 十年流年預測\n\n"
        
        for year in range(current_year, current_year + 10):
            year_gan_zhi = self._get_year_ganzhi(year)
            age = year - birth_year + 1
            
            content += f"{year}年（{age}歲）- {year_gan_zhi}年：\n"
            content += f"{self._get_liunian_prediction(year_gan_zhi, age)}\n\n"
        
        return content
    
    def generate_feng_shui_guide(self, wuxing_analysis: Dict) -> str:
        """生成簡易催運指南"""
        favorable_elements = wuxing_analysis['favorable_elements']
        
        content = f"""● 顏色運用

根據您的喜用神，建議多使用{self._get_favorable_colors(favorable_elements)}等顏色，有助於提升運勢。避免過多使用{self._get_unfavorable_colors(wuxing_analysis)}。

● 方位選擇

在居住和工作環境的選擇上，{self._get_favorable_directions(favorable_elements)}方位對您比較有利。座位或床位朝向這些方位，有助於事業和健康運勢。

● 數字運用

幸運數字：{self._get_lucky_numbers(favorable_elements)}
在選擇電話號碼、車牌號碼等時，可以多考慮這些數字。

● 飾品佩戴

建議佩戴{self._get_favorable_accessories(favorable_elements)}材質的飾品，有助於補強五行，提升個人氣場。

● 植物擺放

在家中或辦公室擺放{self._get_favorable_plants(favorable_elements)}，既能美化環境，又能調和五行能量。

● 日常注意事項

{self._get_daily_precautions(wuxing_analysis)}"""
        
        return content
    
    # 輔助方法
    def _get_strength_description(self, wuxing_analysis: Dict) -> str:
        """獲取五行強弱描述"""
        max_count = max(wuxing_analysis['wuxing_count'].values())
        if max_count >= 4:
            return "偏強"
        elif max_count <= 2:
            return "偏弱"
        else:
            return "中和"
    
    def _get_life_pattern_description(self, wuxing_analysis: Dict) -> str:
        """獲取人生模式描述"""
        strength = self._get_strength_description(wuxing_analysis)
        if strength == "偏強":
            return "需要適當的挑戰和壓力來激發潛能"
        elif strength == "偏弱":
            return "需要更多的支持和幫助來實現目標"
        else:
            return "能夠在穩定中求發展，平衡發展各方面能力"
    
    def _get_relationship_description(self, wuxing: str) -> str:
        """獲取人際關係描述"""
        descriptions = {
            '木': "善於與人建立深度關係，重視友情，但有時過於理想化",
            '火': "熱情開朗，容易與人打成一片，但需要注意情緒管理",
            '土': "忠誠可靠，是很好的朋友和夥伴，但有時過於保守",
            '金': "原則性強，重視品質勝過數量，朋友不多但很深交",
            '水': "靈活變通，善於處理各種人際關係，但需要保持真誠"
        }
        return descriptions.get(wuxing, "具有獨特的人際魅力")
    
    def _get_work_style_description(self, wuxing: str) -> str:
        """獲取工作風格描述"""
        descriptions = {
            '木': "積極進取，富有創新精神",
            '火': "熱情主動，善於表達和溝通",
            '土': "穩重踏實，注重細節和品質",
            '金': "嚴謹認真，執行力強",
            '水': "靈活變通，適應能力強"
        }
        return descriptions.get(wuxing, "具有獨特的工作風格")
    
    def _get_career_advice(self, wuxing: str) -> str:
        """獲取事業建議"""
        advice = {
            '木': "保持創新思維，勇於嘗試新的發展方向",
            '火': "發揮溝通優勢，建立良好的人脈關係",
            '土': "注重基礎建設，穩步推進事業發展",
            '金': "堅持原則，追求專業化發展",
            '水': "善用變通能力，抓住市場機遇"
        }
        return advice.get(wuxing, "發揮個人優勢，持續學習成長")
    
    def _get_entrepreneurship_advice(self, wuxing_analysis: Dict) -> str:
        """獲取創業建議"""
        strength = self._get_strength_description(wuxing_analysis)
        if strength == "偏強":
            return "具有創業的勇氣和決心，適合自主創業"
        elif strength == "偏弱":
            return "建議先積累經驗和資源，或選擇合夥創業"
        else:
            return "創業和就業都有不錯的發展前景，可根據實際情況選擇"
    
    def _analyze_wealth_star(self, bazi_info: Dict) -> str:
        """分析財星類型"""
        # 簡化的財星分析
        day_master = bazi_info['day_master']
        tiangan = bazi_info['tiangan']
        
        # 這裡使用簡化的邏輯，實際應該更複雜
        if '甲' in tiangan or '乙' in tiangan:
            return '正財'
        elif '丙' in tiangan or '丁' in tiangan:
            return '偏財'
        else:
            return '比肩'
    
    def _get_wealth_star_description(self, wealth_type: str) -> str:
        """獲取財星描述"""
        descriptions = {
            '正財': "透出有力",
            '偏財': "暗藏不露",
            '劫財': "過於旺盛",
            '比肩': "平衡適中"
        }
        return descriptions.get(wealth_type, "配置合理")
    
    def _get_wealth_pattern_description(self, wealth_type: str) -> str:
        """獲取財運模式描述"""
        patterns = {
            '正財': "穩健踏實，適合長期投資",
            '偏財': "機會較多，但需要把握時機",
            '劫財': "起伏較大，需要謹慎理財",
            '比肩': "平穩發展，收支平衡"
        }
        return patterns.get(wealth_type, "有一定的財運基礎")
    
    def _get_wealth_method_description(self, wealth_type: str) -> str:
        """獲取求財方式描述"""
        methods = {
            '正財': "勤勞工作，穩定收入",
            '偏財': "投資理財，多元發展",
            '劫財': "合作經營，風險分擔",
            '比肩': "團隊合作，共同發展"
        }
        return methods.get(wealth_type, "發揮個人優勢")
    
    def _get_investment_advice(self, wealth_type: str) -> str:
        """獲取投資建議"""
        advice = {
            '正財': "選擇穩健的投資產品，如定期存款、債券等",
            '偏財': "可以適當進行股票、基金等投資，但要控制風險",
            '劫財': "避免高風險投資，不宜借貸投資",
            '比肩': "可以考慮合夥投資，分散風險"
        }
        return advice.get(wealth_type, "根據個人風險承受能力選擇")
    
    def _get_financial_advice(self, wealth_type: str) -> str:
        """獲取理財建議"""
        advice = {
            '正財': "制定預算計劃，養成儲蓄習慣",
            '偏財': "多元化投資，不要把雞蛋放在一個籃子裡",
            '劫財': "謹慎消費，避免衝動購買",
            '比肩': "平衡收支，適度消費"
        }
        return advice.get(wealth_type, "合理規劃財務")
    
    def _get_unfavorable_period(self) -> str:
        """獲取不利時期"""
        return "五行相沖的年份"
    
    def _analyze_spouse_star(self, bazi_info: Dict, gender: str) -> str:
        """分析配偶星"""
        # 簡化的配偶星分析
        if gender == '男':
            return '正官'
        else:
            return '正印'
    
    def _get_spouse_star_description(self, spouse_star: str) -> str:
        """獲取配偶星描述"""
        descriptions = {
            '正官': "清透有力",
            '七殺': "混雜不清",
            '正印': "溫和有情",
            '偏印': "複雜多變"
        }
        return descriptions.get(spouse_star, "配置適中")
    
    def _get_marriage_pattern_description(self, spouse_star: str) -> str:
        """獲取婚姻模式描述"""
        return self.marriage_templates.get(spouse_star, ['婚姻運勢平穩'])[0]
    
    def _get_spouse_characteristics(self, spouse_star: str) -> str:
        """獲取配偶特徵"""
        characteristics = {
            '正官': "品格端正，有責任感",
            '七殺': "性格強勢，有魄力",
            '正印': "溫和賢慧，有愛心",
            '偏印': "聰明機智，有個性"
        }
        return characteristics.get(spouse_star, "性格溫和")
    
    def _get_spouse_selection_advice(self, spouse_star: str) -> str:
        """獲取擇偶建議"""
        advice = {
            '正官': "選擇品格端正、有責任感的對象",
            '七殺': "選擇能夠相互理解、包容的對象",
            '正印': "選擇溫和體貼、有愛心的對象",
            '偏印': "選擇聰明有趣、有共同話題的對象"
        }
        return advice.get(spouse_star, "選擇合適的對象")
    
    def _get_marriage_timing(self, bazi_info: Dict) -> str:
        """獲取結婚時機"""
        # 簡化的結婚時機分析
        return "25-30"
    
    def _get_relationship_advice(self, spouse_star: str) -> str:
        """獲取感情建議"""
        advice = {
            '正官': "保持誠信，承擔責任",
            '七殺': "學會溝通，相互理解",
            '正印': "給予關愛，細心呵護",
            '偏印': "保持新鮮感，增進了解"
        }
        return advice.get(spouse_star, "真誠相待")
    
    def _get_marriage_precautions(self, spouse_star: str) -> str:
        """獲取婚姻注意事項"""
        precautions = {
            '正官': "避免過於嚴肅，增加生活情趣",
            '七殺': "避免爭強好勝，學會妥協",
            '正印': "避免過度依賴，保持獨立",
            '偏印': "避免三心二意，專一感情"
        }
        return precautions.get(spouse_star, "相互尊重")
    
    def _get_health_constitution_description(self, wuxing: str, wuxing_analysis: Dict) -> str:
        """獲取健康體質描述"""
        return f"您的體質偏向{wuxing}性，五行配置{self._get_strength_description(wuxing_analysis)}"
    
    def _get_constitution_type(self, wuxing_analysis: Dict) -> str:
        """獲取體質類型"""
        strength = self._get_strength_description(wuxing_analysis)
        if strength == "偏強":
            return "較為強健，但需要適當調節"
        elif strength == "偏弱":
            return "相對較弱，需要加強調養"
        else:
            return "比較平衡，整體健康狀況良好"
    
    def _get_health_concerns(self, wuxing: str, weak_elements: List[str]) -> str:
        """獲取健康關注點"""
        concerns = {
            '木': "肝膽、神經系統",
            '火': "心臟、血液循環",
            '土': "脾胃、消化系統",
            '金': "肺部、呼吸系統",
            '水': "腎臟、泌尿系統"
        }
        main_concern = concerns.get(wuxing, "整體健康")
        
        if weak_elements:
            weak_concerns = [concerns.get(elem, "") for elem in weak_elements if elem in concerns]
            if weak_concerns:
                return f"{main_concern}以及{', '.join(weak_concerns)}"
        
        return main_concern
    
    def _get_health_prevention_advice(self, wuxing: str) -> str:
        """獲取健康預防建議"""
        advice = {
            '木': "保持心情愉快，避免過度勞累",
            '火': "注意心血管健康，避免過度興奮",
            '土': "注意飲食規律，避免暴飲暴食",
            '金': "注意呼吸道保健，避免吸煙",
            '水': "注意腎臟保養，避免過度勞累"
        }
        return advice.get(wuxing, "保持良好的生活習慣")
    
    def _get_wellness_advice(self, wuxing: str, favorable_elements: List[str]) -> str:
        """獲取養生建議"""
        return f"多接觸{favorable_elements[0]}、{favorable_elements[1]}相關的環境和活動"
    
    def _get_dietary_advice(self, favorable_elements: List[str]) -> str:
        """獲取飲食建議"""
        dietary_map = {
            '木': "綠色蔬菜、酸味食物",
            '火': "紅色食物、苦味食物",
            '土': "黃色食物、甘味食物",
            '金': "白色食物、辛味食物",
            '水': "黑色食物、鹹味食物"
        }
        
        recommendations = []
        for element in favorable_elements:
            if element in dietary_map:
                recommendations.append(dietary_map[element])
        
        return "多食用" + "、".join(recommendations) if recommendations else "均衡飲食"
    
    def _get_dietary_restrictions(self, wuxing: str) -> str:
        """獲取飲食禁忌"""
        restrictions = {
            '木': "過於辛辣的食物",
            '火': "過於寒涼的食物",
            '土': "過於油膩的食物",
            '金': "過於酸澀的食物",
            '水': "過於甘甜的食物"
        }
        return restrictions.get(wuxing, "刺激性食物")
    
    def _get_exercise_recommendations(self, wuxing: str) -> str:
        """獲取運動建議"""
        exercises = {
            '木': "慢跑、瑜伽、太極拳",
            '火': "游泳、騎車、球類運動",
            '土': "散步、爬山、健身操",
            '金': "武術、舉重、器械運動",
            '水': "游泳、水上運動、冥想"
        }
        return exercises.get(wuxing, "適度的有氧運動")
    
    def _get_parent_relationship_description(self, bazi_info: Dict) -> str:
        """獲取父母關係描述"""
        return "總體和諧，但需要多溝通理解"
    
    def _get_family_role_description(self, bazi_info: Dict) -> str:
        """獲取家庭角色描述"""
        return "扮演著重要的角色，有一定的影響力"
    
    def _get_sibling_relationship_description(self, bazi_info: Dict) -> str:
        """獲取兄弟姊妹關係描述"""
        return "關係較為融洽"
    
    def _get_sibling_interaction_description(self, bazi_info: Dict) -> str:
        """獲取兄弟姊妹互動描述"""
        return "能夠相互支持，偶有小摩擦"
    
    def _get_children_fortune_description(self, bazi_info: Dict) -> str:
        """獲取子女運勢描述"""
        return "子女運勢不錯，能夠帶來快樂"
    
    def _get_parenting_advice(self, bazi_info: Dict) -> str:
        """獲取育兒建議"""
        return "注重品德教育，培養獨立能力"
    
    def _get_benefactor_description(self, bazi_info: Dict) -> str:
        """獲取貴人描述"""
        return "年長的長輩或有經驗的前輩"
    
    def _get_dayun_description(self, dayun: Dict, index: int) -> str:
        """獲取大運描述"""
        wuxing = dayun['wuxing']
        descriptions = {
            '木': "事業發展順利，創新能力強",
            '火': "名聲地位提升，人際關係活躍",
            '土': "財運穩定，基礎建設完善",
            '金': "決斷力強，執行效率高",
            '水': "學習能力強，適應變化快"
        }
        return descriptions.get(wuxing, "運勢平穩發展")
    
    def _get_dayun_advice(self, dayun: Dict, index: int) -> str:
        """獲取大運建議"""
        return "建議把握機遇，穩步發展。"
    
    def _get_year_ganzhi(self, year: int) -> str:
        """獲取年份干支"""
        # 簡化的干支計算
        gan_index = (year - 4) % 10
        zhi_index = (year - 4) % 12
        return self.TIANGAN[gan_index] + self.DIZHI[zhi_index]
    
    def _get_liunian_prediction(self, year_ganzhi: str, age: int) -> str:
        """獲取流年預測"""
        predictions = [
            "整體運勢平穩，適合穩健發展。",
            "事業運勢不錯，有新的機遇出現。",
            "財運有所提升，投資需謹慎。",
            "感情運勢波動，需要多溝通。",
            "健康狀況良好，注意休息。"
        ]
        return random.choice(predictions)
    
    def _get_favorable_colors(self, favorable_elements: List[str]) -> str:
        """獲取有利顏色"""
        color_map = {
            '木': "綠色、青色",
            '火': "紅色、橙色",
            '土': "黃色、棕色",
            '金': "白色、金色",
            '水': "黑色、藍色"
        }
        
        colors = []
        for element in favorable_elements:
            if element in color_map:
                colors.append(color_map[element])
        
        return "、".join(colors) if colors else "中性色調"
    
    def _get_unfavorable_colors(self, wuxing_analysis: Dict) -> str:
        """獲取不利顏色"""
        max_wuxing = wuxing_analysis['max_wuxing']
        color_map = {
            '木': "白色、金色",
            '火': "黑色、藍色",
            '土': "綠色、青色",
            '金': "紅色、橙色",
            '水': "黃色、棕色"
        }
        return color_map.get(max_wuxing, "過於鮮豔的顏色")
    
    def _get_favorable_directions(self, favorable_elements: List[str]) -> str:
        """獲取有利方位"""
        direction_map = {
            '木': "東方",
            '火': "南方",
            '土': "中央",
            '金': "西方",
            '水': "北方"
        }
        
        directions = []
        for element in favorable_elements:
            if element in direction_map:
                directions.append(direction_map[element])
        
        return "、".join(directions) if directions else "適中方位"
    
    def _get_lucky_numbers(self, favorable_elements: List[str]) -> str:
        """獲取幸運數字"""
        number_map = {
            '木': "3、8",
            '火': "2、7",
            '土': "5、0",
            '金': "4、9",
            '水': "1、6"
        }
        
        numbers = []
        for element in favorable_elements:
            if element in number_map:
                numbers.append(number_map[element])
        
        return "、".join(numbers) if numbers else "1、6"
    
    def _get_favorable_accessories(self, favorable_elements: List[str]) -> str:
        """獲取有利飾品"""
        accessory_map = {
            '木': "木質",
            '火': "紅寶石、瑪瑙",
            '土': "玉石、陶瓷",
            '金': "金屬、水晶",
            '水': "黑曜石、珍珠"
        }
        
        accessories = []
        for element in favorable_elements:
            if element in accessory_map:
                accessories.append(accessory_map[element])
        
        return "、".join(accessories) if accessories else "天然材質"
    
    def _get_favorable_plants(self, favorable_elements: List[str]) -> str:
        """獲取有利植物"""
        plant_map = {
            '木': "綠蘿、富貴竹",
            '火': "紅掌、鳳仙花",
            '土': "仙人掌、多肉植物",
            '金': "白蘭花、茉莉花",
            '水': "水仙、荷花"
        }
        
        plants = []
        for element in favorable_elements:
            if element in plant_map:
                plants.append(plant_map[element])
        
        return "、".join(plants) if plants else "綠色植物"
    
    def _get_daily_precautions(self, wuxing_analysis: Dict) -> str:
        """獲取日常注意事項"""
        return "保持積極樂觀的心態，注意五行平衡，定期檢視和調整生活方式。"

# 測試代碼
if __name__ == "__main__":
    from bazi_calculator import BaziCalculator
    import datetime
    
    # 創建實例
    calculator = BaziCalculator()
    generator = ContentGenerator()
    
    # 測試數據
    name = "李小明"
    birth_date = datetime.date(1985, 5, 29)
    birth_time = datetime.time(14, 5)
    gender = "男"
    
    # 計算八字
    bazi_info = calculator.calculate_bazi(birth_date, birth_time)
    wuxing_analysis = calculator.analyze_wuxing_balance(bazi_info)
    dayun = calculator.calculate_dayun(bazi_info, gender, birth_date)
    
    # 生成內容
    print("=== 命主資料 ===")
    print(generator.generate_personal_info(name, bazi_info, wuxing_analysis, birth_date, birth_time, gender))
    
    print("\n=== 人生總論 ===")
    print(generator.generate_life_summary(bazi_info, wuxing_analysis))

