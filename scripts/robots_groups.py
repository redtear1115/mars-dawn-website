#!/usr/bin/env python3
"""Resolve the effective directives for a set of bots against a robots.txt,
per RFC 9309 group semantics: a record is one or more consecutive
User-agent lines followed by the rules that apply to all of them. A bot
uses the most specific group whose user-agent it matches case-insensitively
(exact product-token match here, which is all this file needs), or the `*`
group if none matches.
"""
import sys
from pathlib import Path


def parse_groups(text: str):
    groups = []  # list of (set-of-agents-lower, list-of-(directive, value))
    current_agents = None
    current_rules = None
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip().lower()
        value = value.strip()
        if key == "user-agent":
            if current_agents is not None and current_rules:
                # Already collected rules under this agent set -> new group.
                groups.append((current_agents, current_rules))
                current_agents, current_rules = None, None
            if current_agents is None:
                current_agents = set()
                current_rules = []
            current_agents.add(value.lower())
        elif key == "sitemap":
            continue
        else:
            if current_agents is not None:
                if current_rules is None:
                    current_rules = []
                current_rules.append((key, value))
    if current_agents is not None:
        groups.append((current_agents, current_rules or []))
    return groups


def effective_group(groups, bot: str):
    bot_l = bot.lower()
    for agents, rules in groups:
        if bot_l in agents and "*" not in agents:
            return rules
    for agents, rules in groups:
        if "*" in agents:
            return rules
    return []


def main(argv):
    if len(argv) < 2:
        print("usage: robots_groups.py <robots.txt> [bot ...]", file=sys.stderr)
        return 2
    path = Path(argv[1])
    bots = argv[2:] or [
        "GPTBot", "ChatGPT-User", "OAI-SearchBot",
        "ClaudeBot", "Claude-User", "Claude-SearchBot",
        "PerplexityBot", "*", "Googlebot",
    ]
    text = path.read_text(encoding="utf-8")
    groups = parse_groups(text)
    print(f"# {path}")
    for bot in bots:
        rules = effective_group(groups, bot)
        rendered = "; ".join(f"{k}: {v}" for k, v in rules) if rules else "(no rules)"
        print(f"{bot:<20} -> {rendered}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
