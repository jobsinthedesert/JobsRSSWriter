def remove_newline(item):
    clean_line = item.replace('\n', '')

    return clean_line


def format_element(job, opening_tag, closing_tag):
    """
    Formats <link> and <title> elements
    """
    return('    '+opening_tag+job+closing_tag+'\n')

def format_item(title, link):
    """
    Joins <title> and <link> elements as children of <item>
    """
    return('  <item>\n'+title+link+'  </item>\n')

def sanitize_title(title):
    """
    Alters forbidden chracters in XML
    """
    clean_amp = title.replace('&', '&amp;')
    clean_quot = clean_amp.replace('"', '&quot;')
    clean_apos = clean_quot.replace('\'', '&apos;')
    clean_lt = clean_apos.replace('<', '&lt;')
    clean_gt = clean_lt.replace('>', '&gt;')

    clean_title = clean_gt

    return clean_title

def format_jobs(jobs):
    """
    Concatenates a string to return a list of jobs as <item> elems
    """

    job_item_string = ''

    for job in jobs:
        job_name = sanitize_title(job[1])
        title = format_element(job_name, '<title>', '</title>')
        link_parsed = sanitize_title(job[0])
        link = format_element(link_parsed, '<link>', '</link>')
        item = format_item(title, link)
        job_item_string += item

    return job_item_string

def format_rss(jobs, title, link):
    """
    Returns an RSS feed as a string
    """
    xml_opening = '<?xml version="1.0" encoding="UTF-8" ?>\n'
    rss_opening = '<rss version="2.0">\n\n'
    channel_opening = '<channel>\n'
    
    channel_title = '  <title>'+title+'</title>\n'
    channel_link = '  <link>'+link+'</link>\n'

    header = xml_opening + rss_opening + channel_opening + channel_title + channel_link

    job_items = format_jobs(jobs)

    channel_closing = '</channel>\n'
    rss_closing = '</rss>'

    closing = channel_closing + rss_closing

    rss_feed = header + job_items + closing

    return rss_feed