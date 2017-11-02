import scrapy
from free_scraper.items import SectionItem, CourseItem

"""
Sourced from the ubclaunchpad/sleuth project by @bobheadxi
https://github.com/ubclaunchpad/sleuth
"""

BASE_URL = "https://courses.students.ubc.ca"

def parse_subjects(response):
    """
    Scrape for Courses.
    Iterates through Subjects in this page.
    Passes to parse_course, parse_course_details
    """
    rows = response.xpath('//tbody/tr')
    for row in rows:
        next_rel_url = extract_element(row.xpath('./td/a/@href'), 0)
        if len(next_rel_url) > 1:
            next_url = BASE_URL + next_rel_url
            title = extract_element(row.xpath('./td[2]/text()'), 0)
            code = extract_element(row.xpath('./td/a/text()'), 0)
            subject = {
                "url": next_url,
                "name": code+" "+title.strip(),
                "faculty": utils.extract_element(row.xpath('./td[3]/text()'),0)
            }

            yield scrapy.Request(
                next_url,
                callback=parse_course,
                meta={'data':subject}
            )

def parse_course(response):
    """
    Parse subjct page.
    Iterates through the Courses on this page.
    """
    subject = response.meta['data']
    rows = response.xpath('//tbody/tr')
    for row in rows:
        next_rel_url = extract_element(row.xpath('./td/a/@href'), 0)
        course_code = extract_element(row.xpath('./td/a/text()'), 0)
        course_title = extract_element(row.xpath('./td[2]/text()'), 0)
        course_name = course_code+" "+course_title
        if len(next_rel_url) > 1:
            next_url = BASE_URL + next_rel_url
            course = CourseItem(
                subject=subject,
                url=next_url,
                name=course_name,
            )
            yield scrapy.Request(
                next_url,
                callback=parse_course_details,
                meta={'data':course}
            )

def parse_course_details(response):
    """
    Parse course details page.
    """
    course = response.meta['data']
    course['description'] = utils.extract_element(response.xpath('//p/text()'), 0).strip()
    # TODO: List of sections into course[sections], maybe parse as well
    rows = response.xpath("//table")[1].xpath("//tr") # Includes the header as well
    rows.pop(0); # Get rid of the headers
    for row in rows:
        course_status = extract_element(row.xpath("./td/text()"), 0)
        course_section = extract_element(row.xpath("./td/a/text()"),0)
        course_section_url = extract_element(row.xpath("./td/a/@href"), 0)
        activity_type = extract_element(row.xpath("./td/text()"), 3)
        if len(course_section_url) > 1:
            next_url = BASE_URL + course_section_url
            section = SectionItem(
                status = course_status
                section = scrapy.Field()
                url = course_section_url
                activity = activity_type
            )
            yield scrapy.Request(
                course_section_url,
                callback=parse_section_details,
                meta={'data': section}
            )
            
    return course

def parse_section_details(response):
    """
    Parse course details page.
    """
    section = response.meta['data']
    section['description'] = utils.extract_element(response.xpath('//p/text()'), 0).strip()
    # TODO: List of sections into course[sections], maybe parse as well
    tbl = response.xpath("//table")[3].xpath("tr")[0] # Includes the header as well
    total_remaining = extract_element(tbl.xpath("//td//strong/text()"), 0)
    currently_registered = extract_element(tbl.xpath("//td//strong/text()"), 1)
    general_remaining = extract_element(tbl.xpath("//td//strong/text()"), 2)
    restricted_remaining = extract_element(tbl.xpath("//td//strong/text()"), 3)

    # what do i do now? lol
    # return course


# Separate Method for extraction
def _extract_element(item_list, index):
    """
    Safely extract indexed xpath element
    """
    if index < len(item_list):
        return item_list[index].extract().strip()
    else:
        return ""