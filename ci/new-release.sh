CUR_VER=git tag | tail -1
NEW_VER=`python $TRAVIS_BUILD_DIR/ci/generate_version.py $CUR_VER`
curl -v -i -X POST -H "Content-Type:application/json" -H "Authorization: $github_token" https://api.github.com/repos/Richienb/ROS-Code/releases -d '{"tag_name":"$NEW_VER","target_commitish": "develop","name": "$NEW_VER Automated Release","body": "Description of the release","draft": false,"prerelease": true}'
