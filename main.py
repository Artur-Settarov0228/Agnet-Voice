import os
import sys
import mimetypes
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Sozlamalar va API kalitni yuklash
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    api_key = input("Google Gemini API kalitini kiriting: ").strip()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# 2. Audio fayl yo'lini aniqlash
if len(sys.argv) > 1:
    audio_path = sys.argv[1]
else:
    audio_path = input("Audio fayl yo'lini kiriting (masalan, audio.mp3 yoki voice.wav): ").strip()

if not os.path.exists(audio_path):
    print(f"Xatolik: '{audio_path}' fayli topilmadi!")
    sys.exit(1)

# 3. AGENTS.md dagi tizimli ko'rsatma va qoidalarni o'qish
with open("AGENTS.md", "r", encoding="utf-8") as f:
    agents_instructions = f.read()

# 4. Audio faylni yuklash
print(f"\n[+] Audio fayl yuklanmoqda: {audio_path}...")
try:
    audio_file = genai.upload_file(path=audio_path)
except Exception:
    mime_type, _ = mimetypes.guess_type(audio_path)
    mime_type = mime_type or "audio/mp3"
    with open(audio_path, "rb") as f:
        audio_file = {"mime_type": mime_type, "data": f.read()}

# ----------------------------------------------------
# 1-BOSQICH: Ovozni matnga o'girish (Transkripsiya)
# ----------------------------------------------------
print("[+] 1-bosqich: Ovoz matnga o'girilmoqda...")
stt_prompt = (
    "Quyidagi audio faylni tinglang va undagi barcha gaplarni so'zma-so'z to'liq matn (transkripsiya) "
    "sifatida yozib bering. Hech qanday sharh yoki qo'shimcha so'z qo'shmang."
)
response_1 = model.generate_content([audio_file, stt_prompt])
transcript = response_1.text.strip()

print("\n" + "=" * 60)
print("1-BOSQICH: MATN (Transkripsiya)")
print("=" * 60)
print(transcript)

# ----------------------------------------------------
# 2-BOSQICH: Matndan vazifalarni ajratish (To-Do List)
# ----------------------------------------------------
print("\n[+] 2-bosqich: Vazifalar ajratilmoqda...")
task_prompt = f"""Quyidagi AGENTS.md qoidalari va ko'rsatmalariga qat'iy amal qiling:

{agents_instructions}

Foydalanuvchining transkript matni:
\"\"\"
{transcript}
\"\"\"

Yuqoridagi ko'rsatmalar bo'yicha vazifalarni ajratib, natijani bering:"""

response_2 = model.generate_content(task_prompt)
tasks_result = response_2.text.strip()

print("\n" + "=" * 60)
print("2-BOSQICH: VAZIFALAR (To-Do ro'yxati)")
print("=" * 60)
print(tasks_result)
