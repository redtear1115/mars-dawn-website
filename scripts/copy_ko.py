"""Korean copy for the MarsDawn site: a skeleton, every value empty (website #162).

build(k) returns what copy_ja.py's does, plus "tables": the tables zh-Hans and ja keep in
build_pages.py (see build_pages.locale_tables). Translate every value from the en copy in
build_pages.py, keep every key and every list's length, and keep what is code, a command, a URL or
a placeholder ({langs}, {root}, {mcp}, {a}, {u}, {b}, {file}) as it is in en.
Structure is checked by `python3 scripts/new_locale.py --check`; the build also refuses a locale
that says COMPLETE = True with a key missing or a string empty, and says which.

The privacy and support pages are rendered from content/legal/<slug>.ko.md
(scripts/render_legal.py, on a Mac): their "body" here is k.render_legal_body(slug, "ko"), their
title and description are written here. Also needed before COMPLETE: the hero window snapshot
(scripts/sync_hero_sources.py), and public/assets/templates/<case>-ko.png and
public/assets/cli/plan-ko.png.
"""

# Set to True only when everything below is translated. Until then ko is not built, linked,
# in a sitemap, or anywhere else on the site.
COMPLETE = False


def build(k) -> dict:
    return {
        'ui': {
            'home': '',
            'privacy': '',
            'support': '',
            'cli': '',
            'agents': '',
            'using_cli': '',
            'markdown-to-pdf': '',
            'skill': '',
            'view-markdown-on-mac': '',
            'vs-macmd-viewer': '',
            'updated': '',
            'tagline': '',
            'slogan': '',
            'footer_store': '',
            'footer_nav': '',
            'more': '',
            'yours': '',
            'pay-once': '',
            'pdf': '',
            'native': '',
            'limits': '',
            'mcp': '',
            'token-efficient-review': '',
            'vs-markdown-preview-tools': '',
            'themes': '',
            'sharing-exported-pdfs': '',
            'reviewing-ai-output': '',
            'reading-agent-output': '',
            'agent-transparency': '',
            'reviewing-agent-plans': '',
            'agent-design-patterns': '',
            'changelog': '',
            'consent_text': '',
            'consent_accept': '',
            'consent_decline': '',
            'consent_aria': '',
            'cookie_settings': '',
            'view_markdown_source': '',
        },
        'store_chip': '',
        'schema_notes': {
            'export': '',
            'open': '',
            'open_v2': '',
            'error': '',
            'open_v1': '',
            'error_v1': '',
        },
        'example_plan': '',
        'trait_link': {
            'yours': ['', ''],
            'pay-once': ['', ''],
            'pdf': ['', ''],
            'native': ['', ''],
            'limits': ['', ''],
        },
        'trait_nav_heading': '',
        'figure_list_label': '',
        'figures': {
            'index': {
                'alt': '',
                'callouts': [],
            },
            'yours': {
                'alt': '',
                'callouts': ['', ''],
            },
            'pay-once': {
                'alt': '',
                'callouts': ['', '', '', ''],
            },
            'pdf': {
                'alt': '',
                'callouts': ['', ''],
            },
            'native': {
                'alt': '',
                'callouts': ['', '', '', ''],
            },
            'limits': {
                'alt': '',
                'callouts': ['', '', '', ''],
            },
        },
        'pages': {
            'index': {
                'title': '',
                'description': '',
                'body': '',
                'intro': '',
            },
            'privacy': {
                'title': '',
                'description': '',
                'body': '',
            },
            'support': {
                'title': '',
                'description': '',
                'body': '',
            },
            'cli': {
                'title': '',
                'description': '',
                'body': '',
            },
            'cli/agents': {
                'title': '',
                'description': '',
                'body': '',
            },
            'markdown-to-pdf': {
                'title': '',
                'description': '',
                'body': '',
            },
            'view-markdown-on-mac': {
                'title': '',
                'description': '',
                'body': '',
            },
            'vs/macmd-viewer': {
                'title': '',
                'description': '',
                'body': '',
            },
            'cli/skill': {
                'title': '',
                'description': '',
                'body': '',
            },
            'yours': {
                'title': '',
                'description': '',
                'body': '',
                'intro': '',
            },
            'pay-once': {
                'title': '',
                'description': '',
                'body': '',
                'intro': '',
            },
            'pdf': {
                'title': '',
                'description': '',
                'body': '',
                'intro': '',
            },
            'native': {
                'title': '',
                'description': '',
                'body': '',
                'intro': '',
            },
            'limits': {
                'title': '',
                'description': '',
                'body': '',
                'intro': '',
            },
            'cli/mcp': {
                'title': '',
                'description': '',
                'body': '',
            },
            'token-efficient-review': {
                'title': '',
                'description': '',
                'body': '',
            },
            'vs/markdown-preview-tools': {
                'title': '',
                'description': '',
                'body': '',
            },
            'themes': {
                'title': '',
                'description': '',
                'body': '',
            },
            'sharing-exported-pdfs': {
                'title': '',
                'description': '',
                'body': '',
            },
            'reviewing-ai-output': {
                'title': '',
                'description': '',
                'body': '',
            },
            'reading-agent-output': {
                'title': '',
                'description': '',
                'body': '',
            },
            'agent-transparency': {
                'title': '',
                'description': '',
                'body': '',
            },
            'reviewing-agent-plans': {
                'title': '',
                'description': '',
                'body': '',
            },
            'agent-design-patterns': {
                'title': '',
                'description': '',
                'body': '',
            },
            'changelog': {
                'title': '',
                'description': '',
                'body': '',
            },
        },
        'tables': {
            'app_ui_languages': '',
            'home': {
                'cta_cli': '',
                'cta_store': '',
                'install_h': '',
                'install_lede': '',
                'install_caps': ['', '', ''],
                'proof_h': '',
            },
            'compare': {
                'macmd-features': {
                    'head': ['', '', ''],
                    'rows': [
                        ['', '', ''],
                        ['', '', ''],
                        ['', '', ''],
                        ['', '', ''],
                        ['', '', ''],
                        ['', '', ''],
                        ['', '', ''],
                    ],
                },
                'macmd-buying': {
                    'head': ['', '', ''],
                    'rows': [
                        ['', '', ''],
                        ['', '', ''],
                        ['', '', ''],
                        ['', '', ''],
                        ['', '', ''],
                    ],
                },
                'preview-tools': {
                    'head': ['', '', '', '', ''],
                    'rows': [
                        ['', '', '', '', ''],
                        ['', '', '', '', ''],
                        ['', '', '', '', ''],
                        ['', '', '', '', ''],
                    ],
                },
                'pay-once-states': {
                    'head': ['', '', '', ''],
                    'rows': [
                        ['', '', '', ''],
                        ['', '', '', ''],
                        ['', '', '', ''],
                        ['', '', '', ''],
                        ['', '', '', ''],
                        ['', '', '', ''],
                        ['', '', '', ''],
                        ['', '', '', ''],
                    ],
                },
                'mcp-choice': {
                    'head': ['', '', ''],
                    'rows': [
                        ['', '', ''],
                        ['', '', ''],
                        ['', '', ''],
                    ],
                },
            },
            'exit_table_head': ['', '', ''],
            'exit_remedy': {
                '0': '',
                '2': '',
                '3': '',
                '4': '',
                '5': '',
                '64': '',
            },
            'theme_shots': {
                '01-split': {
                    'name': '',
                    'alt': '',
                },
                '02-classic': {
                    'name': '',
                    'alt': '',
                },
                '04-vivid': {
                    'name': '',
                    'alt': '',
                },
                '03-dark': {
                    'name': '',
                    'alt': '',
                },
            },
            'theme_gallery_note': '',
            'skip_label': '',
            'toc_label': {
                'privacy': '',
                'support': '',
            },
            'not_found': {
                'title': '',
                'headline': '',
                'body': '',
                'home': '',
                'alt': '',
            },
            'hero_window_label': '',
            'hero_window_markdown': {
                'template': '',
                'sep': '',
            },
            'loop': {
                'outline': '',
                'files': '',
                'title': '',
                'sections': [
                    ['', ''],
                    ['', ''],
                    ['', ''],
                ],
                'old': '',
                'new': '',
                'ask': '',
                'reply': '',
                'alt': '',
                'pause': '',
                'pause_short': '',
            },
            'templates': {
                'ui_labels': {
                    'templates': '',
                    'templates-spec': '',
                    'templates-flowchart': '',
                    'templates-meeting-notes': '',
                },
                'labels': {
                    'template': '',
                    'download': '',
                    'looks': '',
                    'ask': '',
                    'share': '',
                    'doesnt': '',
                    'faq': '',
                    'more': '',
                    'sep': '',
                    'img_alt': '',
                },
                'hub': {
                    'title': '',
                    'description': '',
                    'h1': '',
                    'lede': '',
                    'items': {
                        'spec': ['', ''],
                        'flowchart': ['', ''],
                        'meeting-notes': ['', ''],
                    },
                },
                'pages': {
                    'spec': {
                        'title': '',
                        'description': '',
                        'h1': '',
                        'lede': '',
                        'caption': '',
                        'prompt': '',
                        'share': '',
                        'doesnt': '',
                        'faq': [
                            ['', ''],
                            ['', ''],
                        ],
                    },
                    'flowchart': {
                        'title': '',
                        'description': '',
                        'h1': '',
                        'lede': '',
                        'caption': '',
                        'prompt': '',
                        'share': '',
                        'doesnt': '',
                        'faq': [
                            ['', ''],
                            ['', ''],
                        ],
                    },
                    'meeting-notes': {
                        'title': '',
                        'description': '',
                        'h1': '',
                        'lede': '',
                        'caption': '',
                        'prompt': '',
                        'share': '',
                        'doesnt': '',
                        'faq': [
                            ['', ''],
                            ['', ''],
                        ],
                    },
                },
                'templates': {
                    'spec': '',
                    'flowchart': '',
                    'meeting-notes': '',
                },
                'scene_text': {
                    'spec': {
                        'title': '',
                        'req': '',
                        'flow': '',
                        'acc': '',
                        'r1': '',
                        'r2': '',
                        'r3': '',
                        'n1': '',
                        'n2': '',
                        'n3': '',
                        'n4': '',
                        'a1': '',
                        'a3': '',
                        'ask': '',
                        'reply': '',
                        'alt': '',
                    },
                    'flowchart': {
                        'title': '',
                        'diagram': '',
                        'steps': '',
                        'n1': '',
                        'n2': '',
                        'n3': '',
                        'n4': '',
                        's1': '',
                        's2': '',
                        's3': '',
                        's4': '',
                        'ask': '',
                        'reply': '',
                        'alt': '',
                    },
                    'meeting-notes': {
                        'title': '',
                        'decisions': '',
                        'actions': '',
                        'd1': '',
                        'd2': '',
                        't1': '',
                        't2': '',
                        't3': '',
                        'ask': '',
                        'reply': '',
                        'alt': '',
                    },
                },
            },
        },
    }
