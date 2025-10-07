Password Guesser Game

https://www.youtube.com/watch?v=oM06fx9bvBQ

This command-line puzzle turns password creation into a playful challenge. Each guess you type is checked using a set of rules that mix classic security hints with logic riddles, trivia, and a bit of astronomy. After every attempt, the game lists exactly which rules you failed, so you can iterate strategically until you land on a winning “password” that satisfies everything at once.

What you’re up against:

Your password must be at least five characters, include a number, contain an uppercase letter, and include a special (non-alphanumeric) character. That’s the warm-up. To really win, your guess also needs (1) digits that sum to 25, (2) a month name somewhere inside (e.g., “January”), (3) at least one Roman numeral character (I, V, X, L, C, D, M), (4) the current moon phase as an emoji (🌑 🌒 🌓 🌔 🌕 🌖 🌗 🌘, computed for today), (5) a four-digit year (the on-screen rule text says “divisible by 7”), and (6) a palindrome word (any substring of length ≥ 2 that reads the same forwards and backwards). Each rule is independent; your job is to craft a single string that satisfies them all simultaneously.

How it works:

The game loops until all checks pass.

It reports failed rules after each try, plus echoes your last attempt for quick iteration.

Moon phase is computed using astral.moon.phase(date.today()) and mapped to the correct emoji for today.

Palindromes are detected across all substrings, case-insensitive.

Why it’s fun:

You’ll balance arithmetic (digit sum = 25), vocabulary (months), pattern spotting (palindromes), and timing (moon phase changes daily). The constraints interact in surprising ways, so small edits can fix multiple failures at once.
