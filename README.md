# 🎮 مشروع وأداة التعريب الذكي للألعاب بالذكاء الاصطناعي
## Smart Arabic Game Localization Framework & Prompt (Antigravity IDE)

[![License: Non-Commercial / Custom](https://img.shields.io/badge/License-Non--Commercial_/_Attribution-red.svg)](LICENSE)
[![Font License: SIL OFL 1.1](https://img.shields.io/badge/Font_License-SIL_OFL_1.1-blue.svg)](examples/over-the-hill/package/OFL.txt)
[![IDE: Google Antigravity](https://img.shields.io/badge/IDE-Google_Antigravity-purple.svg)](#لماذا-استخدمنا-google-antigravity-ide-وليس-شات-الذكاء-الاصطناعي-العادي)
[![Socials: V7dt1](https://img.shields.io/badge/Socials-bio.site/V7dt1-blue.svg)](https://bio.site/V7dt1)
[![Support: Buy Me a Coffee](https://img.shields.io/badge/Support-axxx503-yellow.svg)](https://buymeacoffee.com/axxx503)

> [!CAUTION]
> ### ⚠️ تنبيه هام جداً: شروط الاستخدام والنشر وحقوق الملكية
> 1. **يُمنع منعاً باتاً الاستخدام التجاري**: لا يُسمح لأي شخص أو جهة باستخدام هذا المشروع أو البرومبت أو الأدوات أو المهارة بشكل تجاري (سواء ببيع التعريبات أو الحزم أو تقديم خدمات مدفوعة تعتمد عليه).
> 2. **الاستثناء للاستخدام التجاري (تقاسم الأرباح)**: إذا كنت ترغب في استخدامه بشكل تجاري، **يجب عليك التواصل معي مسبقاً** عبر حساباتي في مواقع التواصل الاجتماعي (**إنستغرام Instagram** أو **تيك توك TikTok** عبر الرابط: https://bio.site/V7dt1) أو عبر **البريد الإلكتروني Email** (`v7dtads@gmail.com`) وإعلامي بالموضوع للاتفاق على **تقاسم الأرباح** وأخذ موافقة خطية صريحة قبل البدء.
> 3. **النشر العام المجاني (شرط ذكر الاسم / Attribution)**: إذا كنت تستخدم هذا المشروع لنشر تعريب بشكل عام ومجاني للجمهور، فيكفي **ذكر اسمي (`V7dt1` / `axxx503`) في حقوق التعريب** كمساهم ومساعد في التعريب عبر البرومبت والأدوات وفي الاستخدام العام.
>
> **🔗 للتواصل والحسابات الرسمية (Contact & Official Links):**
> - **جميع حسابات التواصل الاجتماعي (Instagram / TikTok / إلخ)**: https://bio.site/V7dt1
> - **البريد الإلكتروني (Email)**: `v7dtads@gmail.com`
> - **رابط الدعم (Buy Me a Coffee)**: https://buymeacoffee.com/axxx503
>
> **Important Notice (Commercial Use & Attribution):**
> - **Commercial Use is Strictly Prohibited**: Nobody is allowed to use this framework, prompt, skill, or toolkit for any commercial purpose without prior permission.
> - **Commercial Licensing & Profit Sharing**: If you wish to use this project commercially, you **must contact me first** via my social media accounts (**Instagram** or **TikTok** at https://bio.site/V7dt1) or **Email** (`v7dtads@gmail.com`), inform me about the project, and agree on **profit-sharing terms**.
> - **Public Non-Commercial Sharing (Attribution Required)**: For free/public releases, simply **crediting my name (`V7dt1` / `axxx503`) in the localization credits** as a contributor/assistant via the prompt and general usage is sufficient.


مشروع يقدّم **منهجية هندسية متكاملة + برومبت ذكي شامل + مهارة جاهزة (Skill) + أدوات بايثون آلية** لتعريب الألعاب بالكامل داخل اللعبة نفسها من الصفر، دون الحاجة إلى خبرة مسبقة في الهندسة العكسية أو معرفة محرك اللعبة.

---

## 🌟 لماذا هذا المشروع مختلف؟

في السابق، كان تعريب أي لعبة يتطلب البحث اليدوي عن المحرك، وفك التشفير أو الضغط، ومعرفة سبب ظهور الحروف العربية مقطعة أو معكوسة (`م ر ح ب ا`) أو اختفاء بعض الحروف من الخطوط، أو تعطل المتغيرات البرمجية `{playerName}` داخل النص العربي.

هذا المستودع يجمع بين:
1. **برومبت التعريب الذكي للألعاب (`prompts/`)**: تعليمات هندسية صارمة تقود الذكاء الاصطناعي في 7 مراحل منظمة (الاكتشاف التلقائي، فحص المحرك، هندسة الخطوط، إثبات العرض المبكر، الجرد والترجمة السياقية الكاملة، تعريب الصور، وبناء حزمة التثبيت والإزالة).
2. **بيئة Google Antigravity IDE**: استخدام وكيل برمجي (Agentic IDE) يمتلك وصولاً مباشراً لملفات الجهاز، والطرفية (Terminal)، والرؤية البصرية لفحص الصور والخطوط، وقراءة سجلات تشغيل اللعبة (`Player.log`).
3. **مهارة جاهزة لـ Antigravity IDE (`antigravity-skill/`)**: ملف `SKILL.md` يمكنك إضافته لبرنامج Antigravity ليتعلم تلقائياً كل أسرار تعريب الألعاب وإصلاح الخطوط والاتجاه العربي.
4. **صندوق أدوات بايثون (`toolkit/`)**: سكريبتات جاهزة لدمج الخطوط العربية، وإصلاح مشكلة الـ 36 حرفاً منفصلاً (`U+FE80..U+FEF1`)، وتشكيل النصوص العربية مع حماية المتغيرات البرمجية والوسوم.
5. **دراسة حالة تطبيقية كاملة (`examples/over-the-hill/`)**: تعريب كامل بنسبة 100% للعبة `over the hill` (محرك Unity 6000.0.75f1 IL2CPP) يشمل 1,499 نصاً وملصقات الأقاليم المصورة وحزمة تثبيت وإزالة خفيفة (`3.8 MB` فقط).

---

## 🛠️ لماذا استخدمنا Google Antigravity IDE وليس شات الذكاء الاصطناعي العادي؟

| الميزة | شات الذكاء الاصطناعي العادي (في المتصفح) | برنامج **Google Antigravity IDE** |
|---|---|---|
| **الوصول لملفات اللعبة** | ❌ لا يستطيع رؤية مجلد اللعبة أو فحص الأصول | ✅ يفحص مجلد اللعبة، يكتشف المحرك والمعمارية تلقائياً |
| **حساب البصمات والنسخ الاحتياطي** | ❌ غير ممكن | ✅ يحسب `SHA-256` لكل ملف أصلي وينشئ نسخة احتياطية آمنة |
| **هندسة الخطوط وإصلاح الحروف الناقصة** | ❌ لا يستطيع تعديل ملفات `TTF` أو `SDF Atlas` | ✅ يدمج الخط العربي بـ `fonttools` ويختبر كل حرف بـ `FreeType` |
| **الرؤية البصرية (Vision)** | ❌ لا يرى النتيجة داخل ملفاتك | ✅ يولّد لوحات اختبار ويعرّب الصور والملصقات ويتحقق منها بصرياً |
| **اختبار اللعبة الفعلي** | ❌ يترك لك التجربة وإصلاح الأخطاء | ✅ يشغّل اللعبة ويقرأ `Player.log` للتأكد من اختفاء كافة الأخطاء |
| **بناء حزمة التثبيت والإزالة** | ❌ يعطيك نصوصاً فقط | ✅ يبني مثبّتاً وأداة إزالة (`Install/Uninstall`) ويختبرهما فعلياً |

### البيئة والمودل والأدوات المستخدمة في التجربة:
- **البرنامج (IDE)**: **Google Antigravity IDE** (بيئة التطوير الوكيلة من Google DeepMind).
- **المودل (Model)**: وكيل Antigravity المدعوم بنماذج Gemini المتقدمة للتفكير والبرمجة الوكيلة والقدرات البصرية (Multimodal Agentic Coding).
- **المهارات المفعّلة (Skills)**:
  - `managing-python-dependencies`: لإنشاء بيئة بايثون افتراضية معزولة (`.venv`) وتثبيت الحزم دون المساس بنظام التشغيل.
  - `arabic-game-localization`: المهارة المضمنة في هذا المستودع.
- **الحزم البرمجية (Python Toolkit)**:
  - `UnityPy`: لفك وحقن ملفات الأصول (`resources.assets` و `.bundle`) والتعامل مع `Stripped TypeTrees`.
  - `fonttools` + `freetype-py`: لدمج الخطوط العربية وفحص تواجد المحارف في جداول `cmap`.
  - `arabic-reshaper` + `python-bidi`: لتشكيل الحروف العربية المتصلة وترتيب الاتجاه من اليمين لليسار (`RTL`) مع حماية المتغيرات.
  - `Pillow (PIL)`: لتعريب الصور والملصقات داخل اللعبة وتوليد صور إثبات الخطوط.

---

## 📥 تحميل البرومبت النصي (`.txt`) والحزم الجاهزة (Releases)

> **💡 لتحميل ملف البرومبت الجاهز للنسخ (`.txt`) أو المهارة أو حزمة تعريب لعبة `over the hill` مباشرة:**
> ادخل إلى قسم **[الـ Releases (الإصدارات) من هنا](../../releases/latest)** وحمّل الملف الذي يناسبك:
> 1. 📄 **`Smart-Arabic-Localization-Prompt-AR.txt`**: ملف البرومبت الذكي باللغة العربية جاهز للنسخ واللصق مباشرة.
> 2. 📄 **`Smart-Arabic-Localization-Prompt-EN.txt`**: ملف البرومبت الذكي باللغة الإنجليزية (English Version).
> 3. 📦 **`Smart-Arabic-Localization-Prompt-and-Skill-v1.0.zip`**: حزمة خفيفة تحتوي على البرومبت + المهارة الجاهزة لبرنامج Antigravity + أدوات بايثون.
> 4. 🎮 **`Over-The-Hill-Arabic-Patch-v1.0.zip`**: حزمة التثبيت والإزالة الجاهزة لتعريب لعبة `over the hill` بالكامل.
>
> ⭐ **لا تنسَ الضغط على زر النجمة (Star) في أعلى المستودع لدعم المشروع!**

---

## 🚀 طريقة الاستخدام خطوة بخطوة (للمبتدئين والمطورين)

لا تحتاج لمعرفة محرك اللعبة أو طريقة استخراج نصوصها. اتبع الخطوات الأربع التالية فقط:

### الطريقة الأولى: عبر تحميل ونسخ ملف البرومبت الذكي مباشرة
1. حمّل ملف البرومبت النصي **`Smart-Arabic-Localization-Prompt-AR.txt`** من قسم **[Releases (الإصدارات)](../../releases/latest)** (أو من مجلد [`prompts/`](prompts/)).
2. افتح برنامج **Google Antigravity IDE**.
3. انسخ البرومبت، وضع مسار مجلد لعبتك في المكان المخصص أول البرومبت:
   ```text
   مسار اللعبة [C:\Program Files (x86)\Steam\steamapps\common\YourGame]
   ```
4. أرسل الطلب في محادثة Antigravity IDE، ووافق على تشغيل الأوامر عندما يستأذنك الوكيل. سيتولى الوكيل كل شيء من الفحص وحتى تسليمك حزمة التثبيت!

### الطريقة الثانية: تثبيت المهارة (Skill) داخل Antigravity IDE (موصى به)
إذا أردت أن يصبح برنامج Antigravity IDE خبيراً دائماً في تعريب الألعاب دون الحاجة لنسخ البرومبت الطويل كل مرة:
1. انسخ مجلد [`antigravity-skill/arabic-game-localization`](antigravity-skill/arabic-game-localization) إلى مسار المهارات في جهازك:
   - في ويندوز: `C:\Users\<Username>\.gemini\antigravity\skills\arabic-game-localization`
2. بعدها، افتح أي محادثة في Antigravity IDE واكتب ببساطة:
   > `عرّب لي اللعبة الموجودة في المسار [ضع مسار اللعبة هنا] بالكامل مع حزمة تثبيت وإزالة.`

---

## 🧠 أهم الابتكارات التقنية في هذا المستودع

### 1. حل مشكلة اختفاء الحروف العربية المنفصلة (36 Isolated Glyphs Fix)
كثير من الخطوط العربية الحديثة (مثل `Tajawal`) تضع أشكال الحروف المتصلة (البداية والوسط والنهاية) في نطاق `Arabic Presentation Forms-B (U+FE70..U+FEFF)`، لكنها تترك الأشكال المنفصلة في النطاق الأساسي `U+0621..U+064A` فقط ولا تسجلها في `U+FE80..U+FEF1`. عندما يقوم `arabic_reshaper` بتحويل الحرف المنفصل إلى `U+FE80..U+FEF1`، يختفي الحرف داخل اللعبة أو يظهر كمربع!
- **الحل في [`toolkit/arabic_font_merger.py`](toolkit/arabic_font_merger.py)**: يقوم السكريبت تلقائياً بربط جميع نقاط `U+FE80..U+FEF1` بمحارفها الأصلية في جدول `cmap` مع ضبط المقاييس (`UPM Scaling`) وفحصها بـ `FreeType` لضمان **صفر حروف مفقودة**.

### 2. حماية المتغيرات البرمجية (`{...}`) والوسوم (`<...>`) أثناء التشكيل والـ BiDi
عند تطبيق خوارزمية `BiDi` الساذجة على نص يحتوي على متغيرات مثل `{playerName}` أو صيغ جمع ذكية `{requiredPlayers:plural:لاعب|لاعبين}`، تنقلب الأقواس أو يتغير ترتيب المتغيرات فتتعطل اللعبة.
- **الحل في [`toolkit/safe_arabic_shaper.py`](toolkit/safe_arabic_shaper.py)**:
  - استبدال كل متغير أو وسم بمحرف حراسة مؤقت قوي الاتجاه من اليمين لليسار (`RTL Sentinel` في النطاق `U+05D0..U+05EA`) قبل التشكيل والـ BiDi، ثم استعادة المتغير الأصلي في مكانه الصحيح 100%.
  - تشكيل الكلمات العربية داخل صيغ `SmartFormat` مثل `{var:plural:خيار1|خيار2}` بشكل مستقل قبل حماية المتغير.
  - تقسيم الفقرات الطويلة عند حدود الكلمات الطبيعية قبل عكس الاتجاه البصري حتى لا تظهر الأسطر مقلوبة من الأسفل إلى الأعلى داخل المحركات التي لا تدعم العربية أصلاً.

### 3. حقن الخطوط في الأصول منزوعة الشجرة (`Stripped TypeTrees`)
في ألعاب Unity الحديثة، قد يكون ملف `resources.assets` منزوع الـ `TypeTree` لكائنات `TMP_FontAsset`. يوضح هذا الإطار كيفية استعارة شجرة الأنواع (`serialized_type.nodes`) من حزم `Addressables` لتفعيل `m_IsMultiAtlasTexturesEnabled = 1` وربط الخطوط البديلة دون الحاجة لتثبيت محمل إضافات خارجي مثل `BepInEx`.

### 4. حزم التثبيت الخفيفة المعتمدة على الكائنات (`Object-Level Patching`)
بدلاً من إعادة توزيع ملفات اللعبة الأصلية الضخمة (التي قد يتجاوز حجمها 300 ميجابايت وتخالف حقوق النشر)، يقوم المثبّت في [`examples/over-the-hill/package/`](examples/over-the-hill/package/) بتخزين الكائنات المعدلة فقط (`~3.8 MB`)، ويتحقق من البصمة الرقمية `SHA-256` لملفات المستخدم الأصلية، ويأخذ نسخة احتياطية تلقائية قبل الحقن، مع أداة إزالة تستعيد اللعبة لحالتها الأصلية بنسبة 100%.

### 5. بوابة النقاء اللغوي وحماية المتغيرات الشاملة (Linguistic Purity Gate v1.1)
في التحديث v1.1 من [`toolkit/safe_arabic_shaper.py`](toolkit/safe_arabic_shaper.py)، تم توسيع نطاق حماية المتغيرات ليشمل كافة المحركات: `{...}` و `[...]` و `$VAR$` و `<tags>` و `#tags#!` و `@icons!` و `%s/%d`. كما أُضيفت "بوابة النقاء اللغوي" لمنع عكس اتجاه الأسطر اللاتينية غير المترجمة، والقضاء نهائياً على تشوه النصوص الهجينة (Frankenstein Text).

### 6. أداة تدقيق وفحص الجودة الآلية (`toolkit/localization_qa_validator.py`)
أداة فحص آلية سريعة وخفيفة تتيح للذكاء الاصطناعي والمطور التأكد من سلامة 100% من المتغيرات والأقواس، واكتشاف أي جمل مختلطة أو غير مكتملة، وحساب نسبة التغطية الحقيقية للتعريب قبل اعتماد الحزمة.

---

## 📂 هيكل المستودع (Repository Structure)

```text
smart-arabic-game-localization/
├── README.md                                      # الدليل الشامل للمشروع (عربي / إنجليزي)
├── LICENSE                                        # شروط الاستخدام والنشر (غير تجاري + شرط ذكر الاسم)
├── prompts/
│   ├── SMART_ARABIC_LOCALIZATION_PROMPT_AR.md     # برومبت التعريب الذكي للألعاب (النسخة العربية v1.1)
│   └── SMART_ARABIC_LOCALIZATION_PROMPT_EN.md     # Smart Arabic Game Localization Prompt (English v1.1)
├── antigravity-skill/
│   └── arabic-game-localization/
│       └── SKILL.md                               # مهارة محدثة للتثبيت في Google Antigravity IDE
├── toolkit/
│   ├── requirements.txt                           # مكتبات بايثون المطلوبة
│   ├── safe_arabic_shaper.py                      # أداة التشكيل v1.1 مع بوابة النقاء اللغوي وحماية المتغيرات
│   ├── localization_qa_validator.py               # أداة فحص الجودة الآلية وكشف النصوص الهجينة
│   └── arabic_font_merger.py                      # أداة دمج الخطوط العربية وإصلاح جدول cmap واختبار FreeType
└── examples/
    └── over-the-hill/                             # دراسة حالة تطبيقية كاملة: تعريب لعبة over the hill
        ├── CASE_STUDY_AR.md                       # التقرير الهندسي لتعريب اللعبة
        ├── posters/                               # الملصقات المعربة ولوحة إثبات الخطوط
        ├── translations/                          # المعجم وملفات النصوص المعربة (1,499 نصاً)
        └── package/                               # حزمة التثبيت والإزالة الجاهزة للمستخدم النهائي
```

---

## 🌍 English Summary

**Smart Arabic Game Localization Framework** is an open-source prompt engineering methodology, **Google Antigravity IDE Skill**, and Python toolkit designed to autonomously localize video games into high-quality, properly shaped RTL Arabic.

### How It Works:
1. Open **Google Antigravity IDE**.
2. Copy the prompt from [`prompts/SMART_ARABIC_LOCALIZATION_PROMPT_EN.md`](prompts/SMART_ARABIC_LOCALIZATION_PROMPT_EN.md) (or install [`antigravity-skill/arabic-game-localization/SKILL.md`](antigravity-skill/arabic-game-localization/SKILL.md)).
3. Paste your local game directory path `[C:\Path\To\Game]`.
4. The agent automatically detects the engine/architecture, records `SHA-256` hashes, backs up originals in an isolated workspace, merges an OFL-licensed Arabic font (`Tajawal`) with full isolated/connected glyph coverage, runs an early in-game rendering proof, translates the complete string inventory with contextual awareness while preserving `{placeholders}` and `<tags>`, localizes in-game graphical posters, and builds a lightweight, reversible `Install/Uninstall` package.
