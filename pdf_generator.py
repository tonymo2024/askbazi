#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修復版傳統風格PDF生成模組
解決文字走位和重疊問題，優化排版布局
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.platypus.frames import Frame
from reportlab.platypus.doctemplate import PageTemplate, BaseDocTemplate
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.utils import ImageReader
import os
from typing import Dict, List
from PIL import Image, ImageDraw, ImageFont
import textwrap

class FortuneReportPDF:
    """修復版傳統風格算命報告PDF生成器"""
    
    def __init__(self):
        """初始化PDF生成器"""
        self.setup_fonts()
        self.setup_styles()
        self.page_width, self.page_height = A4
        
        # 重新設計邊距和安全區域
        self.outer_margin = 1.5*cm  # 外邊距
        self.inner_margin = 2.5*cm  # 內邊距（文字安全區域）
        self.column_width = 1.8*cm  # 每列寬度
        self.line_height = 0.7*cm   # 行高
        self.char_spacing = 2       # 字符間距
        
        # 計算文字安全區域
        self.text_left_boundary = self.inner_margin
        self.text_right_boundary = self.page_width - self.inner_margin
        self.text_top_boundary = self.page_height - self.inner_margin
        self.text_bottom_boundary = self.inner_margin
        
        # 計算可用文字區域
        self.text_area_width = self.text_right_boundary - self.text_left_boundary
        self.text_area_height = self.text_top_boundary - self.text_bottom_boundary
        
    def setup_fonts(self):
        """設置中文字體"""
        try:
            pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
            self.chinese_font = 'STSong-Light'
            print("成功加載內建中文字體：STSong-Light")
        except:
            try:
                pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))
                self.chinese_font = 'HeiseiMin-W3'
                print("成功加載內建中文字體：HeiseiMin-W3")
            except:
                self.chinese_font = 'Helvetica'
                print("使用Helvetica字體作為後備")
    
    def setup_styles(self):
        """設置文本樣式"""
        self.styles = getSampleStyleSheet()
        
        # 標題樣式
        self.title_style = ParagraphStyle(
            'TraditionalTitle',
            fontName=self.chinese_font,
            fontSize=18,
            textColor=colors.black,
            alignment=1,
            spaceAfter=20
        )
        
        # 章節標題樣式
        self.chapter_style = ParagraphStyle(
            'TraditionalChapter',
            fontName=self.chinese_font,
            fontSize=14,
            textColor=colors.black,
            alignment=1,
            spaceAfter=15
        )
        
        # 正文樣式
        self.body_style = ParagraphStyle(
            'TraditionalBody',
            fontName=self.chinese_font,
            fontSize=11,
            textColor=colors.black,
            alignment=0,
            leading=16
        )
    
    def safe_text(self, text: str) -> str:
        """安全處理文本"""
        if not text:
            return ""
        return text
    
    def draw_background_with_safe_zones(self, canvas, background_image_path: str = None):
        """繪製背景圖並標記安全區域"""
        # 設置基礎背景色
        canvas.setFillColor(colors.Color(0.98, 0.96, 0.94, alpha=1))
        canvas.rect(0, 0, self.page_width, self.page_height, fill=1, stroke=0)
        
        if background_image_path and os.path.exists(background_image_path):
            try:
                # 繪製背景圖片，調整透明度
                canvas.saveState()
                canvas.setFillAlpha(0.15)  # 降低透明度，避免干擾文字
                canvas.drawImage(
                    background_image_path, 
                    0, 0, 
                    width=self.page_width, 
                    height=self.page_height,
                    preserveAspectRatio=True,
                    mask='auto'
                )
                canvas.restoreState()
            except Exception as e:
                print(f"背景圖片加載失敗：{e}")
        
        # 繪製邊框（確保不與文字重疊）
        self.draw_safe_border(canvas)
    
    def draw_safe_border(self, canvas):
        """繪製安全邊框，確保不與文字重疊"""
        # 外邊框
        canvas.setStrokeColor(colors.Color(0.4, 0.3, 0.2, alpha=0.6))
        canvas.setLineWidth(2)
        canvas.rect(self.outer_margin, self.outer_margin, 
                   self.page_width - 2*self.outer_margin, 
                   self.page_height - 2*self.outer_margin, 
                   fill=0, stroke=1)
        
        # 內邊框（文字安全區域邊界）
        canvas.setStrokeColor(colors.Color(0.6, 0.5, 0.4, alpha=0.3))
        canvas.setLineWidth(1)
        canvas.rect(self.inner_margin, self.inner_margin, 
                   self.page_width - 2*self.inner_margin, 
                   self.page_height - 2*self.inner_margin, 
                   fill=0, stroke=1)
        
        # 繪製角落裝飾（在安全區域外）
        self.draw_corner_decorations_safe(canvas)
    
    def draw_corner_decorations_safe(self, canvas):
        """繪製角落裝飾，確保在安全區域外"""
        canvas.setStrokeColor(colors.Color(0.6, 0.5, 0.4, alpha=0.4))
        canvas.setLineWidth(1)
        
        decoration_size = 15
        
        # 左上角
        x1, y1 = self.outer_margin + 5, self.page_height - self.outer_margin - 5
        canvas.line(x1, y1 - decoration_size, x1 + decoration_size, y1 - decoration_size)
        canvas.line(x1 + decoration_size, y1, x1 + decoration_size, y1 - decoration_size)
        
        # 右上角
        x2, y2 = self.page_width - self.outer_margin - 5, self.page_height - self.outer_margin - 5
        canvas.line(x2, y2 - decoration_size, x2 - decoration_size, y2 - decoration_size)
        canvas.line(x2 - decoration_size, y2, x2 - decoration_size, y2 - decoration_size)
        
        # 左下角
        x3, y3 = self.outer_margin + 5, self.outer_margin + 5
        canvas.line(x3, y3 + decoration_size, x3 + decoration_size, y3 + decoration_size)
        canvas.line(x3 + decoration_size, y3, x3 + decoration_size, y3 + decoration_size)
        
        # 右下角
        x4, y4 = self.page_width - self.outer_margin - 5, self.outer_margin + 5
        canvas.line(x4, y4 + decoration_size, x4 - decoration_size, y4 + decoration_size)
        canvas.line(x4 - decoration_size, y4, x4 - decoration_size, y4 + decoration_size)
    
    def split_text_into_safe_columns(self, text: str, max_chars_per_column: int = 18) -> List[List[str]]:
        """將文本安全分割成豎列格式，避免重疊"""
        if not text:
            return []
        
        # 清理文本
        text = text.strip().replace('\n\n', '\n').replace('\n', '')
        
        # 按標點符號分句
        sentences = []
        current_sentence = ""
        
        for char in text:
            current_sentence += char
            if char in '。！？；：':
                sentences.append(current_sentence.strip())
                current_sentence = ""
        
        if current_sentence.strip():
            sentences.append(current_sentence.strip())
        
        # 將句子分配到列中，確保不超出安全區域
        columns = []
        current_column = []
        current_column_chars = 0
        
        for sentence in sentences:
            # 檢查是否需要新列
            if current_column_chars + len(sentence) > max_chars_per_column and current_column:
                columns.append(current_column)
                current_column = [sentence]
                current_column_chars = len(sentence)
            else:
                current_column.append(sentence)
                current_column_chars += len(sentence)
        
        if current_column:
            columns.append(current_column)
        
        return columns
    
    def draw_vertical_text_safe(self, canvas, text: str, start_x: float, start_y: float, 
                               max_chars_per_column: int = 18, font_size: int = 11):
        """安全繪製豎直文本，確保不與邊框重疊"""
        if not text:
            return start_x
        
        canvas.setFont(self.chinese_font, font_size)
        canvas.setFillColor(colors.black)
        
        columns = self.split_text_into_safe_columns(text, max_chars_per_column)
        
        # 確保起始位置在安全區域內
        current_x = min(start_x, self.text_right_boundary - self.column_width)
        
        for column in reversed(columns):  # 從右到左排列
            # 檢查是否還有空間
            if current_x < self.text_left_boundary + self.column_width:
                break
            
            current_y = min(start_y, self.text_top_boundary - font_size)
            
            for sentence in column:
                for char in sentence:
                    if char.strip():  # 跳過空白字符
                        # 確保字符位置在安全區域內
                        if current_y > self.text_bottom_boundary + font_size:
                            canvas.drawString(current_x, current_y, self.safe_text(char))
                            current_y -= font_size + self.char_spacing
                        else:
                            # 如果超出底部邊界，停止繪製
                            break
                
                # 句子間距
                current_y -= 8
                if current_y <= self.text_bottom_boundary + font_size:
                    break
            
            # 移動到下一列
            current_x -= self.column_width
        
        return current_x
    
    def create_safe_cover_page(self, canvas, name: str, bazi_info: Dict, 
                              birth_date, birth_time, gender: str):
        """創建安全的封面頁，避免文字重疊"""
        canvas.saveState()
        
        # 繪製背景
        self.draw_background_with_safe_zones(canvas, "/home/ubuntu/chinese_background_2.png")
        
        # 主標題（右側豎直，在安全區域內）
        title_x = self.text_right_boundary - 0.8*cm
        title_y = self.text_top_boundary - 1*cm
        
        canvas.setFont(self.chinese_font, 20)
        canvas.setFillColor(colors.black)
        
        main_title = "八字命書詳批"
        current_y = title_y
        for char in main_title:
            if current_y > self.text_bottom_boundary + 20:
                canvas.drawString(title_x, current_y, self.safe_text(char))
                current_y -= 25
        
        # 命主信息框（右側，在安全區域內）
        info_x = self.text_right_boundary - 3*cm
        info_y = self.text_top_boundary - 4*cm
        
        # 繪製信息框（確保不與邊框重疊）
        canvas.setStrokeColor(colors.Color(0.5, 0.4, 0.3, alpha=0.6))
        canvas.setLineWidth(1)
        box_width = 2.5*cm
        box_height = 6*cm
        canvas.rect(info_x - box_width/2, info_y - box_height, box_width, box_height, fill=0, stroke=1)
        
        # 命主信息
        canvas.setFont(self.chinese_font, 14)
        info_title_x = info_x - 0.3*cm
        info_title_y = info_y - 0.5*cm
        
        info_title = "命主"
        current_y = info_title_y
        for char in info_title:
            canvas.drawString(info_title_x, current_y, self.safe_text(char))
            current_y -= 18
        
        # 姓名
        canvas.setFont(self.chinese_font, 16)
        name_x = info_x + 0.3*cm
        name_y = info_y - 0.5*cm
        
        current_y = name_y
        for char in name:
            if current_y > info_y - box_height + 20:
                canvas.drawString(name_x, current_y, self.safe_text(char))
                current_y -= 20
        
        # 其他信息（橫向排列，避免豎直空間不足）
        canvas.setFont(self.chinese_font, 8)
        detail_x = info_x - box_width/2 + 5
        detail_y = info_y - 3*cm
        
        details = [
            f"出生：{birth_date.year}年{birth_date.month}月{birth_date.day}日",
            f"時間：{birth_time.hour}時{birth_time.minute}分",
            f"性別：{gender}",
            f"生肖：{bazi_info['shengxiao']}",
            f"日主：{bazi_info['day_master']}"
        ]
        
        for i, detail in enumerate(details):
            y_pos = detail_y - i * 12
            if y_pos > info_y - box_height + 10:
                canvas.drawString(detail_x, y_pos, self.safe_text(detail))
        
        # 八字排盤（中央，在安全區域內）
        bazi_x = self.page_width // 2
        bazi_y = self.text_top_boundary - 6*cm
        
        canvas.setFont(self.chinese_font, 14)
        bazi_title = "八字大運"
        current_y = bazi_y + 1*cm
        for char in bazi_title:
            canvas.drawString(bazi_x, current_y, self.safe_text(char))
            current_y -= 18
        
        # 八字四柱（確保間距合適）
        canvas.setFont(self.chinese_font, 12)
        pillars = [bazi_info['year_pillar'], bazi_info['month_pillar'], 
                  bazi_info['day_pillar'], bazi_info['hour_pillar']]
        
        for i, pillar in enumerate(pillars):
            pillar_x = bazi_x + 1*cm - i * 0.8*cm
            current_y = bazi_y
            for char in pillar:
                canvas.drawString(pillar_x, current_y, self.safe_text(char))
                current_y -= 16
        
        # 目錄（左側，在安全區域內）
        toc_x = self.text_left_boundary + 1*cm
        toc_y = self.text_top_boundary - 3*cm
        
        canvas.setFont(self.chinese_font, 12)
        toc_title = "目錄"
        current_y = toc_y
        for char in toc_title:
            canvas.drawString(toc_x, current_y, self.safe_text(char))
            current_y -= 16
        
        # 目錄項目（橫向排列，節省空間）
        canvas.setFont(self.chinese_font, 8)
        toc_items = [
            "命主資料及八字大運", "人生總論", "事業總論", "財運總論", "姻緣總論",
            "健康總論", "六親總論", "五十年大運總論", "十年流年預測", "簡易催運指南"
        ]
        
        for i, item in enumerate(toc_items):
            y_pos = toc_y - 1*cm - i * 12
            if y_pos > self.text_bottom_boundary + 10:
                canvas.drawString(toc_x - 0.5*cm, y_pos, self.safe_text(item))
        
        canvas.restoreState()
    
    def create_safe_content_page(self, canvas, chapter_title: str, content: str, page_num: int):
        """創建安全的內容頁，避免文字重疊"""
        canvas.saveState()
        
        # 繪製背景
        self.draw_background_with_safe_zones(canvas, "/home/ubuntu/chinese_background_1.png")
        
        # 頁面標題（右上角豎直，在安全區域內）
        title_x = self.text_right_boundary - 0.6*cm
        title_y = self.text_top_boundary - 0.5*cm
        
        canvas.setFont(self.chinese_font, 14)
        canvas.setFillColor(colors.black)
        
        current_y = title_y
        for char in chapter_title:
            if current_y > self.text_bottom_boundary + 14:
                canvas.drawString(title_x, current_y, self.safe_text(char))
                current_y -= 18
        
        # 內容區域（豎直排版，從右到左，在安全區域內）
        content_start_x = self.text_right_boundary - 1.5*cm
        content_start_y = self.text_top_boundary - 3*cm
        
        # 繪製豎直文本，確保在安全區域內
        self.draw_vertical_text_safe(
            canvas, content, 
            content_start_x, content_start_y, 
            max_chars_per_column=20, font_size=10
        )
        
        # 頁碼（右下角豎直，在安全區域內）
        page_x = self.text_right_boundary - 0.6*cm
        page_y = self.text_bottom_boundary + 1*cm
        
        canvas.setFont(self.chinese_font, 9)
        page_text = f"第{page_num}頁"
        current_y = page_y
        for char in page_text:
            canvas.drawString(page_x, current_y, self.safe_text(char))
            current_y += 12
        
        canvas.restoreState()
    
    def generate_pdf(self, filename: str, name: str, bazi_info: Dict, 
                    wuxing_analysis: Dict, dayun_list: List[Dict],
                    birth_date, birth_time, gender: str, all_contents: Dict):
        """生成修復版傳統風格PDF報告"""
        
        # 創建PDF文檔
        from reportlab.pdfgen.canvas import Canvas
        
        c = Canvas(filename, pagesize=A4)
        
        # 封面頁
        self.create_safe_cover_page(c, name, bazi_info, birth_date, birth_time, gender)
        c.showPage()
        
        # 內容頁
        chapters = [
            ("人生總論", all_contents.get('life_summary', '')),
            ("事業總論", all_contents.get('career_summary', '')),
            ("財運總論", all_contents.get('wealth_summary', '')),
            ("姻緣總論", all_contents.get('marriage_summary', '')),
            ("健康總論", all_contents.get('health_summary', '')),
            ("六親總論", all_contents.get('family_summary', '')),
            ("五十年大運總論", all_contents.get('dayun_summary', '')),
            ("十年流年預測", all_contents.get('liunian_prediction', '')),
            ("簡易催運指南", all_contents.get('feng_shui_guide', ''))
        ]
        
        page_num = 2
        for chapter_title, content in chapters:
            if content:
                self.create_safe_content_page(c, chapter_title, content, page_num)
                c.showPage()
                page_num += 1
        
        c.save()
        print(f"修復版傳統風格PDF報告已生成：{filename}")

# 測試代碼
if __name__ == "__main__":
    from bazi_calculator import BaziCalculator
    from content_generator import ContentGenerator
    import datetime
    
    # 創建實例
    calculator = BaziCalculator()
    generator = ContentGenerator()
    pdf_gen = FortuneReportPDF()
    
    # 測試數據
    name = "測試修復"
    birth_date = datetime.date(1985, 5, 29)
    birth_time = datetime.time(14, 5)
    gender = "男"
    
    # 計算八字
    bazi_info = calculator.calculate_bazi(birth_date, birth_time)
    wuxing_analysis = calculator.analyze_wuxing_balance(bazi_info)
    dayun = calculator.calculate_dayun(bazi_info, gender, birth_date)
    
    # 生成所有內容
    all_contents = {
        'life_summary': generator.generate_life_summary(bazi_info, wuxing_analysis),
        'career_summary': generator.generate_career_summary(bazi_info, wuxing_analysis),
        'wealth_summary': generator.generate_wealth_summary(bazi_info, wuxing_analysis),
        'marriage_summary': generator.generate_marriage_summary(bazi_info, gender),
        'health_summary': generator.generate_health_summary(bazi_info, wuxing_analysis),
        'family_summary': generator.generate_family_summary(bazi_info),
        'dayun_summary': generator.generate_dayun_summary(dayun),
        'liunian_prediction': generator.generate_liunian_prediction(birth_date.year),
        'feng_shui_guide': generator.generate_feng_shui_guide(wuxing_analysis)
    }
    
    # 生成PDF
    pdf_gen.generate_pdf(
        "修復版_傳統風格_算命報告.pdf",
        name, bazi_info, wuxing_analysis, dayun,
        birth_date, birth_time, gender, all_contents
    )

