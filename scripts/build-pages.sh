#!/bin/sh
set -eu

cd "$(dirname "$0")/.."

# Publish only the profile. The repository also contains unrelated documents.
output=dist/profile
rm -rf "$output"
mkdir -p "$output/profile-assets"
cp index.html 404.html profile.css "$output/"
cp profile-assets/* "$output/profile-assets/"
