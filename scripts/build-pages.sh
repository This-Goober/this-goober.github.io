#!/bin/sh
set -eu

cd "$(dirname "$0")/.."

# Publish only the profile. The repository also contains unrelated documents.
output=dist/profile
mkdir -p "$output/profile-assets"
sed 's|https://this-goober.github.io/|https://eideelaurel.com/|g' index.html > "$output/index.html"
cp 404.html profile.css "$output/"
cp profile-assets/* "$output/profile-assets/"
