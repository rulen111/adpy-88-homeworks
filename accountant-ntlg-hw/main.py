import rick_roll
import time
from datetime import datetime

from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
	print(f"Current date: {datetime.now()}")
	print(f"\nCounting salary:")
	calculate_salary()
	print(f"\nGetting employees:")
	get_employees()
	print(f"\nLoading...")
	time.sleep(3)
	rick_roll.rickroll()