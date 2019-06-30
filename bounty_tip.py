import asyncio
from pyppeteer import launch
import re
import random

def generate_name():

	return ('%06x' % random.randrange(16**6)).upper()

def grab_tweets():

	regex_tw = '((?:http|https):\/\/twitter.com\/\w+\/\w+\/\w+)'

	with open('bugs.json', 'r') as bugs:
		content = bugs.read()


	find_tweet = re.findall(regex_tw, content)
	
	return find_tweet


async def main():
	tweet = grab_tweets()
	for t in tweet:
		generate_path = '/home/ubuntu/bounty_tip/'+ generate_name() + '.png'	
		browser = await launch()
		page = await browser.newPage()
		await page.goto(t)
		await page.screenshot({'path': generate_path,'fullPage': 'true'})
		await browser.close()

asyncio.get_event_loop().run_until_complete(main())
