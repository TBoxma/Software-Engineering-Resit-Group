import click

from src.frontend.cli_functions.function import Function
from src.backend.api.reports_api import ReportsApi
from datetime import datetime
from datetime import date

class Report(Function):
    reports_ = [
        "Total time",
        "Total time by categories",
        "Total time by tasks",
        "Percentage of total time by categories",
        "Percentage of total time by tasks"
    ]

    def report(self) -> None:
        click.echo("Available reports:")
        for idx, report in enumerate(self.reports_, start=1):
            click.echo(f"{idx}. {report}")

        user_input = click.prompt("Enter a number to execute a report", type=str)
        
        try:
            selected_report_idx = int(user_input)
            if 1 <= selected_report_idx <= len(self.reports_):
                selected_report = self.reports_[selected_report_idx - 1]
                click.echo(f"Executing: {selected_report}")
                
                date_from = click.prompt("Enter start date (yyyy-mm-dd)", type=str)
                date_to = click.prompt("Enter end date (yyyy-mm-dd)", type=str)
                
                self.execute_specific_report(selected_report_idx, date_from, date_to)
                
            else:
                click.echo("Invalid number. Please select a valid report number.")
        except ValueError:
            click.echo("Invalid input. Please enter a number.")
    
    def execute_specific_report(self, report_num: int, date_from: str, date_to: str):
        start = datetime.strptime(date_from, "%Y-%m-%d").date()
        end = datetime.strptime(date_to, "%Y-%m-%d").date()

        match report_num:
            case 1:
                total_time = ReportsApi.report_total_time(start, end)
                print()
                print(f"Total time spent on tasks from {date_from} to {date_to}: {total_time}")
            case 2:
                categories = click.prompt("Enter a list of categories (comma-separated)", type=str)
                categories_list = [category.strip() for category in categories.split(',')]
                total_time_cats = ReportsApi.report_total_time_categories(start, end, categories_list)

                print()
                print(f"Total time spent on specified categories from {date_from} to {date_to} is displayed below:")
                print()
                for category in total_time_cats:
                    print(f"{category}: {total_time_cats[category]}")
            case 3:
                tasks = click.prompt("Enter a list of tasks (comma-separated)", type=str)
                tasks_list = [task.strip() for task in tasks.split(',')]

                total_time_tasks = ReportsApi.report_total_time_tasks(start, end, tasks_list)

                print()
                print(f"Total time spent on specified tasks from {date_from} to {date_to} is displayed below:")
                print()
                for task in total_time_tasks:
                    print(f"{task}: {total_time_tasks[task]}")
            case 4:
                categories = click.prompt("Enter a list of categories (comma-separated)", type=str)
                categories_list = [category.strip() for category in categories.split(',')]
                total_time_cats = ReportsApi.report_percentage_categories(start, end, categories_list)

                print()
                print(f"Percentage of total time spent on specified categories from {date_from} to {date_to} is displayed below:")
                print()
                for category in total_time_cats:
                    print(f"{category}: {total_time_cats[category]}%")
            case 5:
                tasks = click.prompt("Enter a list of tasks (comma-separated)", type=str)
                tasks_list = [task.strip() for task in tasks.split(',')]

                total_time_tasks = ReportsApi.report_percentage_tasks(start, end, tasks_list)
                print()
                print(f"Percentage of total time spent on specified tasks from {date_from} to {date_to} is displayed below:")
                print()
                for task in total_time_tasks:
                    print(f"{task}: {total_time_tasks[task]}%")
            case _:
                click.echo("Invalid report number.")

    def execute(self, args:[str] = []) -> None:
        self.report()