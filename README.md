# 🎮 مشروع وأداة التعريب الذكي للألعاب بالذكاء الاصطناعي
## Smart Arabic Game Localization Framework & Prompt (Antigravity IDE ChatGPT Codex Claude Code)

[![License: Non-Commercial / Custom](https://img.shields.io/badge/License-Non--Commercial-red.svg)](LICENSE)
[![IDE: Google Antigravity](https://img.shields.io/badge/IDE-Google%20Antigravity-blue.svg)](https://deepmind.google)
[![Python Toolkit](https://img.shields.io/badge/Python-Toolkit-green.svg)](toolkit/)

---

### ⚠️ تنبيه هام جداً: شروط الاستخدام والنشر وحقوق الملكية

- **يُمنع منعاً باتاً الاستخدام التجاري**: لا يُسمح لأي شخص أو جهة باستخدام هذا المشروع أو البرومبت أو الأدوات أو المهارة بشكل تجاري (سواء ببيع التعريبات، أو الحزم، أو تقديم خدمات مدفوعة تعتمد عليه).
- **الاستثناء للاستخدام التجاري (تقاسم الأرباح)**: إذا كنت ترغب في استخدامه بشكل تجاري، يجب عليك التواصل معي مسبقاً عبر حساباتي في مواقع التواصل الاجتماعي (**إنستغرام Instagram** أو **تيك توك TikTok** عبر الرابط: [https://bio.site/V7dt1](https://bio.site/V7dt1)) أو عبر البريد الإلكتروني (`v7dtads@gmail.com`) وإعلامي بالموضوع للاتفاق على تقاسم الأرباح وأخذ موافقة خطية صريحة قبل البدء.
- **النشر العام المجاني (شرط ذكر الاسم / Attribution)**: إذا كنت تستخدم هذا المشروع لنشر تعريب بشكل عام ومجاني للجمهور، فيكفي ذكر اسمي (`V7dt` / `axxx503`) في حقوق التعريب كمساهم ومساعد في التعريب عبر البرومبت والأدوات والاستخدام العام.

🔗 **للتواصل والحسابات الرسمية (Contact & Official Links):**
- منصات التواصل الاجتماعي (Instagram / TikTok / إلخ): [https://bio.site/V7dt1](https://bio.site/V7dt1)
- البريد الإلكتروني (Email): `v7dtads@gmail.com`
- رابط الدعم (Buy Me a Coffee): [https://buymeacoffee.com/axxx503](https://buymeacoffee.com/axxx503)

---

## 🌟 نظرة عامة على المشروع

مشروع يقدّم منهجية هندسية متكاملة + برومبت ذكي شامل + مهارة جاهزة (`Skill`) + أدوات بايثون آلية لتعريب الألعاب بالكامل داخل اللعبة نفسها من الصفر، دون الحاجة إلى خبرة مسبقة في الهندسة العكسية أو معرفة عميقة بمحرك اللعبة.

### ✨ الميزات الأساسية للإطار
1. **بروتوكول توفير الموارد (Zero-Waste Protocol):** نظام تشغيل صامت يمنع استنزاف الذاكرة والـ Tokens، ويعتمد على السجلات المختصرة.
2. **التوجيه الذكي للمحركات والأدوات:** دعم تلقائي لاستخراج وفحص أصول أشهر المحركات (Unity, Unreal Engine 5, Godot, GameMaker, Ren'Py).
3. **هندسة الخطوط والـ BiDi المتقدمة:** حل جذري لمشكلة الحروف العربية المقطوعة والمنفصلة، وحماية تامّة للمتغيرات البرمجية (`{...}`) ووسوم الواجهات (`<...>`).
4. **بناء الحزم الخفيفة (Object-Level Patching):** اعتماد حزم تثبيت وإزالة نظيفة تعتمد على الكائنات المعدلة فقط دون تضخيم الحجم أو مخالفة حقوق النشر.

---

## 🚀 طريقة الاستخدام خطوة بخطوة

1. **تحميل البرومبت:** احصل على ملف البرومبت النصي من مجلد `prompts/` أو من قسم الإصدارات (`Releases`).
2. **فتح البيئة:** افتح **Codex Claude Google Antigravity IDE**.
3. **لصق المسار:** ضع مسار مجلد اللعبة في المكان المخصص أول البرومبت:
   ```text
   مسار اللعبة [C:\Program Files (x86)\Steam\steamapps\common\YourGame]
   ```
4. **التنفيذ:** أرسل الطلب، ودع الوكيل يتولى الاكتشاف والتعريب وبناء الحزمة بالكامل!

---

## 🕹️ تعريب ألعاب الكونسل والمحاكيات (Emulators & Consoles)

بالإضافة إلى الدعم الأساسي لألعاب الحاسب الشخصي (**PC**)، يتيح لك الإطار إمكانية تعريب **ألعاب الكونسل المعدلة** و**ألعاب المحاكيات** بكل سهولة. 

> **الفكرة العامة:** يتم جلب ملفات اللعبة إلى جهاز الـ PC، وفك حزمتها أو استخراجها باستخدام أدوات التفكيك المخصصة، ثم إعطاء مسار المجلد المستخرج للذكاء الاصطناعي ليتولى هندسة الخطوط والترجمة، وبعد الانتهاء يتم إعادة حزمها وتثبيتها.

### 1️⃣ ألعاب الكونسل (Consoles)
* **PlayStation 4 (PS4):**
  * **الأداة:** `PS4 PKG Tool / shadPKG`
  * **الوظيفة:** فحص، تحليل، وفك ملفات PKG الخاصة بألعاب PS4 واستخراج محتويات مجلد اللعبة.
  * **رابط التحميل الرسمي:** [PS4PKGTool GitHub Releases](https://github.com/pearlxcore/PS4PKGTool)
  * **كلمات البحث للتعلم (YouTube / Google):** `PS4 PKG extraction guide`, `how to unpack ps4 game pkg file`

* **PlayStation 3 (PS3):**
  * **الأداة:** `PS3 Decrypter / EDAT Tool`
  * **الوظيفة:** فك تشفير وفك ملفات ألعاب PS3 ISO وملفات الحزم لتكون جاهزة للمحاكي أو التعديل.
  * **رابط التحميل الرسمي:** [RPCS3 Tools & Wiki](https://rpcs3.net/quickstart)
  * **كلمات البحث للتعلم:** `how to extract ps3 iso game files`, `ps3 decryption tools guide`

### 2️⃣ ألعاب أجهزة نينتندو (Nintendo Emulators)
* **Nintendo Switch:**
  * **الأداة:** `Switch-ROM-Tools / HACBrewPack`
  * **الوظيفة:** فحص، فك، واستخراج ملفات الألعاب بصيغ `XCI` و `NSP` إلى مجلدات بيانات قابلة للقراءة والتعريب.
  * **رابط التحميل الرسمي:** [Switch-ROM-Tools GitHub](https://github.com/tsutsen/Switch-ROM-Tools) | [HACBrewPack GitHub](https://github.com/TheLordScruffy/HACBrewPack)
  * **كلمات البحث للتعلم:** `Switch roms unpack nsp xci tools`, `extract switch game files for emulation`

* **Nintendo Wii U:**
  * **الأداة:** `Cemu / NUS Downloader / U-King Tools`
  * **الوظيفة:** إدارة وفك ملفات العاب Wii U وتفكيك صيغ `WUD`/`WUX` أو المجلدات المشفرة (NUS).
  * **رابط التحميل الرسمي:** [Cemu Emulator GitHub](https://github.com/cemu-project/Cemu)
  * **كلمات البحث للتعلم:** `Cemu wii u game extraction tool`, `how to decrypt wii u nus files`

* **Nintendo Wii & GameCube:**
  * **الأداة:** `Wiimms ISO Tools (WIT / WWT)`
  * **الوظيفة:** مجموعة أدوات سطر أوامر قوية جداً لفحص، تفكيك، استخراج، وإعادة بناء صور ألعاب `ISO` و `WBFS` لأجهزة Wii و GameCube.
  * **رابط التحميل الرسمي:** [Wiimms ISO Tools Official](https://github.com/Wiimm/wiimms-iso-tools)
  * **كلمات البحث للتعلم:** `Wiimms ISO Tools guide`, `extract wii iso wbfs files`

* **Nintendo 3DS:**
  * **الأداة:** `3DS Simple CIA Converter / GodMode9`
  * **الوظيفة:** فك واستخراج ملفات ألعاب 3DS بصيغ `CIA` و `3DS` إلى مجلدات محتوى النظام.
  * **رابط التحميل الرسمي:** [GodMode9 GitHub](https://github.com/d0k3/GodMode9)
  * **كلمات البحث للتعلم:** `extract 3ds cia files tool`, `how to decrypt 3ds roms`

---

## 🛠️ جدول أدوات الأطراف الثالثة (Third-Party Engine Tools)

يعتمد الإطار في الخلفية على تكامل ذكي مع أقوى أدوات ومكتبات المجتمع مفتوح المصدر:

| الأداة (Tool) | المحرك المستهدف / الوظيفة | رابط التحميل الرسمي (GitHub Releases) | الترخيص |
| :--- | :--- | :--- | :--- |
| **UnityPy** | فك وحقن أصول Unity عبر بايثون | [GitHub Releases](https://github.com/K0lb3/UnityPy/releases) | MIT |
| **UABEA** | فك وتعديل حزم أصول Unity الحديثة | [GitHub Releases](https://github.com/nesrak1/UABEA/releases) | MIT |
| **Il2CppDumper** | استخراج بيانات ألعاب Unity IL2CPP | [GitHub Releases](https://github.com/Perfare/Il2CppDumper/releases) | MIT |
| **repak / retoc** | فك وضغط ملفات `.pak` و `IoStore` لأنريل إنجن | [GitHub Releases](https://github.com/trumank/repak/releases) | MIT / Apache |
| **UE4localizationsTool** | استخراج وحقن ملفات `.locres` لأنريل | [GitHub Releases](https://github.com/amrshaheen61/UE4localizationsTool/releases) | GPL-3.0 |
| **GDRETools (gdsdecomp)** | فك حزم ألعاب Godot (`.pck`) | [GitHub Releases](https://github.com/bruvzg/gdsdecomp/releases) | MIT |
| **UndertaleModTool** | تعديل ملفات `data.win` لألعاب GameMaker | [GitHub Releases](https://github.com/UnderminersTeam/UndertaleModTool/releases) | GPL-3.0 |
| **msdf-atlas-gen** | توليد أطالس خطوط SDF و MSDF عالية الدقة | [GitHub Releases](https://github.com/Chlumsky/msdf-atlas-gen/releases) | MIT |
- **HDiffPatch** | إنشاء وتطبيق باتشات الفروقات الثنائية | [GitHub Releases](https://github.com/sisong/HDiffPatch/releases) | MIT |

---

## 📂 هيكل المستودع (Repository Structure)

```text
smart-arabic-game-localization/
├── README.md               # الدليل الشامل للمشروع (هذا الملف)
├── LICENSE                 # شروط الاستخدام وحقوق الملكية
├── prompts/                # ملفات البرومبت الذكي (نسخ عربية وإنجليزية)
├── antigravity-skill/      # مهارات Google Antigravity IDE الجاهزة
├── toolkit/                # أدوات بايثون (تشكيل، BiDi، دمج خطوط)
└── examples/               # دراسات حالة تطبيقية كاملة
```

---

⭐ **لا تنسَ الضغط على زر النجمة (Star) في أعلى المستودع لدعم الاستمرار وتطوير المشروع!**
