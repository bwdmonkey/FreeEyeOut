set -e
echo "Running live crawler tests..."
cd scraper && scrapy crawl course_spider
echo "Test complete."
set +e