#!/bin/bash

set -e

# test simple get, should be empty
echo "OLD DB CONTENTS:"
curl -X GET http://localhost:5000/api/timeline_post
echo "-----------------------------"

# now post, then verify db with get
echo "NEW TIMELINE-POST:"
curl -X POST http://localhost:5000/api/timeline_post -d \
    'name=Perry&email=perry@example.com&content=Testing first post!'

# fetch posts again
RESPONSE=$(curl -s http://localhost:5000/api/timeline_post)

# extract fields from the most recent post
LAST_NAME=$(echo "$RESPONSE" | jq -r '.timeline_posts[-1].name')
LAST_EMAIL=$(echo "$RESPONSE" | jq -r '.timeline_posts[-1].email')
LAST_CONTENT=$(echo "$RESPONSE" | jq -r '.timeline_posts[-1].content')

# validate content
if [[ "$LAST_NAME" == "Perry" && "$LAST_EMAIL" == "perry@example.com" && "$LAST_CONTENT" == "Testing first post!" ]]; then
    echo "--- POST and GET behavior validated. ---"
else
    echo "--- Validation failed. ---"
    echo "Expected: Perry, perry@example.com, Testing first post!"
    echo "Got: $LAST_NAME, $LAST_EMAIL, $LAST_CONTENT"
    exit 1
fi
