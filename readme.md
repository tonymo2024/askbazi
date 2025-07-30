# BaZi (Chinese Astrology) Fortune Teller

A professional Chinese astrology system that generates comprehensive fortune readings based on the Four Pillars of Destiny (BaZi) principles.

## Quick Start

### Prerequisites
```bash
# Check Python version (requires 3.11+)
python3.11 --version

# Install dependencies
pip3 install reportlab lunar-python jieba
```

### Run Application
```bash
python3.11 fortune_teller.py
```

## Features

- Traditional Chinese BaZi calculation
- Dual-style PDF report generation:
  - Modern horizontal layout
  - Traditional vertical Chinese layout
- Comprehensive life analysis
- Personalized fortune reading
- Multi-aspect predictions

## Input Requirements

| Field | Format | Example |
|-------|---------|---------|
| Name | Chinese/English text | 张三 / John |
| Birth Date | YYYY-MM-DD | 1985-05-29 |
| Birth Time | HH:MM (24-hour) | 14:05 |
| Gender | M/F | M |

## Generated Report Sections

1. **Personal Information**
   - Basic data
   - BaZi chart
   - Element analysis

2. **Life Overview**
   - Character analysis
   - Life path prediction
   - Personal strengths

3. **Career Analysis**
   - Career potential
   - Suitable industries
   - Development advice

4. **Wealth Forecast**
   - Wealth patterns
   - Financial timing
   - Investment guidance

5. **Relationship Analysis**
   - Marriage outlook
   - Relationship timing
   - Partner characteristics

6. **Health Assessment**
   - Constitutional analysis
   - Health predictions
   - Wellness advice

7. **Family Relations**
   - Family dynamics
   - Interpersonal connections
   - Relationship guidance

8. **50-Year Fortune Cycles**
   - Major life periods
   - Opportunity timing
   - Challenge periods

9. **Annual Predictions**
   - Yearly forecasts
   - Monthly highlights
   - Key dates

10. **Fortune Enhancement Guide**
    - Favorable elements
    - Timing optimization
    - Practical advice

## Technical Details

### Core Components

- **BaZi Calculator**
  - Lunar calendar conversion
  - Four Pillars computation
  - Element analysis

- **Content Generator**
  - Template-based generation
  - Personalized content
  - Multi-aspect analysis

- **PDF Generator**
  - Professional layout
  - Dual-style support
  - Chinese font integration

### Error Handling

- Input validation
- Exception management
- User-friendly messages

## FAQ

**Q: How accurate are the calculations?**
A: Uses standard BaZi calculation methods with precise lunar calendar conversion.

**Q: What's the PDF file size?**
A: Typically 9-10KB, varying with content and graphics.

**Q: Can I modify the output?**
A: Yes, through content_generator.py templates.

**Q: Supported platforms?**
A: Any OS with Python 3.11+ (Windows, macOS, Linux).

## System Requirements

- Python 3.11 or higher
- 50MB free disk space
- ReportLab library
- lunar-python library
- jieba library

## Support

For issues or questions:
1. Check FAQ section
2. Review error messages
3. Contact developer support

## License

MIT License - free use with attribution

---

© 2025 BaZi Fortune Teller Project