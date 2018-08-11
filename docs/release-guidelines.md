# ROS Code Guidelines For Releasing

## Prepare for release

### Step 1: Fit for release

1.  To prevent a sudden flood of releases, the [time](https://time.is/UTC) must be between 00:00 on Sunday and 24:00 on Monday (Times are in UTC)
2.  The code must also feature 25+ additions, subtractions or changes since the most recent release.

### Step 2: Release type

If the code is in it's **early stages** ie. the code isn't ready or doesn't work yet then it is considered `alpha`,
If the code is **runnable but isn't quite complete** then it is considered `beta`, and
If the code is in a **stable state** then it is considered `stable`.

### Step 3: What part of the version to increment

Increment the **Major** version when you make incompatible API changes,
Increment the **Minor** version when you add functionality in a backwards-compatible manner, and
Increment the **Patch** version when you make backwards-compatible bug fixes.

### Step 4: Create the release

If a **alpha** version will be released, a descriptive title and description is not required but must contain a short title.
The format for the version number should resemble this example: `2.23.1-alpha`.
If it is the second or more consecutive alpha release then follow this example: `2.23.1-alpha.2`.

If a **beta** version will be released, a descriptive title is required but a description is optional.
The format for the version number should resemble this example: `2.23.1-beta`.
If it is the second or more consecutive alpha release then follow this example: `2.23.1-beta.2`.

If a **stable** version will be released, ensure a suitable title and description is chosen.
The format for the version number should resemble this example: `2.23.1`.

### Step 5: Bump the version in the configuration file

After the release is live, edit the `current_version` section of the `.bumpversion.cfg` file in the root of the repository to match the latest version number.

You could also use the [bumpversion Python CLI](https://github.com/peritus/bumpversion#usage) to do this as well.

### Attribution

*The release guidelines are derived from [Semantic Versioning 2.0](https://semver.org/spec/v2.0.0.html).*

## Automatic releases

A new bleeding edge release is created if all [Continuous Integration](https://travis-ci.org/Richienb/ROS-Code) tests pass.
