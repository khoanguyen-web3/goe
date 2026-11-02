from playwright.sync_api import sync_playwright
import sys
with sync_playwright() as p:
  b=p.chromium.launch(executable_path='/usr/bin/google-chrome')
  for n in ['index','about','ledger','activities','blog','article']:
    pg=b.new_page(viewport={'width':1440,'height':900});pg.goto(f'file:///workspace/goe_landing/v2/{n}.html');pg.wait_for_timeout(1500)
    pg.screenshot(path=f'shots/{n}.png',full_page=True)
  pg=b.new_page(viewport={'width':1440,'height':900});pg.goto('file:///workspace/goe_landing/v2/index.html');pg.wait_for_timeout(800);pg.click('button.lang');pg.goto('file:///workspace/goe_landing/v2/about.html');pg.wait_for_timeout(1200);pg.screenshot(path='shots/about_en_top.png')
  pg.goto('file:///workspace/goe_landing/v2/activities.html');pg.wait_for_timeout(800);pg.click('#fl button[data-k=vifc]');pg.screenshot(path='shots/activities_filter.png',full_page=True)
