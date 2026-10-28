# Smart Arabic Game Localization Prompt (English Version v1.1)

> [!CAUTION]
> ### ⚠️ IMPORTANT NOTICE: Commercial Use, Profit Sharing & Attribution
> - **No Commercial Use**: It is strictly prohibited for anyone to use this prompt, framework, or associated tools for any commercial purpose.
> - **Commercial Inquiries & Profit Sharing**: If you intend to use this commercially, you **must contact me in advance** via my social media accounts (**Instagram** or **TikTok** at https://bio.site/V7dt1) or **Email** (`v7dtads@gmail.com`), inform me about the project, and agree on **profit-sharing** terms.
> - **Public Non-Commercial Release (Attribution)**: If you publish or share a localization publicly for free, simply **crediting my name (`V7dt1` / `axxx503`) in the localization credits** (as an assistant/contributor via the prompt and general workflow) is sufficient and required.
> - **Official Social Links**: https://bio.site/V7dt1 | **Email**: `v7dtads@gmail.com`
> - **Support Link**: https://buymeacoffee.com/axxx503

### Important Note
This is an intelligent AI prompt for Arabic game localization (optimized for **Google Antigravity IDE**). Provide the game-folder path and, optionally, attach a font you prefer. The AI will discover the engine, files, text sources, and appropriate localization method, then handle the remaining work with autonomous end-to-end quality.

---

### Prompt Text (Copy Below)

```text
Game folder [insert the game folder path]

Fully localize this game into Arabic inside the game itself. Deliver natural, high-quality translation, correct Arabic rendering, and an easy reversible installation package that preserves originals and user saves.

I may optionally attach any font I prefer. If no font is attached, select a suitable open-source Arabic font (e.g. Tajawal for modern UI, Amiri for historical/medieval parchment) whose license permits distribution.

Discover the technical details and execute the work. Do not require a technical questionnaire or expect me to identify the engine or localization method. Make routine decisions from files and evidence. Ask only when essential information, access, or a consequential decision genuinely requires me.

1. AUTOMATIC DISCOVERY

Verify access to the path. If unavailable, explain what access is needed instead of pretending to inspect it.

Identify the game, engine/version, architecture, platform, active locale, text sources, fonts and archives from available evidence. Distinguish confirmed findings from hypotheses.

Look for previous localization work, progress files, extracted text and verified backups before starting over.

Create a separate workspace in an authorized writable location. Preserve originals and record SHA-256 hashes of targeted files. Never treat unknown modified files as clean originals.

Choose the least invasive viable route: native localization, supported resource overrides, targeted patches, then compatible runtime plugins when necessary. A method working in one game does not establish compatibility with another.

2. MULTI-ENGINE ARCHITECTURAL ROUTING

Investigate the actual build rather than assuming these features exist:

- Paradox Clausewitz / Jomini (e.g., Crusader Kings III, Victoria 3, Hearts of Iron IV):
  Inspect game/localization/<lang>/**/*.yml and game/fonts/fonts.font. Always write localization files with strict UTF-8 with BOM (\xef\xbb\xbf) and language headers (e.g. l_english:). Configure Arabic fonts in fonts.font fallback lists and merge into primary TrueType fonts.
- Unity:
  Mono versus IL2CPP, TMP_FontAsset objects, Addressables CRC, and resources.assets. If TypeTrees are stripped, borrow nodes from Addressables bundles to enable m_IsMultiAtlasTexturesEnabled = 1.
- Unreal Engine (UE4 / UE5):
  Binary .locres files, String Tables, Slate Composite Fonts, and runtime culture overrides (-culture=ar or DefaultGame.ini).
- Godot (3.x & 4.x):
  .po / .csv translation catalogs, TextServer native HarfBuzz shaping and BiDi before adding external preprocessing.
- GameMaker, Ren’Py, RPG Maker & Custom Engines:
  Inspect string tables, glyph lookups, font textures, and custom script blocks according to engine architecture.

Do not bypass DRM, encryption or anti-cheat. Seek a legitimate supported route and request intervention only when necessary.

3. INTELLIGENT FONT HANDLING

If I attach a font:
- Inspect its format, properties, Arabic coverage and licensing. Treat it as a visual preference and test engine readiness.

If no font is attached:
- Select a readable OFL Arabic font matching the game's art and text sizes.

In all cases:
- Fix the 36 isolated Presentation Forms-B glyphs (U+FE80..U+FEF1) by mapping them to base glyphs (U+0621..U+064A) in cmap so arabic_reshaper never outputs missing-character boxes.
- Verify 0 missing glyphs using FreeType across all contextual forms, hamzas, and lam-alef ligatures.

4. PROVE RENDERING EARLY

Before translating thousands of strings, establish a representative Arabic test (30-50 strings) in a separate game copy.

Test joining, reading direction, mixed Arabic/Latin/numeric text, wrapping, buttons, and confirmations.

Use universal token protection covering: {...}, [...], $VAR$, <tags>, #tags#!, @icons!, and %s/%d format specifiers.

Linguistic Purity Gate: Never apply BiDi base_dir="R" on predominantly English or un-translated hybrid sentences to prevent scrambled Latin words and punctuation.

5. CONTEXTUAL LOCALIZATION & QUALITY TRANSLATION

CRITICAL NEGATIVE CONSTRAINT:
- NEVER apply regex or dictionary word-by-word substitution on English sentences (e.g. replacing individual words like 'Exit' in 'Exit to Desktop' produces broken Frankenstein hybrid text).
- Every string selected for translation must be translated as a complete, grammatically sound sentence in natural Arabic.
- If a string is not yet translated in this pass, keep it in its clean original English language.

4-Tier Localization Hierarchy for Large Games (>5,000 strings):
1. Tier 1 (Core Navigation & HUD - Mandatory 100%):
   Main menus, Start/Load/Save/Quit dialogs, Options & Settings (Audio, Video, Controls), HUD bars, Pause banners (e.g. translating Paused to "اللعبة متوقفة مؤقتاً"), and Confirmations.
2. Tier 2 (Game Systems & Primary Concepts - Mandatory 100%):
   Character sheets, Traits, Skills, Combat interfaces, Faiths, Cultures, Laws, and Core Game Concepts.
3. Tier 3 (Dynamic Templates & Grammar Constructs):
   Dynamic templates respecting Arabic Idafa constructs (removing English prepositions like 'of': 'Barony of X' becomes 'بارونية X', and aligning key-value labels).
4. Tier 4 (Bulk Narrative, Events & Lore):
   Story trees, dialogues, historical events, and lore books translated in context-consistent batches.

Preserve placeholders, tags, control codes, and timing. Do not translate programming identifiers, paths, or asset names.

6. CONTINUITY AND AUTOMATED QA AUDITING

Maintain a unified glossary to guarantee 100% terminology consistency across all tiers.

Run automated QA validation (toolkit/localization_qa_validator.py) before packaging to guarantee:
- 0 Frankenstein Hybrid Strings (Zero broken mixed-language sentences).
- 0 Token Mismatches (100% match of all placeholders and format tags).
- 0 Missing FreeType Glyphs (Full font coverage).
- Valid encoding and UTF-8 BOM compliance where required.

7. PRODUCTION-GRADE REVERSIBLE PACKAGE

Build a clean, robust installation and uninstallation package:
- Install-Arabic.bat and Install-Arabic.ps1 with multi-storefront game path detection (Steam, GOG, Epic Games Store, Xbox Game Pass).
- Support silent execution mode (/S or -Quiet).
- Automated backup with SHA-256 hash ledger before any modification.
- Atomic rollback: automatically restores the clean backup if an error occurs mid-way.
- Uninstall-Arabic.bat and Uninstall-Arabic.ps1 to restore 100% original official files and remove added fonts.
- Absolute protection of user save directories (Documents, Saved Games) without touching them.
- Arabic README_AR.txt and OFL.txt license.

Start from the supplied game path: discover the details yourself, prove correct Arabic rendering, then continue authorized implementation until delivery or a genuine blocker.
```
