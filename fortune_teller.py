#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
增強版八字算命程式
支持傳統風格和現代風格兩種PDF輸出格式
"""

import datetime
import os
import sys
from bazi_calculator import BaziCalculator
from content_generator import ContentGenerator
from pdf_generator import FortuneReportPDF
from pdf_generator import FortuneReportPDF

class EnhancedFortuneTeller:
    """增強版算命程式"""
    
    def __init__(self):
        """初始化程式"""
        self.calculator = BaziCalculator()
        self.generator = ContentGenerator()
        self.modern_pdf = FortuneReportPDF()
        self.traditional_pdf = FortuneReportPDF()
    
    def display_welcome(self):
        """顯示歡迎信息"""
        print("=" * 60)
        print("歡迎使用增強版八字算命程式")
        print("=" * 60)
        print("本程式支持兩種PDF輸出風格：")
        print("1. 現代風格 - 橫向排版，表格化展示")
        print("2. 傳統風格 - 豎立由右至左書寫，中國風底圖")
        print("=" * 60)
    
    def get_user_input(self):
        """獲取用戶輸入"""
        print("\n請輸入以下信息：")
        
        # 獲取姓名
        while True:
            name = input("請輸入姓名：").strip()
            if name:
                break
            print("姓名不能為空，請重新輸入。")
        
        # 獲取出生日期
        while True:
            try:
                date_str = input("請輸入出生日期（格式：YYYY-MM-DD，如：1985-05-29）：").strip()
                birth_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                
                # 檢查日期合理性
                if birth_date > datetime.date.today():
                    print("出生日期不能是未來日期，請重新輸入。")
                    continue
                if birth_date.year < 1900:
                    print("出生日期不能早於1900年，請重新輸入。")
                    continue
                
                break
            except ValueError:
                print("日期格式錯誤，請按照 YYYY-MM-DD 格式輸入。")
        
        # 獲取出生時間
        while True:
            try:
                time_str = input("請輸入出生時間（格式：HH:MM，如：14:05）：").strip()
                birth_time = datetime.datetime.strptime(time_str, "%H:%M").time()
                break
            except ValueError:
                print("時間格式錯誤，請按照 HH:MM 格式輸入。")
        
        # 獲取性別
        while True:
            gender = input("請輸入性別（男/女）：").strip()
            if gender in ['男', '女']:
                break
            print("請輸入'男'或'女'。")
        
        return name, birth_date, birth_time, gender
    
    def choose_style(self):
        """選擇輸出風格"""
        print("\n請選擇PDF輸出風格：")
        print("1. 現代風格 - 標準橫向排版，適合現代閱讀習慣")
        print("2. 傳統風格 - 豎立由右至左書寫，古典命書風格")
        
        while True:
            choice = input("請輸入選擇（1或2）：").strip()
            if choice == '1':
                return 'modern'
            elif choice == '2':
                return 'traditional'
            else:
                print("請輸入1或2。")
    
    def calculate_bazi(self, birth_date, birth_time, gender):
        """計算八字信息"""
        print("\n正在計算八字...")
        
        # 計算八字
        bazi_info = self.calculator.calculate_bazi(birth_date, birth_time)
        
        # 分析五行
        wuxing_analysis = self.calculator.analyze_wuxing_balance(bazi_info)
        
        # 計算大運
        dayun_list = self.calculator.calculate_dayun(bazi_info, gender, birth_date)
        
        return bazi_info, wuxing_analysis, dayun_list
    
    def display_basic_info(self, name, bazi_info, wuxing_analysis, birth_date, birth_time, gender):
        """顯示基本信息"""
        print("\n" + "=" * 50)
        print("命主基本信息")
        print("=" * 50)
        print(f"姓名：{name}")
        print(f"出生日期：{birth_date.year}年{birth_date.month}月{birth_date.day}日")
        print(f"出生時間：{birth_time.hour}時{birth_time.minute}分")
        print(f"性別：{gender}")
        print(f"生肖：{bazi_info['shengxiao']}")
        print(f"日主五行：{bazi_info['day_master_wuxing']}")
        print(f"喜用神五行：{', '.join(wuxing_analysis['favorable_elements'])}")
        
        print(f"\n八字排盤：")
        print(f"年柱：{bazi_info['year_pillar']}  月柱：{bazi_info['month_pillar']}  日柱：{bazi_info['day_pillar']}  時柱：{bazi_info['hour_pillar']}")
        print(f"天干：{' '.join(bazi_info['tiangan'])}")
        print(f"地支：{' '.join(bazi_info['dizhi'])}")
        
        # 五行統計
        if 'element_count' in wuxing_analysis:
            wuxing_count = wuxing_analysis['element_count']
            print(f"\n五行統計：")
            for element, count in wuxing_count.items():
                print(f"{element}：{count}個")
        else:
            print("\n五行統計：未能計算")
    
    def generate_content(self, bazi_info, wuxing_analysis, dayun_list, birth_date, gender):
        """生成算命內容"""
        print("\n正在生成算命內容...")
        
        all_contents = {
            'life_summary': self.generator.generate_life_summary(bazi_info, wuxing_analysis),
            'career_summary': self.generator.generate_career_summary(bazi_info, wuxing_analysis),
            'wealth_summary': self.generator.generate_wealth_summary(bazi_info, wuxing_analysis),
            'marriage_summary': self.generator.generate_marriage_summary(bazi_info, gender),
            'health_summary': self.generator.generate_health_summary(bazi_info, wuxing_analysis),
            'family_summary': self.generator.generate_family_summary(bazi_info),
            'dayun_summary': self.generator.generate_dayun_summary(dayun_list),
            'liunian_prediction': self.generator.generate_liunian_prediction(birth_date.year),
            'feng_shui_guide': self.generator.generate_feng_shui_guide(wuxing_analysis)
        }
        
        # 統計內容
        total_chars = sum(len(content) for content in all_contents.values())
        print(f"內容生成完成！總字數：{total_chars} 字符")
        
        return all_contents
    
    def generate_pdf(self, style, filename, name, bazi_info, wuxing_analysis, 
                    dayun_list, birth_date, birth_time, gender, all_contents):
        """生成PDF報告"""
        print(f"\n正在生成{style}風格PDF報告...")
        
        if style == 'modern':
            self.modern_pdf.generate_pdf(
                filename, name, bazi_info, wuxing_analysis, dayun_list,
                birth_date, birth_time, gender, all_contents
            )
        else:  # traditional
            self.traditional_pdf.generate_pdf(
                filename, name, bazi_info, wuxing_analysis, dayun_list,
                birth_date, birth_time, gender, all_contents
            )
        
        # 檢查文件
        if os.path.exists(filename):
            file_size = os.path.getsize(filename)
            print(f"✅ PDF報告生成成功！")
            print(f"文件名：{filename}")
            print(f"文件大小：{file_size:,} 字節")
            print(f"風格：{style}風格")
            return True
        else:
            print("❌ PDF報告生成失敗！")
            return False
    
    def preview_content(self, all_contents):
        """預覽部分內容"""
        print("\n" + "=" * 50)
        print("內容預覽（人生總論）")
        print("=" * 50)
        
        life_summary = all_contents.get('life_summary', '')
        if life_summary:
            preview = life_summary[:300] + "..." if len(life_summary) > 300 else life_summary
            print(preview)
        else:
            print("內容生成失敗")
        
        print("=" * 50)
    
    def run(self):
        """運行主程式"""
        try:
            # 顯示歡迎信息
            self.display_welcome()
            
            # 獲取用戶輸入
            name, birth_date, birth_time, gender = self.get_user_input()
            
            # 選擇輸出風格
            style = self.choose_style()
            style_name = "現代" if style == 'modern' else "傳統"
            
            # 計算八字
            bazi_info, wuxing_analysis, dayun_list = self.calculate_bazi(birth_date, birth_time, gender)
            
            # 顯示基本信息
            self.display_basic_info(name, bazi_info, wuxing_analysis, birth_date, birth_time, gender)
            
            # 確認是否生成PDF
            print(f"\n是否生成{style_name}風格的PDF算命報告？")
            confirm = input("請輸入 y/yes/是 確認，或 n/no/否 取消：").strip().lower()
            
            if confirm in ['y', 'yes', '是']:
                # 生成內容
                all_contents = self.generate_content(bazi_info, wuxing_analysis, dayun_list, birth_date, gender)
                
                # 預覽內容
                self.preview_content(all_contents)
                
                # 生成PDF文件名
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"{style_name}風格_{name}_算命報告_{timestamp}.pdf"
                
                # 生成PDF
                success = self.generate_pdf(
                    style, filename, name, bazi_info, wuxing_analysis,
                    dayun_list, birth_date, birth_time, gender, all_contents
                )
                
                if success:
                    print("\n" + "=" * 50)
                    print("算命報告生成完成！")
                    print("=" * 50)
                    print("報告包含以下章節：")
                    chapters = [
                        "1. 命主資料及八字大運",
                        "2. 人生總論", "3. 事業總論", "4. 財運總論", "5. 姻緣總論",
                        "6. 健康總論", "7. 六親總論", "8. 五十年大運總論",
                        "9. 十年流年預測", "10. 簡易催運指南"
                    ]
                    for chapter in chapters:
                        print(f"  {chapter}")
                    
                    print(f"\nPDF文件已保存為：{filename}")
                    print(f"風格特色：{style_name}風格")
                    if style == 'traditional':
                        print("  • 豎立由右至左書寫")
                        print("  • 中國風水墨背景")
                        print("  • 傳統邊框裝飾")
                    else:
                        print("  • 橫向標準排版")
                        print("  • 表格化信息展示")
                        print("  • 現代簡潔風格")
                    
                    print("\n謝謝使用增強版八字算命程式！")
                else:
                    print("\n報告生成失敗，請檢查相關問題。")
            else:
                print("\n已取消PDF生成。謝謝使用！")
                
        except KeyboardInterrupt:
            print("\n\n程式已被用戶中斷。")
        except Exception as e:
            print(f"\n程式運行出錯：{e}")
            import traceback
            traceback.print_exc()

def main():
    """主函數"""
    app = EnhancedFortuneTeller()
    app.run()

if __name__ == "__main__":
    main()

