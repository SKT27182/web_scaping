#!/usr/bin/env python3

import requests
import bs4
import sys

no_of_results = sys.argv[1]
comp = sys.argv[2]
no_of_results = int(no_of_results)
page_no =no_of_results//10
#base_url = "https://github.com/search?o=desc&p={}&q=google&s=forks&type=Repositories"
base_url = "https://github.com/search?o=desc&p={}&q=org%3A{}&s=forks&type=Repositories"
count = 1
for page in range(1,page_no+2):

		i =2
		request = requests.get(base_url.format(page,comp))
		soup = bs4.BeautifulSoup(request.text,'lxml')

		get_forks = soup.select('.repo-list-item.hx_hit-repo.d-flex.flex-justify-start.py-4.public.source')


		for fork in get_forks:
			name = fork.select('.v-align-middle')[0].getText()
			about = soup.select('.mb-1')[i].getText().strip()
			print(name)
			print(about)
			print('\n')
			if count == no_of_results:
				exit(1)
			else:
				count=count+1
				i=i+1
