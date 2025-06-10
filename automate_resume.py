import os
import time
from playwright.sync_api import sync_playwright, TimeoutError

def main():
    JOB_URL = 'https://job-boards.greenhouse.io/tatari/jobs/7944611002'
    RESUME_FILE = '/Users/dorhun/Desktop/Is arama/Resumes/DENEM_ORHUN'

    if not os.path.exists(RESUME_FILE):
        print(f'Resume not found {RESUME_FILE}')

    try:
        playwright = sync_playwright().start()
        browser = playwright.chromium.launch(headless=false)
        page = browser.new_page()
        page.goto(JOB_URL)

        #Click apply
        
    except TimeoutError:
            print(f"Timeout occurred")
    except Exception as e:
            print(f"Exception occurred {e}")
    finally:
            browser.close()
            playwright.stop()





