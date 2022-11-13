# Python Datalib

Useful Python abstractions around the Pandas file Interaction and other common Tasks.

## Gitlab Release

There are 2 Ways to start a release Pipeline:

1. Via gitlab UI
   1. Create new Pipeline in CI View
   2. Supply Variables "`BUMP_TARGET`" [Valid Values](https://python-poetry.org/docs/cli/#version) and optional "`TAG_NOTE`" to add a text to the Git Tag.
   3. Profit
2. Via Git while Pushing
   - Publish a path release: `git push -o ci.variable="BUMP_TARGET=patch"`
   - Major release with release comment `git push -o ci.variable="BUMP_TARGET=patch" -o ci.variable="TAG_NOTE=This is a super cool new version"`