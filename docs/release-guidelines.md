# ROS Code Guidelines For Releasing

## Prepare For Release

### Step 1: Fit For Release

The following guidelines must be satisfied in order to proceed to step 2

1. The time must be between 00:00 on Sunday and 24:00 on Monday (Times are in GMT +0)
1. The code must feature 25+ additions, subtractions or changes since the most recent release.

### Step 2: Release or Pre-release

The following requirements must be met for the release to be considered `Stable`

1. The continuous integration build is passing
1. The current code is in a state where it is functional

If the requirements were not met, unless in doubt the release should be a pre-release

Other checks **do not** have to pass (for example: CodeFactor) for the release to be considered `stable`

## Further Guidelines

### Versioning Conventions

The versioning conventions closely follow [Semantic Versioning 2.0](https://semver.org/spec/v2.0.0.html)

- **Major** version when you make incompatible API changes,
- **Minor** version when you add functionality in a backwards-compatible manner, and
- **Patch** version when you make backwards-compatible bug fixes.

#### Release

Increment the version as described below

Examples of release versions:

- 2.0.0
- 2.13.9
- 2.65.87

#### Pre-Release

Increment the version as described below

Examples of release versions:

- 2.0.0-pre1
- 2.13.9-pre24
- 2.65.87-pre36

The numbers after `pre` signify the prerelease revision
