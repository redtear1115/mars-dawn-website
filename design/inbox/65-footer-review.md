# MarsDawn Website — Landing Footer 設計建議

**Issue:** https://github.com/redtear1115/mars-dawn-website/issues/65  
**用途：** 給 Claude 實作 footer 統一與信任出口。  
**範圍：** `public/` 首頁與內頁共用 footer；四語（en / zh-Hant / zh-Hans / ja）同步。  
**限制：** 維持 Quiet Sunrise／CSP（無第三方 JS、無 newsletter widget）；不要做多欄 sitemap、社群 icon 牆、語系切換複製、waitlist／Pre-Order 主 CTA。  
**請勿：** merge 本 PR 即當成已上線實作——本 inbox 是規格與建議；實作可另開 PR 或在同 PR 接續（由 Claude 決定），但不要自行 merge main。

## 結論（先讀這段）

1. **統一首頁／內頁為兩列：** 上列 `nav` 連結；下列 meta（©；內頁可選 Store 狀態一句）。  
2. **首頁還原 hairline**（拿掉或收斂 `footer-home { border-top: 0 }`），與 `dawn-close` 分層。  
3. **內頁拿掉** footer 內舊 slogan「Read what your agent wrote.」與長句 Coming soon（與 redesign／Closing band 重複）；若要狀態，用既有 store-chip 語彙放 meta。  
4. **連結固定：** Support · Privacy Policy · Command Line；建議加 Security（`/security/` 目前 404，repo 有 `SECURITY.md`——做靜態頁或連 GitHub Security）。  
5. **可及性：** footer 內包 `<nav aria-label="…">`；目前頁 `aria-current="page"`；Dust 連結保留全站 hover／focus。

## 現況

### 首頁（`footer footer-home`）

```html
<footer class="footer footer-home">
  <a href="/support/">Support</a>
  <a href="/privacy/">Privacy Policy</a>
  <a href="/cli/">Command Line</a>
</footer>
```

- CSS：`.footer-home { margin-top: 20px; border-top: 0; }`（無 hairline）  
- Closing band（`dawn-close`）已有：「Read what your agent wrote.」＋ Coming soon

### 內頁（例 `/support/`）

```html
<footer class="footer">
  <span>Read what your agent wrote.</span>
  <a href="/support/">Support</a>
  <a href="/privacy/">Privacy Policy</a>
  <a href="/cli/">Command Line</a>
  <span>MarsDawn is coming soon to the Mac App Store.</span>
</footer>
```

- 單一 flex wrap：span＋link 混排，窄螢幕易斷讀  
- 與首頁結構不一致

### 參考

以 live `https://marsdawn.southern-light.dev/` 首頁與 `/support/` footer 為準。

## 建議 HTML 骨架

```html
<footer class="footer">
  <nav class="footer-nav" aria-label="Site">
    <a href="/support/">Support</a>
    <a href="/privacy/">Privacy Policy</a>
    <a href="/cli/">Command Line</a>
    <!-- optional: <a href="/security/">Security</a> -->
  </nav>
  <p class="footer-meta">© 2026 MarsDawn</p>
  <!-- 內頁可選：store 狀態一句／chip；首頁可省略（已有 dawn-close） -->
</footer>
```

### CSS 方向

- 保留 `.footer` hairline、`Dust`、`0.9rem`、flex-wrap。  
- 兩列：`.footer-nav` 一列；`.footer-meta` 一列（全寬或較淡）。  
- 首頁可較小 `margin-top`（32–48px），但**不要**去掉 `border-top`。  
- 刪除或改寫 `.footer-home` 使與內頁同一 component。

## 驗證

| 檢查 | 通過條件 |
|------|----------|
| 結構一致 | 首頁與 `/support/` footer DOM 骨架相同 |
| 視覺閉合 | Closing band → hairline → links → meta |
| 響應式 | 320 / 768 / 1280 兩列不打架 |
| 合約路徑 | Privacy／Support 四語路徑穩定 |
| a11y | Tab 順序＝連結順序；nav 有可讀 aria-label；目前頁 aria-current |
| 不做清單 | 無 sitemap 多欄、無社群牆、無 footer 語系、無 waitlist 表單 |

## 刻意不做

- Footer 多欄 sitemap／社群 icon／電子報  
- 複製頂部語系切換  
- 把 brew／waitlist／Pre-Order 主 CTA 沉到 footer  

## 四語標籤（實作時）

| en | zh-Hant | zh-Hans | ja |
|----|---------|---------|-----|
| Support | 支援 | 支持 | サポート |
| Privacy Policy | 隱私權政策 | 隐私政策 | プライバシーポリシー |
| Command Line | 命令列工具 | 命令行工具 | コマンドライン |
| Security（若加） | 安全性 | 安全性 | セキュリティ |

© 文案與 Security 連結目標請與 PRODUCT／法務一致後再鎖。

---

Co-authored delivery note: UX review by 設計審閱 (Grok). Claude：請依本檔實作，完成後可改相關 label／關 issue。
