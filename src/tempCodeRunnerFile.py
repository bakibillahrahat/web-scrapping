    company_name = job.find('h3', class_= 'joblist-comp-name').text.strip()
    skills = job.find('span', class_ = 'srp-skills').text.strip()
    published_date = job.find('span', class_ = 'sim-posted').text.strip()