import re

data = """
TELEPHONE, ELECTRONIC
abcd
Company: hi (jk), . l
tytererw
(a) hsdjkhdjsad ("aaaaaaaaaa")
(b) asdasdwew ("bbbbbbbbbbb")
(c) ttttttttt ("cccccccc")
where:
(i) ttttttttt ("cccccccc")
"""

page_search_sent = 'TELEPHONE, ELECTRONIC'
company_pattern = re.compile(r'^Company:\s+(.*)$', re.IGNORECASE)
inst_line_pattern = re.compile(r"^\(([A-H]{1})\).+\((.*)\)", re.IGNORECASE)
inst_pattern = re.compile(r'\((.*?)\)')

if page_search_sent in data:
  for line in data.splitlines():
    inst_line_match = re.search(inst_line_pattern, line)
    company_match = re.findall(company_pattern, line)
    if inst_line_match:
      print(f'Instruction: {re.findall(inst_pattern, line)[1]}')
    elif company_match:
      print(f'Company Name: {company_match[0]}')
