#!/bin/sh

curl -X POST -u elastic:fIwigNlyIKXpqEvbJCjx6B3O "https://i-o-optimized-deployment-601c98.es.eastus2.azure.elastic-cloud.com:9243/cs172-index/_bulk" -H "Content-Type: application/x-ndjson" --data-binary @data.json > /dev/null 2>&1

curl --http1.1 -X GET -u elastic:fIwigNlyIKXpqEvbJCjx6B3O "https://i-o-optimized-deployment-601c98.es.eastus2.azure.elastic-cloud.com:9243/cs172-index/_search?pretty" -H "Content-Type: application/json" -d"{\"query\": {\"match\": {\"html\": \"$1\"}}}" > $2
echo "Output results to $2"