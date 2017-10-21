set -e
find . -name \*.pyc -delete
echo "Running live crawler tests..."
cd scraper && scrapy crawl course_spider
echo "Test complete."
set +e