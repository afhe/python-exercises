import re

html_text = '''<div>
    <span class="actionBar__text"> 
        Showing 18 of 101 products.
    </span>
</div>
'''

print(html_text)

pattern = r'Showing (\d+) of (\d+) products.'

if matches := re.findall(pattern, html_text):
    total_amount = matches[0][1]
    print(f"Total amount of products is {total_amount}")
else:
    print("")
