---
name: arabic-game-localization
description: Autonomous end-to-end Arabic game localization skill for Google Antigravity IDE. Discovers game engines (Unity, Clausewitz, Unreal, Godot, GameMaker, Ren'Py, custom), backs up originals with SHA-256 verification, merges OFL Arabic fonts with full isolated/connected Presentation Forms-B coverage, shapes RTL/BiDi Arabic while protecting {placeholders}, [brackets], $vars$, <tags>, and formatting, translates full inventories in context without naive word substitution, localizes in-game graphical posters, runs automated QA validation, and builds reversible lightweight install/uninstall packages.
---

# Arabic Game Localization Skill (`arabic-game-localization` v1.1)

> **⚠️ تنبيه الاستخدام وحقوق الملكية (Usage & Licensing Notice)**:
> - **يُمنع الاستخدام التجاري** لهذا الإطار أو المهارة أو البرومبت دون التواصل المسبق مع صاحب المشروع (`V7dt1` / `axxx503`) عبر حسابات التواصل الاجتماعي (https://bio.site/V7dt1) أو الإيميل (`v7dtads@gmail.com`) وإعلامه بالموضوع للاتفاق على **تقاسم الأرباح**.
> - **عند النشر العام (غير التجاري)**: يكفي ويُشترط **ذكر اسم صاحب المشروع (`V7dt1` / `axxx503`) في حقوق التعريب** (وفي ملف `README_AR.txt` داخل الحزمة) كمساعد في البرومبت ومساعد في الاستخدام العام.

Use this skill whenever the user asks to localize/translate a video game into Arabic (`تعريب لعبة`), fix disconnected/reversed Arabic letters in a game, merge Arabic glyphs into game fonts, or build an Arabic localization patch.

## Mandatory 7-Phase Workflow

### Phase 1: Automatic Discovery & Safe Workspace
1. Verify access to the target game directory. Never claim inspection if the path is inaccessible.
2. Detect the engine, exact version, architecture (`x86` / `x86_64`), runtime (`Mono` / `IL2CPP` / `Clausewitz-Jomini` / `Unreal Pak-IoStore` / `Godot PCK`), active localization system, and font assets from binary/file evidence.
3. Create an isolated workspace in `<scratch>/<game_name>_arabic` with a local Python virtual environment (`.venv`).
4. Record `SHA-256` hashes of all target original files in `backups/original_hashes.json` and copy clean originals to `backups/originals/` before any modification. Never touch user save directories (`Documents/...`, `Saved Games`).

### Phase 2: Multi-Engine Technical Routing (Least Invasive Path)
- **Unity**: Inspect `StreamingAssets/aa` (`Addressables`), `resources.assets`, `sharedassets*.assets`, `Unity.Localization` `StringTable` MonoBehaviours, and `TMP_FontAsset` / `Font` objects.
  - Check `catalog.bin` for `m_Crc` values before modifying Addressables bundles.
  - If `resources.assets` strips custom MonoBehaviour TypeTrees (`obj.read_typetree()` fails), extract `obj.serialized_type.nodes` from a `TMP_FontAsset` inside an Addressables bundle and pass those nodes to `read_typetree(nodes)` / `save_typetree(tree, nodes)`.
- **Paradox Clausewitz / Jomini** (CK3, Victoria 3, HOI4, EU4):
  - Inspect `game/localization/<language>/**/*.yml` and `game/fonts/fonts.font`.
  - Always write localization files with strict **UTF-8 with BOM (`\xef\xbb\xbf`)** and language header (`l_english:`).
  - Add OFL Arabic fonts into fallback lists in `fonts.font` and merge into primary TrueType fonts.
- **Unreal Engine** (UE4 / UE5):
  - Inspect `.locres` binary localization catalogs, String Tables, and Slate Composite Fonts.
  - Set runtime culture via `-culture=ar` or `DefaultGame.ini`.
- **Godot Engine** (3.x & 4.x):
  - Inspect `.po` / `.csv` translation catalogs.
  - Enable native HarfBuzz and BiDi in `TextServer` when supported, or use `safe_arabic_shaper.py` for legacy bitmap/dynamic font stacks.
- **Ren'Py & RPG Maker**:
  - Inspect `game/tl/<language>/` translation blocks or `data/*.json` files.

### Phase 3: Intelligent Font Engineering
1. Select an OFL-licensed Arabic font matching the game's visual style (e.g., `Tajawal` for clean modern UI, `Amiri` for historical/medieval parchment) under SIL OFL 1.1 unless the user attached a distributable font.
2. **Critical Isolated Presentation Forms-B Fix**:
   - Many Arabic fonts map isolated glyphs only to `U+0621..U+064A` and omit the 36 isolated codepoints in `U+FE80..U+FEF1` emitted by `arabic_reshaper`.
   - Always map all `LETTERS_ARABIC` `(isolated, initial, medial, final)` codepoints in `cmap`, falling back to `U+0621..U+064A` whenever `isolated` (`U+FE80..U+FEF1`) is absent from `cmap`.
3. Scale merged Arabic glyphs proportionally (`scale = 1.15 * (base_upm / arabic_upm)`) and verify `0` missing glyphs using `freetype-py` (`face.get_char_index(cp) != 0`) across all contextual forms, hamzas (`أ إ آ ؤ ئ ء`), and lam-alef ligatures (`لا لأ لإ لآ`).
4. Enable `m_IsMultiAtlasTexturesEnabled = 1` on static `TMP_FontAsset` objects or link dynamic fallback font assets.

### Phase 4: Early In-Game Rendering Proof
1. Before translating the full inventory, inject a representative 30–60 string Arabic test build covering connected letters, mixed Arabic + Latin + numbers, multi-line wrapping, `{placeholders}`, `[brackets]`, `$vars$`, and UI buttons.
2. Keep logical Arabic (`logical_ar`) strictly separate from shaped/visual display Arabic (`display_ar`).
3. **Token-Safe Shaping & Linguistic Purity Gate**:
   - Use `safe_arabic_shaper.py` (v1.1) with universal token protection covering `{...}`, `[...]`, `$VAR$`, `<...>`, `#tag#!`, `@icon!`, and `%s`/`%d`.
   - **Purity Gate**: Never apply BiDi `base_dir="R"` on predominantly Latin sentences. Prevent hybrid "Frankenstein" text reversal.
4. Launch the game or inspect `Player.log` / debug logs to confirm `0` missing-character warnings and `0` bundle load errors.

### Phase 5: Autonomous Staged Localization & Quality Translation
1. **Critical Negative Constraint**:
   - **NEVER** apply regex or dictionary word-by-word substitution on English sentences (e.g. replacing `Exit` with `خروج` in `Exit to Desktop` produces broken hybrid sentences).
   - Every string selected for translation must be translated as a **complete, coherent sentence** in natural Modern Standard Arabic.
   - If a string is not yet translated in this pass, keep it in its clean original English language.
2. **4-Tier Localization Hierarchy for Large Games (>5,000 strings)**:
   - **Tier 1 (Core Navigation & HUD - Mandatory 100%)**: Main menu, Start/Load/Save/Quit, Options & Settings (Audio, Video, Controls), HUD bars, Pause banners (`Paused` -> `اللعبة متوقفة مؤقتاً`), Notifications, Confirmations.
   - **Tier 2 (Game Systems & Primary Mechanics - Mandatory 100%)**: Character sheets, Attributes, Skills, Combat interfaces, Faiths, Cultures, Laws, Primary game concepts.
   - **Tier 3 (Dynamic Templates & Grammar Constructs)**: Dynamic templates (Idafa constructs replacing English `of`: `Barony of X` -> `بارونية X`, Key-Value pairs: `Holder: X` -> `الحاكم: X`).
   - **Tier 4 (Bulk Lore, Dialogues & Events)**: Story trees, lore books, narrative events translated in context-consistent batches.
3. Establish a unified glossary (`reports/glossary.json`) to guarantee 100% terminology consistency across all tiers.
4. Localize editable graphical text/posters using `Pillow` and visually inspect the result before injecting into game textures.

### Phase 6: Automated Linguistic QA & Verification Gate
1. Run `toolkit/localization_qa_validator.py` on the translated inventory:
   - Verify `frankenstein_strings == 0` (0 mixed broken hybrid sentences).
   - Verify `token_mismatches == 0` (100% match of all placeholders and format tags).
   - Verify `missing_freetype_glyphs == 0` (full glyph coverage).
   - Verify correct encoding and `UTF-8 BOM` headers where required.
2. Confirm clean engine asset re-opening and zero load crashes.

### Phase 7: Production-Grade Reversible Package
1. Build a beginner-friendly `package/` containing:
   - `Install-Arabic.bat` & `Install-Arabic.ps1` (with multi-launcher auto-detection: Steam, GOG, Epic, Xbox Game Pass, and atomic rollback on error).
   - `Uninstall-Arabic.bat` & `Uninstall-Arabic.ps1` (100% clean restoration with SHA-256 verification).
   - `README_AR.txt` & font license (`OFL.txt`).
   - Object-level patch payload rather than redistributing multi-hundred-MB proprietary game archives.
2. Test clean install, re-install/update, and full uninstall (verifying restored `SHA-256` hashes match `original_hashes.json` 100%) before declaring completion.
