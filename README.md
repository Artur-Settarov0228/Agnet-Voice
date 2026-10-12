# 🤖 Ovozli Vazifa Menejeri (Voice Task Agent)

Ovozli xabarlarni Google Gemini API orqali matnga o'giruvchi va `AGENTS.md` dagi ko'rsatmalar asosida avtomatik To-Do ro'yxatiga aylantirib beruvchi sodda va tezkor yechim.

## 🚀 Ishga tushirish

1. **Kutubxonalarni o'rnatish:**
   ```bash
   pip install -r requirements.txt
   ```

2. **API kalitni sozlash:**
   `.env` fayliga Gemini API kalitini yozing:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

3. **Skriptni ishga tushirish:**
   ```bash
   python main.py audio.mp3
   ```
   yoki to'g'ridan-to'g'ri:
   ```bash
   python main.py
   ```

## 📋 Bosqichlar
- **1-bosqich:** Audio fayldan to'liq transkripsiya (qora matn) olinadi.
- **2-bosqich:** `AGENTS.md` qoidalari asosida tozalangan, ustuvorligi va muddatlari belgilangan strukturalangan To-Do ro'yxati ekranga chiqariladi.
