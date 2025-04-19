# lab3_code-refactor - Tennis Game

## Overview
This repository contains refactored implementations of a tennis scoring system, originally developed as part of a Programming Practices course. The goal was to improve code quality by applying various refactoring techniques while maintaining all existing functionality.

### TennisGame1
#### Improvements:
- Added `SCORE_NAMES` constant for score translations
- Split `score()` into 3 helper methods:
  - `_even_score()`
  - `_advantage_or_win()` 
  - `_regular_score()`
- Better variable names (`p1_points` instead of `p1points`)

### TennisGame2
#### Improvements:
- Score dictionary replaces conditionals
- Simplified logic
- Removed redundant loops
- Fixed hardcoded player names

### TennisGame3  
#### Improvements:
- Game phase detection (`_is_early_game()`)
- Separate scoring methods
- Clearer variable names
