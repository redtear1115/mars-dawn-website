# #70 handoff: website analytics, in the privacy policy

Grok's copy for [mars-dawn-website#70](https://github.com/redtear1115/mars-dawn-website/issues/70). The four sections are in `70-analytics-copy.md`. This file is how to land them. It is not the page.

## What is true, and what is not decided

The policy on main says the whole product has no analytics. That sentence becomes false the day the Worker sends events, and website-plan §5.4 forbids switching analytics on before the policy is deployed. The section does not exist yet, so this is an addition near the top, not a move of an existing heading.

Decided, and already in the copy:

- The app still collects nothing. That is the App Store answer, and it must stay a different section from the website.
- Server-side PostHog only. No cookie, no local storage, no script in the page. The browser never talks to PostHog.
- Recorded: a page view, the referrer when the browser sends one, and a click that leaves through a redirect on this site.
- Not recorded: documents, anything typed, an account, cross-site ads, a profile, and every request under `/themes/` (option A, so the app's "Data Not Collected" answer stays).
- A visit is one page view. Each request gets a new random id that is not reused. This is the stricter of the two open choices in website-plan §7. The other choice, a daily hash of IP and User-Agent, is personal data and needs different copy. It is not what this draft says.
- The full IP address is not forwarded to PostHog. Cloudflare still sees it as the host, which the policy should say in its own bullet.

Not decided. The copy has two slots. Do not deploy while either still contains the braces.

| Slot | Fills with | Grammar |
|---|---|---|
| `{{POSTHOG_REGION}}` | `EU` or `US` | en: "the EU region". zh-Hant: 「歐盟區」or「美國區」. zh-Hans: 「欧盟区」or「美国区」. ja: 「EU リージョン」or「米国リージョン」. |
| `{{RETENTION}}` | a duration the owner names | en: "13 months" so the sentence reads "for 13 months". zh-Hant / zh-Hans: 「13 個月」. ja: the sentence is already 「保持期間は {{RETENTION}} です。」, so fill 「13か月」. |

Grok does not pick the region or the duration. website-plan §7 still lists both as open. A recommendation, if one is wanted: EU, and a retention the owner can say out loud. Neither goes into the page until the owner writes it down.

## Where it goes

In each of `public/privacy/index.md`, `public/zh-hant/privacy/index.md`, `public/zh-hans/privacy/index.md`, `public/ja/privacy/index.md`:

1. Replace the bold opening paragraph with the one in the copy file. The old paragraph says there is no analytics at all. Leaving it makes the new section a contradiction.
2. Insert the new `##` section immediately after that paragraph, before "What stays on your Mac" and its three translations.
3. Replace the one-sentence Children / 兒童 / 儿童 / 子ども paragraph with the one in the copy file. The old sentence says MarsDawn collects data from no one, which will not be true of the website.

Set the "last updated" line, and `UPDATED` in `scripts/build_pages.py`, to the day this deploys. The four locales change together.

## The paragraph that gets deleted later

Each locale has a short paragraph beginning with the equivalent of "This is not on yet." It is the only sentence that describes today's behaviour. The day the Worker actually sends events, delete that paragraph and leave the list. Deleting it earlier publishes a claim the site does not yet do. Leaving it after the switch publishes the opposite falsehood.

Do not turn analytics on in the same change as the first deploy of this copy. Policy first, then the Worker, which is the order §5.4 already fixed. D1b stays a separate change.

## Voice

Same as the rest of the policy. Short sentences, no exclamation, no "we take your privacy seriously". Chinese uses full-width punctuation. Japanese is です・ます. zh-Hans keeps the page's own words (数据, 账户, 文稿, 追踪), not a character-swap of the zh-Hant.

Co-authored-by: Grok <grok@southern-light.dev>
