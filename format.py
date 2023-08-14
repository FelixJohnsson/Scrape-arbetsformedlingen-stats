import json

def format_jobs(text):
    # Split the text by 'Page'
    pages = text.split('Page')

    jobs = []

    for page in pages:
        lines = page.strip().split('\n')
        
        # Find the index of the line that contains the URL
        url_index = next((i for i, line in enumerate(lines) if line.startswith('/platsbanken/annonser/')), None)
        
        if url_index is not None:
            title = lines[url_index - 2].split('(')[0].strip()
            
            company = lines[url_index - 1]

            
            url = lines[url_index]
            job = {
                "title": title,
                "company": company.strip(),
                "location": 'Stockholm',
                "url": url
            }
            jobs.append(job)

    return jobs


with open('jobs.txt', 'r', encoding='utf-8') as f:
    text = f.read()

formatted_jobs = format_jobs(text)
with open('jobs.json', 'w', encoding='utf-8') as f:
    json.dump(formatted_jobs, f, ensure_ascii=False, indent=4)