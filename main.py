import datetime
import time
import tkinter as tk
from typing import Union


class DataCleaning:
    def clean_data(self, data: str) -> str:
        cleaned_data = data.replace('dirty', '')
        return cleaned_data


class DataNormalizing:
    def normalize_data(self, data: str) -> str:
        normalized_data = data.lower()
        return normalized_data


class DataProcessing:
    def __init__(self):
        self.data_cleaning = DataCleaning()
        self.data_normalizing = DataNormalizing()

    def preprocess_data(self, data: str) -> str:
        cleaned_data = self.data_cleaning.clean_data(data)
        normalized_data = self.data_normalizing.normalize_data(cleaned_data)
        return normalized_data

    def calculate_metrics(self, data: str) -> int:
        calculated_metrics = len(data)
        return calculated_metrics


class DataVisualization:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("200x100")

    def visualize_results(self, results: Union[str, int]) -> None:
        label = tk.Label(self.root, text=f"Results: {results}")
        label.pack()

    def close_window(self) -> None:
        self.root.destroy()


class Program:
    def __init__(self):
        self.data_processing = DataProcessing()
        self.data_visualization = DataVisualization()

    def run_program(self) -> str:
        try:
            data = self.get_data()
            preprocessed_data = self.data_processing.preprocess_data(data)
            metrics = self.data_processing.calculate_metrics(preprocessed_data)
            self.display_results(metrics)
            return preprocessed_data
        except Exception as e:
            print(f"Error running program: {e}")
            return ""

    def get_data(self) -> str:
        max_attempts = 3
        for attempt in range(max_attempts):
            try:
                data = self.get_real_time_data()
                return data
            except Exception as e:
                print(f"Error retrieving data: {e}")
                print(f"Retrying in 5 seconds...")
                time.sleep(5)
        print("Data retrieval failed. Exiting program.")
        exit(1)

    def get_real_time_data(self) -> str:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"Dirty data retrieved at {current_time}"

    def display_results(self, results: Union[str, int]) -> None:
        self.data_visualization.visualize_results(results)
        self.data_visualization.root.after(
            5000, self.data_visualization.close_window)


class ClassBasedOnContext:
    def __init__(self, context: str):
        self.context = context

    def perform_task(self) -> None:
        print(f"Performing task based on context: {self.context}")


class AutonomousProgram:
    def __init__(self):
        self.program = Program()

    def run(self) -> None:
        program_results = self.program.run_program()
        if program_results:
            advanced_class = AdvancedClass(program_results)
            advanced_class.perform_task()

    def run_autonomously(self) -> None:
        try:
            self.run()
        except KeyboardInterrupt:
            print("\nAutonomous program terminated by user.")


class AdvancedClass:
    def __init__(self, program_results: str):
        self.program_results = program_results

    def perform_task(self) -> None:
        new_class = NewClass(self.program_results)
        new_class.do_something()


class AdditionalClass:
    def __init__(self):
        self.autonomous_program = AutonomousProgram()
        self.brand_new_class = BrandNewClass()

    def execute(self) -> None:
        self.autonomous_program.run_autonomously()
        self.brand_new_class.process_results(10)


class NewClass:
    def __init__(self, program_results: str):
        self.results = program_results

    def do_something(self) -> None:
        if self.results:
            print(f"Do something with results: {self.results}")
        else:
            print("No results to do something with")


class BrandNewClass:
    def __init__(self):
        self.data_visualization = DataVisualization()

    def process_results(self, results: Union[str, int]) -> None:
        self.data_visualization.visualize_results(results)


class ContextBasedClass:
    def __init__(self, context: str):
        self.context = context

    def perform_task(self) -> None:
        print(f"Performing {self.context}-based task")


if __name__ == "__main__":
    additional_class = AdditionalClass()
    additional_class.execute()

    class_based_on_context = ClassBasedOnContext("Context Based Task")
    class_based_on_context.perform_task()

    context_based_class = ContextBasedClass("Advanced")
    context_based_class.perform_task()
